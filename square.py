import pyautogui
import time



print(pyautogui.size())
print("Podaj dlufosc boku w pixelach:")
x: float =input()

pyautogui.moveTo(10, 650, duration = 1)

pyautogui.click(10, 650)
time.sleep(5)
pyautogui.moveTo(500, 300, duration = 1)
pyautogui.dragRel(x, 0, duration = 1)
pyautogui.dragRel(0, x, duration = 1)
pyautogui.moveTo(500, 300, duration = 1)
pyautogui.dragRel(0, x, duration = 1) #nie działa -x nie wiem dlaczego?
pyautogui.dragRel(x, 0, duration = 1)


