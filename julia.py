import numpy
import math
#def transform(x):
#    return 1/(x)

def generate_julia(f):
    """
    Generates a Julia set image
    """
    print('=========================================================')

    w = 1080
    h = 720
    #f = float(input('Enter a value between 0 and 1 (like 0.75): '))
   #name_input = input('Enter name of file: ')

    re_min = -2.0
    re_max = 2.0
    im_min = -2.0
    im_max = 2.0
    name = (str(f) + '.pgm')
    c = complex(0.0, f)
    real_range = numpy.arange(re_min, re_max, (re_max - re_min) / w)
    image_range = numpy.arange(im_max, im_min, (im_min - im_max) / h)
    output = open(name, 'w')
    output.write('P2\n# Julia Set image\n' + str(w) + ' ' + str(h) + '\n255\n')
    for im in image_range:
        for re in real_range:
            z = complex(re, im)
            n = 255
            while abs(z) < 10 and n >= 5:
                z = z * z + c
                n -= 5
            output.write(str(n) + ' ')
        output.write('\n')
    output.close()

    print('Created photo ' + name)
    print('=========================================================')

print("Enter the number of images you want to generate: \n")
n= int(input())
for i in range(n):
    f=i/n
    generate_julia(f)

