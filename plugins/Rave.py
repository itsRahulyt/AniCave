from pyrogram import Client, filters

@Client.on_message(filters.command("rave") & filters.private)
async def rave_test(client, message):
    await message.reply(
        "🔥 Rave system is active!\n\n"
        "Next step: we'll connect the 480p / 720p / 1080p files."
    )
