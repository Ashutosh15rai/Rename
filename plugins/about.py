
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("Bot :- @Shadow_Kun_Bot\nCreater :- @Shadow_Sanpai\nLanguage :-Python3\nLibrary :- Pyrogram 1.4.16\nServer :- Heroku")
