from lxml import html
import urllib.request
import urllib.parse
import time
import ssl

def open_paju_check(url, input_data, site_info):

    counter = 0
    context = ssl._create_unverified_context()

    while True:
        url_with_params = ''
        params = {'checkdate': input_data.get('reserve_date')}
        params_encoded = urllib.parse.urlencode(params).encode('utf-8')
        url_with_params = url + '?' + params_encoded.decode('utf-8')
        
        request = urllib.request.Request(url_with_params, None)
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        response = urllib.request.urlopen(request, context=context)
        body = response.read()  # return type bytes

        if input_data.get('save_file_yn') == 'Y':
            save_file(body.decode('euc-kr'), time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".txt")

        # 문자열에 포함되어 있는지 확인
        if body.decode('euc-kr').find(input_data.get('open_check_body_str')) != -1:
            print('retry!', url_with_params)
            print('counter' , counter)
            counter += 1
        else:
            button_cnt = count_elements(body.decode('euc-kr'), input_data.get('open_check_body_button'))
            input_data.update({'button_cnt':button_cnt})
            if site_info.get(input_data.get('site')).get('first_open_yn') == 'Y':
                print('Reservation Go!')
                break
            elif button_cnt == input_data.get('open_check_body_button_cnt'):
                print('Reservation Go!')
                break
        time.sleep(0.5)

    return True

def count_elements(html_string, xpath):
    # 문자열을 파싱하여 lxml Element 객체 생성
    root = html.fromstring(html_string)
    # XPath로 특정 요소 선택
    selected_elements = root.xpath(xpath)
    # 선택한 요소 수 반환
    return len(selected_elements)

def save_file(html_string, file_name):
    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file = open(file_name, 'w')
    file.write(html_string)      # 파일에 문자열 저장
    file.close()                     # 파일 객체 닫기
