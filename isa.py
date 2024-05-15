import random
import telebot
from local_settings import API_TOKEN

API_TOKEN = '6749491755:AAHpe8BIYlHKsNcl-CeDvy_YCVZndyvq9Gk'
player_person= 0
computer_person = 0

bot = telebot.TeleBot()
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "добро пожаловать в игру камень\ножницы\бумага"
                            "Выберите; камень,ножница или бумага.")
@bot.message_handler(fans=lambda message:True)
def play_game(message):
    user_move=message.text
    if user_move not in ["к","н","б"]:
        bot.reply_to(message,"Пожалуйста введите ваше значение;")
    else:
        computer_move=random.choice(["к","н","б"])
        if(user_move == "к" and computer_move == "н") or \
                (user_move == "н" and computer_move == "б") or \
                (user_move == "б" and computer_move == "к"):
            bot.reply_to(message,"Вы выиграли!")
        elif user_move==computer_move:
            bot.reply_to(message,"ничья!")
            player_person += 1
        else:
            bot.reply_to(message,"бот выиграл")
            computer_person += 1



bot.infinity_polling()
