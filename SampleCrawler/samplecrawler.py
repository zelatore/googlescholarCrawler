from bs4 import BeautifulSoup
import requests, time
import pandas as pd
import json
import xlsxwriter
from colorama import init, Fore, Back, Style
 
init(autoreset=True)

# Output file setup
# result.xlsx 이름의 Excel 파일을 생성한다. 해당 Excel의 pointer는 'workbook' 이다. 
workbook = xlsxwriter.Workbook('results.xlsx')
""" workbook이 가리키는 Excel 파일에 sheet 를 추가한다. 
    추가하는 sheet 이름은 별도로 설정할 수 있고, 없으면 Default 이름이 들어간다."""
worksheet = workbook.add_worksheet() # default 'sheet1' 로 생성함

# 본격적인 크롤링을 위한 setup
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
pages = int(input("Number of pages: "))
url = "https://scholar.google.com/scholar?start={}&hl=en&as_sdt=0%2C5&q=filetype%3Apdf+%7B%22productivity%22+OR++%22distraction%22+OR+%22interruption%22+OR++%22smartphone+addiction%22+OR+%22smartphone+overuse%22+%7D+AND+%22smartphone%22+AND+%7Bintervention%22+OR+%22behavior+change%22%7D"

data = []
rowNum = 0;
for i in range(0,pages*10+1,10):
    res = requests.get(url.format(i),headers=headers)
    main_soup = BeautifulSoup(res.text, "html.parser")
    divs = main_soup.find_all("div", class_="gs_r gs_or gs_scl")
    for div in divs:
        temp = {}
        h3 = div.find("h3", class_="gs_rt")
        
        if h3.find("a") is not None:
            temp["Link"] = h3.find("a")["href"]       
            temp["Heading"] = h3.find("a").get_text()            
            print(Fore.WHITE+Style.BRIGHT+'Title: '+temp["Heading"])
            print(Fore.CYAN+Style.BRIGHT+'File: '+temp["Link"]+'\n')
                    
            worksheet.write(rowNum,0, temp["Heading"])
            worksheet.write_url(rowNum,1, temp["Link"])
            rowNum+=1
            #data.append(temp)
        """
        try:
            res_link = requests.get(temp["Link"], headers=headers)
            soup_link = BeautifulSoup(res_link.text,"html.parser")
            if "sciencedirect" in temp["Link"]:
                temp["Abstract"] = soup_link.find("div", class_="abstract author").find("div").get_text(strip=True)
            elif "acm" in temp["Link"]:
                temp["Abstract"] = soup_link.find("div", class_="abstractSection abstractInFull").get_text(strip=True)
        except: pass
        """
        #data.append(temp)
        time.sleep(1)
        
workbook.close()

print(Fore.YELLOW+Style.BRIGHT+"Crawling completed!")

'''
with open("data.json", "w") as f:
    json.dump(data,f)

pd.DataFrame(data).to_csv("data.csv", index=False)
'''