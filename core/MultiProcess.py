import multiprocessing
from multiprocessing import Lock
#from core.main import getAllReviews
from core.getReview import getReview

def fun(i):
    print(i)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target= fun, args = (str(1)))
    process2 = multiprocessing.Process(target=fun, args=(str(2)))
    process3 = multiprocessing.Process(target=fun, args=(str(3)))
    process4 = multiprocessing.Process(target=fun, args=(str(4)))
    process1.start()
    process1.join()
    process2.start()
    process2.join()
    process3.start()
    process3.join()
    process4.start()
    process4.join()


    print("Finished!")