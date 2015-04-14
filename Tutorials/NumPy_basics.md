
# NumPy basics
This is mostly a refresher, but I want to make sure I'm not missing some basic
syntax.


        import numpy as np

## Testing basic commands


    a = np.arange(15).reshape(3, 5)
    a




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])



### the number of dimensions in this array


    a.ndim




    2



### The data type of the elements


    a.dtype.name




    'int64'



### The size in bytes of each element


    a.itemsize




    8



### The number of elements in the array


    a.size




    15



## Creating arrays

### We can make an array with different types


    a = np.array([1,2,3])
    a.dtype.name




    'int64'




    b = np.array([1.2,3.4,5.6])
    b.dtype.name




    'float64'



### We can even specify the type


    c = np.array([[1,2], [3,4]], dtype='complex')
    c




    array([[ 1.+0.j,  2.+0.j],
           [ 3.+0.j,  4.+0.j]])



### Creating placeholder arrays with set size, but default values
This is useful when the size of the array is known, but not the values.
It is possible to construct the array one row at a time, but that is
much more expensive than creating the array with the final size,
filled with default values, and then filling it in afterward.


    np.zeros((2,3))




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




    np.ones((2,3,4))




    array([[[ 1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.]],
    
           [[ 1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.]]])




    np.empty((2,3)) # the default value is random, and depends on the state of memory




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])



### Create a sequence of numbers


    np.arange(10, 30, 5)




    array([10, 15, 20, 25])




    np.arange(0.1, 3.4, 0.4)




    array([ 0.1,  0.5,  0.9,  1.3,  1.7,  2.1,  2.5,  2.9,  3.3])



When working with floating point divisions, it is usually better to use
`linspace` as the number of values is specified, rather than the step size. This
results in a more predictable array size.


    np.linspace(0, 5, 11)




    array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ])




    np.linspace(0, 2*np.pi, 100)




    array([ 0.        ,  0.06346652,  0.12693304,  0.19039955,  0.25386607,
            0.31733259,  0.38079911,  0.44426563,  0.50773215,  0.57119866,
            0.63466518,  0.6981317 ,  0.76159822,  0.82506474,  0.88853126,
            0.95199777,  1.01546429,  1.07893081,  1.14239733,  1.20586385,
            1.26933037,  1.33279688,  1.3962634 ,  1.45972992,  1.52319644,
            1.58666296,  1.65012947,  1.71359599,  1.77706251,  1.84052903,
            1.90399555,  1.96746207,  2.03092858,  2.0943951 ,  2.15786162,
            2.22132814,  2.28479466,  2.34826118,  2.41172769,  2.47519421,
            2.53866073,  2.60212725,  2.66559377,  2.72906028,  2.7925268 ,
            2.85599332,  2.91945984,  2.98292636,  3.04639288,  3.10985939,
            3.17332591,  3.23679243,  3.30025895,  3.36372547,  3.42719199,
            3.4906585 ,  3.55412502,  3.61759154,  3.68105806,  3.74452458,
            3.8079911 ,  3.87145761,  3.93492413,  3.99839065,  4.06185717,
            4.12532369,  4.1887902 ,  4.25225672,  4.31572324,  4.37918976,
            4.44265628,  4.5061228 ,  4.56958931,  4.63305583,  4.69652235,
            4.75998887,  4.82345539,  4.88692191,  4.95038842,  5.01385494,
            5.07732146,  5.14078798,  5.2042545 ,  5.26772102,  5.33118753,
            5.39465405,  5.45812057,  5.52158709,  5.58505361,  5.64852012,
            5.71198664,  5.77545316,  5.83891968,  5.9023862 ,  5.96585272,
            6.02931923,  6.09278575,  6.15625227,  6.21971879,  6.28318531])



## Printing arrays
When printing, in general:
- Last index: printed horizonatally
- Second to last index: printed vertially
- All other indices: printed as separate grids separated by an empty line


    np.arange(5)




    array([0, 1, 2, 3, 4])




    np.arange(9).reshape(3,3)




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




    np.arange(18).reshape(2,3,3)




    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8]],
    
           [[ 9, 10, 11],
            [12, 13, 14],
            [15, 16, 17]]])



## Basic operations
We can perform arithmetic operations, which are applied element-wise. A new
array is created with the result.


    a = np.linspace(1, 9, 9)
    b = np.linspace(11, 19, 9)


    a - b




    array([-10., -10., -10., -10., -10., -10., -10., -10., -10.])




    a/b




    array([ 0.09090909,  0.16666667,  0.23076923,  0.28571429,  0.33333333,
            0.375     ,  0.41176471,  0.44444444,  0.47368421])




    np.sin(a)




    array([ 0.84147098,  0.90929743,  0.14112001, -0.7568025 , -0.95892427,
           -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849])




    a > 5




    array([False, False, False, False, False,  True,  True,  True,  True], dtype=bool)




    a*b




    array([  11.,   24.,   39.,   56.,   75.,   96.,  119.,  144.,  171.])



Notice how the product is also applied element-wise. Matrix multiplication can
be achieved using the `numpy.dot` function or the matrix class


    np.dot(a,b)




    735.0




    np.dot(a.reshape(3,3), b.reshape(3,3))




    array([[  90.,   96.,  102.],
           [ 216.,  231.,  246.],
           [ 342.,  366.,  390.]])



We can use the `+=`, `*=`, etc. operators as well


    a = np.ones((5,5))


    a




    array([[ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.]])




    a += np.ones((5,5))
    a




    array([[ 2.,  2.,  2.,  2.,  2.],
           [ 2.,  2.,  2.,  2.,  2.],
           [ 2.,  2.,  2.,  2.,  2.],
           [ 2.,  2.,  2.,  2.,  2.],
           [ 2.,  2.,  2.,  2.,  2.]])




    a *= np.ones((5,5))*3
    a




    array([[ 6.,  6.,  6.,  6.,  6.],
           [ 6.,  6.,  6.,  6.,  6.],
           [ 6.,  6.,  6.,  6.,  6.],
           [ 6.,  6.,  6.,  6.,  6.],
           [ 6.,  6.,  6.,  6.,  6.]])



## Unary operators performed on arrays
These include things like `sum`, `min`, `max`


    a = np.random.random((3,2))
    a




    array([[ 0.30050529,  0.78642735],
           [ 0.98630357,  0.20639702],
           [ 0.45195205,  0.73952578]])




    a.sum()




    3.4711110655308173




    a.min()




    0.20639702303234342




    a.max()




    0.98630357240644584



These operators are applied across all the elements in the array, however it is
possible to specify a dimension.


    a = np.arange(12).reshape(3,4)
    a




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




    a.sum(axis=0) # sum across columns




    array([12, 15, 18, 21])




    a.sum(axis=1) # sum across rows




    array([ 6, 22, 38])




    a.cumsum(axis=1) # cumulative sum across rows




    array([[ 0,  1,  3,  6],
           [ 4,  9, 15, 22],
           [ 8, 17, 27, 38]])



## Indexing, slicing, and looping
We can index, slice, and loop similar to a standard array


    a = np.arange(10)**3
    a




    array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])




    a[8]




    512




    a[2:5]




    array([ 8, 27, 64])




    a[:6:2] = -1000 # replace even elements less than 6 with -1000
    a




    array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])




    a[::-1] # reverse array




    array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])




    for i in a:
        print i,
    print
    for i in a:
        print i**(1/3.),

    -1000 1 -1000 27 -1000 125 216 343 512 729
    nan 1.0 nan 3.0 nan 5.0 6.0 7.0 8.0 9.0


    -c:5: RuntimeWarning: invalid value encountered in power


Multidimensional arrays can have one index per dimension


    a = np.fromfunction(lambda x,y: 10*x+y, (5,4), dtype=int)
    a




    array([[ 0,  1,  2,  3],
           [10, 11, 12, 13],
           [20, 21, 22, 23],
           [30, 31, 32, 33],
           [40, 41, 42, 43]])




    a[2,3] # get a single element




    23




    a[0:5, 1] # get the complete second column




    array([ 1, 11, 21, 31, 41])




    a[:, 1] # same as above with less typing




    array([ 1, 11, 21, 31, 41])




    a[1:3, :] # get the complete second and third rows




    array([[10, 11, 12, 13],
           [20, 21, 22, 23]])



If fewer indices is given than the number of dimensions, the missing indices
will be taken as complete slices


    a[-1]




    array([40, 41, 42, 43])




    a[0]




    array([0, 1, 2, 3])



We can also use `...` to indicate "enough `:`'s as needed to represent the
remaining rows." This is useful when the first or middle indices are complete
slices, but not the indices at the end


    a[..., 1]




    array([ 1, 11, 21, 31, 41])



### Iterating over a multimensional array


    for row in a:
        print row, ' - ',
        for col in row:
            print col,
        print

    [0 1 2 3]  -  0 1 2 3
    [10 11 12 13]  -  10 11 12 13
    [20 21 22 23]  -  20 21 22 23
    [30 31 32 33]  -  30 31 32 33
    [40 41 42 43]  -  40 41 42 43


It's also possible to iterate over all the elements in the array using the
`flat` attribute


    for element in a.flat:
        print element,

    0 1 2 3 10 11 12 13 20 21 22 23 30 31 32 33 40 41 42 43


## Shape manipulation


    a = np.floor(10*np.random.random((3,4)))
    a




    array([[ 2.,  8.,  4.,  0.],
           [ 1.,  7.,  5.,  3.],
           [ 0.,  2.,  8.,  1.]])




    a.shape




    (3, 4)



We can change the shape of the array using any of these commands


    a.ravel() # flatten




    array([ 2.,  8.,  4.,  0.,  1.,  7.,  5.,  3.,  0.,  2.,  8.,  1.])



Notice that when `ravel()` is called, the array is flattened as a "C-style"
array. That is the right-most number changes the fastest, and the rows are
appended to one another.


    a.shape = (6,2)
    a




    array([[ 2.,  8.],
           [ 4.,  0.],
           [ 1.,  7.],
           [ 5.,  3.],
           [ 0.,  2.],
           [ 8.,  1.]])



Notice again, the order is treated as C-style when the dimension is changed


    a.transpose()




    array([[ 2.,  4.,  1.,  5.,  0.,  8.],
           [ 8.,  0.,  7.,  3.,  2.,  1.]])



The `reshape` function returns a modified array with new dimensions, while the
`resize` fucntion modifies the array in place


    a.resize((4,3))
    a




    array([[ 2.,  8.,  4.],
           [ 0.,  1.,  7.],
           [ 5.,  3.,  0.],
           [ 2.,  8.,  1.]])




    a.reshape(6,-1) # a dimension with -1 will be calculated automatically




    array([[ 2.,  8.],
           [ 4.,  0.],
           [ 1.,  7.],
           [ 5.,  3.],
           [ 0.,  2.],
           [ 8.,  1.]])




    a # unmodified




    array([[ 2.,  8.,  4.],
           [ 0.,  1.,  7.],
           [ 5.,  3.,  0.],
           [ 2.,  8.,  1.]])



### Arrays can be stacked as well


    a = np.floor(10*np.random.random((2,2)))
    b = np.floor(10*np.random.random((2,2)))


    a




    array([[ 2.,  9.],
           [ 6.,  3.]])




    b




    array([[ 9.,  8.],
           [ 4.,  1.]])



`vstack()` can be used to stack arrays vertically


    np.vstack((a,b))




    array([[ 2.,  9.],
           [ 6.,  3.],
           [ 9.,  8.],
           [ 4.,  1.]])




    np.vstack((a,b,a))




    array([[ 2.,  9.],
           [ 6.,  3.],
           [ 9.,  8.],
           [ 4.,  1.],
           [ 2.,  9.],
           [ 6.,  3.]])



`hstack()` can be used to stack arrays horizontally


    np.hstack((a,b))




    array([[ 2.,  9.,  9.,  8.],
           [ 6.,  3.,  4.,  1.]])



`column_stack()` is essentially a wrapper around `vstack()`. This has slightly
different behavior which can be quite convenient.


    np.column_stack(([1,2,3],[4,5,6]))




    array([[1, 4],
           [2, 5],
           [3, 6]])




    np.vstack(([1,2,3],[4,5,6]))




    array([[1, 2, 3],
           [4, 5, 6]])




    np.hstack(([1,2,3],[4,5,6]))




    array([1, 2, 3, 4, 5, 6])



### Splitting an array
An array can be split into n equal sub-arrays or split at particular divisors


    a = np.floor(10*np.random.random((2,12)))
    a




    array([[ 2.,  4.,  4.,  4.,  2.,  6.,  2.,  6.,  7.,  6.,  5.,  0.],
           [ 6.,  6.,  8.,  7.,  3.,  2.,  3.,  4.,  8.,  3.,  9.,  3.]])




    np.hsplit(a, 3) # split into 3 equal sub-arrays




    [array([[ 2.,  4.,  4.,  4.],
            [ 6.,  6.,  8.,  7.]]), array([[ 2.,  6.,  2.,  6.],
            [ 3.,  2.,  3.,  4.]]), array([[ 7.,  6.,  5.,  0.],
            [ 8.,  3.,  9.,  3.]])]




    np.hsplit(a,(4,6,8)) # split on columns 4, 6, and 8




    [array([[ 2.,  4.,  4.,  4.],
            [ 6.,  6.,  8.,  7.]]), array([[ 2.,  6.],
            [ 3.,  2.]]), array([[ 2.,  6.],
            [ 3.,  4.]]), array([[ 7.,  6.,  5.,  0.],
            [ 8.,  3.,  9.,  3.]])]



`vsplit` can be used to split on the rows rather than columns


    b = np.floor(10*np.random.random((12,2)))
    b




    array([[ 2.,  5.],
           [ 4.,  9.],
           [ 7.,  5.],
           [ 9.,  7.],
           [ 3.,  3.],
           [ 4.,  8.],
           [ 9.,  4.],
           [ 4.,  4.],
           [ 7.,  8.],
           [ 1.,  6.],
           [ 0.,  9.],
           [ 2.,  7.]])




    np.vsplit(b, 4)




    [array([[ 2.,  5.],
            [ 4.,  9.],
            [ 7.,  5.]]), array([[ 9.,  7.],
            [ 3.,  3.],
            [ 4.,  8.]]), array([[ 9.,  4.],
            [ 4.,  4.],
            [ 7.,  8.]]), array([[ 1.,  6.],
            [ 0.,  9.],
            [ 2.,  7.]])]




    np.vsplit(b, (5,6))




    [array([[ 2.,  5.],
            [ 4.,  9.],
            [ 7.,  5.],
            [ 9.,  7.],
            [ 3.,  3.]]), array([[ 4.,  8.]]), array([[ 9.,  4.],
            [ 4.,  4.],
            [ 7.,  8.],
            [ 1.,  6.],
            [ 0.,  9.],
            [ 2.,  7.]])]



## Columns and views


    
