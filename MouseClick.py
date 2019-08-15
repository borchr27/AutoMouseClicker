# AutoMouseClicker.yml environment
# python -v 3.7.3
# pillow -v 5.3.0
# pyautogui -v 0.9.44
# multiprocessing

from PIL import Image
import pyautogui
import time

def Click_Bot(duration):#In seconds

    time.sleep(5)#Time to switch to https://www.mouseaccuracy.com/game


    #im = Image.new('RGBA', (1280, 200), 'black')# A Black strip to cover the browser header
    #im2 = Image.new('RGBA', (1280, 80), 'black')# A Black Strip to cover taskbar

    im = Image.new('RGBA', (1920, 80), 'black')# A Black strip to cover the browser header
    #im2 = Image.new('RGBA', (1920, 0), 'black')# A Black Strip to cover taskbar

    initial = time.time()

    while True:

        c_break = False

        pic = pyautogui.screenshot(region=(0,0,1920,1080))

        pic.paste(im,(0,0))
        #pic.paste(im2,(0,960))
        #pic.save("pic.png","PNG")

        x, y = pic.size
        

        for i in range(0,x,10):#Skip 10 pixels at each iter.

            if c_break == True: break

            for j in range(200,y,10):
                r,g,b = pic.getpixel((i,j))

                if (r in range(235,255)):#RED
                    pyautogui.click(i,j)
                    c_break = True
                    break

        if time.time() - initial > duration: break

Click_Bot(30)