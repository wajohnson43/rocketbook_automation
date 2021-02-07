#!/bin/python3

import os
import glob
import time
from PyPDF2 import PdfFileMerger

path = ''

def sort():

    debug = False

    for filename in glob.glob(path + '*.pdf'):
        fileparts = filename.split('_', 1)
        directory = fileparts[0]
        name = fileparts[1]
        
        if(debug):
            print("directory: " + directory)
            print("name: " + name)

        try:
            os.mkdir(directory)
            os.rename(filename, directory + "/" + name)
        except:
            os.rename(filename, directory + "/" + name)
    return

def merge():
    for directory in glob.glob(path + '*/'):
        pdfs = glob.glob(directory + '*.pdf')
        
        if len(pdfs) == 1:
            continue

        pdfs.sort(key=os.path.getmtime)
        
        merger = PdfFileMerger()

        for pdf in pdfs:
            merger.append(open(pdf, 'rb'))
            os.remove(pdf)
        notebook = directory.split('/')[-2]

        with open(directory + notebook + '.pdf', 'wb') as fout:
            merger.write(fout)

def main():
    sort()
    merge()

if __name__ == '__main__':
    main()
