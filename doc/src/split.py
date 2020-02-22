# -*- encoding: utf-8 -*-
'''
Module *split*
================

The module *split* basically contains the functions for the color image proccessing, 
like converting the fromat of the image into another, for example, convert an image in RGB 
to a Greyscale format.


This is the list of all of it:

'''

from transf import *

def split_digits(img):

	"""
	This feature will receive a cropped black and white img image
	vertically and returns a tuple (D, R) where D is an image
	with the leftmost digit and R is the rest of the image.\n
	The image corresponding to the extracted digit D is conveniently returned
	cut in the horizontal direction. The rest R becomes a null() image
	when all digits have been extracted.

        :param img: Image file name
        :type img: file
        :returns: A tuple (D, R)
        :rtype: tuple

	|

	In the following examples whe have the :file:`split_test_1.jpeg` that is the image at the left
	and :file:`split_test_2.jpeg` at the rigth.

	.. image:: split_test.jpeg
	   :alt: Example of licence plate that can be processed by the program
	   :width: 500
	
	|

	>>> split_digits('split_test_1.jpeg')
	([[0], [0], [0]], [[255], [255], [255]])
	>>> split_digits('split_test_2.jpeg')
	([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[255], [255], [255], [255], [255]])
	
	|

	"""

	if mode(img) == 'RGB':
		img = TransMatrix(trim(img))


	else:
		img = L_to_bn(img)
		img = TransMatrix(img)

	D = []
	R = []
	index = 0

	for col in img:
		c = 0
		for pixel in col:
			if pixel == 255:
				c += 1

		if c != len(col):
			D.append(col)

		else:
			break

		index += 1

	R = img[index:]
	if R == []:
		R = null() # Segons el que diu el pdf

	else:
		R = whiteElim(R)
		R = ('1', R)
		R = TransMatrix(R)
		matrix2img(R,'R.jpeg','1')

	D = ('1', D)
	D = TransMatrix(D)
	matrix2img(D,'D.jpeg','1')

	return (D, R)


def get_digits(img):

	j = 0
	for lletra in img:
		if lletra == '.':
			break
		j += 1

	tuple = split_digits(img)
	first_digit = tuple[0]
	next_digit = tuple[1]
	matrix2img(first_digit, 'D1.jpeg', '1')
	matrix2img(next_digit, 'R1.jpeg', '1')

	i = 1
	while True:
		tuple = split_digits('R'+str(i)+'.jpeg')
		matrix2img(tuple[0], ('D'+str(i+1)+'.jpeg'), '1')
		os.remove('R'+str(i)+'.jpeg')
		i += 1
		if tuple[1] == null():
			return (i) # per saber quans digits
			break

		matrix2img(tuple[1], ('R'+str(i)+'.jpeg'), '1')

	# matrix2img(n[0], 'hola'+str(i)+'.jpeg')
	#split_digit_L = split_digit_rgb == -> (D,R)


if __name__ == '__main__':
	get_digits('m1.jpeg')
	#split_digits('m3.jpeg')
	#split_digit_rgb('R.jpeg')
	#print split_digit_L('R2.jpeg')
	#get_digits('m1.jpeg')
	#L_to_bn ('R.jpeg')
