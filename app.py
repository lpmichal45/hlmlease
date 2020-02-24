#! /usr/bin/python3

import connexion

def main():
    APP = connexion.App('gotravel')
    APP.add_api('api.yml')
    APP.run(port=8080)

if __name__ == '__main__':
    main()
