import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define your bot token
BOT_TOKEN = '7339929733:AAHdD-YGmYF2Pu6XRyw1XBZfifjQq__Gt9Q'

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your entertainment bot. Type /joke to get a joke, /trivia for trivia, or /quiz to start a quiz.')

def joke(update: Update, context: CallbackContext) -> None:
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised."
    ]
    update.message.reply_text(random.choice(jokes))

def trivia(update: Update, context: CallbackContext) -> None:
    trivia_questions = [
        "What is the capital of France? (A) Paris (B) London (C) Rome",
        "Who wrote 'To Kill a Mockingbird'? (A) Harper Lee (B) J.K. Rowling (C) Ernest Hemingway"
    ]
    update.message.reply_text(random.choice(trivia_questions))

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("joke", joke))
    dispatcher.add_handler(CommandHandler("trivia", trivia))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
