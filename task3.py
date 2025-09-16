import os, time

def zombie():
    pid = os.fork()
    if pid == 0:
        print(f"Child (PID={os.getpid()}) exiting immediately")
        os._exit(0)   
    else:
        print(f"Parent (PID={os.getppid()}) not waiting → child becomes zombie")
        time.sleep(15)   
        os.wait()
        print("Parent: child reaped, zombie cleared")

zombie()


def orphan():
    pid = os.fork()
    if pid == 0:
        time.sleep(5)  
        print(f"Child (PID={os.getpid()}) new Parent PID={os.getppid()} (adopted by init)")
        os._exit(0)
    else:
        print(f"Parent (PID={os.getpid()}) exiting immediately → child becomes orphan")
        os._exit(0)

orphan()