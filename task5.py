import os, time

def cpu_task():
    x = 0
    for i in range(10**7):
        x += i

def task5():
    for nice_val in [0, 5, 10]:
        pid = os.fork()
        if pid == 0:
            os.nice(nice_val)
            print(f"Child PID={os.getpid()} with nice={nice_val}")
            cpu_task()
            print(f"Child PID={os.getpid()} finished")
            os._exit(0)
    for _ in range(3):
        os.wait()

task5()
