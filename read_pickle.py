import sys
import pickle

with (open(sys.argv[1], "rb")) as openfile:
    obj = pickle.load(openfile)
    print(obj, len(obj),obj[0])
