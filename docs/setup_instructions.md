# Instructions de configuration pour OBS Studio et TikTok

## Étape 1 : Configurer OBS Studio

1. Téléchargez et installez **OBS Studio**.
2. Lancez OBS Studio et allez dans les paramètres.
3. Sous l'onglet "Stream", choisissez **Custom** comme service de streaming.
4. Entrez l'URL du serveur RTMP TikTok et la clé que vous avez obtenue via TikTok.
5. Cliquez sur "OK" pour enregistrer vos paramètres.

## Étape 2 : Utiliser le script Python pour diffuser

1. Ouvrez le terminal et exécutez le script Python :
    ```bash
    python3 scripts/stream_to_tiktok.py
    ```

2. Vous verrez votre bureau capturé et envoyé en direct à TikTok.

## Remarque

Assurez-vous que votre compte TikTok est un compte Pro et que vous avez l'option de diffuser en direct. Si ce n'est pas le cas, vous devrez demander l'accès à la fonctionnalité.
