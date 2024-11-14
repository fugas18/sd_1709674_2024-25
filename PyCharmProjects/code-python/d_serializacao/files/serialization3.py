import pickle
def identity(n):
    return n
y=identity(4)

outfile = open("outputser3", "wb")
pickle.dump(identity, outfile)
#pickle.dump(y, outfile)