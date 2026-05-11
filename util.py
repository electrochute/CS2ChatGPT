import winreg
import pydirectinput

last_offset = 0

def get_last_chat(log_dir, n=10):
    global last_offset
    try:
        with open(log_dir, encoding='utf-8', errors='replace') as f:
            f.seek(0, 2)
            file_size = f.tell()

            if last_offset > file_size:
                last_offset = 0

            f.seek(last_offset, 0)
            lines = f.readlines()
            last_offset = f.tell()

            return lines[-n:]
    except Exception as e:
        print(f"Ошибка чтения лога: {e}")
        return []


def write_command(command):
    try:
        cfg_path = "E:\\www\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\cfg\\message.cfg" # измени на свой путь
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(command)
    except Exception as e:
        print(f"Ошибка записи команды: {e}")


def press_key():
    pydirectinput.press('f5')  # по желанию можно поменять


def get_cs_path():
    try:
        hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\Valve\\cs2')
        path = winreg.QueryValueEx(hKey, 'installpath')[0]
        winreg.CloseKey(hKey)
        return str(path)
    except:
        return None
