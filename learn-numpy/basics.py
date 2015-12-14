import numpy as np

a = np.arange(15)
print 'a=np.arange(15): {0}'.format(a)

a = a.reshape(3, 5)

print 'after a.reshape(3, 5): {0}'.format(a)
print 'a.ndim: {0}'.format(a.ndim)
print 'a.shape: {0}'.format(a.shape)
print 'a.dtype: {0}'.format(a.dtype)

def dividor():
    print '-' * 30

dividor()

print 'create an array of complex'

a = np.array([ [1, 2], [4, -1] ], dtype = complex)

print a
