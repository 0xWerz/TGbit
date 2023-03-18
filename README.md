# Telegram Bot Shop

This is a simple skeleton Telegram bot shop that accepts testnet BTC nodes. It allows customers to place orders, and provides them with a Bitcoin address where they can send payment and it verify it.

## Installation

1. Clone the repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Create a `.env` file and fill in the necessary configuration variables. An example `config.py` file has been provided for you.
4. Run the bot using `python main.py`.

## Usage

-   For chat help `/help`

1. Start a chat with the bot.
2. Type `/start` to see the list of available products.
3. Type the product number to place an order for the specified product.
4. Follow the bot's instructions to complete payment.

## Configuration

The following configuration variables are required in the `.env` file:

-   `BOT_TOKEN`: The API token for your Telegram bot.
-   `RPC_NODE`: The URL for the Bitcoin RPC node.
-   `BITCOIN_ADDRESS`: Your Bitcoin address for receiving payments.
-   `BLOCK_IO_API_KEY`: Your Block.io API key.
-   `BLOCK_IO_PIN`: Your Block.io PIN.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. If you want to contribute code, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
