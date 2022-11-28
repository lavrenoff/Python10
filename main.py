import requests as rq
from datetime import datetime as dt
import telebot
from auth_data import token
import time

globalid = 0


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        global globalid
        globalid = message.chat.id
        bot.send_message(globalid, f"Hello={message.chat.id}")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = rq.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(message.chat.id,
                                 f"{dt.now().strftime('%Y-%m-%h %H:%M:%S')}-{sell_price}")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Код ошибки 001!")
        else:
            bot.send_message(
                message.chat.id, f"Незнакомый запрос!")

    # def tr():
    #     print("ddddd")
    #     bot.send_message(globalid, "Тест1")

    bot.polling()


def tr(token):
    bot = telebot.TeleBot(token)
    while True:
        bot.send_message(
            235947448, f"{dt.now().strftime('%Y-%m-%h %H:%M:%S')}=тест1")
        time.sleep(1)

#     @bot.message_handler(commands=["start"])
#     def start_message(message):
#         bot.send_message(message.chat.id, "Hello")

#     @bot.message_handler(content_types=["text"])
#     def msg(message):
#         bot.send_message(message.chat.id, str)


if __name__ == "__main__":
    # telegram_bot(token)

    tr(token)
