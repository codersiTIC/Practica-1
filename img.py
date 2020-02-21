# -*- encoding: utf-8 -*-
'''
Module *img*
============

The module *img* contain the structural functions of the project (the simpliest
elements of it), which are able to, for example, control the Image's format,
create new ones, encode a picture into a matrix...


This is the list of all of it:

'''
from PIL import Image
import img, os, sys

def null():
	"""

        Returns an empty image: ('NULL', None)

        :returns: The null image
        :rtype: Tuple: ('NULL', None)
        

	>>> null()
	('NULL', None)

      	"""

	return('NULL',None)


def is_null(img):
	"""

        Checks if an image (Type, Matrix) is null

        :param img: Image representation (Type, Matrix)
        :type img: tuple
        :returns: True (if it is null) or False (if not)
        :rtype: bool

	>>> is_null(('NULL',None))
	True
        >>> is_null(('RGB',[(255,255,255),(255,255,255)]
        False
	"""

	if img[0] == 'NULL' and img[1] == None:
		return True

	else:
		return False


def white_rgb(w,h):
	"""

        Returns an image in RGB format with all white pixel and size w * h	

        :param w: The width of the new image
        :type w: int
        :param h: The height of the new image
        :type h: int
        :returns: An all white new image (w * h) in 'RGB' mode
        :rtype: tuple, ('RGB', Matrix)

	>>> white rgb(3,3)
	('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], 
        [(255, 255, 255), (255, 255, 255), (255, 255, 255)], 
        [(255, 255, 255), (255, 255, 255), (255, 255,    
 
        """

	img = Image.new('RGB', (w,h), 'white')
	print img
	img.save('blancRGB.jpeg')
	return (img.mode, matrix('blancRGB.jpeg'))


def white_grey(w,h):
	""" 
  
        Returns an image in grey format ('L') with all white pixels and size w * h

        :param w: The width of the new image
        :type w: int
        :param h: The height of the new image
        :type h: int
        :returns: An all white new image (w * h) in 'L' mode
        :rtype: tuple, ('L', Matrix)

	>>> white grey(3,3)
	('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	>>> white grey(5,2)
	('L', [[255, 255, 255, 255, 255], [255, 255, 255, 255, 255]]) 

	"""

	img = Image.new('L', (w,h), 'white')
	img.save('blancL.jpeg')
	return (img.mode, matrix('blancL.jpeg'))


def white_bn(w,h):
	"""

        Returns an image in black and white ('1') with all white pixels and size w*h

        :param w: The width of the new image
        :type w: int
        :param h: The height of the new image
        :type h: int
        :returns: An all white new image (w * h) in '1' mode
        :rtype: tuple, ('1', Matrix)

	>>> white bn(3,3)
	('1', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	>>> white_bn(2,3)
	('1', [[255, 255], [255, 255], [255, 255]])

	"""
	img = Image.new('1', (w,h), 'white')
	img.save('blanc1.jpeg')
	return (img.mode, matrix('blanc1.jpeg'))


def mode(img):
	"""
	Retuns the image mode

        :param img: Image representation (Type, Matrix)
        :type img: tuple
        :returns: The image mode
        :rtype: str

	>>> mode(('1', [[255, 255], [255, 255], [255, 255]])
	'1'
	>>> mode(('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]]))
	'L'

	"""
        return img[0]


def matrix(img):
	"""
	Returns the pixel matrix of the image

        :param img: Image's file name
        :type img: str
        :returns: The matrix of the image
        :rtype: list

	>>> matrix('blanc_bn.jpeg')
	[[255, 255], [255, 255], [255, 255]]
	>>> matrix('blanc_grey.jpeg')
	[[255, 255, 255], [255, 255, 255], [255, 255, 255]]

	"""

	fila=[]
	with Image.open(img) as I:
		X = I.size[0]
		Y = I.size[1]
		pix = I.load()

		for y in range(Y):
			s = []

			for x in range(X):
				s.append(pix[x,y])

			fila.append(s)

	return fila


def img(matrix, model):
	"""

        This function has diferent utilities depending on the value of *model*
        argument. On one hand, if model = 'RGB','L' or '1' (the diferent image
        modes / types), the function verify if the matrix estructure is valid
        for the selected mode, then returns the image representation 
        (Type, Matrix) of it. If not, the function returns a warning.

        On the other hand, if model = 'DISCOVER' the function tries to discover
        the mode of the image from matrix. Unless the matrix has some sintactic
        mistakes (in which case returns a warning), the function returns the 
        image representation (Type (discovered), Matrix).
        

        :param matrix: Image matrix
        :param mode: The mode of the image or the parameter 'DISCOVER'
        :returns: Image representation (Type, Matrix)
        :rtype: tuple

	>>> img([[255,255,0],[255,128,255],[191,255,255]],'DISCOVER') 
	('L', [[255, 255, 0], [255, 128, 255], [191, 255, 255]])
	>>> img([[255,255,0],[255,0,255],[0,255,255]],'DISCOVER')
	('1', [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
	"""

	c = 0
	l = 0
	u = 0

	if model == 'DISCOVER':
		format = ''
		for element in matrix:
			if len(element)!=len(matrix[0]):
				return 'Incorrect matrix'

			for pixel in element:
				if type(pixel)==tuple and len(pixel)==3:
					c += 1
					for j in pixel:
						if j not in range(256):
							return 'Incorrect matrix'

				elif pixel not in range(256):
					return 'Incorrect matrix'

				else:
					if pixel == 0 or pixel == 255:
						u += 1

		if c >= 1:
			if c == len(matrix[0])*len(matrix):
				format = 'RGB'
			else:
				return 'Incorrect Matrix'

		elif u == len(matrix[0])*len(matrix):
			format = '1'

		else:
			format = 'L'

		return (format,matrix)


	elif model == 'RGB':
		for element in matrix:
			for pixel in element:
				if type(pixel)==tuple and len(pixel) == 3:
					for j in pixel:
						if j not in range(256):
							return 'Incorrect matrix'
				else:
					return 'Incorrect picture mode'


		return ('RGB', matrix)

	elif model == 'L':
		for element in matrix:
			for pixel in element:
				if pixel not in range(256):
					return 'Incorrect matrix'

				elif type(pixel) == tuple:
					return 'Incorrect picture mode'
		else:
			return ('L', matrix)

	elif model == '1':
		for element in matrix:
			for pixel in element:
				if pixel not in range(256):
					return 'Incorrect matrix'

				elif pixel != 0 and pixel != 255:
					return 'Incorrect picture mode'

		return ('1', matrix)


def get_w(img):
	"""

	Returns the image width

        :param img: Image representation (Type, Matrix)
        :type img: tuple
        :returns: The witdh of the image
        :rtype: int

	>>> get_w(('1', [[255, 255], [255, 255], [255, 255]]))
	2
	>>> get_w(('L', [[255, 255, 255, 255, 255], [255, 255, 255, 255, 255]]))
        5
	"""
        return len(img[1][0]) #Totes les files tenen el mateix número de pixels


def get_h(img):
	"""

	Returns the image height

        :param img: Image representation (Type, Matrix)
        :type img: tuple
        :returns: The height of the image
        :rtype: int

	>>> get h(('1', [[255, 255], [255, 255], [255, 255]]))
	3
	>>> get h(('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]]))
        3
	"""

        return len(img[1]) #Comptar quantes files hi ha, per tant, saber l'alçada de la imatge en píxels


def subimg(img, ow, oh, w, h):
	'''

	Returns a sub-region of an image with size (w * h), starting at 
        pixel (ow,oh). Naturally, the sub-image must be fully contained in img.
        The parameter img must be the name of the picture you want to trim
        (the path or the file's name (if the image is in the same directory of
        the module)). This funciton don't return anything, only saves the 
        sub-region image as 'subregion.jpeg'. 

        :param img: Image's name (including the format (.jpeg, .png...))
        :type img: str
        :param ow: Horizontal position of the origin pixel
        :type ow: int (lower than img horizontal size)
        :param oh: Vertical position of the origin pixel
        :type oh: int (lower than img vertical size)
        :param w: Witdh of the subregion
        :type w: int
        :param h: Height of the subregion
        :type h: int
        :returns: None (saves the trimmed image) 
        
	'''

	with Image.open(img) as I:
		box = (ow,oh,w,h)
		try:
			subregion = I.crop(box)
			subregion.save('subregion.jpeg')
		except:
			if ow >= I.size[0]:
				print "Error. Horizontal component of coordinates origin out of range"
			if oh >= I.size[1]:
				print "Error. Vertical component of coordinates origin out of range"


if __name__=='__main__':

	print white_rgb(4,4)

