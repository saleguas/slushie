import slushie
import sys, os

with slushie.gulp('..'):
    # print pythonpath
    print(sys.path)
    import hello