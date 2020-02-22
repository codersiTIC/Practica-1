# -*- encoding: utf-8 -*-

from split import*

def load_patterns(prefix):
	files = os.listdir('.')
	index = len(prefix)

	pf = []

	for file in sorted(files):
		try:
			if file[:index] == prefix:
				pf.append(file)

		except:
			pass

	return pf



def match_digits(img, patlist):

	h = get_h(patlist[0])
	new_img = scale(img,h)
	m_img = new_img[1]
	m_img = L_to_bn(m_img)

	dic = dict()

	digit_value = 0
	for pattern in patlist:

		equality = 0

		m_pat = L_to_bn(pattern)
		for i, j in zip(m_pat[1], m_img[1]):

			for pixel_pat, pixel_img in zip(i,j):

				if pixel_img == pixel_pat:
					equality += 1

		dic[equality] = digit_value

		digit_value += 1

	keys = dic.keys()

	return  str(dic[max(keys)])

def match_letters(img, patlist):

	h = get_h(patlist[0])
	new_img = scale(img,h)
	m_img = new_img[1]
	m_img = L_to_bn(m_img)

	dic = dict()

	translator = {'10':'A','11':'B','12': 'C', '13':'D',' 14':'E', '15':'F', '16':'G', '17':'H', '18':'I','19':'J','20':'K','21':'L','22':'M','23':'N','24':'P','25':'R','26':'S','27':'T','28':'U','29':'V','30':'W','31':'X','32':'Y','33':'Z'}

	digit_value = 10
	for pattern in patlist:

		equality = 0

		m_pat = L_to_bn(pattern)
		for i, j in zip(m_pat[1], m_img[1]):

			for pixel_pat, pixel_img in zip(i,j):

				if pixel_img == pixel_pat:
					equality += 1

		dic[equality] = digit_value

		digit_value += 1

	keys = dic.keys()

	return  str(translator[str(dic[max(keys)])])
