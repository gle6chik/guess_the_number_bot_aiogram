from aiogram import Router, types, F

router = Router()

@router.callback_query(F.data == 'start_easy')
async def easy_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Теперь легко)')
    await callback.answer()

@router.callback_query(F.data == 'start_medium')
async def medium_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Теперь средне)')
    await callback.answer()

@router.callback_query(F.data == 'start_difficult')
async def difficult_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Теперь сложно)')
    await callback.answer()

@router.callback_query(F.data == 'back')
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Надо назад как-то...')
    await callback.answer()
