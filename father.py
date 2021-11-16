import datetime
from datetime import date
from datetime import timedelta
import json

birth = datetime.date(1980,6,11)
def calcAge():
    today = datetime.datetime.now()
    return (date.today() - birth) // timedelta(days=365.2425)


father = {
    "name": "Lupin Jr",
    "age": calcAge()
    
}


