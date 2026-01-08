from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def text_handler(message: types.Message):
    text = message.text

    await message.answer(f"Я вижу, что ты отправляешь) Ты написал: {text}")

    if text.isdigit(): # type: ignore
        number = int(text) # type: ignore
        await message.answer(f"И кстати, {number} - это число")
    else:
        await message.answer(f"{text} - это не число")
