from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# selenium3, 4

options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option(
    "excludeSwitches", ['enable-logging'])  # 불필요한 메시지 제거


print(options)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)
# 보통 크롬드라이버를 맞춰서 다운 받은 뒤 실행시킨다 하지만 이렇게하면 계속 버전에 맞춰 다운을 받아줘야함
# 이때 사용할 수있는게 webdriver manager이다
# 버전업이 되더라도 진행된다

driver.maximize_window()

# 일자
tDate = "2023-03-15"
# 사이트선택
# 1:전체, 2:평화, 3:힐링, 4:누리, 5:에코, 6:렌탈A, 7:렌탈B, 8:카라반A, 9:카라반B, 10:카라반C
tSite = "4"
# 자리번호
tNo = "15"
# 박수
# 1: 1박2일, 2:2박3일
tDay = "2"
# 인원(대인으로 퉁)
tMember = "4"

# 예약자 정보
tName = "이름"
tPhone = "010111122222"
tEmail = "이메일"
tBirth = "19000101" #yyyymmdd
tCar = "11허1111"


driver.get("https://imjingakcamping.co.kr/resv/res_01.html?checkdate="+tDate+"#cs")
driver.implicitly_wait(time_to_wait=1)

driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[5]/div[1]/button["+tSite+"]").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[5]/div["+str(int(tSite)+1)+"]/div["+tNo+"]/label").click()

driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[6]/form/div/div/table/tbody/tr[1]/td[4]/select").send_keys(tDay)
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[6]/form/div/div/table/tbody/tr[1]/td[5]/select").send_keys(tMember)

driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[8]/label").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[9]/div/button").click()

## 2번째 PAGE
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[1]/dd[1]/input").send_keys(tName)
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[1]/dd[2]/input").send_keys(tPhone)
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[2]/dd/input").send_keys(tEmail)
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[3]/dd/input").send_keys(tBirth)
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[4]/dd/input[1]").send_keys(tCar)

driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[12]/label").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[14]/label").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[15]/label").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[16]/button").click()
