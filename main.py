import telebot

TOKEN = '7214584388:AAH64oOfRG2wpFv4uOin7vZenrsKyZ7copM'  # ⚠️ Обязательно вставь реальный токен!

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я FinBroBot и я работаю!")

bot.polling()
