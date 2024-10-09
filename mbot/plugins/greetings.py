from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from mbot import LOG_GROUP, OWNER_ID, SUDO_USERS, Mbot
from os import execvp, sys

@Mbot.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = [
        [InlineKeyboardButton(text="• ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ᴄʜᴀᴛ •", url='http://t.me/movieverse_2_bot?startgroup=true')],
        [InlineKeyboardButton(text="Movie Channel", url="https://t.me/movieverse_2"),
         InlineKeyboardButton(text="Movie Group", url="https://t.me/movieverse_discussion_2")],
        [InlineKeyboardButton(text="Help", callback_data="helphome"),
         InlineKeyboardButton(text="Buy Me a Coffee", callback_data="DONATE")]
    ]

    if LOG_GROUP:
        invite_link = await client.create_chat_invite_link(chat_id=int(LOG_GROUP))
        reply_markup.append([InlineKeyboardButton("• ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ •", url="https://t.me/movieversepremium")])

    await message.reply_text(
        f"Hello {message.from_user.first_name}, I'm a Simple Music Downloader Bot. I Currently Support Download from Spotify, Deezer, Facebook, Instagram or Youtube.",
        reply_markup=InlineKeyboardMarkup(reply_markup)
    )


@Mbot.on_message(filters.command("restart") & filters.user(OWNER_ID) & filters.private)
async def restart(_, message):
    await message.delete()
    execvp(sys.executable, [sys.executable, "-m", "mbot"])


@Mbot.on_message(filters.command("donate"))
async def donate(client, message):
    donate_buttons = [
        [InlineKeyboardButton("QR Code", url="https://graph.org/file/e2d9b5e15e15daafb64e8.jpg")],
        [InlineKeyboardButton("More Method", url="https://t.me/spotiverse_donation")],
    ]

    await message.reply_text(
        f"Hello {message.from_user.first_name}!\n\n"
        "If you'd like to support this project, feel free to make a donation using any of the methods below. "
        "Your contribution helps keep the bot running and adds more features! 💖",
        reply_markup=InlineKeyboardMarkup(donate_buttons)
    )

@Mbot.on_callback_query(filters.regex(r"DONATE"))
async def donate_callback(_, query):
    donate_buttons = [
        [InlineKeyboardButton("QR Code", url="https://graph.org/file/e2d9b5e15e15daafb64e8.jpg")],
        [InlineKeyboardButton("More Method", url="https://t.me/spotiverse_donation")],
    ]

    await query.message.edit_text(
        f"Hello {query.from_user.first_name}!\n\n"
        "If you'd like to support this project, feel free to make a donation using any of the methods below. "
        "Your contribution helps keep the bot running and adds more features! 💖",
        reply_markup=InlineKeyboardMarkup(donate_buttons)
    )

@Mbot.on_message(filters.command("log") & filters.user(SUDO_USERS))
async def send_log(_, message):
    await message.reply_document("Spotiverse.log")


@Mbot.on_message(filters.command("ping"))
async def ping(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ms = (datetime.now() - start).microseconds / 1000
    await message.reply_text(f"**Pong!**\nResponse time: `{ms} ms`")


HELP = {
    "Youtube": "Send **Youtube** Link in Chat to Download Song.",
    "Spotify": "Send **Spotify** Track/Playlist/Album/Show/Episode's Link. I'll Download It For You.",
    "Deezer": "Send Deezer Playlist/Album/Track Link. I'll Download It For You.",
    "Jiosaavn": "Not Implemented yet",
    "SoundCloud": "Not Implemented yet",
    "Group": "Will add later."
}


@Mbot.on_message(filters.command("help"))
async def help(_, message):
    button = [[InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP]
    button.append([InlineKeyboardButton(text="Back", callback_data="backdome")])

    await message.reply_text(
        f"Hello **{message.from_user.first_name}**, I'm [SpotiVerse](https://t.me/Spotiverse_bot).\nI'm Here to download your music.",
        reply_markup=InlineKeyboardMarkup(button)
    )


@Mbot.on_callback_query(filters.regex(r"backdome"))
async def backdo(_, query):
    button = [[InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP]
    button.append([InlineKeyboardButton(text="Back", callback_data="backdome")])

    await query.message.edit(
        f"Hello **{query.from_user.first_name}**, I'm [SpotiVerse](https://t.me/Spotiverse_bot).\nI'm Here to download your music.",
        reply_markup=InlineKeyboardMarkup(button)
    )


@Mbot.on_callback_query(filters.regex(r"help_(.*?)"))
async def helpbtn(_, query):
    i = query.data.replace("help_", "")
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="helphome")]])
    text = f"Help for **{i}**\n\n{HELP[i]}"

    await query.message.edit(text=text, reply_markup=button)


@Mbot.on_callback_query(filters.regex(r"helphome"))
async def help_home(_, query):
    button = [[InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP]

    await query.message.edit(
        f"Hello **{query.from_user.first_name}**, I'm [SpotiVerse](https://t.me/Spotiverse_bot).\nI'm Here to download your music.",
        reply_markup=InlineKeyboardMarkup(button)
    )
