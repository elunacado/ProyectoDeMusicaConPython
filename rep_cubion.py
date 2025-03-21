from pygame import mixer

mixer.init()

cumbion = 'cumbion.mid'

while True:
    tecla = input()
    if tecla == 'c':
        mixer.music.load(cumbion)
        mixer.music.play()