import zipfile

com_file = zipfile.ZipFile('Collections/Zip_Unzip/comp_file.zip','w')
com_file.write('Collections/Zip_Unzip/file_one.txt',compress_type=zipfile.ZIP_DEFLATED)
com_file.write('Collections/Zip_Unzip/file_two.txt',compress_type=zipfile.ZIP_DEFLATED)
com_file.write('Collections/Zip_Unzip/file_three.txt',compress_type=zipfile.ZIP_DEFLATED)

com_file.close()

