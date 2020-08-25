import numpy

inp = raw_input().strip().split(" ")
result = numpy.array(inp, int)
print(numpy.reshape(result,(3,3)))
