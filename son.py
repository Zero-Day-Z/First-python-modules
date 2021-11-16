import datetime
from datetime import date
from datetime import timedelta
import json

birth = datetime.date(1999,12,30)
def calcAge():
    today = datetime.datetime.now()
    return (date.today() - birth) // timedelta(days=365.2425)


son = {
    "name": "Lupin the 3rd",
    "age": calcAge()
    
}
