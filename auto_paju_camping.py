from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import urllib.parse

def chrome_driver_on():
    options = Options()
    options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
    options.add_experimental_option("excludeSwitches", ['enable-logging'])  # 불필요한 메시지 제거

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    # 보통 크롬드라이버를 맞춰서 다운 받은 뒤 실행시킨다 하지만 이렇게하면 계속 버전에 맞춰 다운을 받아줘야함
    # 이때 사용할 수있는게 webdriver manager이다
    # 버전업이 되더라도 진행된다

    driver.maximize_window()
    return driver

def paju_reservation(driver, url, input_data, site_info):
    driver = driver
    
    print(input_data,'input_data')
    url_with_params = ''
    params = {'checkdate': input_data.get('reserve_date')}
    params_encoded = urllib.parse.urlencode(params).encode('utf-8')
    url_with_params = url + '?' + params_encoded.decode('utf-8')
    
    driver.get(url_with_params)
    driver.implicitly_wait(time_to_wait=1)

    site_no = site_info.get(input_data.get('site')).get('site_no')
    site_btn_no = site_no if input_data.get('button_cnt') == input_data.get('open_check_body_button_cnt') else site_no - 4

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[5]/div[1]/button["+str(site_btn_no)+"]").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[5]/div["+str(site_no+1)+"]/div["+str(input_data.get('room_no'))+"]/label").click()

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[6]/form/div/div/table/tbody/tr  [1]/td[4]/select").send_keys(input_data.get('reserve_day'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[6]/form/div/div/table/tbody/tr[1]/td[5]/select").send_keys(input_data.get('member'))

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[8]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[9]/div/button").click()

    ## 2번째 PAGE
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[1]/dd[1]/input").send_keys(input_data.get('name'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[1]/dd[2]/input").send_keys(input_data.get('phone'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[2]/dd/input").send_keys(input_data.get('email'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[3]/dd/input").send_keys(input_data.get('birth'))
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/fieldset/div/dl[4]/dd/input[1]").send_keys(input_data.get('car'))

    if input_data.get('local_discount') == 'Y':    
        driver.find_element(By.XPATH, "//*[@id='order_info']/div[2]/div[1]/div[1]/label").click()
        alert = Alert(driver)
        alert.accept()
    
    if input_data.get('needy_discount') == 'Y':
        driver.find_element(By.XPATH, "//*[@id='order_info']/div[2]/div[2]/div[1]/label").click()
        alert = Alert(driver)
        alert.accept()

    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[12]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[14]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[15]/label").click()
    driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/form/div[16]/button").click()
