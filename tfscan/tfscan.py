#!/usr/bin/python3

import os,sys
from itertools import (takewhile,repeat)

def get_file_size(file):
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size

def count_file_lines(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\n') for buf in bufgen )

def match_file_ext(fname,extNames):
    return os.path.splitext(fname)[1] in extNames

def list_files(path,extNames,ignore_hidden_dir=True):
    flist = []
    if os.path.exists(path):   
        can_read = os.access(path, os.R_OK)
        if not can_read:
            print('Warn: Permission denied, {}'.format(path))
            return
        files = os.listdir(path)
        for f in files :
            if ignore_hidden_dir and f.startswith('.'):
                continue
            subpath=os.path.join(path,f)
            if os.path.isfile(subpath):
                if match_file_ext(f,extNames):
                    flist.append(subpath)
            if os.path.isdir(subpath):
                sub_fl=list_files(os.path.join(path,f), extNames)
                if sub_fl:
                    flist.extend(sub_fl)
    return flist

def fmt_num(n):
    return '{:,}'.format(n)

def fix_dot_prefix(s):
    if len(s)==0:
        return ""
    return '.{}'.format(s) if s[0]!='.' else s

if __name__ == '__main__':
    dir='/home/tony'
    exts=['.py']

    if len(sys.argv)>1:
        dir = sys.argv[1]
    
    if len(sys.argv)>2:
        exts =[fix_dot_prefix(ext) for ext in sys.argv[2:]]


    print('Scanning directory {}, searching for {} files'.format(dir,exts))

    all_files=list_files(dir,exts)
    tt_files=len(all_files)
    tt_size=0
    tt_lines=0
    for fpath in all_files:
        rel_path=os.path.relpath(fpath,dir)
        fsize=get_file_size(open(fpath))
        lines=0 if fsize==0 else count_file_lines(fpath)
        print('{:>12}{:>9}\t{}'.format(fmt_num(fsize),fmt_num(lines),rel_path))
        #
        tt_size += fsize
        tt_lines += lines

    print('TOTAL: {:,} bytes IN {:,} lines IN {:,} files'.format(tt_size,tt_lines,tt_files))