import os

def task4(pid):
    with open(f"/proc/{pid}/status") as f:
        for line in f:
            if line.startswith(("Name:", "State:", "VmSize:")):
                print(line.strip())
    print("Executable Path:", os.readlink(f"/proc/{pid}/exe"))
    print("Open FDs:", os.listdir(f"/proc/{pid}/fd"))

task4(os.getpid())
