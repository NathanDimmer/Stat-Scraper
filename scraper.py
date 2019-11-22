import pyautogui
import time
from tkinter import Tk
import sys
from progress.bar import Bar

# TODO: Change Tabs

day = 1
month = int(sys.argv[1])
year = int(sys.argv[2])
getChildrensComputers = (str(sys.argv[3]).lower() == "true")


def numDays(month):
    if (month == 1):
        return 31
    elif (month == 2):
        if (year % 4 == 0):
            return 29
        else:
            return 28
    elif (month == 3):
        return 31
    elif (month == 4):
        return 30
    elif (month == 5):
        return 31
    elif (month == 6):
        return 30
    elif (month == 7):
        return 31
    elif (month == 8):
        return 31
    elif (month == 9):
        return 30
    elif (month == 10):
        return 31
    elif (month == 11):
        return 30
    elif (month == 12):
        return 31


bar = Bar('Collecting data', max=numDays(month) +
          (1 if getChildrensComputers else 0))
time.sleep(3)
endResult = ""
f = open("countOf-"+str(month)+"-"+str(day)+"-" +
         str(year)+".csv", mode='w', encoding='utf-8')
while day <= numDays(month):
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.typewrite(str(month))
    if (month == 1):
        pyautogui.press('tab')
    pyautogui.typewrite(str(day))
    if (day < 4):
        pyautogui.press('tab')
    pyautogui.typewrite(str(year))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(str(month))
    if (month == 1):
        pyautogui.press('tab')
    pyautogui.typewrite(str(day))
    if (day < 4):
        pyautogui.press('tab')
    pyautogui.typewrite(str(year))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(.25)
    if (day < 2):
        try:
            boxLocation = pyautogui.locateOnScreen('timesAsked.png')
        except:
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
    bar.next()
    day += 1

f.write(endResult)
f.close()
if (getChildrensComputers == True):
    endResult = ""
    f = open("childrenCompUse-"+str(month)+"-" +
             str(year)+".csv", mode='w', encoding='utf-8')
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
    if (month == 1):
        pyautogui.press('tab')
    pyautogui.typewrite(str(1))
    pyautogui.press('tab')
    pyautogui.typewrite(str(year))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(str(month))
    if (month == 1):
        pyautogui.press('tab')
    pyautogui.typewrite(str(numDays(month)))
    pyautogui.typewrite(str(year))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(.5)
    try:
        boxLocation = pyautogui.locateOnScreen('timesAsked.png')
    except:
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
    bar.next()
bar.finish()
