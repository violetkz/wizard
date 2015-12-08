#!/usr/bin/python

import argparse
import json
import os
op = os.path

def parse_option():
    parser = argparse.ArgumentParser(description='the utility to create new project')

    sub_parser = parser.add_subparsers(title='sub-command list', dest='subcommand')
    cmd_init_parser = sub_parser.add_parser('init')
    cmd_init_parser.add_argument('-l','--lang', choices={'cpp', 'c', 'python'}, 
            default = 'cpp', 
            help = 'the language name.')
    cmd_add_parser = sub_parser.add_parser('add')
    cmd_add_parser.add_argument('type', choices = {'file', 'exe'}, 
            default = 'file',
            help = 'file type')

    args = parser.parse_args()
    return args

class wizard_configfile:
    def __init__(self, filename = '.wizard_configfile'):
        self.filename = filename
        self.setting_items = {
                'project_name': 'pname',
                'lang': 'cpp',
                'target_name': '',
                'source_files': [],
                'external_include_paths':[],
                'extra_definiations' : [],
                'external_link_libs': []
                }

    def check(self):
        if not op.exists(self.filename):
            self.init_configfile()
        return self.get_values()

    def init_configfile(self):
        #json.dump(setting_items, open(self.filename, 'w'))
        self.save_values(self.setting_items)
        
    def get_values(self):
        if op.exists(self.filename):
            return json.load(open(self.filename), 'utf-8') 
        return None
    
    def save_values(self,  items):
        json.dump(items, open(self.filename, 'w'), indent = 4)

    def get_keys(self):
        return self.setting_items.keys()
    
    def set_value(self, key, value):
        if self.setting_items.has_key(key) and  isinstance(self.setting_items[key], list):
            if isinstance(value, str):
                # if already in the list. do nothing 
                if value not in self.setting_items[key]:
                    self.setting_items.append(value)
            elif isinstance(value, list):
                for v in values:
                    # if already in the list. do nothing 
                    if v not in self.setting_items[key]:
                        self.setting_items.append(v)
            else:
                pass # fixme, bad type 
        else:
            self.setting_items[key] = value

def init_cpp_proj(setting):
    init_wk_env(setting)
    init_makefile(setting)
    init_main_file(setting)

def init_project_by_lang(setting):
    lang = setting['lang'].lower() 
    if lang in lang_init_tbl.keys():
        lang_init_tbl[lang](setting)
        

def action_init(args):
    config = wizard_configfile()
    setting = config.check()
    
    init_project_by_lang(setting)
   
def action_add(args):
    pass


action_map = {
        'init':action_init,
        'add': action_add,
        }

lang_init_tbl = {
        'cpp' : init_cpp_proj, 
        'python' : init_py_proj
        }

def dispatch(args):
    subcommand = args.subcommand
    if action_map.has_key(subcommand):
        action_map[subcommand](args)
    else:
        # fixme, add error handle.
        pass

if __name__=="__main__":
    args =  parse_option()
    dispatch(args)
