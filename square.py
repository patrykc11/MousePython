import pyautogui
import time



print(pyautogui.size())
print("Podaj dlufosc boku w pixelach:")
x =input()

pyautogui.moveTo(10, 650, duration = 1)

pyautogui.click(10, 650)
time.sleep(2)
#drawing a square
pyautogui.moveTo(500, 300, duration = 1)
pyautogui.dragRel(x, 0, duration = 1)
pyautogui.dragRel(0, x, duration = 1)
pyautogui.moveTo(500, 300, duration = 1)
pyautogui.dragRel(0, x, duration = 1) #nie działa -x nie wiem dlaczego?
pyautogui.dragRel(x, 0, duration = 1)
#saving a work of art
pyautogui.hotkey("ctrlleft", "s")
pyautogui.click(960, 720)
print("Kwadrat o boku",x)
#pyautogui.typewrite("Kwadrat o boku",x)

