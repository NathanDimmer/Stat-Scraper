import pyautogui
import time
from tkinter import Tk
import datetime

# TODO: Change Months, Change Years, Change Tabs
monthLength = 31
month = 10
time.sleep(5)
endResult = ""
f = open("childrenCompUse-"+str(month)+"-"+
         str(datetime.datetime.now().year)+".csv", mode='w', encoding='utf-8')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.typewrite(str(month))
pyautogui.typewrite(str(1))
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(str(month))
pyautogui.typewrite(str(monthLength))
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(.5)
boxLocation = pyautogui.locateOnScreen('timesAsked.png')
boxPoint = pyautogui.center(boxLocation)
pyautogui.moveTo(boxPoint.x, boxPoint.y + 50)
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.hotkey('ctrl', 'c')
pyautogui.moveTo(boxPoint.x, boxPoint.y + 200)
endResult += Tk().clipboard_get().strip() + "\n"
pyautogui.click()
f.write(endResult)
f.close()
