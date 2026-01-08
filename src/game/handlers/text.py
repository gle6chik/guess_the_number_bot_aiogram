from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def text_handler(message: types.Message):
    text = message.text

    await message.answer(f"Ты написал: {text}\nПроверки на число не будет, потому что это режим игры!")
