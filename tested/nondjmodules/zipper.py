from os import listdir
from zipfile import ZipFile, ZIP_DEFLATED

def zip_file(file:str) -> str:
    with ZipFile(file.split('.')[0]+'.zip', 'w', ZIP_DEFLATED) as zipf:
        zipf.write(file)
    return file.split('.')[0]+'.zip'

def zip_path(path:str) -> str:
    with ZipFile(path+'.zip', 'w', ZIP_DEFLATED) as zipf:
        for file in listdir(path):
            zipf.write(path+'/'+file)
    return path+'.zip'