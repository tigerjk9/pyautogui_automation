import pyautogui
import time
import pyperclip

pyautogui.moveTo(1286, 266, 0.2) # 네이버 검색창의 좌표로 0.2초 동안 이동
pyautogui.click()  # 마우스 클릭
time.sleep(0.5)  # 0.5초 기다리기

pyperclip.copy("서울 날씨") # 클립보드에 서울날씨를 저장
pyautogui.hotkey("ctrl", "v")  # 클립보드에 저장된 내용을 붙여넣기
time.sleep(0.5)

pyautogui.write(["enter"]) 
time.sleep(1)