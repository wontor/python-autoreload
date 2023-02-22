#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Runner for testing autoreload module."""

# https://github.com/wenjunxiao/python-autoreload
# https://github.com/wontor/python-autoreload
__author__="Wenjun Xiao && wangt@njust.edu.cn"

import os,time


def main():
    print( "[%s]enter main ..." % os.getpid())
    while True:
        time.sleep(2)
        print( "[%s]runner." % os.getpid())


if __name__ == '__main__':
    from autoreload import * 
    run_with_reloader(main)
