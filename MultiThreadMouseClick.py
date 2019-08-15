# AutoMouseClicker.yml environment
# python -v 3.7.3
# pillow -v 5.3.0
# pyautogui -v 0.9.44
# multiprocessing

from PIL import Image
import pyautogui
import time
from multiprocessing import Process
pyautogui.FAILSAFE = True

def clicker(startingPixel): #in seconds
    time.sleep(5) #time to switch to https://www.mouseaccuracy.com/game

    initial = time.time()

    while True:                
        c_break = False
        pic = pyautogui.screenshot()

        for i in range(startingPixel,startingPixel+480,2):#skip 2 pixels at each iter.

            if c_break == True: break

            for j in range(67,1080,2): #cycling thru y coord pixels, 67 is just underneath title bar when in full screen

                r,g,b = pic.getpixel((i,j))

                if (r in range(245,254)):#RED

                    pyautogui.click(i,j)
                    c_break = True
                    break

        if time.time() - initial > 30: break

if __name__ == "__main__":
    procs = []
    
    proc1 = Process(target=clicker, args=(0,))
    proc2 = Process(target=clicker, args=(480,))
    proc3 = Process(target=clicker, args=(960,))
    proc4 = Process(target=clicker, args=(1440,))

    procs.append(proc1)
    procs.append(proc2)
    procs.append(proc3)
    procs.append(proc4)

    proc1.start()
    proc2.start()
    proc3.start()
    proc4.start()

    for proc in procs:
        proc.join()