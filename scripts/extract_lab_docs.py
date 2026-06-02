import os
import zipfile
import xml.etree.ElementTree as ET
import re

def parse_docx(file_path):
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    text_data = []
    
    with zipfile.ZipFile(file_path, 'r') as docx:
        if 'word/document.xml' in docx.namelist():
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Find all paragraphs
            for p in tree.findall('.//w:p', namespaces):
                para_text = []
                for t in p.findall('.//w:t', namespaces):
                    if t.text:
                        para_text.append(t.text)
                joined_text = "".join(para_text).strip()
                if joined_text:
                    text_data.append(joined_text)
                    
    return text_data

def extract_sections(text_data):
    sections = {
        "Experiment Number": "",
        "Aim": "",
        "Theory": "",
        "Conclusion": ""
    }
    
    current_section = None
    
    for line in text_data:
        line_lower = line.lower().strip()
        
        # Experiment Number
        if not sections["Experiment Number"] and re.search(r"experiment\s*(?:no\.?|number)[:\-]?\s*(\d+)", line_lower):
            match = re.search(r"experiment\s*(?:no\.?|number)[:\-]?\s*(\d+)", line_lower)
            sections["Experiment Number"] = match.group(1)
        elif not sections["Experiment Number"] and re.search(r"^experiment\s*(\d+)$", line_lower):
            match = re.search(r"^experiment\s*(\d+)$", line_lower)
            sections["Experiment Number"] = match.group(1)
            
        # Aim
        elif line_lower.startswith("aim:") or line_lower == "aim":
            current_section = "Aim"
            if len(line) > 5 and ":" in line:
                sections["Aim"] = line.split(":", 1)[1].strip()
        # Theory
        elif line_lower.startswith("theory:") or line_lower == "theory":
            current_section = "Theory"
            if len(line) > 8 and ":" in line:
                sections["Theory"] = line.split(":", 1)[1].strip()
        # Conclusion
        elif line_lower.startswith("conclusion:") or line_lower == "conclusion":
            current_section = "Conclusion"
            if len(line) > 12 and ":" in line:
                sections["Conclusion"] = line.split(":", 1)[1].strip()
        elif not sections["Conclusion"] and (line_lower.startswith("result:") or line_lower == "result"):
            current_section = "Conclusion"
            if len(line) > 8 and ":" in line:
                sections["Conclusion"] = line.split(":", 1)[1].strip()
        # Algorithm / Code -> stop theory collection or other collections
        elif line_lower.startswith("algorithm") or line_lower.startswith("code") or line_lower.startswith("pseudo code"):
            current_section = None
        elif current_section:
            sections[current_section] += "\n" + line if sections[current_section] else line
            
    # Clean up sections
    for k in sections:
        sections[k] = sections[k].strip()
        
    return sections

def extract_images(file_path, exp_id, output_dir):
    extracted = 0
    with zipfile.ZipFile(file_path, 'r') as docx:
        for name in docx.namelist():
            if name.startswith('word/media/') and name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                ext = name.split('.')[-1]
                img_data = docx.read(name)
                extracted += 1
                out_name = f"{exp_id}_screenshot_{extracted}.{ext}"
                with open(os.path.join(output_dir, out_name), 'wb') as f:
                    f.write(img_data)
    return extracted

def main():
    docs_dir = 'docs'
    theory_dir = 'theory'
    images_dir = 'assets/images'
    
    os.makedirs(theory_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    
    print("Starting Extraction...")
    
    stats = []
    
    for filename in os.listdir(docs_dir):
        if filename.endswith('.docx'):
            file_path = os.path.join(docs_dir, filename)
            
            # Map filename to exp_id
            # Assuming filename is like Exp1.docx -> exp1
            match = re.search(r'exp(\d+)', filename, re.IGNORECASE)
            if match:
                exp_id = f"exp{match.group(1)}"
            else:
                exp_id = filename.replace('.docx', '').lower()
                
            text_data = parse_docx(file_path)
            sections = extract_sections(text_data)
            
            # Write Markdown
            md_path = os.path.join(theory_dir, f"{exp_id}.md")
            with open(md_path, 'w', encoding='utf-8') as f:
                if sections["Experiment Number"]:
                    f.write(f"# Experiment {sections['Experiment Number']}\n\n")
                if sections["Aim"]:
                    f.write(f"# Aim\n{sections['Aim']}\n\n")
                if sections["Theory"]:
                    f.write(f"# Theory\n{sections['Theory']}\n\n")
                if sections["Conclusion"]:
                    f.write(f"# Conclusion\n{sections['Conclusion']}\n")
                    
            # Extract Images
            num_images = extract_images(file_path, exp_id, images_dir)
            
            stats.append({
                "file": filename,
                "exp_id": exp_id,
                "images": num_images,
                "has_aim": bool(sections["Aim"]),
                "has_theory": bool(sections["Theory"]),
                "has_conclusion": bool(sections["Conclusion"])
            })
            
    print(f"Processed {len(stats)} files.")
    for stat in stats:
        print(stat)

if __name__ == '__main__':
    main()
