import datetime
import pandas as pd
import webbrowser
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# ---------------Set your config---------------

# Select your appointment type
# OUT OF STATE TRANSFERS = 7
# REAL ID = 12
# LICENSE OR NON DRIVER ID RENEWAL = 11
# CDL RENEWAL = 6
# CDL PERMIT OR ADD/REMOVE ENDORSEMENT = 14
# PERMIT/LICENSE OR ADD/REMOVE ENDORSEMENT (NON CDL) = 15
# NON-DRIVER ID (INITIAL & DOWNGRADE) = 16
# NEW TITLE OR REGISTRATION = 8
# SENIOR NEW TITLE OR REGISTRATION (65+) = 9
# TITLE DUPLICATE/ REPLACEMENT = 13
# REGISTRATION RENEWAL = 10
appointment_type = 11

prefer_dmv = ['Bayonne', 'Newark', 'Rahway', 'North Bergen', 'Lodi', 'Paterson', 'Wayne', 'Edison', 'South Plainfield', 'Randolph', 'Oakland']
prefer_starttime = '2021-03-20 00:00:00'
prefer_endtime = '2021-04-15 00:00:00'
fname = 'YenChing'
lname = 'Tseng'
email = 'speculate123@gmail.com'
phone = '7027415834'
driverlicense = 'T80157890001951'

# ---------------------------------------------
    
def login():
    driver.find_element_by_id('firstName').send_keys(fname)
    driver.find_element_by_id('lastName').send_keys(lname)
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('phone').send_keys(phone)
    driver.find_element_by_id('driverLicense').send_keys(driverlicense)
    driver.find_element_by_name('Attest').click()
    driver.find_element_by_css_selector("input[value='Submit'][type='submit']").click()
    
import winsound
duration = 1000  # milliseconds
freq = 900  # Hz

# 透過Browser Driver 開啟 Chrome
driver = webdriver.Chrome(r"C:\Users\yt335\Desktop\chromedriver.exe")
driver.set_window_position(0, 0)
driver.set_window_size(360, 768)
# 前往特定網址
default_url = "https://telegov.njportal.com/njmvc/AppointmentWizard/" + str(appointment_type)
driver.get(default_url)

found = False

while found==False:
    while True:
        try:
            check = driver.find_element_by_link_text("CHECK EARLIEST AVAILABILITY")
        except: 
            break
        time.sleep(0.2)
        check.click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    dmvs = soup.find_all('span', style='font-weight:bold;')
    date = soup.find_all('span', id=lambda x: x and x.startswith('dateText'))
    df = pd.DataFrame({'id':[], 'DMV':[], 'time':[]})
    web = []
    for i in range(len(dmvs)):
        if 'Next Available:' in date[i].getText():
            dateformat = pd.to_datetime(date[i].getText()[16:])
            new = {'id':date[i].get('id')[-5:-2], 'DMV':dmvs[i].getText().replace(' - License or Non Driver ID Renewal', ''), 'time':dateformat}
            df = df.append(new, ignore_index=True)     
    df.sort_values(['time'], inplace=True)
    print(df)
    prefer = df[df['DMV'].isin(prefer_dmv)]
    for ti in range(len(prefer)):
        if (prefer.iloc[ti,2] > pd.to_datetime(prefer_starttime)) & (prefer.iloc[ti,2] < pd.to_datetime(prefer_endtime)):
            found = True
            url = 'https://telegov.njportal.com/njmvc/AppointmentWizard/11/' + str(prefer.iloc[ti,0]) + '/' + str(prefer.iloc[ti,2])[:10] + '/' + str(prefer.iloc[ti,2])[11:13] + str(prefer.iloc[ti,2])[14:16]
            driver.get(url)
            login()
            winsound.Beep(freq, duration)
    driver.get(default_url)
    time.sleep(15)
       
    

    

    






