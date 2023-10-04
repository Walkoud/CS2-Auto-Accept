
import pyautogui
import time
from colorama import Fore, Style
import sys
import os

# Made by <3 by Walkoud

print(Fore.RED + Style.BRIGHT + """
   ___  __  ____________    ___  _________________  ______
  / _ |/ / / /_  __/ __ \  / _ |/ ___/ ___/ __/ _ \/_  __/
 / __ / /_/ / / / / /_/ / / __ / /__/ /__/ _// ___/ / /   
/_/ |_\____/ /_/  \____/ /_/ |_\___/\___/___/_/    /_/    
"""+ Fore.BLUE + """
                                            By Walkoud v1 """ + Fore.YELLOW + """
  ____________ 
 / ___/ __/_  |
/ /___\ \/ __/ 
\___/___/____/ 
               
                                    """+ Fore.WHITE + """

            https://github.com/walkoud          
                                                
""")


print(Fore.GREEN + "Starting in 3 seconds !" + Style.RESET_ALL)




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Utilisation de la fonction resource_path pour obtenir le chemin absolu de "image.png"
image_path = resource_path("image.png")

def detect_and_click(image_path):
    time.sleep(3)
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(image_path)
            pyautogui.click(x, y)
            print(Fore.GREEN + "CLICKED IN AUTOACCEPT Successfully" + Style.RESET_ALL)
            input("Click in the window and press a key to restart")
        except TypeError:
            print("Searching accept button... Retrying in 1 seconds...")
            time.sleep(1)




detect_and_click(image_path)



























# Made by <3 by Walkoud
