import pandas as pd
import numpy as np

class readToDF():

    def __init__(self, file, ext):

        self.file = file
        self.ext = ext

    def read(self):

        if self.ext == '.txt':
            return self.readTxt()
        elif self.ext == '.csv':
            return self.readCsv()
        elif self.ext == '.m40':
            return self.readM40()
        elif self.ext =='':
            return self.readFile()

    def readTxt(self):

        head = pd.read_csv(self.file, na_filter=True, nrows=1, skiprows=0, header=None,
                                       encoding='iso-8859-1')

        if 'Oscilloscope' in head.iloc[0][0]:

            head_1 = pd.read_csv(self.file, na_filter=True, nrows=1, skiprows=1, header=None,
                               encoding='iso-8859-1')
            head_1 = head_1.merge(pd.read_csv(self.file, na_filter=True, nrows=1, skiprows=4,
                                              header=None, encoding='iso-8859-1'), how='outer')
            head_2 = pd.read_csv(self.file, na_filter=True, nrows=1, skiprows=2, header=None,
                                 encoding='iso-8859-1')
            head_2 = head_2.merge(pd.read_csv(self.file, na_filter=True, nrows=5, skiprows=6,
                                              header=None, encoding='iso-8859-1'), how='outer')
            head_2 = head_2.merge(pd.read_csv(self.file, na_filter=True, nrows=1, skiprows=14,
                                              header=None, encoding='iso-8859-1'), how='outer')
            head_3 = pd.read_csv(self.file, sep='\t', na_filter=True, nrows=3, skiprows=11, header=None,
                               encoding='iso-8859-1')

            data = pd.read_csv(self.file, sep='\s+', header=None, skiprows=19, decimal='.')

            typeExp = head.values[0][0]

            metadata = {i[0].split(': ')[0]: i[0].split(': ')[1] for i in head_2.values}
            metadata.update({i[0].split(' : ')[0]: i[0].split(r' : ')[1] for i in head_1.values})
            metadata.update({'GPS_'+str(i): head_3.values[i] for i in range(len(head_3))})

            return {'head': typeExp, 'metadata': metadata, 'data': data}

        else:
            head = pd.read_csv(self.file, sep='\t', na_filter=True, nrows=3, header=None, encoding='iso-8859-1')
            data = pd.read_csv(self.file, sep='\t', header=None, skiprows=3, decimal=',').fillna('0')


            exp = head.iloc[0].dropna().unique()
            attrib = head.iloc[1].unique()
            meas = head.iloc[2].unique()

            typeExp = 'Shimadzu'
            metadata = {'exp':exp, 'attrib':attrib, 'meas':meas}

            return {'head':typeExp, 'metadata':metadata, 'data':data}

    def readCsv(self):

        head = pd.read_csv(self.file, na_filter=True, nrows=3, header=None, encoding='iso-8859-1')
        data = pd.read_csv(self.file, header=None, skiprows=3, decimal=',').fillna('0')

        exp = head.iloc[0].dropna().unique()
        attrib = head.iloc[1].unique()
        meas = head.iloc[2].unique()

        typeExp = 'Shimadzu'
        metadata = {'exp': exp, 'attrib': attrib, 'meas': meas}

        return {'head': typeExp, 'metadata': metadata, 'data': data}

    def readM40(self):

        head = pd.read_csv(self.file, nrows=7, header=None, encoding='iso-8859-1')
        data = pd.read_csv(self.file, sep='\s+', header=None, skiprows=9, decimal='.')

        typeExp = head.values[0][0]
        metadata = {'version': head.values[1][0], 'mark': head.values[2][0],
                    'size': dict([i.split('=') for i in filter(None, head.values[3][0].split(';'))]),
                    'add_1': dict([i.split(':') for i in filter(None, head.values[4][0].split(';'))]),
                    'date': head.values[5][0],
                    'add_2': dict([i.split(':') for i in filter(None, head.values[6][0].split(';'))])}

        return {'head': typeExp, 'metadata': metadata, 'data': data}

    def readFile(self):

        head_1 = pd.read_csv(self.file, sep='\s+', nrows=1, skiprows=0, header=None, encoding='iso-8859-1')
        head_2 = pd.read_csv(self.file, sep='\s+', nrows=1, skiprows=1, header=None, encoding='iso-8859-1')
        head_3 = pd.read_csv(self.file, sep='\s+', nrows=1, skiprows=2, header=None, encoding='iso-8859-1')

        data = pd.read_csv(self.file, sep='\s+', header=None, skiprows=3, decimal='.')

        typeExp = 'sensor'
        metadata = {'numbExp': head_1.values[0][0], 'size': head_2.values[0], 'sensor': head_3.values[0]}

        return {'head': typeExp, 'metadata': metadata, 'data': data}
