from music21 import note, stream, instrument

def silence(un_pentagrama, time):
    un_pentagrama.append(note.Rest(time))

def snare(un_pentagrama, time, force, midi):
    snare_hit = note.Note("G3", quarterLength=time)  # Nota de tarola en MIDI
    snare_hit.volume.velocity = force  # Ajusta la fuerza del golpe
    snare_hit.pitch.midi = midi
    un_pentagrama.append(snare_hit)

pentagrama = stream.Stream()
pentagrama.append(instrument.SnareDrum())  # Tarola en lugar de bombo

def snare_rhytm(pentagrama):
    for _ in range(4):
        snare(pentagrama, 0.25, 100, 44)
        silence(pentagrama, 0.1)
        snare(pentagrama, 0.25, 75, 42)
        silence(pentagrama, 0.1)
        snare(pentagrama, 0.25, 75, 42)
        silence(pentagrama, 0.1)
        snare(pentagrama, 0.25, 100, 44)
        silence(pentagrama, 2)

parte_snare = stream.Part()

parte_snare.insert(0, instrument.SnareDrum())
snare_rhytm(parte_snare)

pentagrama.append(parte_snare)

pentagrama.show('midi')
#pentagrama.show()
