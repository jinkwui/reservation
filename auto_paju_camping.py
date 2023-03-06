from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def chrome_driver_on():
    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
    options.add_experimental_option(
        "excludeSwitches", ['enable-logging'])  # 불필요한 메시지 제거

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    # 보통 크롬드라이버를 맞춰서 다운 받은 뒤 실행시킨다 하지만 이렇게하면 계속 버전에 맞춰 다운을 받아줘야함
    # 이때 사용할 수있는게 webdriver manager이다
    # 버전업이 되더라도 진행된다

    driver.maximize_window()
    return driver

def paju_reservation(driver, url, json_data):
    driver = driver

    driver.get(url)
    driver.implicitly_wait(time_to_wait=1)

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[5]/div[1]/button["+json_data.get('check_site')+"]").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[5]/div["+str(int(json_data.get('check_site'))+1)+"]/div["+json_data.get('check_room_no')+"]/label").click()

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[6]/form/div/div/table/tbody/tr[1]/td[4]/select").send_keys(json_data.get('check_day'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[6]/form/div/div/table/tbody/tr[1]/td[5]/select").send_keys(json_data.get('check_member'))

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[8]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[9]/div/button").click()

    ## 2번째 PAGE
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[1]/dd[1]/input").send_keys(json_data.get('check_name'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[1]/dd[2]/input").send_keys(json_data.get('check_phone'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[2]/dd/input").send_keys(json_data.get('check_email'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[3]/dd/input").send_keys(json_data.get('check_email'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[4]/dd/input[1]").send_keys(json_data.get('check_car'))

    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[12]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[14]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[15]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[16]/button").click()
