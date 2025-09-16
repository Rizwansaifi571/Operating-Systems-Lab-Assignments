import os
import time

def task2(commands):
    for cmd in commands:
        pid = os.fork()
        if pid == 0:
            print(f"Child PID={os.getpid()} executing: {' '.join(cmd)}", flush=True)
            os.execvp(cmd[0], cmd)
            os._exit(1)
        else:
            time.sleep(0.05)
    for _ in commands:
        os.wait()

task2([["ls"], ["date"], ["ps", "-el"]])
