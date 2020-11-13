import pyautogui

def main():
    print(pyautogui.size())
    x, y = pyautogui.size()
    print(0.005*x)
    pyautogui.moveTo(0.005*x, 0.6*y, duration = 1)
    #pyautogui.click(0.005*x, 0.6*y)
    #pyautogui.typewrite("git status")
    #pyautogui.hotkey("enter")

main()




