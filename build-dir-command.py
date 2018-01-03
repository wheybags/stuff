#!/usr/bin/env python3

import os
import sys
import pathlib
import configparser
import subprocess

class DirCommandHandler:
    def __init__(self):
        self.filename = str(pathlib.Path.home()) + "/.dircommandhandler"
        self.config = configparser.ConfigParser()
        
        if os.path.exists(self.filename):
            self.config.read(self.filename)
        else:
            self.config['dirs'] = {}

    def set(self, directory, command):
        self.config['dirs'][directory] = command

    def get(self, directory):
        if directory in self.config['dirs']:
            return self.config['dirs'][directory]
        else:
            return None

    def clear(self, directory):
        if directory in self.config['dirs']:
            del self.config['dirs'][directory]

    def __str__(self):
        strs = []
        for k in self.config['dirs']:
            strs.append("{}: {}".format(k, self.config['dirs'][k]))
        
        return '\n'.join(strs)

    def __repr__(self):
        return self.__str__()

    def save(self):
        with open(self.filename, 'w') as f:
            self.config.write(f)

def show_help():
    print(  'Usage:\n' +
            '   ' + sys.argv[0] + '      - (no args) runs command specified for current working directory, or prompts for one if there isn\'t one.\n' +
            '   ' + sys.argv[0] + ' list - lists commands specified for all dirs.\n' +
            '   ' + sys.argv[0] + ' del  - deletes command specified for current working directory\n')
    exit(1)

def __main__():
    handler = DirCommandHandler()
    directory = os.getcwd()

    if len(sys.argv) == 1:
        command = handler.get(directory)
        if command:
            print('running {}'.format(command))
            subprocess.run(command, shell=True, check=True)
        else:
            new_command = input('Input new command: ') 
            handler.set(directory, new_command)
            handler.save()

    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            print(handler)
        elif sys.argv[1] == 'del':
            handler.clear(directory)
            handler.save()
        else:
            show_help()
    else:
        show_help()

if __name__ == "__main__":
    __main__()
