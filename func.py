import os
import re
import time
import configparser
from urllib.parse import urlparse
from native import copytree
import shutil

"""Класс используемый для операций с логами"""


class Operations(object):
    """Constructor"""

    def __init__(self, allpath, arg):
        self.allpath = allpath
        self.arg = arg

    """Парсинг cookie"""

    def parscookie(self):
        start_directory = os.getcwd()
        count = -1
        request_file = self.requestsread()
        if not os.path.isdir("Cookie"):
            os.mkdir("Cookie")
        os.chdir(rf"{os.getcwd()}\Cookie")
        main_directory = os.getcwd()
        current_time = time.strftime("%H.%M.%S", time.localtime())
        os.mkdir(f"{current_time}")
        os.chdir(rf"{os.getcwd()}\{current_time}")
        if self.arg == 2:
            temp_set = set()
            temp_set2 = set()
            os.mkdir(f"temp")
            os.chdir(rf"{os.getcwd()}\temp")
            for path in self.allpath:
                if "Cookies" in path and ".txt" in path:
                    copytree(os.path.dirname(path), rf"{os.getcwd()}")
            for root, dirs, files in os.walk(os.getcwd()):
                for filename in files:
                    temp_set.add(os.path.join(root, filename))
            for request in request_file:
                os.mkdir(rf"{main_directory}\{current_time}\{request}")
            for request in request_file:
                count += 1
                for file in temp_set:
                    with open(file, errors="ignore") as f:
                        for line in f:
                            if request in line:
                                temp_set2.add(file)

                for request_files in temp_set2:
                    os.chdir(rf"{main_directory}\{current_time}\{request_file[count]}")
                    shutil.copy(request_files, os.getcwd())
                else:
                    temp_set2 = set()
            shutil.rmtree(rf"{main_directory}\{current_time}\temp")
        elif self.arg == 1:
            for path in self.allpath:
                if "Cookies" in path and "cookies" in path and ".txt" in path:
                    copytree(os.path.dirname(path), os.getcwd())
        os.chdir(start_directory)

    """Парсинг Telegram"""

    def parstg(self):
        start_directory = os.getcwd()
        count = 0
        if not os.path.isdir("Telegram"):
            os.mkdir("Telegram")
        os.chdir(rf"{os.getcwd()}\Telegram")
        current_time = time.strftime("%H.%M.%S", time.localtime())
        os.mkdir(f"{current_time}")
        os.chdir(rf"{os.getcwd()}\{current_time}")
        for path in self.allpath:
            dirname = os.path.dirname(path)
            if "settingss" in path:
                count += 1
                os.mkdir(f"tg{count}")
                copytree(dirname, rf"{os.getcwd()}\tg{count}")
        else:
            os.chdir(start_directory)

        """Парсинг дискорд"""

    def parsdiscord(self):
        start_directory = os.getcwd()
        current_time = time.strftime("%H.%M.%S", time.localtime())
        if not os.path.isdir("Discord"):
            os.mkdir("Discord")
        os.chdir(rf"{os.getcwd()}\Discord")
        os.mkdir(f"{current_time}")
        os.chdir(rf"{os.getcwd()}\{current_time}")
        all_tokens = set()
        for path in self.allpath:
            if "ProcessList.txt" not in path and "InstalledSoftware.txt" not in path \
                    and "InstalledBrowsers.txt" not in path and "DomainDetects.txt" not in path:
                r = open(path, 'r+', errors="ignore", encoding="cp1251").read()
                lst = re.findall(rf"[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", r)
                if not lst:
                    pass
                else:
                    for token in lst:
                        all_tokens.add(token)
        else:
            with open("Discord_tokens.txt", "w") as f:
                for token in all_tokens:
                    f.write(f"{token}\n")
        os.chdir(start_directory)

    """Парсинг паролей"""

    def passpars(self):
        cfg = []
        regular = ["URL: (.+)\nUsername: (.+)\nPassword: (.+)\n", "url: (.+)\nlogin: (.+)\npassword: (.+)\n",
                   "URL: (.+)\nLogin: (.+)\nPassword: (.+)\n", "URL: (.+)\nUSER: (.+)\nPASS: (.+)\n"]
        config = configparser.ConfigParser()
        config.read("settings.ini")
        for section in config.sections():
            for key in config["format"]:
                cfg.append(config[section][key])
        loginpass = (cfg[0])
        urlpass = (cfg[1])
        passw = (cfg[2])
        start_directory = os.getcwd()
        request_file = self.requestsread()
        current_time = time.strftime("%H.%M.%S", time.localtime())
        if not os.path.isdir("Passwords"):
            os.mkdir("Passwords")
        os.chdir(rf"{os.getcwd()}\Passwords")
        main_directory = os.getcwd()
        os.mkdir(f"{current_time}")
        os.chdir(rf"{os.getcwd()}\{current_time}")
        tempset = set()
        if self.arg == 1:
            for path in self.allpath:
                base = os.path.basename(path)
                if "password.txt" == base or 'Password.txt' == base or "Passwords.txt" == base or "passwords.txt" == base:
                    try:
                        with open(path, errors="ignore", encoding="cp1251", mode="r") as f:
                            text = f.read()
                    except (NameError, UnicodeEncodeError, IndexError):
                        continue
                    for reg in regular:
                        lst = re.findall(reg, text)
                        if len(lst) != 0:
                            for line in lst:
                                tempset.add(f"{urlparse(line[0]).netloc}|{line[1]}|{line[2]}")

            else:
                if loginpass == "True":
                    tempset2 = set()
                    with open(f'all_lp.txt', mode="a", errors="ignore", encoding="cp1251") as f:
                        for request_files in tempset:
                            lp = (request_files).split("|")
                            tempset2.add(f"{lp[1]}:{lp[2]}")
                        for passwo in tempset2:
                            f.write(f"{passwo}\n")
                if urlpass == "True":
                    with open(f'all_url.txt', mode="a", errors="ignore", encoding="cp1251") as f:
                        for request_files in tempset:
                            lp = ((request_files)).split("|")
                            f.write(f"{lp[0]}:{lp[1]}:{lp[2]}\n")
                if passw == "True":
                    tempset2 = set()
                    with open(f'all_pass.txt', mode="a", errors="ignore", encoding="cp1251") as f:
                        for request_files in tempset:
                            lp = request_files.split("|")
                            if len(lp[2]) >= 8 and len(lp[2]) <= 36:
                                tempset2.add(lp[2])
                        for passwo in tempset2:
                            f.write(f"{passwo}\n")
        elif self.arg == 2:
            count = -1
            tempset = set()
            for request in request_file:
                os.mkdir(rf"{main_directory}\{current_time}\{request.replace(':', ' ')}")
            for reqs in request_file:
                count += 1
                for path in self.allpath:
                    base = os.path.basename(path)
                    if "password.txt" == base or 'Password.txt' == base or "Passwords.txt" == base or "passwords.txt" == base:
                        try:
                            with open(path, errors="ignore", encoding="cp1251", mode="r") as f:
                                text = f.read()
                        except (NameError, UnicodeEncodeError, IndexError) as e:
                            continue

                        for reg in regular:
                            lst = re.findall(reg, text)
                            if len(lst) != 0:
                                for line in lst:
                                    if reqs in line[0]:
                                        tempset.add(f"{(line[0])}:{line[1]}:{line[2]}")
                for request_files in tempset:
                    os.chdir(rf"{main_directory}\{current_time}\{request_file[count].replace(':', ' ')}")
                    if loginpass == "True" and urlpass == "True":
                        lp = request_files.split("|")
                        with open(f'{request_file[count]}_lp.txt', mode="a") as f:
                            f.write(f"{lp[1]}:{lp[2]}\n")
                        with open(f'{request_file[count]}_url.txt', mode="a") as f:
                            f.write(f"{lp[0]}:{lp[1]}:{lp[2]}\n")
                    elif urlpass == "True":
                        lp = request_files.split("|")
                        with open(f'{request_file[count]}_url.txt', mode="a") as f:
                            f.write(f"{lp[0]}:{lp[1]}:{lp[2]}\n")
                    elif loginpass == "True":
                        lp = request_files.split("|")
                        with open(f'{request_file[count]}_lp.txt', mode="a") as f:
                            f.write(f"{lp[1]}:{lp[2]}\n")
                else:
                    tempset = set()
        os.chdir(start_directory)

    """Очистка логов"""

    def clean(self):
        extensions_delete = [".exe", ".bat", ".scr", ".lnk", ".bin",
                             ".cmd", ".js", ".jse", ".gadget", ".jar",
                             ".msi", ".wsf", ".vbs", ".ps1", ".app",
                             ".vb", ".hta"]
        temp_path = self.allpath
        for extension in extensions_delete:
            for path in temp_path:
                basename = os.path.basename(path)
                if extension in basename:
                    try:
                        os.remove(path)
                    except (NameError, UnicodeEncodeError, IndexError) as e:
                        continue

    """Чтение запросов"""

    @staticmethod
    def requestsread():
        all_requests = []
        with open('requests.txt', "r") as f:
            for g in f:
                all_requests.append(g.rstrip())
        return all_requests
