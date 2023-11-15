import time
import multiprocessing

"""
def calc_square(numbers):
    for n in numbers:
        time.sleep(2)
        print('Square ' + str(n*n))
def calc_cube(numbers):
    for n in numbers:
        time.sleep(2)
        print('Cube ' + str(n*n*n))

if __name__  == "__main__":
    a = [2,3,8,9]

    p1 = multiprocessing.Process(target=calc_square, args=(a,))
    p2 = multiprocessing.Process(target=calc_cube, args=(a,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Done!')
"""

square_result = []

def calcu_square(numbers):
    global square_result
    for n in numbers:
        time.sleep(2)
        print('Square ' + str(n*n))
        square_result.append(n*n)
    print('Within a process : Result ' + str(square_result))

if __name__ == "__main__":
    a = [2,4,8,9]
    t1 = multiprocessing.Process(target=calcu_square, args=(a,))
    t1.start()
    t1.join()
    print('Resul'+ str(square_result))
    print('Done!')