import slushie
import sys, os

with slushie.gulp('..'):
    from funs import hello

    hello()
	
	

slushie.freeze('../folder2/folder3')
from funs import hello
hello()