from music21 import note, stream, instrument

def silence(un_pentagrama, time):
    un_pentagrama.append(note.Rest(time))

def snare(pentagrama, time, force, midi):
    snare_hit = note.Note("G3", quarterLength=time)  
    snare_hit.volume.velocity = force 
    snare_hit.pitch.midi = midi 
    pentagrama.append(snare_hit)

def bass(pentagrama, time, force):
    bass=note.Note("G2", quarterLength=time)
    bass.volume.velocity = force
    pentagrama.append(bass)

pentagrama = stream.Stream()
pentagrama.append(instrument.SnareDrum())  # Tarola en lugar de bombo
pentagrama.append(instrument.ElectricBass())

def snare_rhytm(pentagrama):
    for _ in range(8):
        snare(pentagrama, 0.25, 127, 44)
        silence(pentagrama, 0.25)
        snare(pentagrama, 0.25, 75, 42)
        silence(pentagrama, 0.1)
        snare(pentagrama, 0.25, 75, 42)
        silence(pentagrama, 0.25)
        snare(pentagrama, 0.25, 127, 44)
        silence(pentagrama, .4)

def bass_rhytm(pentagrama):
    for _ in range(8):
        bass(pentagrama, 0.25, 80)
        silence(pentagrama, 1)
        bass(pentagrama, 0.25, 80)
        silence(pentagrama, .4)


parte_snare = stream.Part()
parte_bass = stream.Part()

parte_snare.insert(0, instrument.SnareDrum())
parte_bass.insert(0, instrument.BassDrum())

snare_rhytm(parte_snare)
bass_rhytm(parte_bass)

#pentagrama.append(parte_snare)
pentagrama.append(parte_bass)

pentagrama.show('midi')
