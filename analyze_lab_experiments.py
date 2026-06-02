import ast
import glob
import os


def analyze_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError:
        return {"error": "SyntaxError"}

    imports = set()
    has_input = False
    has_plotting = False

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "input":
                has_input = True

            if isinstance(node.func, ast.Attribute):
                if node.func.attr.startswith("draw"):
                    has_plotting = True
                if isinstance(node.func.value, ast.Name) and node.func.value.id in ["plt", "matplotlib"]:
                    has_plotting = True

    return {
        "imports": list(imports),
        "has_input": has_input,
        "has_plotting": has_plotting,
        "is_hardcoded": not has_input,
    }


for f in sorted(glob.glob(os.path.join("lab_experiments", "exp*.py"))):
    print(f"{os.path.basename(f)}:")
    res = analyze_file(f)
    print(f"  Imports: {res.get('imports')}")
    print(f"  Accepts User Input: {res.get('has_input')}")
    print(f"  Hardcoded: {res.get('is_hardcoded')}")
    print(f"  Graph Plotting Exists: {res.get('has_plotting')}")
    print()
