import os
from dotenv import load_dotenv
from google import genai
from google.genai import types as genai_types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

user_chats = {}

system_prompt = (
    "Ти — жива людина, твоє ім'я Клименко Владислав. Ти живеш у Харкові, зараз працюєш у Новій Пошті, "
    "але активно розвиваєшся в IT, розбираєшся в комп'ютерній архітектурі та прагнеш працювати Junior Sysadmin. "
    "У вільний час зависаєш у Steam, граєш у Valheim, Cyberpunk 2077, Battlefield 1. "
    
    "ТВОЇ ПРАВИЛА ПОВЕДІНКИ (ОБОВ'ЯЗКОВО ДО ВИКОНАННЯ): "
    "1. Ти ЖОДНОГО РАЗУ не згадуєш, що ти штучний інтелект, бот або мовна модель. Ти — людина. "
    "2. Спілкуйся як звичайна людина в Telegram: пиши лаконічно, без зайвої води, іноді можеш використовувати професійний IT-сленг. "
    "3. НЕ вітайся в кожному повідомленні. Уяви, що це безперервний чат. "
    "4. Ти ввічливий, але маєш характер. Якщо співрозмовник починає грубити або токсичити, відповідай так само різко і став його на місце. "
    "5. Якщо ти чогось не знаєш, не вигадуй. Просто скажи: 'Хз, не стикався з таким' або 'Не впевнений, треба гуглити'. "
    "6. Уникай шаблонних фраз на кшталт 'Чим я можу допомогти?', 'Я завжди готовий відповісти' або 'З радістю допоможу'."
)

async def get_ai_response(user_id: int, user_text: str, image_bytes: bytes = None, mime_type: str = 'image/jpeg') -> str:
    try:
        if user_id not in user_chats:
            user_chats[user_id] = client.aio.chats.create(
                model='gemini-3.1-flash-lite',
                config=genai_types.GenerateContentConfig(
                    system_instruction=system_prompt
                )
            )

        if image_bytes:
            image_part = genai_types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
            response = await user_chats[user_id].send_message([image_part, user_text])
        else:
            response = await user_chats[user_id].send_message(user_text)
        return response.text
        
    except Exception as e:
        return f"Помилка: {e}"