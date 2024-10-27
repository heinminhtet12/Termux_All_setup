import subprocess

def run_command(command):
    subprocess.run(command, shell=True)

# Update and upgrade
run_command("apt update")
run_command("apt upgrade -y")
run_command("pkg update -y && pkg upgrade -y")
run_command("termux-setup-storage")

# Install packages
packages = [
    "pip", "pip2", "git", "python2", "python", "bash", "php",
    "curl", "nano", "rdf", "chr", "http", "sudo", "tsu"
]

for package in packages:
    run_command(f"pkg install {package} -y")

# Install Python modules with pip and pip2
pip_modules = [
    "bs4", "requests", "mechanize", "pyrogram", "rich", 
    "mechanize requests", "locat", "futures", "sys", "so"
]

for module in pip_modules:
    run_command(f"pip install {module}")

for module in pip_modules:
    run_command(f"pip2 install {module}")
