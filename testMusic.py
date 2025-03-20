from music21 import note, stream, instrument

def silence(un_pentagrama, time):
    un_pentagrama.append(note.Rest(time))

def snare(pentagrama, time, force, midi):
    snare_hit = note.Note("G3", quarterLength=time)  
    snare_hit.volume.velocity = force 
    snare_hit.pitch.midi = midi 
    pentagrama.append(snare_hit)

def epiano(pentagrama, time, force):
    epiano=note.Note("G4", quarterLength=time)
    epiano.volume.velocity = force
    pentagrama.append(epiano)

pentagrama = stream.Stream()
pentagrama.append(instrument.SnareDrum())  # Tarola en lugar de bombo

def snare_rhytm(pentagrama):
    for _ in range(8):
        snare(pentagrama, 0.35, 127, 44)
        silence(pentagrama, 0.25)
        snare(pentagrama, 0.35, 75, 42)
        silence(pentagrama, 0.1)
        snare(pentagrama, 0.35, 75, 42)
        

def epiano_rhytm(pentagrama):
    for _ in range(8):
        epiano(pentagrama, 0.35, 80)
        silence(pentagrama, 1.05)


parte_snare = stream.Part()
parte_epiano = stream.Part()

parte_snare.insert(0, instrument.SnareDrum())
parte_epiano.insert(0, instrument.ElectricPiano())

snare_rhytm(parte_snare)
epiano_rhytm(parte_epiano)

pentagrama.append(parte_snare)
pentagrama.append(parte_epiano)

pentagrama.show('midi')
