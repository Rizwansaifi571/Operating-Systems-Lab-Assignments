import platform,subprocess

print("System:",platform.system(),platform.release())
out=subprocess.getoutput("systemd-detect-virt")

print("VM Type:" if out!="none" else "Physical Machine:",out)
