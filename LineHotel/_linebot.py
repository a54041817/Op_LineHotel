from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage
)
from Class import link as link
def data(event):
    userID=event.source.user_id
    text=event.message.text
    if(text[0]=="/"):
        
        test(text[1],text[3:],userID)

    return 0

def test(k,text,userID):
    print(text)
    if(k=='a'):
        link.reg(userID,text)

    if(k=='k'):
        link.reg_NFC(userID,text)



    print("test:{0}".format(str))