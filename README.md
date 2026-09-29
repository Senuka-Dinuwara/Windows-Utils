# Windows-Utils

A collection of small utilities for Windows maintenance and everyday tasks. Each utility lives in its own folder with its own instructions.

## Utilities

### [temp-cleaner](temp-cleaner/)

A Python script that clears the current user's temporary folder, `C:\Windows\Temp`, and `C:\Windows\Prefetch`. It requests administrator access when needed. Because it deletes files without confirmation, review its [README](temp-cleaner/README.md) before running it.