import requests
from fileinput import filename 
import telebot
from telnetlib import*
from config import *
import config as cf
from namaztimes import*
# from keybards.keybard import name,hello
# import keybards
# from keybards import keybard
# from keybards import markup

# print(keybard.hello())
# print(hello())

# print(__name__)
# if __name__ == "__main__":
#     print("bu imprt qilimmagan nomi maybot fayil")
# else:
#     print("bu import qilingan")

bot = telebot.TeleBot(cf.token)


@bot.message_handler(commands=["start"])
def salom(message):
    user_id = message.from_user.id
    text= "<b>assalomu alekum men namoz vaqtlardan habar brruchi botman\n  quydagi tugmalarni tallang</b> "
    bot.send_message(chat_id=message.from_user.id,text=text, parse_mode="HTML", reply_markup=markup)



@bot.message_handler(content_types=["text"])
def echo(message):
    text = message.text
    # print(text)
    filename ="users.txt"
    if text == "andijon":
        filename = "andijon.txt"
    elif text == "namangan":
        filename = "namangan.txt"
    elif text == "fargona":
        filename = "fargona.txt"
    else :
        filename = "hato.txt"

    f = open(f"{filename}" , "rb" )
    bot.send_document(1038994072,f)
    # bot.send_message(chat_id=1038994072,text=text)
if __name__ == "__main__":
    bot.polling()


