#! /usr/bin/env python
import shutil
import sys

shutil.copytree('template', f'day{sys.argv[1]}')
