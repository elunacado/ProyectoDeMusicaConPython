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

for i in range(0, 5):
    snare(pentagrama, 0.25, 127, 44)
    silence(pentagrama, 0.75)
    snare(pentagrama, 0.25, 75, 42)
    snare(pentagrama, 0.25, 75, 42)
    silence(pentagrama, 0.25)
    snare(pentagrama, 0.25, 100, 44)
    silence(pentagrama, 2)

pentagrama.show('midi')
