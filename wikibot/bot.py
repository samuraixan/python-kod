import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5861953520:AAGldrBMJaYzqdrl8k_ETuOe4xMyD_oTiiQ'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    Этот обработчик будет вызываться, когда пользователь отправляет команду `/start` или `/help`
    """
    await message.reply("Wikipediya Botiga Xush kelibsiz.")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

    # old style:
    # await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)