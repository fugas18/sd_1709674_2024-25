# A test object
import pickle

f = open("demo1.txt", "r",encoding='utf8')
x=f.read()

# Serialization
with open("outputser1.pickle", "wb") as outfile:
    pickle.dump(x, outfile)
print("Written object outputser1")