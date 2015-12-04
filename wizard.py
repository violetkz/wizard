#!/user/bin/python

import argparse

def parse_option():
    parser = argparse.ArgumentParser(description='the utility to create new project')
    g1 = parser.add_argument_group('compilation options')
    g1.add_argument('-l','--lang',  choices={'cpp', 'c', 'python'}, help='the language name.')

    g2 = parser.add_argument_group('cmake options')
    g2.add_argument('-t', '--create',choices={'makefile', 'sln'}, default='makefile', 
             nargs='?', 
            help = 'create new CMake Cache with type makefile or VS sln')
    g2.add_argument('-r', '--rebuild', action='store_true',  
            help='rebuilt CMake Cache')
    g2.add_argument('-f', '--fastrebuild', action='store_true',  
            help='fast rebuilt CMake Cache')
    g2.add_argument('-R', '--rebuild-all', action='store_false',
            help= 'rebuilt entire project')
    g2.add_argument('-c', '--no-colored', action='store_true',
            help= 'disable cmake colored output.')

    g3 = parser.add_argument_group('Doxygen options')
    g3.add_argument('-d', '--doxygen', action='store_true',
            help= 'generate documents')


    args = parser.parse_args()

