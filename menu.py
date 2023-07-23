from func import Operations
import os
clear = lambda: os.system('cls')


class Menu:
    """Constructor"""

    def __init__(self, allpath):
        self.allpath = allpath

    """start menu"""

    def startmenu(self):
        clear()
        arg = 0
        setting = Operations(self.allpath, arg)
        print(f"sorter by mossad."
              f"\n1. [Garbage clearance]"
              f"\n2. [Get strings]"
              f"\n3. [Get Discord]"
              f"\n4. [Get cookies]"
              f"\n5. [Get TG]")
        button = int(input())
        if button == 1:
            setting.clean()
            self.startmenu()
        elif button == 2:
            arg = int(input(f"sorter by mossad."
                            f"\n1. [Get all passwords]"
                            f"\n2. [Get passwords on demand]\n"))
            setting = Operations(self.allpath, arg)
            setting.passpars()
            self.startmenu()
        elif button == 3:
            setting.parsdiscord()
            self.startmenu()
        elif button == 4:
            arg = int(input(f"sorter by mossad."
                            f"\n1. [Get all cookies]"
                            f"\n2. [Get cookies on request]\n"))
            setting = Operations(self.allpath, arg)
            setting.parscookie()
            self.startmenu()
        elif button == 5:
            setting.parstg()
            self.startmenu()
        else:
            self.backfunc()
    def backfunc(self):
        clear()
        print("Enter the correct command")
        self.startmenu()