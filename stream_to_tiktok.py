import pyautogui
import numpy as np
import cv2
import subprocess

# Remplacez par votre URL RTMP TikTok et la clé de stream
rtmp_url = "rtmp://<serveur_de_tiktok>/<stream_key>"  # Remplacez par l'URL et la clé RTMP

# Résolution de l'écran
screen_width, screen_height = pyautogui.size()

# Taille de la capture
frame_width = screen_width
frame_height = screen_height

# Commande FFmpeg pour diffuser sur TikTok
ffmpeg_command = [
    'ffmpeg',
    '-y',  # Écraser les fichiers existants
    '-f', 'rawvideo',  # Format vidéo brut
    '-vcodec', 'rawvideo',
    '-pix_fmt', 'bgr24',  # Format de pixel
    '-s', f"{frame_width}x{frame_height}",  # Taille de l'écran
    '-r', '30',  # Fréquence d'images
    '-i', '-',  # Lire depuis stdin
    '-c:v', 'libx264',  # Encoder en x264
    '-preset', 'ultrafast',  # Streaming à faible latence
    '-tune', 'zerolatency',  # Latence minimale
    '-f', 'flv',  # Format de flux
    rtmp_url  # L'URL RTMP de TikTok
]

# Lancer le processus FFmpeg
process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

# Capturer l'écran en boucle et envoyer les images à FFmpeg
while True:
    screenshot = pyautogui.screenshot()  # Capture l'écran
    frame = np.array(screenshot)  # Convertir en tableau numpy
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convertir l'image en BGR

    # Envoyer l'image à FFmpeg via stdin
    process.stdin.write(frame.tobytes())

    # Afficher l'image localement
    cv2.imshow("Streaming to TikTok", frame)

    # Quitter avec "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fermer proprement
process.stdin.close()
process.wait()
cv2.destroyAllWindows()
