import telebot;

bot = telebot.TeleBot('1746558651:AAF0EvFQHjONj9xUmtxLGjevWCXK0S8t5s4')

bot.polling(none_stop=True, interval=0)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, я Ботанический Бот - меня зовут Сакрок ")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши Привет ")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


            