import os
import time
import requests
import block_io


BITCOIN_ADDRESS = os.getenv("BITCOIN_ADDRESS")
RPC_NODE = os.getenv("RPC_NODE")
BLOCK_IO_API_KEY = os.getenv("BLOCK_IO_API_KEY")
BLOCK_IO_SECRET_PIN = os.getenv("BLOCK_IO_SECRET_PIN")

block_io_client = block_io.BlockIo(BLOCK_IO_API_KEY, BLOCK_IO_SECRET_PIN, 4)


def generate_address(client_id):
    """
    Generates a new Bitcoin address for the given client ID.

    :param client_id: The ID of the client.
    :return: The newly generated Bitcoin address.
    """
    response = block_io_client.get_new_address(label=client_id)
    return response['data']['address']


def check_payment(client_id, amount):
    """
    Checks if the client has paid the specified amount to their Bitcoin address.

    :param client_id: The ID of the client.
    :param amount: The amount of Bitcoin to check for.
    :return: True if the client has paid the specified amount, False otherwise.
    """
    address = generate_address(client_id)
    url = f"{RPC_NODE}/address/{address}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        balance = response.json().get("balance", 0)
        if float(balance) >= amount:
            return True
    except requests.exceptions.RequestException as e:
        print(f"Request to RPC node failed: {e}")
    return False


def pay_with_bitcoin(bot, chat_id, order_id, amount):
    """
    Sends a payment request to the client and waits for payment to be received.

    :param bot: The Telegram bot instance.
    :param chat_id: The ID of the Telegram chat.
    :param order_id: The ID of the order.
    :param amount: The amount of Bitcoin to pay.
    """
    client_id = f"{chat_id}:{order_id}"
    address = generate_address(client_id)

    bot.send_message(
        chat_id, f"Please send {amount} BTC to the following address:\n\n{address}")

    payment_received = False
    while not payment_received:
        payment_received = check_payment(client_id, amount)
        time.sleep(10)

    bot.send_message(
        chat_id, f"Payment received. Thank you for your purchase!")
