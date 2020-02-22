# -*- encoding: utf-8 -*-

'''
Module *img2char*
=================

The module *img2char* basically contains the functions for the color image proccessing, 
like converting the fromat of the image into another, for example, convert an image in RGB 
to a Greyscale format.


This is the list of all of it:

'''

#from match import *
#import time

def img2char(img):
    """
        This is the final module that contains merges all the modules together to get the digits
        of the car plate.\n
        It compares the digits splited with the patterns loaded, the licence plate must have 4 digits and 3 letters,
        if the machin doesn't reconogsizes anything it will add **'?'** 

            :param img: Image file name
            :type img: file
            :returns: The number of the license plate
            :rtype: str

        .. code-block:: bash

            $ python ~/GitProjects/Projecte/img2char.py
            $ python img2char.py

            ********** LICENCE PLATE RECOGNIZER **********
            1 - Enter image file name (use extension)
            0 - Exit

            > Enter option: 1
            >> Enter file name: m_4.jpeg
            8784 ???

            ********** LICENCE PLATE RECOGNIZER **********
            1 - Enter image file name (use extension)
            0 - Exit

            > Enter option: 1
            >> Enter file name: m_3.jpeg
            4130 ???

            ********** LICENCE PLATE RECOGNIZER **********
            1 - Enter image file name (use extension)
            0 - Exit

            > Enter option: 1       
            >> Enter file name: m_1.jpeg
            5134 ???

            ********** LICENCE PLATE RECOGNIZER **********
            1 - Enter image file name (use extension)
            0 - Exit

            > Enter option: 1
            >> Enter file name: m_2.jpeg
            3066 G??





    """

    license_plate = ''

    try:
        i = get_digits(img)

        digits_patterns = load_patterns('ptr')
        letters_pattern = load_patterns('patro')

        for element in range(1,5):
            try:
                value = match_digits('D'+str(element)+'.jpeg', digits_patterns)
                license_plate += value

            except:
                license_plate += '?'

        license_plate += ' '


        for element in range(5,8):
            try:

                value = match_letters('D'+str(element)+'.jpeg', letters_pattern)
                license_plate += value

            except:
                license_plate += '?'



        for element in range(1, 8):

            try:
                os.remove('D'+str(element)+'.jpeg')

            except:
                pass

    except:
        print '\nUnexpected Error'+' \n'+'> The image must be a license plate'



    return license_plate


def menu():
    while True:
        print
        print '*'*10, 'LICENCE PLATE RECOGNIZER', '*'*10
        print '1 - Enter image file name (use extension)'
        print '0 - Exit\n'

        while True:
            try:
                option = input('> Enter option: ')
                if option in range(2):
                    break

            except:
                pass


        if option == 1:

            while True:
                try:
                    option = raw_input('>> Enter file name: ')

                    break

                except:
                    pass

            print img2char(option)

        else:
            print 'Bye bye'
            break

        time.sleep(1)

if __name__ == '__main__':
    menu()

    '''
    print load_patterns('patro')
    print img2char('m_4.jpeg')
    print img2char('anass.jpeg')
    print img2char('dani.jpeg')
    print img2char('marcel.jpeg')
    '''
