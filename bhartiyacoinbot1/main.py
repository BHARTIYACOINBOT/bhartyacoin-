import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
import random
import time
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = '7471673520:AAHac0KTh9d0mD4FpftKlSjrUpT_G0k47Po'

# Define game data
game_data = {
    'users': {},
    'combo_cards': [
        {'one': 'Card 1', 'reward': 10},
        {'two': 'Card 2', 'reward': 20},
        {'ravi': 'Card 3', 'reward': 30}
    ],
    'mining_cards': [
        {'five': 'Mining Card 1', 'reward': 100},
        {'india': 'Mining Card 2', 'reward': 200},
        {'bhartiya': 'Mining Card 3', 'reward': 300}
    ]
}

def start(update, context):
    user_id = update.effective_user.id
    if user_id not in game_data['users']:
        game_data['users'][user_id] = {
            'balance': 0,
            'boost': 1,
            'combo_cards': [],
            'mining_cards': []
        }
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to the game!')

def daily_check_in(update, context):
    user_id = update.effective_user.id
    user_data = game_data['users'][user_id]
    user_data['balance'] += 100
    context.bot.send_message(chat_id=update.effective_chat.id, text='You have earned 100 coins for daily check-in!')

def boost(update, context):
    user_id = update.effective_user.id
    user_data = game_data['users'][user_id]
    user_data['boost'] += 1
    context.bot.send_message(chat_id=update.effective_chat.id, text='Your boost has been increased by 1!')

def collect_combo_card(update, context):
    user_id = update.effective_user.id
    user_data = game_data['users'][user_id]
    combo_card = random.choice(game_data['combo_cards'])
    user_data['combo_cards'].append(combo_card)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'You have collected {combo_card["name"]}!')

def collect_mining_card(update, context):
    user_id = update.effective_user.id
    user_data = game_data['users'][user_id]
    mining_card = random.choice(game_data['mining_cards'])
    user_data['mining_cards'].append(mining_card)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'You have collected {mining_card["name"]}!')

def wallet(update, context):
    user_id = update.effective_user.id
    user_data = game_data['users'][user_id]
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your balance is {user_data["balance"]} coins.')

def tap_and_earn(update, context):
    user_id = update.effective_user.id
    user_data = game_data['users'][user_id]
    user_data['balance'] += user_data['boost'] * 10
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'You have earned {user_data["boost"] * 10} coins!')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('daily_check_in', daily_check_in))
    dp.add_handler(CommandHandler('boost', boost))
    dp.add_handler(CommandHandler('collect_combo_card', collect_combo_card))
    dp.add_handler(CommandHandler('collect_mining_card', collect_mining_card))
    dp.add_handler(CommandHandler('wallet', wallet))
    dp.add_handler(CommandHandler('tap_and_earn', tap_and_earn))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()