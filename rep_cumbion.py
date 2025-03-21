import keyboard, time
from pygame import mixer

mixer.init()
cumbion = 'cumbion.mid'

mixer.music.load(cumbion)

# Volumen inicial
mixer.music.set_volume(1.0)

musica_reproduciendo = False  

print("Presiona espacio para reproducir la cumbia ")

while True:
    if keyboard.is_pressed("space") and not musica_reproduciendo:
        mixer.music.play(-1)
        musica_reproduciendo = True  
        time.sleep(0.5)  
        
    if keyboard.is_pressed("s"):  
        mixer.music.stop()
        musica_reproduciendo = False  
        time.sleep(0.5)



