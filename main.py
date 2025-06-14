from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('ZQ5wXTYi8SMCvL7/7acg3YNVwz58gUDnF6N6vJ62vR5okcnmCq5Q9obtF2Rr31uy0y9KLQAaJCJ81pFmptMZaq12xYxI9eKHOZiNe0SdeLdg3zX/kVVJbBFMICEv8oA7obj1TswCTrzLK/5xIY9zuwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.source.type == "group":
        if event.message.text == "هاي":
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="أهلاً بيك 👋"))

if __name__ == "__main__":
    app.run()