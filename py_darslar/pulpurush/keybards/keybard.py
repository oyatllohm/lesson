from telebot import types


markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True) 
# bu ^ kinopka ichun maydon
pr1 = types.KeyboardButton("makkah")
pr2 = types.KeyboardButton("andijon")
pr3 = types.KeyboardButton("namangan")
pr4 = types.KeyboardButton("fargona")
#  bular ^ kinopka
markup.add(pr1,pr2,pr3,pr4)
# bu kinopkani ektanga chiqaradi