from aiogram import types

def keyboard():
    kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Мужчина"),
                    types.KeyboardButton(text="Женщина"),
                    types.KeyboardButton(text="Другое 0_0")
                ]
            ])
    return kb