import multiprocessing,logging,time

logging.basicConfig(filename='system_log.txt',level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s')

def task(n):logging.info(f"{n} started");time.sleep(2);logging.info(f"{n} ended")
if __name__=="__main__":
    print("System Booting...")
    p1=p2=None
    p1=multiprocessing.Process(target=task,args=("Process-1",))
    p2=multiprocessing.Process(target=task,args=("Process-2",))
    p1.start();p2.start();p1.join();p2.join()
    print("System Shutdown.")
