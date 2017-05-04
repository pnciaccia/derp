"""
Created: 05-03-2017
Author: Peter Ciaccia
Description: Changes working directory through directory trees by prompting the user with responses that correspond to
directories or files.
"""

import os

defaultbeginningprompt = 'Type the key corresponding to the file you wish to call or the directory you wish to move' \
                           'into.'
defaultprompt = 'At any time press \'q\' to quit'

def navigate(beginningprompt=defaultbeginningprompt, prompt=defaultprompt):
    print(os.getcwd())






if __name__ == '__main__':
    navigate(beginningprompt='test')