from threading import Thread
from time import sleep, time
from multiprocessing import Process


# for class thread 

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello: ", i+1,"\n")
#             sleep(0.3)



# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi: ", i+1)
#             sleep(0.1)



# if __name__=="__main__":
    # t1=Thread(target=hello)
    # sleep(0.3)
    # t2=Thread(target=hi)

    # t1.start()
    # t2.start()


    # t1.join()
    # t2.join()


# for fucntion thread 

def hello():
    for i in range(5):
        print("Hello: ", i+1,"\n")
        sleep(0.3)
      

def hi():
     for i in range(5):
      print("Hi: ", i+1)
      sleep(0.1)


def download(file_name):      
    print("Downloading file...", file_name)
    sleep(0.3)
    print("Download complete")


# if __name__=="__main__":


#     start=time()
#     files=['video.mp4', 'image.png', 'data.csv']

#     for f in files:
#         download(f)

#     end=time()

#     print(f"serial time {end-start:.2f} seconds")


#     threads=[]

#     for f in files:
#         t=Thread(target=download, args=(f,))
#         threads.append(t)

#     start=time()    

#     for t in threads:
#         t.start()

#     for t in threads:    
#         t.join()

#     end=time()    

#     print(f"parallel with thread  time {end-start:.2f} seconds")
#     print("Bye")


# io bound operation 

def calculate(n1, n2): 
    sum=0
    for n in range(n1, n2):
        sum+=n*n



if __name__=="__main__":

    num=50000000
    start=time()

    calculate(0, num)
 

    end=time()

    print(f"serial time {end-start:.2f} seconds")

    mid=num // 2

   

    t1=Thread(target=calculate, args=(0, mid))
    t2=Thread(target=calculate, args=(mid, num))


    start=time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=time()

    print(f"parallel with thread time {end-start:.2f} seconds")


    t1=Process(target=calculate, args=(0, mid))
    t2=Process(target=calculate, args=(mid, num))
    
    
    start=time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=time()

    print(f"parallel with process time {end-start:.2f} seconds")

    print("Bye")
