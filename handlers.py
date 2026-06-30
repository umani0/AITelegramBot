from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router, Bot, types
from ai_service import get_ai_response
user = Router()

PREFIX = "Клим"
@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привіт. Я Клименко АІ, розроблений на Харківському Траткорному Заводі. Задавай мені питання.")

@user.message(F.photo)
async def handle_photo(message: Message, bot: Bot):
    is_group = message.chat.type in ["group", "supergroup"]
    caption = message.caption if message.caption else ""
    if is_group:
        if not caption.lower().startswith(PREFIX.lower()):
            return
        prompt = caption[len(PREFIX):].strip(" ,.!")
    else:
        prompt = caption if caption else "Відреагуй на фото, як би то ти розмовляєш з другом. Коротко."
    processing_msg = await message.answer("Розглядаю зображення...")
    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        image_bytes = downloaded_file.read()
        response_text = await get_ai_response(message.from_user.id, prompt, image_bytes)
        await processing_msg.edit_text(response_text)
    except Exception as e:
        await processing_msg.edit_text(f"Помилка при надсиланні фото: {e}")

@user.message(F.sticker)
async def handle_sticker(message: types.Message, bot: Bot):
    if message.sticker.is_animated:
        await message.answer("Я поки не бачу таке, мені лінь")
        return
    processing_msg = await message.answer("Зачекайте...")
    try:
        file_info = await bot.get_file(message.sticker.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        sticker_bytes = downloaded_file.read()
        if message.sticker.is_video:
            file_mime_type = 'video/webm'
            prompt = "Відреагуй на цей стікер якбито ти у чаті з другом. Коротко."
        else:
            file_mime_type = 'image/webp'
            prompt = "Відреагуй на цей стікер якбито ти у чаті з другом. Коротко."
        ai_answer = await get_ai_response(
            user_id=message.from_user.id, 
            user_text=prompt, 
            image_bytes=sticker_bytes, 
            mime_type=file_mime_type
        )
        await processing_msg.edit_text(ai_answer)
    except Exception as e:
        await processing_msg.edit_text(f"Помилка при надсиланні стікеру: {e}")

@user.message(F.text)
async def handle_user_message(message: Message):
    text = message.text
    is_group = message.chat.type in ["group", "supergroup"]
    if is_group:
        if not text.lower().startswith(PREFIX.lower()):
            return
        text = text[len(PREFIX):].strip(" ,.!")
        if not text:
            return
    processing_msg = await message.answer("Зачекайте...")
    try:
        context_id = message.chat.id if is_group else message.from_user.id
        ai_answer = await get_ai_response(context_id, message.text)
        await processing_msg.edit_text(ai_answer)
    except Exception as e:
        await processing_msg.edit_text(f"Помилка: {e}")