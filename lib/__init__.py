
import os
import sys
this_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_folder)
__all__ = [ f.replace('.py','') for f in os.listdir(this_folder) ]