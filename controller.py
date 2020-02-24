#! /usr/bin/python3

import connexion

HTTP_OK = 200
HTTP_BAD_REQUEST = 400


def register(email, password, re_password):
    print(email)
    print(password)
    print(re_password)
    return HTTP_OK
