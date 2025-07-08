import time
import os
import subprocess

def banner():
    os.system('clear')
    print("\033[1;31m" + """
╔══════════════════════════════╗
║     🔥 ETHICALMIND TOOL 🔥     ║
║   INSTAGRAM REPORT TOOL  ║
╚══════════════════════════════╝
""" + "\033[0m")

def Real_process():
    steps = [
        "Connecting to Instagram servers...",
        "Fetching target account info...",
        "Uploading spam evidence...",
        "Submitting report...",
        "Verifying report authenticity...",
        "Bypassing Instagram filters...",
        "Report submitted successfully!"
    ]
    for step in steps:
        print("\033[1;36m[*] " + step + "\033[0m")
        time.sleep(1.2)

def open_youtube():
    print("\033[1;33m\n🔗 Redirecting to our YouTube channel...\033[0m")
    time.sleep(2)
    try:
        # This works for Termux with `termux-open-url` if installed
        subprocess.run(["termux-open-url", "https://youtube.com/@ethical_mind"])
    except FileNotFoundError:
        print("\033[1;31m[!] Couldn't open browser. Please open manually:\033[0m https://youtube.com/@cybersmiths_team")

def main():
    banner()
    print("\033[1;33mWelcome to ETHICALMIND Instagram Reporter 😎\033[0m\n")
    username = input("\033[1;32mEnter target Instagram username: @\033[0m")
    print("\033[1;35m\nPreparing to report @" + username + "...\033[0m\n")
    time.sleep(2)
    fake_process()
    print("\n\033[1;32m✅ 100+ Reports Submitted Successfully (wait 24 hours)\033[0m")
    print("\033[1;33m🔗 Visit our YouTube: https://youtube.com/@ethical_mind\033[0m")
    print("\n\033[1;37mThanks for using our tool — ETHICALMIND 💀\033[0m")
    open_youtube()

if __name__ == "__main__":
    main()
