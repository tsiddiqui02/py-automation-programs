import pyautogui
import time

# Move the mouse left & right, click, and press "W" every 5 seconds
while True:
    pyautogui.moveRel(100, 0, duration=0.50)
    pyautogui.moveRel(-100, 0, duration=0.50)
    pyautogui.click()
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')
    time.sleep(5)