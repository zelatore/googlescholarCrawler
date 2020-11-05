import time
from selenium import webdriver
 
driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
 
# 구글에 접속
driver.get('http://www.google.com/')
 
# 2초간 대기 (웹 브라우저가 켜지는 것을 기다립니다.)
time.sleep(2)
 
# element name이 q인 곳을 찾습니다. (구글 검색창의 html 인풋태그 name은 'q'로 되어 있습니다.)
elem = driver.find_element_by_name('q')
 
# 검색 키워드 입력, 실행
elem.send_keys('Wordbe')
elem.submit()
 
# 5초간 동작하는 것을 보고 종료
time.sleep(5)
driver.quit()