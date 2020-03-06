#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Interpret(object):
    def __init__(self):
        self.dcom = {}

    def set_prompt(self,p):
        self.prompt = p  

    def afegeix_ordre(self, nomc, ordre):
        '''
        Es pot afegir qualsevol cosa al diccionari, però a main farem que
        entrin funcions obligatoriament
        '''
        
        if self.dcom.has_key(nomc):
            return 'Failed. This command already exists'
        else:
            self.dcom[nomc] = ordre

    def run(self):
        '''
        Només vàlid per funcions amb només un paràmetre com argument. 
        No caldrà arreglar res, a main ho hem de tenir en compte.
        Farem que les funcions siguin amb argument obligatoriament.

        '''
        while True:
            print self.prompt,
            p = raw_input()
            ll = p.split()
            ordres = ll[1:len(ll)]
            
            if self.dcom.has_key(ll[0]):
                for element in ordres:                    
                    self.dcom[ll[0]](element)
                    
            elif ll[0] == 'surt' or ll[0] == 'Surt':
                break
                
                    
        
        
