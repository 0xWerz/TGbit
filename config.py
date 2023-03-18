import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BTC_ADDRESS = os.getenv("BITCOIN_ADDRESS")
BITCOIN_ADDRESS = os.getenv("BITCOIN_ADDRESS")
RPC_NODE = os.getenv("RPC_NODE")
BLOCK_IO_API_KEY = os.getenv("BLOCK_IO_API_KEY")
BLOCK_IO_SECRET_PIN = os.getenv("BLOCK_IO_SECRET_PIN")
