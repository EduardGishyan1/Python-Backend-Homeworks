from threading import Thread
from queue import Queue,Empty
import time
queue = Queue()

def log_reader(fs):
    with open("server_log.txt") as fs:
        fs.seek(0,2)
        while True:
            line = fs.readline()
            if line:
                queue.put(line)
            else:
                time.sleep(0.1)

def log_analyzer():
    while True:
        try:
            line = queue.get(timeout=1)
            if line == None:
                break
            
            if "ERROR" in line:
                print("Error")
        
        except Empty:
            continue
            
            
if __name__ == "__main__":
    
    reader_thread = Thread(target=log_reader,args=["server_log.txt"])
    analyzer_thread = Thread(target=log_analyzer)
    
    reader_thread.start()
    analyzer_thread.start()
    
    reader_thread.join()
    analyzer_thread.join()
