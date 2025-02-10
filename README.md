# tiktok-live-streaming-



# Diffusion en direct sur TikTok

Ce projet vous permet de diffuser en direct sur TikTok depuis votre PC Ubuntu 24.04 en utilisant Python et FFmpeg. 

## Prérequis

1. **TikTok Pro** : Assurez-vous que votre compte TikTok est un compte Pro. Vous devez avoir l'option pour diffuser en direct dans votre application TikTok.
2. **Clé RTMP** : Vous devez récupérer la clé de stream RTMP depuis l'application TikTok via **OBS Studio** ou un autre logiciel de streaming. 
3. **FFmpeg** : Installez **FFmpeg** sur votre machine Ubuntu.

## Installation

1. Installez les dépendances requises :
    ```bash
    sudo apt update
    sudo apt install python3-pip ffmpeg
    pip3 install -r requirements.txt
    ```

2. Récupérez la clé RTMP TikTok depuis OBS Studio.

3. Configurez le script pour utiliser votre clé RTMP dans le fichier `scripts/stream_to_tiktok.py`.

4. Lancez le script pour commencer à diffuser :
    ```bash
    python3 stream_to_tiktok.py
    ```

## Note

Le script capture l'écran de votre bureau et l'envoie à TikTok via un flux RTMP. Assurez-vous de respecter les règles de la plateforme TikTok et d'utiliser ces outils de manière conforme.


