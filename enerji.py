import pyautogui
import time

def get_item() :
    pyautogui.displayMousePosition(300,300) # oyun içerisinde silah satıcısını bul  #güncellenecek
    time.sleep(0.2)
    
    pyautogui.doubleClick(300,300) # marketi aç
    time.slep(0.2)
    for i in range (1,80) : 
        pyautogui.leftClick(450,700) # marketten 80 tane item al # envanterin ilk 10 satırına 10 adet enerji parçası önceden koy
        time.sleep(0.7)
    
    
'''  
def throw_item() : # bir item 
    pyautogui.displayMousePosition(750,578) # simyacıyı bul 
    time.sleep(0.2)
    
    pyautogui.rightClick(750,15) # tek bir itemi seçme
    time.sleep(0.1)
    pyautogui.moveTo(400,133)  # itemi simyacı üzerine bırakma
    time.sleep(0.1)
    pyautogui.press("enter") # çıkan yazıyı onaylama
    
'''  

def throw_item () : # bir çok itemi sırayla simyacı üzerine bırakma 
    pyautogui.displayMousePosition(750,578) # simyacıyı bul   #güncellenecek
    time.sleep(0.2)
    
    # +65 her seferinde
    x1 = 970
    x2 = 1035 
    x3 = 1095
    x4 = 1160
    x5 = 1225
    
    # +50 her seferinde 
    y1 = 200
    y2 = 250
    y3 = 300
    y4 = 350
    y5 = 400
    y6 = 450
    y7 = 500
    y8 = 550
    y9 = 600
    
    for i in range (1,2) : 
    
        for i in range (1,9) : 
            pyautogui.rightClick(x1,y1) # itemi seçme
            time.sleep(0.1)
            pyautogui.moveTo(400,133)  # itemi simyacı üzerine bırakma
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.rightClick(x2,y1) # itemi seçme
            time.sleep(0.1)
            pyautogui.moveTo(400,133)  # itemi simyacı üzerine bırakma
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50
            
        for i in range (1,9) : 
            pyautogui.rightClick(x3,y1) # itemi seçme
            time.sleep(0.1)
            pyautogui.moveTo(400,133)  # itemi simyacı üzerine bırakma
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.rightClick(x4,y1) # itemi seçme
            time.sleep(0.1)
            pyautogui.moveTo(400,133)  # itemi simyacı üzerine bırakma
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
            
        for i in range (1,9) : 
            pyautogui.rightClick(x5,y1) # itemi seçme
            time.sleep(0.1)
            pyautogui.moveTo(400,133)  # itemi simyacı üzerine bırakma
            time.sleep(0.1)
            pyautogui.press("enter") # çıkan yazıyı onaylama
            y1 = y1 + 50 
        
        pyautogui.rightClick(750,15) # 2. envanteri aç ve işlem döngüsü 2. defa çalışsın.
        
        
    
  
    
    
get_item()
throw_item()

def end () : # 10 veya 20 paket enerji parçası yapıldıktan sonra bunu depoya aktarmak lazım. İlk aşamada el ile yapılabilir.  #güncellenecek
    time.sleep(5400)