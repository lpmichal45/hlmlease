'''

    Module: user.py
    Author: Logan Michalak
    Date  : Febuary 23, 2020
'''

class User:
    '''
        A user in the system
    '''

    def __init__(self, first, last, email, pwhash, pwhash2):
        '''
            Initializes the user
        '''

        self.first = first
        self.last = last
        self.email = email
        self.pwhash = pwhash
        self.pwhash2 = pwhash2
