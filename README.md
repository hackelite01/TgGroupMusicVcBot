# Tg Group Music Player — The first open-source PyTgCalls based Pyrogram bot to play music in voice chats

## Note

Neither this, or PyTgCalls are fully stable.

## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

### Credits

[!ItzMe] (https://github.com/ballicipluck)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/hackelite01/TgGroupMusicVcBot/)

 ## Join Us on Telegram

<a href="https://t.me/hackelite01"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram" width="190" height="28"></a>
