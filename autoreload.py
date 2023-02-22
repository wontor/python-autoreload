#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is used to test how to reload the modules automatically when any
changes is detected.
"""
__author__="Wenjun Xiao && wangt@njust.edu.cn"

import os,sys,time
import multiprocessing

moduleFiles = set() 
def iter_module_files():
    for module in sys.modules.values():
        filename = getattr(module, '__file__', None)

        if filename:
            # ignore lib pys
            if '/lib/' not in filename \
                and '\\lib\\' not in filename \
                and filename[-3:] == '.py':
                moduleFiles.add(filename) 

def is_any_file_changed(mtimes):
    global moduleFiles
    for filename in moduleFiles:
        try:
            mtime = os.stat(filename).st_mtime
        except IOError:
            continue

        old_time = mtimes.get(filename, None)
        if old_time is None:
            mtimes[filename] = mtime
        elif mtime > old_time:
            mtimes[filename] = mtime
            return True 

    return False 

def run_with_reloader(runner):
    mainProcess = multiprocessing.Process(target=runner)
    mainProcess.start()

    iter_module_files()
    # for filename in moduleFiles:
    #     print(filename)

    mtimes = {}
    while True:
        if is_any_file_changed(mtimes):
            print('file changed, restarting...')
            mainProcess.terminate()

            mainProcess = multiprocessing.Process(target=runner)
            mainProcess.start()
        time.sleep(1)


# def main():
#     print( "[%s]enter main ..." % os.getpid())
#     while True:
#         time.sleep(2)
#         print( "[%s]runner." % os.getpid())

# if __name__ == '__main__':
#     # from autoreload import * 
#     run_with_reloader(main)