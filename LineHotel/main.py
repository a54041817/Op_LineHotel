import re
from sys import meta_path
from flask import Flask, request, abort,render_template,jsonify

from linebot import (
    LineBotApi, WebhookHandler,api
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage,PostbackEvent,PostbackTemplateAction,rich_menu
)
from datetime import timedelta, date
import _post
import _linebot,json


app = Flask(__name__)

line_bot_api = LineBotApi('*********************************')
handler = WebhookHandler('*****************************************************')


@app.route("/",methods=['GET'])
def main():
    data=["",date.today(),date.today()+timedelta(days=1),1]
    return render_template("hotel/index.html",data=data)

@app.route("/hotelBoss/index.html",methods=['GET'])
def hotelBoss_Login():
    #return render_template("Login.html")
    return render_template("hotelBoss/index.html")

@app.route("/hotelBoss/user_data.html",methods=['GET'])
def hotelBoss_index():
    return render_template("hotelBoss/index.html")


 
@app.route("/hotel.html",methods=['GET'])
def hotel_get():
    page=request.args.get('liff.state')
    rr=request.args.get('code')
    if(page==None and rr==None):
        data=[request.values['poin'],
        request.values['data_s'],
        request.values['data_d'],
        request.values['man_Len'],
        _post.hotel_id(request.values['id']),
        request.values['id']]
        return render_template("hotel/hotel.html",data=data)
    else:
        print("\n\n\n\n\n\n\n\n\n")
        return render_template("hotel/hotel.html",data=[None,None,None,None,None])
        

@app.route("/api/GetBossData",methods=['POST'])
def Get_boss_data():
    data = request.get_json()
    res_data = _post.Boss.Get_Hotel_data(data['userID']) # json資料物件'''
    return jsonify(res_data)

@app.route("/chick_hotel_pag.html",methods=['POST'])
def page_chick_hotel():
    #
    return render_template("hotel/chick_hotel.html",data=request.values['key'])

@app.route("/Search.html",methods=['GET'])
def page_Search():
    data=[request.values['poin'],
            request.values['data_s'],
            request.values['data_d'],
            request.values['man_Len'],
            str(_post.search_hotel(request.values['poin']))]
    return render_template("hotel/Search.html",data=data)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@app.route("/",methods=['POST'])
def post():
    _post.post()
  #ff=request.values['orem']
  #print(ff)


@handler.add(MessageEvent)
def handle_message(event):
    _linebot.data(event)




if __name__ == "__main__":
    app.run(debug=True)
    app.send_file_max_age_default = timedelta(seconds=1)
