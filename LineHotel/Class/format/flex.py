
class flex_friend:

    def _IN_header(_name,_sname):
        
        return {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": _name,
            "align": "end",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "hello, world",
            "contents": [
              {
                "type": "span",
                "text": "綽號："
              },
              {
                "type": "span",
                "text": _sname
              }
            ],
            "size": "xxs",
            "gravity": "bottom",
            "align": "start",
            "style": "italic"}
        ],
        "paddingTop": "10px",
        "paddingBottom": "1px"
      }

    def _IN_hero(_Last_time):
        return{
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "上次見面",
            "size": "xxs",
            "contents": [
              {
                "type": "span",
                "text": "上次見面"
              },
              {
                "type": "span",
                "text": "："
              },
              {
                "type": "span",
                "text": _Last_time
              },
              {
                "type": "span",
                "text": str(3-3),
                "style": "italic",
                "decoration": "underline"
              },
              {
                "type": "span",
                "text": "日前"
              }
            ],
            "align": "center",
            "gravity": "bottom"
          }]}

    def _IN_body(_img,_gender,_personality,_work,_birthday,_interest):
        return{
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": _img,
                    "aspectMode": "cover",
                    "size": "full"
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "contents": [
                          {
                            "type": "span",
                            "text": "性別",
                            "weight": "bold",
                            "color": "#000000"
                          },
                          {
                            "type": "span",
                            "text": "："
                          },
                          {
                            "type": "span",
                            "text": _gender
                          }
                        ],
                        "size": "sm",
                        "wrap": True
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "contents": [
                          {
                            "type": "span",
                            "text": "個性",
                            "weight": "bold",
                            "color": "#000000"
                          },
                          {
                            "type": "span",
                            "text": "："
                          },
                          {
                            "type": "span",
                            "text": _personality
                          }
                        ],
                        "size": "sm",
                        "wrap": True
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "contents": [
                          {
                            "type": "span",
                            "text": "工作",
                            "weight": "bold",
                            "color": "#000000"
                          },
                          {
                            "type": "span",
                            "text": "："
                          },
                          {
                            "type": "span",
                            "text": _work
                          }
                        ],
                        "size": "sm",
                        "wrap": True
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "contents": [
                          {
                            "type": "span",
                            "text": "生日",
                            "weight": "bold",
                            "color": "#000000"
                          },
                          {
                            "type": "span",
                            "text": "："
                          },
                          {
                            "type": "span",
                            "text": _birthday
                          },
                          {
                            "type": "span",
                            "text": str(30-5),
                            "size": "xxs"
                          }
                        ],
                        "size": "sm",
                        "wrap": True
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "contents": [
                          {
                            "type": "span",
                            "text": "興趣",
                            "weight": "bold",
                            "color": "#000000"
                          },
                          {
                            "type": "span",
                            "text": "："
                          },
                          {
                            "type": "span",
                            "text": str("#"+"#".join(_interest))
                          }
                        ],
                        "size": "sm",
                        "wrap": True
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          },
          {
            "type": "separator",
            "margin": "xs",
            "color": "#000000"
          }
        ],
        "paddingAll": "0px"
      }
    
    def _IN_footer(_Else,_contact):
        print(str(_contact))
        return  {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "備註",
            "weight": "bold",
            "contents": [
              {
                "type": "span",
                "text": "備註："
              }
            ]
          },
          {
            "type": "text",
            "text": "hello, world",
            "offsetStart": "50px",
            "contents": [
              {
                "type": "span",
                "text": _Else
              }
            ],
            "wrap": True
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "修改信息",
              "uri": "http://linecorp.com/"
            }
          },
          {
        "type": "button",
        "action": {
          "type": "message",
          "label": "聯絡方式",
          "text": "連絡電話："+_contact['number']+'\n'+"Email："+_contact['email']+'\n'+'地址：'+_contact['address']
        },
        "style": "primary"
      }
        ]
      }

    def output(_friend):
        contents=[]
        for fd in _friend:
            #print(str(page))
            contents.append(
                        {
                            "type":"bubble",
                            "header":flex_friend._IN_header(fd['name'],fd['sname']),

                            "hero":flex_friend._IN_hero(fd['Last_time']),

                            "body":flex_friend._IN_body(fd['img'],
                                                        fd['gender'],
                                                        fd['personality'],
                                                        fd['work'],
                                                        fd['bitrhday'],
                                                        fd['interest']),
                            "footer":flex_friend._IN_footer(fd['else'],fd['contact']),
                            "styles":fd['styles'],
                        })    

        _data={ "type":"carousel","contents":contents}

        return _data


class flex_title_events():

    def _IN_header(_month):
      return {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": _month,
        "align": "center",
        "color": "#FFFFFF"
      }
    ],
    "paddingAll": "xs"
  }
    
    def _IN_hero(_dtod):
      return{
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": _dtod,
        "size": "3xl",
        "align": "center",
        "color": "#FFFFFF",
        "margin": "xxl",
        "weight": "bold",
        "style": "italic"
      },
      {
        "type": "separator",
        "color": "#000000"
      }
    ],
        "spacing": "50px"
  }

    def _IN_body():
      return{
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "空閒日：",
        "offsetTop": "-15px",
        "offsetStart": "-15px",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": "hello, worl"
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#666666"
      }
    ]
  }

    def _IN_footer():
      return{
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "未安排：",
        "offsetTop": "-12px",
        "offsetStart": "-5px",
        "weight": "bold",
        "style": "italic"
      },
      {
        "type": "text",
        "text": "hello, world",
        "offsetStart": "10px"
      }
    ]
  }

    def output(_title):
        contents=[]
        for te in _title:
            #print(str(page))
            contents.append(
                        {
                            "type":"bubble",

                            "header":flex_title_events._IN_header(te['month']),

                            "hero":flex_title_events._IN_hero(te['dtod']),
                            "size": "micro",
                            "styles":te['styles'],
                        })    

        _data={ "type":"carousel","contents":contents}

        return _data



'''
{
  "type": "bubble",
  "header": 
  "hero": ,
  "body": ,
  "footer": ,
  "styles": {
    "header": {
      "backgroundColor": "#0000A5"
    },
    "hero": {
      "backgroundColor": "#1010FF"
    },
    "footer": {
      "backgroundColor": "#AAAAFF"
    }
  }
}


'''





class flex_events():

    def _IN_header():
      return""
    
    def _IN_hero():
      return""

    def _IN_body():
      return""

    def _IN_footer():
      return""

    def output():
      return""