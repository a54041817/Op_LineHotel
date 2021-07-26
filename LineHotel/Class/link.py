import Class.serverData as sd
import base64
import random
from datetime import datetime


_seed_const="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def hotel_id(id):
  _data=sd.read(f"/hotel/{id}")
  return _data

def search_hotle(poin):
  _data=sd.read("/search_hotel")
  ret_data={}
  _ke=0
  for k in _data.keys():
    if(str(k).find(poin)!=-1):
      _ke+=1
      _id=_data[k]
      _sc_img=sd.read(f"/hotel/{_id}/img/main")
      ret_data[k]={"id":_data[k],"img":_sc_img}
      ret_data['len']=_ke#_ke
  return ret_data


class Boss:
  def get_boss_hotel_list(userID):
    _data=sd.read(f"/Boss_list/{userID}")
    if(_data is None):
      _data=[]
    print(str(_data))
    return {'len':len(_data),'data':_data}
    



def reg(userID,NAME):
  sd.writ("/user",{userID:{
                    'name':NAME
  }})
  
def reg_NFC(userID,nfcID):
  sd.writ("/nfcID",{nfcID:userID})

  sd.addList("/user/{0}".format(userID),'car',nfcID)

