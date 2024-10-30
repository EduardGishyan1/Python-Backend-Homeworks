from threading import Thread
from queue import Queue,Empty

queue = Queue()

def log_reader(fs):
    ls = open(fs,"r+")
    read_line = ls.read()
    new_txt = open("New_File.txt","w")
    words = read_line.split()
    for word in words:
        new_txt.write(f"{word} ")
        queue.put(word)
        
def log_analyzer():
    while True:
        try:
            line = queue.get(timeout=1)
            if line == None:
                break
            
            if "ERROR:" in line:
                print("Error")
            queue.task_done()
        
        except Empty:
            continue
            
            
if __name__ == "__main__":
    
    reader_thread = Thread(target=log_reader,args=["server_log.txt"])
    analyzer_thread = Thread(target=log_analyzer)
    
    reader_thread.start()
    analyzer_thread.start()
    
    reader_thread.join()
    analyzer_thread.join()
    