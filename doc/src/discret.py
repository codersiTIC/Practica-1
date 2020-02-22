# -*- encoding: utf-8 -*-

'''
Module *discret*
================

The module *discret* basically contains the functions for the color image proccessing, 
like converting the fromat of the image into another, for example, convert an image in RGB 
to a Greyscale format.


This is the list of all of it:

'''

#from img import *
#from imgio import *


def rgb_to_lum(pixel):
	
	"""

        Returns the luminance level of a RGB (R, G, B) pixel using a simple formula:\n

        The luminance of a pixel in RGB is **(R + G + B) / 3**

        :param pixel: Pixel
        :type pixel: tuple
        :returns: The luminance of the RGB pixel
        :rtype: int

	>>> rgb_to_lum((255,255,255))
	255
	>>> rgb_to_lum((255,0,0))
	85

	"""

	l = 0
	if len(pixel) != 3:
		return 'Incorrect pixel'

	else:
		for element in pixel:
			if element not in range(256):
				return 'Incorrect pixel'

			else:
				l += element

	return l/3

def luminance_img(i):

	"""

        Transforms a RGB image into a L image using *rgb_to_lum(i)* for each pixel tuple in RGB

        :param i: Image ('RGB', Matrix)
        :type i: tuple
        :returns: The an L image format from an RGB image
        :rtype: tuple ('L', Matrix)

	>>> luminance_img('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])
	('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	>>> luminance_img('RGB', [[(255, 0, 255), (255, 255, 255)], [(0, 0, 255), (255, 0, 255)]])
	('L', [[170, 255], [85, 170])

	"""

	l = []
	for fila in matrix(i):
		s = []
		for pixel in fila:
			s.append(rgb_to_lum(pixel))

			if rgb_to_lum(pixel)=='Incorrect pixel':
				return 'Incorrect image'

		l.append(s)

	return ('L', l)


def histogram(i):

	"""
	Histogram of grey values of the L image i

        :param i: Image (Type, Matrix)
        :type i: tuple
        :returns: A list of the 256 values (0 upto 255) of the grey scale values of the L format image
        :rtype: list

	>>> histogram(('L', [[255, 255, 255, 255], [255, 255, 255, 255]]))
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
	>>> histogram(('L', [[255, 255, 0, 0], [0, 250, 250, 250]]))
	[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2]
	"""

	dic = {}
	img = luminance_img(i)
	for element in img[1]:
		for value in element:
			dic[value] = dic.get(value,0)+1

	for grey in range(256):
		dic[grey] = dic.get(grey,0)

	return dic.values()


def get_threshold(i):

	histData = histogram(i)

	srcData = luminance_img(i)

	total = len(srcData[1]) # len(srcData[1])*len(srcData[1][0]) TOTS els pixels (NO)

	suma = 0.0
	for t in range(256):
		suma += t * histData[t]

	sumB = 0.0
	wB = 0
	wF = 0

	varMax = 0.0
	threshold = 0

	for t in range(256):
		wB += histData[t]
		if (wB == 0): continue

		wF = total - wB
		if (wF == 0): break

		sumB += float(t * histData[t])

		mB = float(sumB)/wB
		mF = float(suma - sumB) / wF

		varBetween = float(wB) * float(wF) * ((mB - mF)**2)

		if (varBetween > varMax):
			varMax = varBetween
			threshold = t
			return threshold



def rgb_to_bn(i):

	"""

        Transforms a RGB image into a 1 image format using luminance and histogram, with the image
        converted into a grey scale format (L).\n
        The function goes through each pixel of the 
        L image and compares it with a certain value to know if it is part from the Backgound or Foreground.\n
        In this case we've decieded that the medium value to know if a L pixel
        is black or white is the 128, if is greater or equally to 128 is a white pixel and is a black pixel if not.

        .. note::
        	We've had troubles in the making of the project because of the Otsu Thresholding Method Algorithm,
        	it is supposed that using this algorithm should give us the medium value to know if the pixel
        	it is a part from the Background (black) or Foreground (white).\n
        	But we’be translated the code that it is written natively in java to python and it didn't work, 
        	even though that the code is almost exactly the same.

        :param i: Image ('RGB', Matrix)
        :type i: tuple
        :returns: The an 1 image format from an RGB image using *luminance_img(i)*
        :rtype: tuple ('1', Matrix)

	>>> rgb_to_bn(('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)],[(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]))
	('1', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	>>> rgb_to_bn(('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)],[(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]))
	('1', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])

	"""


	#threshold = get_threshold(i)
	image_RGB = luminance_img(i)
	s = []
	for element in image_RGB[1]:
		f = []
		for pixel in element:
			if pixel >= 128: #thresehold:
				f.append(255)
			else:
				f.append(0)

		s.append(f)


	im_bn = ('1', s)
	#matrix2img(s,'rgb_to_bn.jpeg', '1')
	return ('1', s)

def L_to_bn(i):

	#threshold = get_threshold(i)
	try:
		image_L = (matrix(i))

	except AttributeError:
		image_L = i

	s = []
	for element in image_L:
		f = []
		for pixel in element:
			if pixel >= 128: #thresehold:
				f.append(255)
			else:
				f.append(0)

		s.append(f)


	im_bn = ('1', s)
	#matrix2img(s,'L_to_bn.jpeg', '1')

	return ('1', s)

if __name__ =='__main__':

	#print histogram(('L',[[255,255,255,255],[255,255,255,255]]))
	print rgb_to_bn('m_5.jpeg')
	#print get_threshold ('m5.jpeg')
	#print histogram('m1.jpeg')
	#show('m1bn.jpeg')
	#print luminance_img('rainbow.jpg')
	#print histogram(luminance_img((matrix('m1.jpeg'))))
	#print rgb_to_lum((0,125,255))
	#print luminance_img(('RGB', [[(255, 125, 0), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]]))
	#print histogram(('RGB', [[(255, 125, 0), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]]))
	#print histogram(('L', [[255, 255, 255, 255], [255, 255, 255, 255]]))
	#show(rgb_to_bn('rainbow.jpg'))
	#imatge = rgb_to_bn('blancRGB.jpeg')
	#imatge.save('wrgbbn.jpeg')
	#save(img, 'pusssi.jpeg')
	#show('rainbow.jpg')


