'''
Real time example:donwloading

'''
import threading
import time
def donwload_file(file):
    print("Donwloading",file)
    time.sleep(2)
    print(file,"Finished")
files =[
    "movie.mp4"
    "song.mp3"
    "image.jpg"
]
threads = []
for f in files:
    t = threading.Thread(target=donwload_file,args=(f,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("All downloads finished")


import threading
import time

def student(name):
    print(name,"started exam")
    time.sleep(4)
    print(name,"Submitted paper")

t1 = threading.Thread(target=student,args=("Anas",),name="Student-1")
t2 = threading.Thread(target=student,args=("Akhil",),name="Student-2")

t1.start()
t2.start()

t1.join()
t2.join()
print("Teacher collected all papers")
