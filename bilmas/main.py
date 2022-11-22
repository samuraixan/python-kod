import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

import random

API_TOKEN = '5916237438:AAHaRme4dLyqYP68CtwjBSubz2Bdnh1yZow'

logging.basicConfig(level=logging.INFO)


# Инициализировать бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id,'Salom {0.first_name}'.format(message.from_user),reply_markup = nav.mainMenu)



@dp.message_handler()
async def echo(message: types.Message):
    if message.text == '🔸 Hohlagan raqam':
        await bot.send_message(message.from_user.id, 'Sizni raqamiz: ' + str(random.randint(1000, 9999)))

    elif message.text == '⬅️Menyu boshi':
        await bot.send_message(message.from_user.id, '⬅️Menyu boshi', reply_markup=nav.mainMenu)



    elif message.text == '➡️Boshqa narsa':
        await bot.send_message(message.from_user.id, '➡️Boshqa narsa', reply_markup=nav.otherMenu)

    elif message.text == '📚 Informatsiya':
        await bot.send_message(message.from_user.id, 'Qanaqadir informatsiya')

    elif message.text == '📈 Valyuta kursi':
        await bot.send_message(message.from_user.id, 'Valyuta kursi')

    else:
        await message.reply('Tushunarsiz buyruq')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
