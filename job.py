from readToDF import readToDF
from checkFileType import checkFileType
from graphPlotter import graphPlotter
import click
# filename="data/бумага_маг_1_поперёк.txt"

def job(filename):
    e = checkFileType(file=filename).checking()
    a = readToDF(file=filename, ext=e)
    d = a.read()

    name = d['head']
    data = d['data']
    metadata = d['metadata']

    print("-----------------")
    print(name)
    print("-----------------")
    for i,j in metadata.items():
        print(i,j)
    print("-----------------")

    graphPlotter(name=name, data=data, metadata=metadata).plotFile()

@click.command()
@click.argument('filename')
# @click.option('--name')
def main(filename):
    job(filename)
    print('OK')

if __name__ == "__main__":
    main()