from auto_paju_camping import *
from open_check import *

def main():
    url = 'https://imjingakcamping.co.kr/resv/res_01.html?checkdate=2023-04-22#cs'
    # 일자 - check_date
    # 사이트선택 - check_site
    #   1:전체, 2:평화, 3:힐링, 4:누리, 5:에코, 6:렌탈A, 7:렌탈B, 8:카라반A, 9:카라반B, 10:카라반C
    # 자리번호 - check_room_no
    # 박수 - check_day
    #   1: 1박2일, 2:2박3일
    # 인원(대인으로 퉁) - check_member
    # 예약자 정보 - check_name, check_phone, check_email, check_birth(yyyymmdd), check_car
    json_data = {
        'check_date': '2023-04-22',
        'check_site': '10',
        'check_room_no': '1',
        'check_day': '1',
        'check_member': '4',
        'check_name': '홍길동',
        'check_phone': '01011112222',
        'check_email': '홍길동@naver.com',
        'check_birth': '19000101',
        'check_car': '00하0001'
    }
    check_json_data = {
        'check_body_str': 'location.href="/resv/res_01.html";'
    }

    driver = chrome_driver_on()
    
    if open_paju_check(url, check_json_data) == True:
       paju_reservation(driver, url, json_data)

if __name__ == '__main__':
    main()


