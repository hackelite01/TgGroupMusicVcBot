from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>馃憢馃徎 Hi {message.from_user.first_name}!</b>

I am Tg Group Music Bot, an open-source bot that lets you play music in your Telegram groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "鈿� Source code", url="https://t.me/hackelitebotsupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "馃挰 Report", url="https://t.me/mayank_ka_b_for_bot"
                    ),
                    InlineKeyboardButton(
                        "Channel for more 馃攬", url="https://t.me/hackelitebotsupport"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "馃拋馃徎鈥嶁檪锔� Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "鉁� Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No 鉂�", callback_data="close"
                    )
                ]
            ]
        )
    )
