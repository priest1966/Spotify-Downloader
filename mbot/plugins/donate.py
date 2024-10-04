from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from mbot import Mbot

# Define the /donate command
@Mbot.on_message(filters.command("donate"))
async def donate(client, message):
    # Define the inline keyboard for donation options
    donate_buttons = [
        [InlineKeyboardButton("☕ Buy Me a Coffee", url="https://www.buymeacoffee.com/YourUsername")],
        [InlineKeyboardButton("💵 Donate via PayPal", url="https://www.paypal.me/YourUsername")],
        [InlineKeyboardButton("💰 Patreon Support", url="https://www.patreon.com/YourUsername")]
    ]
    
    # Send a reply with the donation options
    await message.reply_text(
        f"Hello {message.from_user.first_name}!\n\n"
        "If you'd like to support this project, feel free to make a donation using any of the methods below. "
        "Your contribution helps keep the bot running and adds more features! 💖",
        reply_markup=InlineKeyboardMarkup(donate_buttons)
    )

# Add this handler to your bot's main loop
