import json, os, threading, time, requests, colorama, sys
from colorama import Fore


class Main:
    def __init__(self):
        def sex():
            print(f"1 - Reporter\n2 - Help\n3 - Exit")
            poo = input("->")
            if poo == "1":
                print("\n")
                self.TOKEN = input('Enter your token-> ')
                self.GUILD_ID = input('Server ID-> ')
                self.CHANNEL_ID = input('Channel ID-> ')
                self.MESSAGE_ID = input('Message ID-> ')
            elif poo == "2":
                print("This spams reports a message someone has sent\nThis does not mean an automatic ban\nIt's up to discord to ban them, or the server")
                os.system("pause")
                os.system("cls")
                sex()
            elif poo == "3":
                exit()
            else:
                print("Invalid command")
                os.system("pause")
                os.system("cls")
                sex()
        sex()
        REASON = input(
            '\n1 - Illegal content\n'
            '2 - Harassment\n'
            '3 - Spam or phishing links\n'
            '4 - Self-harm\n'
            '5 - NSFW content\n\n'
            'Reason -> '
        )

        if REASON.upper() in ('1', 'ILLEGAL CONTENT'):
            self.REASON = 0
        elif REASON.upper() in ('2', 'HARASSMENT'):
            self.REASON = 1
        elif REASON.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            self.REASON = 2
        elif REASON.upper() in ('4', 'SELF-HARM'):
            self.REASON = 3
        elif REASON.upper() in ('5', 'NSFW CONTENT'):
            self.REASON = 4
        else:
            print(Fore.RED +'\nInvalid reason inputted.'+ Fore.RESET)
            os.system("pause")
            os.system("python main.py")

        self.RESPONSES = {
            '401: Unauthorized': f'{Fore.RED}Invalid discord token{Fore.RESET}',
            'Missing Access': f'{Fore.RED}Missing access to channel or guild given.{Fore.RESET}',
            'You need to verify your account in order to perform this action.': 'Please verify your discord account.'
        }
        self.sent = 0
        self.errors = 0

    def _reporter(self):
        report = requests.post(
            'https://discordapp.com/api/v8/report', json={
                'channel_id': self.CHANNEL_ID,
                'message_id': self.MESSAGE_ID,
                'guild_id': self.GUILD_ID,
                'reason': self.REASON
            }, headers={
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'sv-SE',
                'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                'Content-Type': 'application/json',
                'Authorization': self.TOKEN
            }
        )
        if (status := report.status_code) == 201:
            self.sent += 1
        elif status in (401, 403):
            self.errors += 1
        else:
            self.errors += 1
            print(f'[!] Error: {report.text} | Status Code: {status}')

    def _update_title(self):
        while True:
            os.system(f'title discord reporter successful: {self.sent} ^- errors: {self.errors}')
            print(f"{Fore.CYAN}Reports sent: {self.sent}{Fore.RESET}")
            print(f"{Fore.CYAN}Errors: {self.errors}{Fore.RESET}")
            time.sleep(0.1)
            os.system("cls")

    def _multi_threading(self):
        threading.Thread(target=self._update_title).start()
        while True:
            if threading.active_count() <= 300:
                threading.Thread(target=self._reporter).start()

    def setup(self):
        print()
        self._multi_threading()


if __name__ == '__main__':
    os.system('cls && title discord reporter fbi#0001')
    main = Main()
    main.setup()
