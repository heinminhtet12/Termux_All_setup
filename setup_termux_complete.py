import subprocess

# List of commands to run
commands = [
    "apt update",
    "apt upgrade -y",
    "pkg update -y && pkg upgrade -y",
    "termux-setup-storage",
    "pkg install pip -y",
    "pkg install pip2 -y",
    "pkg upgrade -y",
    "pkg install git -y",
    "pkg install python2 -y",
    "pkg install python -y",
    "pkg install python2 -y",
    "pkg install bash -y",
    "pkg install php -y",
    "pkg install curl -y",
    "pkg install nano -y",
    "pkg install git -y",
    "pkg install bs4 -y",
    "pkg install rdf -y",
    "pkg install chr -y",
    "pkg install http -y",
    "pkg install sudo -y",
    "pkg install tsu -y",
    "pip2 install mechanize",
    "pip2 install requests",
    "pip3 install -U pyrogram",
    "pip install rich",
    "pip install requests",
    "pip install mechanize",
    "pip install locat",
    "pip install bs4",
    "pip2 install bs4",
    "pip install futures",
    "pip2 install futures",
    "pip install sys",
    "pip2 install sys",
    "pip install so"
]

# Run each command in the list
for command in commands:
    print(f"Running: {command}")
    subprocess.run(command, shell=True)
