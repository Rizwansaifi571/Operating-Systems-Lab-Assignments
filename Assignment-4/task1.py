import subprocess
scripts=['script1.py','script2.py','script3.py']
for s in scripts:
    print(f"Running {s}...")
    subprocess.call(['python3',s])