from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask("yo")

@app.route('/')
def index():
    url = 'https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/4/wo/zl0CCRssMUa61SIP3TjraM/0.3.10.7.3.0'

    response = requests.get(url)

    if response.status_code==200:
        print("got repsonse 200")
        soup = BeautifulSoup(response.content,'html parser')

        timetable = soup.find(table, class_ ='timetable')

        times=[]
        courses=[]

        for row in timetable.find_all('tr'):
            time_cell = row.find('td',class_='timetable_left')
            if time_cell:
                time_text = time_cell.span.text.strip()
                times.append(time_text)


        print(time_text)
        return time_text
    
    return 'Faikled'

if __name__ == '__main__':
    app.run()