from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", url="https://telegra.ph/Full-details-of-YoutubeYorkBot-12-17")],
        [InlineKeyboardButton(
            "Github Repo Link", url="https://github.com/Skievoid/Youtube-Downloader-Bot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help- To learn how to use me. Please go through the buttons below before using me."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
