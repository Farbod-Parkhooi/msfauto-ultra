from tkinter import * 
from colorama import Fore, Back, Style, init
import platform, os
init(autoreset=True)
def banner():
    print(Back.BLUE + Fore.BLACK + """
  \/________________                                                                                                             
 /     _____________)                                                                                                            
/     /      _  _ |                                                                                                              
\/\/\/     (O) (O)|                                                                                                              
  |           ------,                                                                                                            
  |  _       ______/        ___________________________________________________                                                  
  | (_      /   \  \       /                                                  /___________________________________________       
  |        /  ___\_ \     /  ░▒█▀▄▀█░▒█▀▀▀█░▒█▀▀▀░░░▒█░▒█░█░░▀█▀░█▀▀▄░█▀▀▄   /                                             \     
  |        \      / /     \  ░▒█▒█▒█░░▀▀▀▄▄░▒█▀▀░░░░▒█░▒█░█░░░█░░█▄▄▀░█▄▄█  / (https://github.com/Unknow-Per/msfauto-ultra) \    
__|_________\______/      /  ░▒█░░▒█░▒█▄▄▄█░▒█░░░░░░░▀▄▄▀░▀▀░░▀░░▀░▀▀░▀░░▀ /  (by Unknow-Per)                               /    
\______________\./__\     \_______________________________________________/________________________________________________/     
 /     .       | \  |                                                                                                            
 \    /_\   .  |  \ |\                                                                                                           
 |`\       /_\ |   \| \                                                                                                          
""")
def check_os():
    if platform.uname()[0] != "Linux": print(Fore.RED + Style.BRIGHT + "[-] Your platform must be Kali Linux."), exit()
    else: print(Fore.GREEN + Style.BRIGHT + "[+] OS Accepted! Continue...")
