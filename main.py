from flask import Flask, request
from flask_frozen import Freezer
import requests

app = Flask(__name__)


def send_message(chat_id, text):
    method = "sendMessage"
    token = "1682831725:AAEXtMpakbJn5bNG731mhpZcduXiAxmfmSs"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


def send_notification(mod, obj):
    carlist = {'585':{"driver_tgid": 54436582}}
    match mod:
        case 'onl':
            send_message(carlist[obj]['driver_tgid'], f'Тестим post-запросы из Виалона\n\nСейчас Рено 585 должна была появится в сети🟢')
        case 'offl':
            send_message(carlist[obj]['driver_tgid'], f'Тестим post-запросы из Виалона\n\nСейчас Рено 585 должна была пропасть из сети🔴')
        case _:
            print('нет такого mod', mod)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        if "message" in request.json:
            chat_id = request.json["message"]["chat"]["id"]
            send_message(chat_id, "pong")
    return {"ok": True}


@app.route("/wi", methods=["GET", "POST"])
def wi():
    if request.method == "POST":
        print(request.args)
        send_notification(request.args.get('mod'), request.args.get('obj'))
    return {"ok": True}


if __name__ == '__main__':
    app.run(port=8080)
    Freezer(app).freeze()