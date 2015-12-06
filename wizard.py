#!/usr/bin/python

import argparse

def parse_option():
    parser = argparse.ArgumentParser(description='the utility to create new project')

    sub_parser = parser.add_subparsers(title='sub-command list', dest='subcommand')
    cmd_init_parser = sub_parser.add_parser('init', prog='init')
    cmd_init_parser.add_argument('-l','--lang', choices={'cpp', 'c', 'python'}, 
            default = 'cpp', 
            help = 'the language name.')
    cmd_add_parser = sub_parser.add_parser('add')
    cmd_add_parser.add_argument('-l','--lang', choices={'cpp', 'c', 'python'}, 
            default = 'cpp', 
            help = 'the language name.')
    cmd_add_parser.add_argument('type', choices = {'file', 'exe'}, 
            default = 'file',
            help = 'file type')

    args = parser.parse_args()
    print args
    
    return args


if __name__=="__main__":
    print parse_option()
