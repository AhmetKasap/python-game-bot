import pyautogui
import time
from python_imagesearch import imagesearch

def start(x,y): 
    pyautogui.leftClick(x,y)

def get_item():
    while (True) :
        market = imagesearch.imagesearch("market.png")
        if market[0] != -1:
            pyautogui.moveTo(market[0]+20, market[1]+110)
            pyautogui.click(button='left', clicks=1)
           
            time.sleep(0.2)
            pyautogui.moveTo(680, 300)  # marketi aç konumu
            pyautogui.click(button='left', clicks=1)  # marketi aça tıkladı
            break
        else:
            print("market açılamadı, tekrar açmayı dene")


def go_alchemistry () :  #ekran klavyesi ile çalışır, simyacıya gidiş
    w = 200,915
    a = 164,953
    s = 223,946
    d = 290,953
    q = 144,915
    e = 268,915
    pyautogui.leftClick(346,15)

    pyautogui.moveTo(s)
    pyautogui.mouseDown()
    time.sleep(6.5)
    pyautogui.mouseUp()

    pyautogui.moveTo(e)
    pyautogui.mouseDown()
    time.sleep(0.6)
    pyautogui.mouseUp()

    pyautogui.moveTo(w)
    pyautogui.mouseDown()
    time.sleep(16.5)
    pyautogui.mouseUp()

    pyautogui.moveTo(q)
    pyautogui.mouseDown()
    time.sleep(0.28)
    pyautogui.mouseUp()

    pyautogui.moveTo(w)
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()



def go_market () :  #ekran klavyesi ile çalışır, silah  satıcısına gidiş
    w = 200,915
    a = 164,953
    s = 223,946
    d = 290,953
    q = 144,915
    e = 268,915
    pyautogui.leftClick(346,15)

    pyautogui.moveTo(s)
    pyautogui.mouseDown()
    time.sleep(4.5)
    pyautogui.mouseUp()

    pyautogui.moveTo(q)
    pyautogui.mouseDown()
    time.sleep(1.4)
    pyautogui.mouseUp()

    pyautogui.moveTo(w)
    pyautogui.mouseDown()
    time.sleep(11)
    pyautogui.mouseUp()

    pyautogui.moveTo(e)
    pyautogui.mouseDown()
    time.sleep(0.75)
    pyautogui.mouseUp()

    pyautogui.moveTo(w)
    pyautogui.mouseDown()
    time.sleep(6)
    pyautogui.mouseUp()



def throw_item () : 
    pyautogui.displayMousePosition(750,578) # simyacıyı kordinantı
    time.sleep(0.2)
    
    # +65 her seferinde
    x1 = 970
    
    x2 = 1035 
    x3 = 1095
    x4 = 1160
    x5 = 1225
    
    # +50 her seferinde 
    y1 = 200
    
    #y2 = 250
    #y3 = 300
    #y4 = 350
    #y5 = 400
    #y6 = 450
    #y7 = 500
    #y8 = 550
    #y9 = 600

    for i in range (1,2) : 
    
        for i in range (1,9) : 
            pyautogui.moveTo(x1, y1) #item kordinantı
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x2, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x3, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x4, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.moveTo(x5, y1)
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            pyautogui.moveTo(680, 363)  
            time.sleep(0.5)
            pyautogui.click(button='left', clicks=1)
            time.sleep(0.5)
            y1 = y1 + 50 
        
        pyautogui.leftClick(750,15) # 2. envanteri aç ve işlem döngüsü 2. defa çalışsın.
        

start(500,500) 
time.sleep(1)
for i in range (1,15):     
    get_item()
    go_alchemistry()
    throw_item()
    go_market()






'''
OLD

def get_item() :
    pyautogui.moveTo(680,363) #silah satıcısı kordinantı
    time.sleep(0.1)
    pyautogui.click(button='left', clicks=1) #silah satıcısına tıkla
    time.sleep(0.1)
    pyautogui.moveTo(680, 300) #silah satıcısını aç
    pyautogui.click(button='left', clicks=1) #marketi aça tıkla
    for i in range (1,80) : # item al
        pyautogui.leftClick(450,700) 
        time.sleep(0.7)   

def go_alchemistry () :
    for i in range (1,45): #4.5 sn
        pyautogui.press('s')
    
    for i in range (1,10):  # 1 sn
        pyautogui.press('e')
        
    for i in range (1,120): # 12sn 
        pyautogui.press('w')
    
    for i in range (1,20):  # 2 sn 
        pyautogui.press('q')
    
    for i in range (1,20):  # 2 sn 
        pyautogui.press('w')

def go_alchemistry () :
    #15 press 1 sn
    pyautogui.press('s', presses=68, interval=0.02)  # 4.5 sn
    pyautogui.press('e', presses=15, interval=0.02)  # 1 sn
    pyautogui.press('w', presses=180, interval=0.02) # 12 sn
    pyautogui.press('q', presses=30, interval=0.02)  # 2 sn
    pyautogui.press('w', presses=30, interval=0.02)  # 2 sn

def go_market () :
    for i in range (1,30): #3 sn
        pyautogui.press('s')
    
    for i in range (1,15):  # 1.5 sn
        pyautogui.press('q')
        
    for i in range (1,70): # 7sn 
        pyautogui.press('w')
    
    for i in range (1,3):  # 0.3 sn 
        pyautogui.press('e')
    
    for i in range (1,65):  # 6.5 sn 
        pyautogui.press('w')
        
    for i in range (1,2):  # 0.2 sn 
        pyautogui.press('e')
        
    for i in range (1,15):  # 1.5 sn 
        pyautogui.press('w')

def go_market () :
    #15 press 1 sn
    pyautogui.press('s', presses=45, interval=0.02)  # 3 sn
    pyautogui.press('q', presses=21, interval=0.02)  # 1.5 sn
    pyautogui.press('w', presses=105, interval=0.02) # 7 sn
    pyautogui.press('e', presses=5, interval=0.02)  # 0.3 sn
    pyautogui.press('w', presses=98, interval=0.02)  # 6.5 sn
    pyautogui.press('e', presses=3, interval=0.02)  # 0.2 sn
    pyautogui.press('w', presses=21, interval=0.02)  # 1.5 sn

'''










        

    

