import urllib.request
import urllib.parse
import time
import ssl

def open_paju_check(url, json_data):

    counter = 0
    context = ssl._create_unverified_context()

    while True:
        post_data = urllib.parse.urlencode(json_data).encode('utf-8')
        request = urllib.request.Request(url, post_data)
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        response = urllib.request.urlopen(request, context=context)
        body = response.read()  # return type bytes

        # 문자열에 포함되어 있는지 확인
        if body.decode('euc-kr').find(json_data.get('check_body_str')) != -1:
            print('retry!', url)
            print('counter' , counter)
            counter += 1
            # if counter > 10:
            #     url = url.replace('2023-04-22', '2023-03-15')

        else:
            print('Reservation Go!')
            break
        time.sleep(0.5)

    return True