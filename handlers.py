from aiogram import Router, types
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from generators import create_response
from config import SYSTEM_MESSAGE
from utils import trim_messages

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в AI Bot!")


@router.message(Command("reset"))
async def cmd_reset(message: types.Message, state: FSMContext):
    try:
        await state.clear()
        await message.answer("История сообщений сброшена.")
    except Exception as e:
        await message.answer(f"Произошла ошибка при сбросе истории: {e}")
        
@router.message(StateFilter(['generating']))
async def wait_response(message: types.Message):
    await message.answer("Ожидайте! Идёт генерация ответа...")

@router.message()
async def generate_answer(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        
        messages = data.get("messages", [SYSTEM_MESSAGE])
        messages.append({"role": "user", "content": message.text})
        messages = trim_messages(messages)
        
        await state.update_data(messages=messages)
        await state.set_state('generating')

        response = await create_response(messages)
        messages.append({"role": "assistant", "content": response})
        messages = trim_messages(messages)
        
    except Exception as e:
        await message.answer(f'Произошла ошибка: {e}')
    else:
        await message.answer(response)
    finally:
       await state.clear()
       await state.update_data(messages=messages)