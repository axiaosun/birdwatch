#!/usr/bin/env python3

from src import omnibus

if __name__ == '__main__':
    #local = testing on machine
    omnibus.run(host = '127.0.0.1', port = 5000, debug = True)
    #staging = testing on server, production environment that reflects reality
    #omnibus.run(host = '0.0.0.0', port = 5000, debug = True)
    #production
    #omnibus.run(host = '0.0.0.0', port = 5000)
