from bs4 import BeautifulSoup
import requests
import pyfiglet
from time import sleep
from os import system, name

disp = pyfiglet.figlet_format("NSE\n Live", font="banner3-D")
print(disp)
print("Use Ticker Code For Better Results")

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
        
def search():
  stock = input("\nSearch  :  ")
  url1 = "https://www.screener.in/company/"+stock+"/"
  html = requests.get(url1).content
  soup = BeautifulSoup(html, 'html.parser')  
  m_data = soup.find_all('span' ,class_="name")
  m_value = soup.find_all('span' ,class_="number")
  
  print(m_data[1].string.strip() + "  -> ₹" + m_value[1].string.strip())
  print(m_data[7].string.strip() +" -> "+m_value[7].string.strip() +"%")
  print(m_data[0].string.strip()+" -> "+m_value[0].string.strip()+"Cr.")



for sea in range(7):
     try:
         search() 
         sleep(1)
         input()
         clear()
         print(disp)
     except:
         print("\n\tNot Found! ")
         sleep(1)
         clear()
         print(disp)


print("\tSeason Timeout, Restart Program!!! ")  
print(pyfiglet.figlet_format("Star + Follow + Fork + :) "))

  