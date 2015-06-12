import sys
import time
def readfile(arg):
    with open(arg,'r') as my_file:
        a = [items.rstrip("\n\r") for items in my_file.readlines()]
        print a
if __name__ == '__main__':
    start = time.clock()
    readfile(sys.argv[1])
    stop = time.clock()
    run_time= stop - start
    print "This program ran in %d second(s)" % (run_time)
