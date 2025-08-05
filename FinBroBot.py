import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(
    KeyboardButton("💰 Баланс"),
    KeyboardButton("🎯 Цели")
)
main_keyboard.add(
    KeyboardButton("📊 Статистика"),
    KeyboardButton("📝 Советы")
)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в Fin_BroBot!", reply_markup=main_keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "💰 Баланс":
        bot.send_message(message.chat.id, "Ваш баланс: 0₽")
    elif message.text == "🎯 Цели":
        bot.send_message(message.chat.id, "Цели ещё не установлены.")
    elif message.text == "📊 Статистика":
        bot.send_message(message.chat.id, "Пока нет статистики.")
    elif message.text == "📝 Советы":
        bot.send_message(message.chat.id, "Совет: ведите учёт расходов каждый день.")
    else:
        bot.send_message(message.chat.id, "Я вас не понял. Выберите действие с клавиатуры.")

bot.polling(none_stop=True)