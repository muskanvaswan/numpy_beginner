import numpy


#You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis .
nmp = [ int(item) for item in raw_input().split()]
arr1 = []; arr2 = [];
for n in range(nmp[0]):
    a = raw_input().split()
    arr1.append(a)

for m in range(nmp[1]):
    a = raw_input().split()
    arr2.append(a)

arra1 = numpy.array(arr1, int)
arra2 = numpy.array(arr2, int)

print numpy.concatenate((arra1, arra2), axis=0)
