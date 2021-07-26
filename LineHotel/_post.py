from typing import ClassVar
from Class import link as link
def post():
    return 0

def search_hotel(poin):
    data=link.search_hotle(poin)
    return data

def hotel_id(id):
    data=link.hotel_id(id)
    return data

class Boss:

    def Get_Hotel_data(userID):
        data=link.Boss.get_boss_hotel_list(userID)
        return data