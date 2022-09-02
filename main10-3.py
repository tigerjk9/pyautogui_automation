import pyautogui
import time
import pyperclip

pyautogui.moveTo(1286, 266, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨") 
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"]) 
time.sleep(1)

start_x = 982   # 스크린샷의 시작 좌표와 종료 좌표를 넣어줍니다. 
start_y = 145
end_x = 1878
end_y = 1004

pyautogui.screenshot(r'10. 오토마우스를 활용한 웹페이지 자동화\서울날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
# 서울날씨.png 라는 이름의 캡쳐로 저장하며, 사이즈를 지정해줍니다. (시작좌표 x, 시작좌표 y, 크기 x, 크기 y)
# 크기는 종료좌표에서 시작좌표를 빼서 구합니다. 