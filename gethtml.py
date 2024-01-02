from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = "https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/10/wo/p1afSVQSmuO4huIlQN81o0/0.3.10.7.3.0"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

driver = webdriver.Chrome(options=options)


driver.get(url)

driver.implicitly_wait(10)
# print("success driver", driver)
element = driver.find_element(By.XPATH,"//table[@class='timetable']")

print("printing: ")

# print(element.text)

# html_content = driver.page_source
html_content = element.get_attribute('outerHTML')


soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', class_='timetable')
rows = table.find_all('tr')


# Initialize variables to store parsed information


counter=0
newdict={}
timeslot=[]

# Initialize variables to store parsed information
day = None
name = None
start_time = None
end_time = None

# Iterate over each row in the table
for row in table.find_all('tr'):
    cells = row.find_all('td', class_='timetablecell')
    if(row.find('td',class_='timetable_left')):
        tempx=row.find('td',class_='timetable_left').text.strip().split()
            
    print(cells)
    # Check if the row contains the day information
    if cells is not None:
      
        for i in range(len(cells)):
            if(cells[i].text.strip()!=""):
                print('ye')
                timeslot.append(tempx)
                rv = int(cells[i] ['rowspan'])

                newdict[cells[i].font.text.strip()] = [i,cells[i].font.text.split()[1],timeslot,rv]
            # Check if the row contains the course information
            
            
    timeslot=[]  
            # course_cell = cells[0]
            # if course_cell.a:
            #     name = course_cell.a.text.strip()
            #     if course_cell.font:
            #         if 'Section' in course_cell.font.text:
            #             time_info = course_cell.font.text.split('[')[0].strip().split()
            #             if len(time_info) >= 3:
            #                 start_time, end_time = time_info[-3], time_info[-1]

        # Print the parsed information for this row
    # if day and name and start_time and end_time:
    #         print(f"Day: {day}, Name: {name}, StartTime: {start_time}, EndTime: {end_time}")
F=""
print(newdict)
for keys,values in newdict.items(): 
    F += f'Course: {keys} Day : {values[0]} Start Time ={values[2]} endTime = {values[3]}\n'
    print(F)

    # # Check if the row contains the day information
    # day_cell = cells[0]
    # if day_cell.get('class') and 'timetable_top' in day_cell['class']:
    #     day = day_cell.text.strip()
    
    # # Check if the row contains the course information
    # course_cell = cells[1]
    # if course_cell.a:
    #     name = course_cell.a.text.strip()
    #     if course_cell.font:
    #         if 'Section' in course_cell.font.text:
    #             start_time, end_time = course_cell.font.text.split('[')[0].strip().split()[-3:]

    # # Print the parsed information for this row
    # if day and name and start_time and end_time:
    #     print(f"Day: {day}, Name: {name}, StartTime: {start_time}, EndTime: {end_time}")

# Save the HTML content to a file
with open("example.html", "w", encoding="utf-8") as file:
    file.write(str(F))
with open("dict",'w',encoding='utf-8') as file:
    file.write(str(newdict))

driver.quit()