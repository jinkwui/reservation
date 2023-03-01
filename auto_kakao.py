import pyautogui
import time

print(pyautogui.size()) # 현재 모니터의 크기 파악

time.sleep(3) # 마우스를 움직일 시간 추가 (카톡프로필로 들어가서 공감위치에 마우스 올리기)
print(pyautogui.position()) # 마우스의 현재 위치 표시

# 현재위치에서 자동클릭
pyautogui.click(clicks=10000, interval=0.001) #클릭횟수, 클릭시간차
