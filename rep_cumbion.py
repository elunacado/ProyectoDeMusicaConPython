import keyboard
import time
from pygame import mixer

# Inicializar pygame.mixer
mixer.init()

# Archivos de audio
cumbion = 'cumbion.mid'
primera_llamada = 'primera_llamada.mp3'
segunda_llamada = 'segunda_llamada.mp3'
tercera_llamada = 'tercera_llamada.mp3'
redes_sociales = 'redes_sociales.mp3'

# Configurar la cumbia
mixer.music.load(cumbion)

# Variables de estado
musica_reproduciendo = False  
musica_pausada = False
volumen_original = 1.0  

print("Presiona espacio para reproducir la cumbia ")
print("Presiona espacio de nuevo para pausarla o reanudarla ")
print("Presiona s para ddetenerla ")
print("Presiona los numeros del 1 al 4 para recibir los anuncios ")

while True:
    if keyboard.is_pressed("space"):
        if not musica_reproduciendo:
            mixer.music.play(-1)
            musica_reproduciendo = True 
            musica_pausada = False    
        elif musica_pausada:
            mixer.music.unpause()
            musica_pausada = False  
        else:
            mixer.music.pause()
            musica_pausada = True  
        time.sleep(0.3)  
        
    if keyboard.is_pressed("s"):  
        mixer.music.stop()
        musica_reproduciendo = False  
        time.sleep(0.5)

    for key, sonido in zip(["1", "2", "3", "4"], [primera_llamada, segunda_llamada, tercera_llamada, redes_sociales]):
        if keyboard.is_pressed(key):

            mixer.music.set_volume(0.3)

            # Reproducir la llamada
            sonido_llamada = mixer.Sound(sonido)
            sonido_llamada.play()

            # Esperar a que termine el sonido
            time.sleep(sonido_llamada.get_length())

            # Restaurar el volumen de la cumbia
            mixer.music.set_volume(volumen_original)
            
            time.sleep(0.3)  
