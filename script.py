from tkinter import * 
from colorama import Fore, Back, Style, init
import platform, os, random, time
init(autoreset=True)
class msfauto_ultra():
    def __init__(self, app_name, ip, port_one, port_two, payload):
        self.app_name = app_name
        self.ip = ip
        self.port1 = port_one
        self.port2 = port_two
        self.payload = payload
def banner():
    banners = {
        1 : f"""{Fore.CYAN}
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
""",
        2 : f"""{Fore.CYAN}                                  ___
    .    _  .     _____________  /   \_______________________________________________
    |\_|/__/|    /             \/                                                   /
   / / \/ \  \  /    This is    \  (https://github.com/Unknow-Per/msfauto-ultra)   /
  /__|O||O|__ \ \ MSFAuto-Ultra /   (by Unknow-Per)                _______________/
 |/_ \_/\_/ _\ | \  ___________/__________________________________/
 | | (____) | ||  |/
 \/\___/\__/  // _/
 (_/         ||
  |          ||\ 
   \        //_/ 
    \______//
   __|| __||
  (____(____)
 
""",
        3 : f"""{Fore.CYAN}
        .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    \         ___________________
   /        .-----.        \       /                   \ 
   |       .-.   .-.       |      /  Ohh... Im again?   \ 
   |      /   \ /   \      |     /   Ok,  THIS IS        \ 
    \    | .-. | .-. |    /     /                        /
     '-._| | | | | | |_.-'     /      MSFAuto           /
         | '-' | '-' |         \             Ultra     /
          \___/ \___/           \  ___________________/
       _.-'  /   \  `-._         |/
     .' _.--|     |--._ '.     __/
     ' _...-|     |-..._ '
            |     |
            '.___.'
"""
    }
    print(banners[random.randint(1, 3)])
def clear(): os.system("clear")
def check_os():
    if platform.uname()[0] != "Linux": print(Fore.RED + Style.BRIGHT + "[-] Your platform must be Kali Linux."), exit()
    else: print(Fore.GREEN + Style.BRIGHT + "[+] OS Accepted! Continue...")
    time.sleep(5)
    clear()
def get_info():
    root = Tk()
    Label(root, text="your application's name:").place(x=15, y=47)
    Label(root, text="your ip:").place(x=15, y=97)
    Label(root, text="your first port:").place(x=15, y=147)
    Label(root, text="your srconf port:").place(x=15, y=197)
    Label(root, text="your payload:").place(x=15, y=247)
    Label(root, text="(android, windows, or mac)").place(x=15, y=275)
    app_name = Entry(root, width=50)
    ip = Entry(root, width=50)
    port1 = Entry(root, width=50)
    port2 = Entry(root, width=50)
    payload = Entry(root, width=50)
    app_name.place(x=150, y=50)
    ip.place(x=150, y=100)
    port1.place(x=150, y=150)
    port2.place(x=150, y=200)
    payload.place(x=150, y=250)
    def save():
        with open("config", "w") as writer:
            writer.write(f"{app_name.get()},{ip.get()},{port1.get()},{port2.get()},{payload.get()}")
    Button(root, command=save, text="submit", width=8, height=2).place(x=300, y=290)
    root.geometry("500x350")
    root.title("Get informations")
    root.resizable(False, False)
    root.mainloop()

get_info()