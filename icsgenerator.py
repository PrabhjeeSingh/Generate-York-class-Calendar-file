from ics import Event, Calendar
from datetime import datetime

x="fall"
if(x=="fall"):
    start_date= datetime(datetime.year,9,1)
    end_date = datetime(datetime.year,12,31)
elif(x=="winter"):
    start_date= datetime(datetime.year,1,1)
    end_date = datetime(datetime.year,4,31)

elif(x=="summer"):
    start_date= datetime(datetime.year,5,1)
    end_date = datetime(datetime.year,8,31)


else:
    start_date= datetime(datetime.year,datetime.month,1)
    end_date= datetime(datetime.year,datetime.month,31)


def getdate(day):
    return

cal = Calendar()
newdict={{'FA THEA 3060  3.00 Section A Term F   Laboratory 03  [Keele: CFT  138      ]': [2, 'THEA', [['8:30', '-', '9:00']], 6], 'LE EECS 3401  3.00 Section A Term F   Lecture [Keele: LSB  105      ]': [2, 'EECS', [['14:30', '-', '15:00'], ['14:30', '-', '15:00']], 3], 'LE EECS 3215  4.00 Section A Term F   Laboratory 02  [Keele: LAS  1004     ]': [4, 'EECS', [['16:30', '-', '17:00']], 6], 'LE EECS 3421  3.00 Section A Term F   Lecture [Keele: LSB  103      ]': [0, 'EECS', [['17:30', '-', '18:00'], ['17:30', '-', '18:00'], ['17:30', '-', '18:00']], 3], 'LE EECS 3421  3.00 Section A Term F   Lecture [Keele: CLH  H        ]': [2, 'EECS', [['17:30', '-', '18:00'], ['17:30', '-', '18:00'], ['17:30', '-', '18:00']], 3], 'LE EECS 3215  4.00 Section A Term F   Lecture [Keele: SLH  B        ]': [3, 'EECS', [['17:30', '-', '18:00'], ['17:30', '-', '18:00'], ['17:30', '-', '18:00']], 6]}}

for key,val in newdict.items():
    event =Event()
    event.name= key
    event.begin=val[2]
    event.description = key.split()[2:]
    event.rule = {'freq':'weekly'}
    
    cal.events.add(event)









