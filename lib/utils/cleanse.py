'''
    Module: cleanse.py
    Author: Logan Michalak
    Date  ; Febuary 24, 2020
'''

import hashlib


def hashpw(pw):
    '''
        Hashes a password
    '''

    hashpw = hashlib.md5(pw)

    return hashpw
