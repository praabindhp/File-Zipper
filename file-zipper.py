import zipfile
import shutil

# Zipping The Files

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as file_zip:
    file_zip.write('files/test.txt')
    file_zip.write('files/test2.txt')
    file_zip.write('files/Ubuntu_Internal-Server.png')

# Un-Zipping The Files

with zipfile.ZipFile('files.zip', 'r') as file_unzip:
    print(file_unzip.namelist())
    file_unzip.extractall('files')
    file_unzip.extract('test2.txt')

# Archiving The Files
# zip
shutil.make_archive('new-file', 'zip', 'files')
# tar
shutil.make_archive('new-file', 'tar', 'files')
# gztar
shutil.make_archive('new-file', 'gztar', 'files')
# bztar
shutil.make_archive('new-file', 'bztar', 'files')
# xztar
shutil.make_archive('new-file', 'xztar', 'files')

# Upacking Archived Files
# zip
shutil.unpack_archive('new-file.zip', 'new-files-2')
# tar
shutil.unpack_archive('new-file.tar', 'new-files-2')
# gztar
shutil.unpack_archive('new-file.tar.gz', 'new-files-2')
# bztar
shutil.unpack_archive('new-file.tar.bz2', 'new-files-2')
# xztar
shutil.unpack_archive('new-file.tar.xz', 'new-files-2')