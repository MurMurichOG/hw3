from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from pprint import pprint
from keyboard import keyboard

start_router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    gender = State()
    how_many = State()

@start_router.message(Command("stop"))
@start_router.message(F.text == "stop")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Ок")

@start_router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Введите ваше имя")

@start_router.message(Form.name)
async def name(message: types.Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer("Слишком короткое имя")
    else:
        await state.update_data(name=message.text)
        await message.answer(f"Спасибо {message.text}")
        await state.set_state(Form.age)
        await message.answer("Введите ваш возраст:")

@start_router.message(Form.age)
async def age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры")
    elif int(age) < 0 or int(age) > 99:
        await message.answer("Введите верный возраст")
    else:
        await state.update_data(age=int(age))
        await state.set_state(Form.gender)
        await message.answer("Введите ваш пол:", reply_markup=keyboard())

@start_router.message(Form.how_many)
async def num(message: types.Message, state: FSMContext):
    await state.set_state((Form.how_many))
    await message.answer("Сколько книг вы прочитали в этом месяце?")
    data = await state.get_data()
    pprint(data)
    await message.answer(f"Спасибо! ;)")
    await state.clear()