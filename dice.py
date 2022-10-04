import random
import time

ask = input("Press 'y' if you want to roll a dice:")

ran = 0

while ask == "y" and ask != "s":
    ran = random.randint(1,6)

    if(ran == 1):
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
        ask = "s"
        ask = input("Press 'y' if you want to roll a dice again:")
    

    if(ran == 2):
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
        ask = "s"
        ask = input("Press 'y' if you want to roll a dice again:")

    if(ran == 3):
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
        ask = "s"
        ask = input("Press 'y' if you want to roll a dice again:")

    if(ran == 4):
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
        ask = "s"
        ask = input("Press 'y' if you want to roll a dice again:")

    if(ran == 5):
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
        ask = "s"
        ask = input("Press 'y' if you want to roll a dice again:")

    if(ran == 6):
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")
        ask = "s"
        ask = input("Press 'y' if you want to roll a dice again:")
    



