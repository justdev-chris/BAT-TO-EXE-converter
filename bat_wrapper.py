import os
import tempfile
import subprocess

def run_bat_from_exe(input_file='input.bat'):
    with open(input_file, 'r', encoding='utf-8') as f:
        bat_content = f.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat') as temp_bat:
        temp_bat.write(bat_content.encode('utf-8'))
        temp_bat_path = temp_bat.name

    subprocess.call(['cmd.exe', '/c', temp_bat_path])
    os.remove(temp_bat_path)

if __name__ == "__main__":
    run_bat_from_exe()
