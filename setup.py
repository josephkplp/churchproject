import os
import platform
import subprocess

def create_venv():
    subprocess.call(['python', '-m', 'venv', 'venv'])

def install_requirements():
    if platform.system() == "Windows":
        activate = '.\\venv\\Scripts\\activate.bat'
    else:
        activate = 'source venv/bin/activate'
    
    subprocess.call(activate, shell=True)
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    create_venv()
    install_requirements()
