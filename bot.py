from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "6931147463:AAFCz9USpta1bChz05lqdjnNYMrlmnnbhQM")

API_ID = int(os.environ.get("API_ID", "20421248"))

API_HASH = os.environ.get("API_HASH", "90da70b17365b3709b8a0346a7749ce7")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
