from telebot import TeleBot, types
from colorama import Fore, init
import os

init(autoreset=True)

TOKEN = "8881766204:AAFabfRij0KbLF9wYXFTJ2m8LID5Kgn-dMc"

bot = TeleBot(TOKEN)

os.system("cls")

banner = f"""{Fore.CYAN}

████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

"""

print(banner)
print(Fore.GREEN + "[+] Bot started successfully")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "📢 Группа 1",
        url="https://t.me/+_xqH4QJodgE2Y2Ri"
    )
    
    btn2 = types.InlineKeyboardButton(
        "📢 Группа 2",
        url="https://t.me/+VW4ASW0N6bExZDhi"
    )
    btn3 = types.InlineKeyboardButton(
        "⚙️ Разное",
        url="https://t.me/+uXR4zgOUbDJkM2Qy"
    )

    

    keyboard.add(btn1, btn2)
    keyboard.add(btn3)

    bot.send_message(
    message.chat.id,
    f"""
🔥 Привет! тут все что нужно))) 

""",
    reply_markup=keyboard
)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        """
📚 Commands:

/start - Launch bot
/help - Show help
/menu - Open menu
"""
    )


@bot.message_handler(commands=['menu'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row("👤 Profile", "ℹ️ Info")
    keyboard.row("⚙️ Settings", "❌ Exit")

    bot.send_message(
        message.chat.id,
        "⚡ Main Menu",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    if call.data == "help":
        bot.answer_callback_query(
            call.id,
            "Opening help..."
        )

        bot.send_message(
            call.message.chat.id,
            "📚 Use /menu to open menu"
        )

    elif call.data == "menu":
        bot.answer_callback_query(
            call.id,
            "Opening menu..."
        )

        menu(call.message)


@bot.message_handler(func=lambda m: True)
def all_messages(message):

    if message.text == "👤 Profile":
        bot.send_message(
            message.chat.id,
            f"""
👤 Your profile

ID: {message.from_user.id}
Name: {message.from_user.first_name}
"""
        )

    elif message.text == "ℹ️ Info":
        bot.send_message(
            message.chat.id,
            "🤖 Demo styled Telegram bot"
        )

    elif message.text == "⚙️ Settings":
        bot.send_message(
            message.chat.id,
            "⚙️ Settings section"
        )

    elif message.text == "❌ Exit":
        bot.send_message(
            message.chat.id,
            "👋 Bye!"
        )


print(Fore.YELLOW + "[*] Waiting for users...")

bot.infinity_polling()