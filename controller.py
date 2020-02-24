#! /usr/bin/python3

import connexion
import lib.utils.cleanse

HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_IN_DEVELOPMENT = 999


def register(email, password, re_password):
    '''
        Registers a user with the system

        Returns
            200 for successful
            400 for bad parameters
            999 for in development
    '''
    response = 0
    message  = ''

    if(password != re_password):
        message = 'Passwords do not match'
        response = HTTP_BAD_REQUEST
    
    else:
        # Actually proceed with request
        hashpw = cleanse.hashpw(password)
        message = 'Success'
        response = HTTP_OK

    return response, message
