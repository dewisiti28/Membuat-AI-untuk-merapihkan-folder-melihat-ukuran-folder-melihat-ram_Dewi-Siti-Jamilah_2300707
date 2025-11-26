import os
import shutil
import psutil  

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        return f"Folder '{folder_path}' tidak ditemukan."

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.replace(".", "").lower() or "no_ext"

        dest_folder = os.path.join(folder_path, ext)
        os.makedirs(dest_folder, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(dest_folder, filename))
        except:
            pass

    return "Folder berhasil dirapikan berdasarkan jenis file."


def get_folder_size(folder_path):
    total = 0
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                total += os.path.getsize(fp)
            except:
                pass
    return total


def check_ram_status():
    mem = psutil.virtual_memory()
    total = mem.total / (1024 * 1024 * 1024)
    available = mem.available / (1024 * 1024 * 1024)
    used = total - available
    percent = mem.percent

    return (
        f"RAM Total: {total:.2f} GB\n"
        f"RAM Terpakai: {used:.2f} GB ({percent}%)\n"
        f"RAM Tersedia: {available:.2f} GB"
    )
