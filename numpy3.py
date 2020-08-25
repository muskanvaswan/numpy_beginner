import numpy

x = raw_input().strip().split()
result = []
for i in range(int(x[0])):
    row = raw_input().strip().split()
    result.append(row)
final = numpy.array(result, int)
print(numpy.transpose(final))
print(final.flatten())
