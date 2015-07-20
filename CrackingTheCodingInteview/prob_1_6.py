def rotate_image(image):
    N = len(image)
    num_layers = N/2

    for layer in xrange(num_layers):
        right_col = N-1-layer
        bottom_row = N-1-layer
        for col in xrange(layer, right_col):
            temp = image[layer][col]
            image[layer][col] = image[bottom_row-col][layer]
            image[bottom_row-col][layer] = image[bottom_row][right_col-col]
            image[bottom_row][right_col-col] = image[layer+col][right_col]
            image[layer+col][right_col] = temp

# ------------------------------------------------------------------------------
test_image = [['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]
print '\n'.join([str(item) for item in test_image])
print
rotate_image(test_image)
print '\n'.join([str(item) for item in test_image])
print

test_image = [['0','1','2','3'],
              ['4','5','6','7'],
              ['8','9','a','b'],
              ['c','d','e','f']]
print '\n'.join([str(item) for item in test_image])
print
rotate_image(test_image)
print '\n'.join([str(item) for item in test_image])
print

test_image = [['0','1','2','3','4'],
              ['5','6','7','8','9'],
              ['a','b','c','d','e'],
              ['f','g','h','i','j'],
              ['k','l','m','n','o'],
              ]
print '\n'.join([str(item) for item in test_image])
print
rotate_image(test_image)
print '\n'.join([str(item) for item in test_image])
print
