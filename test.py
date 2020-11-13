import pyautogui
import time


def main():
    print(pyautogui.size())
    x, y = pyautogui.size()
    print("Wybierz a aby narysowac kwadrat, wybierz b aby zagrać w sapera")
    option = input()
    if option == "a":
        print("Podaj dlugosc boku w pixelach:")
        bok = input()
        pyautogui.hotkey("ctrlleft", "altleft", "t")
        time.sleep(1)
        pyautogui.typewrite("cd Pobrane")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(1)
        pyautogui.typewrite("./krita.appimage")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(20)
        pyautogui.click(0.7*x, 0.7*y)
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "n")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "q") #pełny ekran
        time.sleep(1)
        pyautogui.moveTo(0.2*x, 0.2*y, duration=1)
        pyautogui.dragRel(bok, 0, duration=1)
        pyautogui.dragRel(0, bok, duration=1)
        pyautogui.moveTo(0.2*x, 0.2*y, duration=1)
        pyautogui.dragRel(0, bok, duration=1)  # nie działa -x nie wiem dlaczego?
        pyautogui.dragRel(bok, 0, duration=1)
    elif option == 2:
        print("W trakcie budowy")
    else:
        print("Wybrano niedozwolony znak")

main()