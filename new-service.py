import distutils.dir_util
import sys
import os
import glob
import stat
import pathlib


service_name = sys.argv[1]

from_dir = "_template"
to_dir = "karton-" + sys.argv[1]

distutils.dir_util.copy_tree(from_dir, to_dir)

os.rename(f"./{to_dir}/karton/class", f"./{to_dir}/karton/{service_name}")
os.rename(f"./{to_dir}/karton/{service_name}/class.py", f"./{to_dir}/karton/{service_name}/{service_name}.py")

for filepath in glob.iglob(f"./{to_dir}/**/*.*", recursive=True):
    
    if pathlib.Path(filepath).suffix == ".py":
        st = os.stat(filepath)
        os.chmod(filepath, st.st_mode | stat.S_IEXEC)
    
    with open(filepath) as file:
        s = file.read()
    s = s.replace("%CLASS%", service_name)
    with open(filepath, "w") as file:
        file.write(s)
    
    with open(filepath) as file:
        s = file.read()
    s = s.replace("%UCASE_CLASS%", service_name.title())
    with open(filepath, "w") as file:
        file.write(s)
