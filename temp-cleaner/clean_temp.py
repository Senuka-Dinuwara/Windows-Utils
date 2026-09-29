import os
import shutil
import ctypes
import sys

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relaunch the current script with administrator privileges."""
    try:
        # ShellExecuteW passes 'runas' verb to trigger the UAC prompt
        script_path = os.path.abspath(sys.argv[0])
        params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script_path}" {params}', None, 1)
    except Exception as e:
        print(f"[!] Failed to elevate to admin: {e}")

def clean_folder(folder_path):
    """Deletes all files and subdirectories inside the given folder path."""
    if not os.path.exists(folder_path):
        print(f"[-] Folder not found: {folder_path}")
        return

    print(f"\n[+] Cleaning: {folder_path}")
    deleted_files = 0
    deleted_folders = 0
    skipped = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                deleted_files += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                deleted_folders += 1
        except Exception:
            skipped += 1

    print(f"    -> Deleted: {deleted_files} files, {deleted_folders} folders. Skipped (in use): {skipped}")

def main():
    # Check for admin rights; if not present, trigger elevation and exit current instance
    if not is_admin():
        print("[*] Requesting Administrator privileges...")
        run_as_admin()
        sys.exit(0)

    # Get target folder paths
    user_temp = os.environ.get('TEMP')  # Equivalent to %temp%
    system_temp = r"C:\Windows\Temp"
    prefetch = r"C:\Windows\Prefetch"

    folders_to_clean = [user_temp, system_temp, prefetch]

    print("=== Starting Windows Temporary File Cleanup ===")
    for folder in folders_to_clean:
        if folder:
            clean_folder(folder)

    print("\n=== Cleanup Complete! ===")
    input("Press Enter to exit...")  # Keeps the window open so you can see results

if __name__ == "__main__":
    main()