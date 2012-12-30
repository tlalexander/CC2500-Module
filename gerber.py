from shutil import make_archive
import glob, os, shutil



dest_dir=os.getcwd()+"/gerber"
source_dir=""


print dest_dir


if os.path.isdir(dest_dir) is False:
    os.mkdir(dest_dir)


arr=['*.GBO','*.GBS','*.GBL','*.GTL','*.GTO','*.GTP','*.GTS','*.TXT']

files=[]

for filename in arr:
    files += glob.iglob(os.path.join(source_dir, filename))
    
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dest_dir)


archive_name = os.path.splitext(files[0])[0]

make_archive(archive_name, 'zip', dest_dir)

shutil.move(archive_name+".zip", dest_dir)

print archive_name + ".zip created successfully"

raw_input("Press Enter to close")
