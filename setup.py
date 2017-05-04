"""
Created 05/03/2017
Description:

"""

dbrootdir = navigate.navigate
exe = "makedirtree {0}".format(dbrootdir)
subprocess.call(exe)