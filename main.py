import pyautogui



print(pyautogui.size())

#pyautogui.moveTo(100, 100, duration = 1) #moves mouse pointer to coordinates (x, y) in duration time

#pyautogui.moveRel(0, 50, duration = 1) #moves mouse pointer relative to its previous position

#print(pyautogui.position()) # return current position of the mouse pointer

pyautogui.click(100, 100) #function used for clicking and dragging the mouse

#We have two functions associated with drag operation of mouse, dragTo and dragRel.
# They perform similar to moveTo and moveRel functions, except they hold the left mouse button while moving,
# thus initiating a drag.

#pyautogui.scroll(200) #function take no. of pixels and scrolls the screen up to given number of pixels

pyautogui.typewrite("hello World!") #function which write a string in coordinates





