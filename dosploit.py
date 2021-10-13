import pyfiglet
import colorama
import os
os.system("clear")

result = pyfiglet.figlet_format("dosploit",font="slant")
print (colorama.Fore.CYAN+result)

code_with = """
##########################################
#              coded with                #
#         ARMIN,YASER,MOHAMMAD           #
#         github: @amicheh,@PAIREN1383   #
#                                        #
#                                        #
#                                        #
#           dosploit v.demo1             #
##########################################
"""


print (colorama.Fore.MAGENTA+code_with)
print(colorama.Fore.RED+"this code demo of dos sploit")

print ("(1) udp flood vip for dosploit")
print ("(2) syn flood attack vip dosploit")
try:
    osk = input(colorama.Fore.BLUE+" ┌─["+colorama.Fore.LIGHTGREEN_EX+"dosploit"+colorama.Fore.BLUE+"~"+colorama.Fore.BLUE+"@HOME"+colorama.Fore.GREEN+"""]
    └──╼ """+colorama.Fore.WHITE+"$ ")

    if osk == 1 :
        os.system("cls")
    elif osk == 2:
        os.system("cl2")
        
except:
    pass