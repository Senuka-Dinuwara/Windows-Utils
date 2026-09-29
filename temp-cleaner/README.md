# Windows Temporary File Cleaner

A small Python script that removes the contents of three Windows temporary-file locations:

- The current user's `%TEMP%` folder
- `C:\Windows\Temp`
- `C:\Windows\Prefetch`

## Requirements

- Windows
- Python 3
- An account that can approve the Windows User Account Control (UAC) administrator prompt

## Run

Open a terminal in this folder and run:

```powershell
python clean_temp.py
```

If it is not already running as an administrator, the script requests elevation through UAC and starts an elevated copy. Approve the prompt to continue.

## What it does

For each listed folder, the script deletes its files and subfolders. It reports how many files and folders it deleted, and how many items it could not remove. Items that are in use or otherwise inaccessible are skipped. The console stays open at the end until you press Enter.

## Caution

This script deletes data without asking for confirmation and does not provide a dry-run mode. Review the target folders and the script before running it. Windows or applications may recreate temporary and Prefetch data as needed; cleanup does not guarantee a performance improvement.
