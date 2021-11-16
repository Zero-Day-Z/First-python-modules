import datetime
from datetime import date
from datetime import timedelta
import json

birth = datetime.date(1950,4,18)
def calcAge():
    today = datetime.datetime.now()
    return (date.today() - birth) // timedelta(days=365.2425)


grandfather = {
    "name": "Lupin",
    "age": calcAge()
    
}


