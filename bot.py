from telebot import TeleBot, types
from colorama import Fore, init
import os

init(autoreset=True)

TOKEN = "8881766204:AAFabfRij0KbLF9wYXFTJ2m8LID5Kgn-dMc"

bot = TeleBot(TOKEN)

os.system("cls")

banner = f"""{Fore.CYAN}
"""
print(banner)

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

"""
    )





print(Fore.YELLOW + "[*] Waiting for users...")

bot.infinity_polling()
