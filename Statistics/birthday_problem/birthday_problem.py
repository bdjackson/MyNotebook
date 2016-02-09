from operator import mul

def n_choose_k(n, k):
    return int(reduce(mul, [float(n-i)/(i+1) for i in xrange(k)], 1))

def unique_birthday_prob(class_size):
    return 1-reduce(mul, [float(365-i)/365 for i in xrange(class_size)], 1)

if __name__ == '__main__':
    for n in xrange(5):
        print ' '.join(['%5d' % n_choose_k(n, k) for k in
                        xrange(n+1)]).center(100)

    for class_size in xrange(1, 366):
        print '%d: %0.2f %%' % (class_size, 100*unique_birthday_prob(class_size))
