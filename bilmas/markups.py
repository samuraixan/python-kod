from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

btnMain = KeyboardButton('⬅️Menyu boshi')

# --- Main Menu ---
btnRandom = KeyboardButton('🔸 Hohlagan raqam')
btnOther = KeyboardButton('➡️Boshqa narsa')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom,btnOther)


#  ---Other Menu ---
btnInfo = KeyboardButton('📚 Informatsiya')
btnMonkey = KeyboardButton('📈 Valyuta kursi')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMonkey, btnMain)