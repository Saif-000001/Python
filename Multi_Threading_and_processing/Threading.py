import time
import threading

def calculate_square(n):
    print("Calculate square number :")
    for i in n:
        time.sleep(2)
        print("Square = ", i*i)
def calculate_cube(n):
    print("Calculate cube number :")
    for i in n:
        time.sleep(2)
        print("Cube = ", i*i*i)
a = [2,3,8,9]
# calculate_square(a)
# calculate_cube(a)


t = time.time()

t1 = threading.Thread(target=calculate_square, args=(a,))
t2 = threading.Thread(target=calculate_cube, args=(a,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in :",time.time()-t)
print("Hah....I am done my with all my work now!")