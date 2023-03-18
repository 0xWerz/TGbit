import os
import uuid
import telebot
from items.items import ITEMS
from utils.payment import pay_with_bitcoin


class VirtualStoreBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.bot.message_handler(commands=["start"])(self.send_menu)
        self.bot.message_handler(commands=["help"])(self.send_help)
        self.bot.message_handler(regexp="^[1-5]$")(self.process_order)

    def send_menu(self, message):
        """
        Handles the /start command and sends the menu to the user
        """
        items_text = "\n".join([f"{i+1}. {item['name']} - {item['price']:.5f} XMR/BTC"
                                for i, item in enumerate(ITEMS)])
        response = f"Welcome to our virtual store!\n\nHere's our menu:\n\n{items_text}\n\nPlease choose an item by entering its number."
        self.bot.reply_to(message, response)

    def send_help(self, message):
        """
        Handles the /help command and sends a help message to the user
        """
        help_text = "This is a simple bot that allows you to purchase items from a virtual store using Monero or Bitcoin.\n\nTo get started, please send the /start command."
        self.bot.reply_to(message, help_text)

    def process_order(self, message):
        """
        Handles the user's selection of an item and prompts for a payment method
        """
        item_num = int(message.text)
        item = ITEMS[item_num-1]
        amount = "{:.5f}".format(item["price"])

        payment_text = f"Please select a payment method for {item['name']}:\n\n1. Monero\n2. Bitcoin"
        self.bot.reply_to(message, payment_text)

        # Set the state of the user to payment method selection
        self.bot.register_next_step_handler(
            message, self.select_payment_method, amount, item)

    def select_payment_method(self, message, amount, item):
        """
        Handles the user's selection of a payment method and prompts for confirmation
        """
        method_num = int(message.text)

        order_id = uuid.uuid4().hex[:10]

        if method_num == 2:
            bot.send_message(
                message.chat.id, f"Please confirm that you want to purchase {item['name']} for {amount} BTC by replying with 'Yes' or 'No'.")
            self.bot.register_next_step_handler(
                message, self.confirm_payment, order_id, amount)

    def confirm_payment(self, message, order_id, amount):
        """
        Handles the user's confirmation of the payment and processes the payment
        """
        confirmation_text = message.text.lower()

        if confirmation_text == 'yes':
            payment_result = pay_with_bitcoin(
                self.bot, message.chat.id, order_id, amount)
            self.bot.reply_to(message, payment_result)
        elif confirmation_text == 'no':
            self.bot.reply_to(message, "Payment canceled.")
        else:
            self.bot.reply_to(
                message, "Invalid confirmation. Please type Yes or No.")

    def start(self):
        """
        Starts the bot
        """
        self.bot.polling()


if __name__ == "__main__":
    from config import TOKEN
    bot = VirtualStoreBot(TOKEN)
    bot.start()
