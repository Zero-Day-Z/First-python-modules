#import modules
import datetime
from datetime import date
from datetime import timedelta
import json
import grandfather
import father
import son

grandfatherfinal = {
"name": grandfather.grandfather["name"],
"age": grandfather.grandfather["age"]
}

fatherfinal = {
"name":father.father["name"],
"age": father.father["age"]
}

sonfinal = {
"name": son.son["name"],
"age": son.son["age"]
}
GF = json.dumps(grandfatherfinal)
print(GF)
F = json.dumps(fatherfinal)
print(F)

S = json.dumps(sonfinal)
print(S)