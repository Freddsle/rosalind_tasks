from contextlib import contextmanager
import timeit


def my_timer(my_code):

    def print_timer():
        start = timeit.default_timer()        
        my_code()
        stop = timeit.default_timer()
        print('Running time: ', stop - start)  

    return print_timer
    