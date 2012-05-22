#!/bin/python
# -*- codind:utf-8
import os

config = {
    'command': './web2py/web2py.py',
    'argument': '-a',
    'password': 'dev',
    'domain': 'http://localhost',
    'port': '8000',
}

def main():
    try:
        print '-'*100
        print 'Acesse: %(domain)s:%(port)s' % ( config )
        print '-'*100
        print '\n'
        
        run = os.system( '%(command)s %(argument)s%(password)s' % ( config ) )
        return True
    except Exception:
        print 'Erro ao executar commando tente manualmente usand: %(command)s %(argument)s%(password)s' % (config)
        return False

if __name__ == '__main__':
    main()
