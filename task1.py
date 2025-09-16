import os

def task1(n):
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1} : PID = {os.getpid()} , Parent PID = {os.getppid()}, Hello from child")
            os._exit(0)
    for i in range(n):
        os.wait()

task1(5)
