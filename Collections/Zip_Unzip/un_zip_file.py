import zipfile

zip_obj = zipfile.ZipFile('Collections/Zip_Unzip/comp_file.zip' , 'r')

zip_obj.extractall('Collections/Zip_Unzip/unzipped')