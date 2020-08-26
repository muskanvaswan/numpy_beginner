import numpy

inp = [int(item) for item in raw_input().split()]
i  = tuple(inp)
print numpy.zeros(i, dtype = numpy.int)
print numpy.ones(i, dtype = numpy.int)
