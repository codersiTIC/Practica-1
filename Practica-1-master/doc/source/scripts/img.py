# -*- encoding: utf-8 -*-

from PIL import Image
import img, os, sys

def null():
	"""
	Returns the null image (Type,Matrix)==('NULL',None)
	>>> null()
	('NULL', None)
	"""

	return('NULL',None)


def is_null(img):
	"""
	Checks if an image (Type,Matrix) is null
	>>> is_null(('NULrgb_to_bn('rainbow.jpg')L',None))
	True
	"""

	if img[0] == 'NULL' and img[1] == None:
		return True

	else:
		return False


def white_rgb(w,h):
	"""
	Returns an image in RGB format with all white pixels w x h
	>>> white rgb(3,3)
	('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])
	"""

	img = Image.new('RGB', (w,h), 'white')
	print img
	img.save('blancRGB.jpeg')
	return (img.mode, matrix('blancRGB.jpeg'))


def white_grey(w,h):
	"""
	Returns an image in grey format with all white pixels w x h 
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
	Returns an image in black and white format with all white pixels w x h 
	>>> white bn(3,3)
	('1', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	>>> white_bn(2,3)
	('1', [[255, 255], [255, 255], [255, 255]])
	"""
	img = Image.new('1', (w,h), 'white')
	img.save('blanc1.jpeg')
	return (img.mode, matrix('blanc1.jpeg'))


def format(img):
	"""
	Retuns the image format
	>>> format(('1', [[255, 255], [255, 255], [255, 255]])
	'1'
	>>> format(('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]]))
	'L'
	"""
	with Image.open(img) as im:
		return im.format


def mode(img):
	"""
	Retuns the image mode
	>>> mode(('1', [[255, 255], [255, 255], [255, 255]])
	'1'
	>>> mode(('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]]))
	'L'
	"""
	with Image.open(img) as im:
		return im.mode


def matrix(img):
	"""
	Return the pixel matrix of the image
	>>> matrix(('1', [[255, 255], [255, 255], [255, 255]]))
	[[255, 255], [255, 255], [255, 255]]
	>>> matrix(('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]]))
	[[255, 255, 255], [255, 255, 255], [255, 255, 255]]
	"""

	'''
	Altre manera de fer-ho:

	with Image.open(img) as I:
		data = list(I.getdata())
		return data
	'''

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

	#return (I.mode,fila)
	return fila


def img(matrix, model):

	"""
	Returns the image representation format (T,m)
	>>> img([[255,255,0],[255,128,255],[191,255,255]],'DISCOVER') 
	('L', [[255, 255, 0], [255, 128, 255], [191, 255, 255]])
	>>> img([[255,255,0],[255,0,255],[0,255,255]],'DISCOVER')
	('1', [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
	"""
	'''
	S'usa per crear una imatge d'una matriu de píxels matrix. Si
	el paràmetre model val 'DISCOVER' la funció mira de descobrir
	automàticament de quin tipus d'imatge es tracta. Ho fa explorant
	la matriu i determinant com són els píxels. Si el paràmetre
	model val 'RGB', 'L' o '1' usa aquest model després de comprovar
	que els píxels de la matriu són coherents amb el model


	data = (seqüència de valors dels píxels)
	nom_imatge.putdata(data)

	o bé:

	nom_imatge.putpixel((x,y), color)   color --> En funció format imatge
	'''

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

					#elif pixel == 0 or pixel == 255:
						#u += 1

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
	>>> get w(('1', [[255, 255], [255, 255], [255, 255]]))
	2
	>>> get w( ('L', [[255, 255, 255, 255, 255], [255, 255, 255, 255, 255]])) 5
	"""

	with Image.open(img) as im:
		return im.size[0]


def get_h(img):
	"""
	Returns the image height
	>>> get h(('1', [[255, 255], [255, 255], [255, 255]]))
	3
	>>> get h(('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])) 3
	"""

	with Image.open(img) as im:
		return im.size[1]


def subimg(img, ow, oh, w, h):
	'''
	Retorna una sub-imatge de la imatge img que té l'origen a les
	coordenades (ow,oh) i té mides w i h. Naturalment la sub-imatge
	ha d'estar totalament continguda a img.
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

	'''
	print img([[(215, 23, 39), (125, 255, 255), (255, 0, 0)], [(255, 255, 255), (255, 255, 255), (0, 0, 0)]], 'DISCOVER')
	print
	print img([[(215, 23), (125, 255, 255), (255, 0, 0)], [(255, 255, 255), (255, 255, 255), (0, 0, 0)]], 'DISCOVER')
	print
	print img([[(23, 23, 23)], [(33, 33 ,33)]], 'DISCOVER')
	print
	print img([[255, 11], [0, 0], [0, 0]], 'DISCOVER')
	print
	print img([[255, 11], [0, 0, 33], [0, 0]], 'DISCOVER')
	print
	print img([[255, 0], [34, 23], [230, 03]], 'DISCOVER')
	print
	print img([[125,(0,255,0)], [0, 0], [0, 0]], 'DISCOVER')
	print
	print img([[0,0], [0, 0], [0, 0]], 'RGB')
	print
	print img([[(255, 255, 255), (255, 255, 255),(0,0,0)], [(255, 255, 255), (255, 255, 255),(0,0,0)]], 'RGB')
	print
	print img([[0,0], [0, 0], [0, 0]], 'L')
	print
	print img([[0,255], [0, 0], [0, 0]], '1')
	print
	print img([[0,255], [0, 0], [0, 0]], 'RGB')
	print

	#print img([[0,0], [0, 0], [0, 0]], 'DISCOVER')
	#print img([[0,0], [0, 0], [0, 0]], 'RGB')
	#print img([[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]], 'RGB')
	#print img([[0,0], [0, 0], [0, 0]], 'L')
	#print img([[0,255], [0, 0], [0, 0]], '1')
	# print img([[126, 0], [255, 0]], 'DISCOVER')
	# subimg('matricula1.jpeg',20,20,200,200)
	# print white_grey(5, 5)
	# print white_bn(5, 5)
	# print white_rgb(2, 2)
	# print matrix('blancRGB.jpeg')
	# print matrix('a.jpeg')
	# print img([[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]],'DISCOVER')
	# print img([[255,255], [255, 0], [0, 255]], 'DISCOVER')
	# print img([[500,255], [255, 0], [0, 255]], 'DISCOVER')
	# print img([[255,255], [255, 0], [45, 255]], 'DISCOVER')
	# print
	# print img([[255,255], [255, 255], [255, 255]], 'DISCOVER')
	# print img([[0,0], [0, 0], [0, 0]], 'DISCOVER')
	# print img([[1,0], [0, 0], [0, 0]], 'DISCOVER')

	'''
