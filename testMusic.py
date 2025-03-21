from music21 import note, stream, instrument, key, clef, tempo

def silence(un_pentagrama, time):
    un_pentagrama.append(note.Rest(time))

def snare(un_pentagrama, time, force, midi):
    snare_hit = note.Note("G3", quarterLength=time)  # Nota de tarola en MIDI
    snare_hit.volume.velocity = force  # Ajusta la fuerza del golpe
    snare_hit.pitch.midi = midi
    un_pentagrama.append(snare_hit)

def sax(un_pentagrama, time, myNote):
    sax_hit = note.Note(myNote, quarterLength=time)
    un_pentagrama.append(sax_hit)

pentagrama = stream.Stream()
pentagrama.append(instrument.SnareDrum())  # Tarola en lugar de bombo

def snare_rhytm(pentagrama):
    silence(pentagrama, 3)
    snare(pentagrama, 0.25, 100, 44)
    silence(pentagrama, 0.75)
    for i in range(0, 15):
        snare(pentagrama, 0.25, 50, 42)
        silence(pentagrama, 0.75)
        snare(pentagrama, 0.25, 50, 42)
        silence(pentagrama, 0.75)
        snare(pentagrama, 0.25, 100, 44)
        silence(pentagrama, 1.75)

def sax_rhytm(pentagrama):
    silence(pentagrama, 2)
    sax(pentagrama, 2, "B4")
    sax(pentagrama, 2, "D5")
    sax(pentagrama, 2, "F5")
    sax(pentagrama, 3, "G5")
    silence(pentagrama, 0.5)
    sax(pentagrama, 0.5, "G5")
    sax(pentagrama, 1, "G5")
    sax(pentagrama, 1, "F5")
    sax(pentagrama, 1, "E5")
    sax(pentagrama, 0.5, "F5")
    sax(pentagrama, 3.5, "G5")
    silence(pentagrama, 0.5)
    sax(pentagrama, 0.5, "G5")
    sax(pentagrama, 1, "G5")
    sax(pentagrama, 1, "F5")
    sax(pentagrama, 1, "E5")
    sax(pentagrama, 0.5, "G5")
    sax(pentagrama, 1.5, "F5")
    sax(pentagrama, 1, "E5")
    sax(pentagrama, 1, "D5")
    sax(pentagrama, 0.5, "E5")
    sax(pentagrama, 1.5, "F5")
    sax(pentagrama, 1, "E5")
    sax(pentagrama, 1, "D5")
    sax(pentagrama, 0.5, "E5")
    sax(pentagrama, 4.5, "F5")
    silence(pentagrama, 1)
    sax(pentagrama, 1, "B4")
    sax(pentagrama, 1, "D5")
    sax(pentagrama, 0.5, "F5")
    sax(pentagrama, 3.5, "E5")
    silence(pentagrama, 0.5)
    sax(pentagrama, 0.5, "E5")
    sax(pentagrama, 1, "E5")
    sax(pentagrama, 1, "D5")
    sax(pentagrama, 1, "C#5")
    sax(pentagrama, 0.5, "D5")
    sax(pentagrama, 1.5, "F#5")
    sax(pentagrama, 1, "F#4")
    sax(pentagrama, 1, "B-4")
    sax(pentagrama, 0.5, "C#5")
    sax(pentagrama, 1.5, "F#5")
    sax(pentagrama, 1, "F#4")
    sax(pentagrama, 1, "D5")
    sax(pentagrama, 0.5, "C#5")
    sax(pentagrama, 8.5, "B4")
    

nuevo_tempo = tempo.MetronomeMark(number=220)

parte_snare = stream.Part()
parte_snare.insert(0, instrument.SnareDrum())
snare_rhytm(parte_snare)

parte_sax = stream.Part()
armadura = key.KeySignature(2)
parte_sax.insert(0, armadura)
parte_sax.insert(0, clef.TrebleClef())
parte_sax.insert(0, instrument.Marimba())
sax_rhytm(parte_sax)

pentagrama.insert(0, nuevo_tempo) 
pentagrama.append(parte_snare)
pentagrama.append(parte_sax)

pentagrama.show('midi')
#pentagrama.write('midi', 'cumbion.mid')
#pentagrama.show()
