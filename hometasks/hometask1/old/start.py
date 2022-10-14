import os
import sys
system_ = sys.platform

if system_ == "win32":
    os.system(f'python main_h1.py {os.getcwd()}/file_system.zip')
elif system_ == "linux":
    os.system(f'python3 main_h1.py {os.getcwd()}/file_system.zip')
