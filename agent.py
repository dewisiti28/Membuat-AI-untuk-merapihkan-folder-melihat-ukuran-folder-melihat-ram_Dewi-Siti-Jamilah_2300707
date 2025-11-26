import re
import json
import requests
from colorama import init, Fore, Style
from tool_schema import Command
from tools import organize_folder, get_folder_size, check_ram_status

init(autoreset=True)

a = 
b =
c =
d =

#sengaja dikosongkan

OPENROUTER_API_KEY = a + b + c + d
OPENROUTER_BASE_URL = ""
OPENROUTER_URL = f""

def ask_ai(user_text):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content":
                (
                    "Tugas Anda adalah mengubah perintah bahasa manusia menjadi JSON "
                    "dengan format: {\"folder\":..., \"organize\":..., \"size\":..., \"check_ram\":...}.\n"
                    "Jika user minta rapikan folder → organize=True.\n"
                    "Jika user minta ukuran folder → size=True.\n"
                    "Jika user minta cek RAM → check_ram=True.\n"
                    "Jika user menyebut folder (misal C:\\Folder) → ambil sebagai folder."
                )
            },
            {"role": "user", "content": user_text}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    res = requests.post(OPENROUTER_URL, headers=headers, json=payload).json()

    try:
        return json.loads(res["choices"][0]["message"]["content"])
    except:
        return {"error": "AI gagal parsing JSON", "raw": res}

print("=== SIMPLE AI AGENT (OpenRouter) ===")
print("Ketik 'exit' untuk keluar.\n")
input("Tekan ENTER untuk mulai...\n")

while True:
    user_text = input(Fore.GREEN + "User: ")

    if user_text.strip().startswith("& \"C:/Users/"):
        print(Fore.RED + "(Input otomatis PowerShell terdeteksi → diabaikan)\n")
        continue

    if user_text.lower() == "exit":
        print("Keluar...")
        break

    print(Fore.YELLOW + "Agent thinking...")

    ai = ask_ai(user_text)
    if "error" in ai:
        print(ai)
        continue

    cmd = Command(
        folder=ai.get("folder"),
        organize=ai.get("organize"),
        size=ai.get("size"),
        check_ram=ai.get("check_ram")
    )

    print(Fore.WHITE + f"\nCommand AI: {cmd}\n")


    if cmd.organize and cmd.folder:
        print(Fore.CYAN + organize_folder(cmd.folder))

    if cmd.size and cmd.folder:
        size_bytes = get_folder_size(cmd.folder)
        size_mb = size_bytes / (1024 * 1024)
        print(Fore.CYAN + f"Ukuran folder '{cmd.folder}': {size_mb:.2f} MB")

    if cmd.check_ram:
        print(Fore.CYAN + check_ram_status())

    print()

