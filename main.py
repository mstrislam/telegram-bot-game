

import telebot
import random

API_TOKEN = '6749491755:AAHpe8BIYlHKsNcl-CeDvy_YCVZndyvq9Gk'

def get_computer_choice():
  return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(player_choice, computer_choice):
  print(f"Вы выбрали {player_choice}, компьютер выбрал {computer_choice}.")
  if player_choice == computer_choice:
    return "Ничья!"
  elif (player_choice == "камень" and computer_choice == "ножницы") or \
       (player_choice == "ножницы" and computer_choice == "бумага") or \
       (player_choice == "бумага" and computer_choice == "камень"):
    return "Вы выиграли!"
  else:
    return "Компьютер выиграл!"

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id,
                           text="Привет! Давай сыграем в камень, ножницы, бумага! Выбери: камень, ножницы или бумага")

def play(update, context):
  player_choice = update.message.text.lower()
  if player_choice in ["камень", "ножницы", "бумага"]:
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    context.bot.send_message(chat_id=update.effective_chat.id, text=result
print("конец игры")