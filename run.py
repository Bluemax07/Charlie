import multiprocessing

def beggin():
    print("process 1")
    from main import start
    start()

def detect():
    print("process 2")
    from back.feature import hotword
    hotword()

if __name__=='__main__':
    p1=multiprocessing.Process(target=beggin)
    p2=multiprocessing.Process(target=detect)
    p1.start()
    p2.start()
    p1.join()
    if p2.is_alive():
        p2.terminate()
        p2.join
    print("stop")
