import json
from linebot import LineBotApi
from linebot.models import TextSendMessage


file = open('info.json','r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text="Enpit参加 \n Toeic750 \n 応用技術者試験 \n Line bot開発(Line Api) \n ハッカソン参加 \n 確率論アルゴ回収 \n 講義gpa3.5")
    line_bot_api.push_message(USER_ID,messages=messages)
    
if __name__ == "__main__":
    main()
