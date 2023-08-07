from auto_paju_camping import *
from open_check import *
import constant

def main():
    url = 'https://imjingakcamping.co.kr/resv/res_01.html'

    input_data = {
        # 수정 필요
        'reserve_date': '2023-09-05',
        'site': '누리',
        'room_no': '22',
        'reserve_day': '2',
        'member': '4',
        'name': '홍길동',
        'phone': '01011112222',
        'email': 'hong@test.com',
        'birth': '500101',
        'car': '11쀍1111',

        # 아래는 수정 안하고 필요시 할 것
        'open_check_body_str': 'location.href="/resv/res_01.html";',
        'open_check_body_button': '/html/body/div[4]/div[1]/div/div[5]/div[1]/button',
        'open_check_body_button_cnt': 10,
        'save_file_yn': 'N',
        'local_discount': 'N',
        'needy_discount': 'N'
    }

    #print(search_site_info(input_data['site']))

    driver = chrome_driver_on()
    
    if search_site_info(input_data['site']) is not None and open_paju_check(url, input_data, constant.PAJU_SITE_INFO) == True:
        paju_reservation(driver, url, input_data, constant.PAJU_SITE_INFO)
    else:
        print('예약 불가')

def search_site_info(site):
    for key, value in constant.PAJU_SITE_INFO.items():
        if key == site:
            return value

if __name__ == '__main__':
    main()
