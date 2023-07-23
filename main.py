import os
from os import system
from menu import Menu

clear = lambda: os.system('cls')

"""start def"""
def start():
    system("title " + f"sorter by mossad v.1.10")
    menuset = Menu(scan())
    menuset.startmenu()

"""path def"""
def path():
    while True:
        try:
            pathtologs = str(input("Enter path\n"))
            break

        except ValueError:
            print("You entered the wrong path. Try again: ")
        else:
            if False == os.path.isdir(pathtologs):
                print("Enter the correct path")
                clear()
    return pathtologs

def scan():
    all_path = set()
    for root, dirs, files in os.walk(path()):
        for filename in files:
            all_path.add(os.path.join(root, filename))
    return all_path


if __name__ == "__main__":
    start()
