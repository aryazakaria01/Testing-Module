from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode

async def send_message(message: Message):
  user_id = message.from_user.id
  user = message.from_user.mention()
  group = message.link
  await app.send_message(
    user_id,
    f"<u>Notifications you've been tagged</u>\n• User: {message.from_user.mention()}\n• User id: {message.from_user.id}\n• Groups: {message.chat.title}",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("👉 Go to message", url=f"{message.link}")]]),
    parse_mode=ParseMode.HTML)
    
