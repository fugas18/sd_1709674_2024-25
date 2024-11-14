# A test object
import pickle

# Deserialization
x_reconstructed=""
with open("outputser1.pickle", "rb") as infile:
    x_reconstructed = x_reconstructed+pickle.load(infile)
print("Reconstructed object outputser1.pickle\n", x_reconstructed)
