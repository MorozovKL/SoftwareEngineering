import os

class checkFileType():

    def __init__(self, file):

        self.file = file

    def checking(self):

        a, e = os.path.splitext(self.file)
        return e
