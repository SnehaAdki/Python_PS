import shutil 

dir_to_zip = '/workspaces/Python_PS/Collections/Zip_Unzip'

output_filename = 'Collections/zipped_folder_example'

shutil.make_archive(output_filename,'zip',dir_to_zip)
