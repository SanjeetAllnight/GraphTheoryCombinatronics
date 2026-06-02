import os
import glob
import textwrap

gtc_dir = r"c:\Users\SAMJEET\Downloads\GraphTheoryCombinatronics\GTC"
out_dir = r"c:\Users\SAMJEET\Downloads\GraphTheoryCombinatronics\lab_experiments"

os.makedirs(out_dir, exist_ok=True)

# create __init__.py
with open(os.path.join(out_dir, "__init__.py"), "w") as f:
    pass

for i in range(1, 12):
    exp_dir = os.path.join(gtc_dir, f"Exp{i}")
    if os.path.exists(exp_dir):
        # find .py file
        py_files = glob.glob(os.path.join(exp_dir, "*.py"))
        if py_files:
            file_to_migrate = py_files[0]
            with open(file_to_migrate, "r", encoding='utf-8') as f:
                content = f.read()
            
            # Wrap content in def run():
            # Indent content by 4 spaces
            indented_content = textwrap.indent(content, "    ")
            
            wrapped_code = f"def run():\n{indented_content}\n"
            
            out_file = os.path.join(out_dir, f"exp{i}.py")
            with open(out_file, "w", encoding='utf-8') as f:
                f.write(wrapped_code)
            print(f"Migrated Exp{i} -> {out_file}")
        else:
            print(f"No python file found in {exp_dir}")
    else:
        print(f"Directory {exp_dir} not found")
