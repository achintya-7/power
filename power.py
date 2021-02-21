import time
import json

global signal2
global trigger1 
global trigger2
global W_mains, W_UPS, W_DG

TW_UPS = 0
TW_DG = 0

signal2='ON MAINS'
Watt = 0


def reset():   ## calling reset at the end of the day
    
    trigger1 = 0
    trigger2 = 0
    W_mains = 0
    W_mains2 = 0
    W_UPS = 0
    W_DG = 0
    
    global TW_UPS 
    global TW_DG 

def check():
    
    while True:
        print('power2 \n')
        if(signal2 != 'ON MAINS'):
            trigger1 = trigger1 + 1
            W_mains = Watt #records the power here 
            while True:
                if(signal2 != 'ON UPS'):
                    trigger2 = trigger2 + 1
                    W_UPS = Watt
                    while True:
                        if(signal2 == 'ON MAINS'):
                            TW_UPS = TW_UPS + (W_UPS - W_mains)
                            print(TW_UPS)
                            	#power_dict = {"Total UPS watt": TW_UPS}
                            	#with open('power.txt', 'w') as json_file:
                             #json.dump(power_dict, json_file)
                            check()
                        elif(signal2 == 'ON DG'):
                            W_DG = Watt
                            TW_UPS = TW_UPS + (W_UPS - W_mains)
                            if(signal2 == 'ON MAINS'):
                                W_mains2 = Watt
                                TW_DG = TW_DG + (W_mains2 - W_UPS)
                                print(TW_DG)
                                #power_dict = {"Total DG watt": TW_DG}
                                #with open('power.txt', 'w') as json_file:
                                # json.dump(power_dict, json_file)  
                                check()
        
        
        time.sleep(0.5)
    print(TW_DG, TW_UPS)
    print(trigger1, trigger2)




            
                
        






