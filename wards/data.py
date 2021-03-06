import numpy as np

def makeGaussian(size, fwhm = 3, center=[8, 15.5]):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    output = np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)
    for array in output:
    	print '[',
    	for num in array:
    		print str(int(num*200))+',',
    	print '],',

print '[',
makeGaussian(20)
print ']'

# python data.py | sed 's/, ]/ ]/g' | sed 's/, \[/,'$'\ \[/g' > heatmap.json
