import requests
import time
import telebot 
import random
# habar= "https://api.telegram.org/bot5258610079:AAHsP6BtBZQHUj8FBAtB7lNSpTaFp4mWxm8/sendmessage?chat_id=1038994072&text=assalomualekum"

token = "5258610079:AAHsP6BtBZQHUj8FBAtB7lNSpTaFp4mWxm8"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    javoblar = ["assalamu alekum","nimagap","qovoqmiyya","tentak ekansan",
    "sal oylanib yoz","kulgimni qistatma","men shahmatga qiziqmiman",
    "sal g'alati ekansiz" , "kop gaprma","jonga tegdin","kechirin","uzur"]
    hat = random.choice(javoblar)
    text= message.text
    bot.send_message(chat_id=1038994072,text=hat.title())

bot.polling()





# server = f"https://api.telegram.org/bot{token}/getUpdates"
# r = requests.get(server)
# print(r.json()["result"][0]['message']['date'])

# may_id = 1038994072
# while True:
#     r = requests.get(server)
#     print(r.json()["result"][0]['message']['text'])
#     time.sleep(1)

# def ohshahs(word,orginalword):
#     x=len(word)
#     y=len(orginalword)
#     yuz = 100
#     foiz = 0
#     hisob = -1
#     if x == y:
#         for i in word:
#             hisob+=1
#             if i == orginalword[hisob]:
#                 foiz+=1
#     else: 
#         return print("satirlardagi hariflarini soni ten emas")
#     print(f"satirlar {yuz/x*foiz}% ohshash {word}  {orginalword} ")
# ohshahs("andijon","andajon")



# a = {'ok': True, 'result': [{'update_id': 379829642, 'message': {'message_id': 270, 'from': {'id': 1038994072, 'is_bot': False, 'first_name': 'Oyatillo', 'language_code': 'ru'}, 'chat': {'id': 1038994072, 'first_name': 'Oyatillo', 'type': 'private'}, 'date': 1642692967, 'text': 'aoioih😰awefgihogi'}}]}
# print(a['result'][0]['message']['date'])


