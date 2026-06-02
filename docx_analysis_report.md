# Lab Documents (.docx) Analysis Report

## Overview
This report details the findings from inspecting the `.docx` files located in the `docs/` directory. The goal was to extract specific sections, detect screenshots, and provide a recommendation for integrating this content into the Streamlit application.

## Extraction Results

The inspection script scanned all 11 experiment documents (`Exp1.docx` through `Exp11.docx`). The following table summarizes the sections successfully found, missing sections, and the number of screenshots detected in each document.

| Document | Found Sections | Missing Sections | Screenshots Detected |
| :--- | :--- | :--- | :--- |
| **Exp1.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp2.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp3.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp4.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp5.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp6.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp7.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp8.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp9.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp10.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 1 |
| **Exp11.docx** | Experiment Number, Aim, Theory, Conclusion | Title, Algorithm | 2 |

> [!NOTE]
> - The **"Algorithm"** section was consistently missing across all documents, indicating that it may be omitted or documented under a different heading (e.g., "Code").
> - The **"Title"** section was not explicitly labeled in a way that could be programmatically distinguished from the Aim or surrounding text.

## Recommendations for Streamlit Integration

Currently, the Streamlit app's `dynamic_experiment.py` uses hardcoded placeholder text for the **Theory** and **Algorithm** tabs. To fully integrate the content from these `.docx` files into the application, I recommend the following architecture:

### 1. Data Extraction and Conversion
Instead of parsing `.docx` files on-the-fly when the Streamlit app runs (which is slow and error-prone), you should perform a one-time extraction:
- Use a library like `python-docx` to parse the documents.
- Convert the extracted "Aim", "Theory", and "Conclusion" text into clean **Markdown** files (e.g., `theory/exp1.md`).
- Extract the embedded screenshots and save them as standard image files (e.g., `.png` or `.jpg`) into an `assets/images/` directory.

### 2. Streamlit UI Updates
Modify the dynamic rendering engine (`experiments/dynamic_experiment.py`) to consume the new structured data:

#### Theory Tab
- Update the **Theory** tab to read the corresponding Markdown file (e.g., `theory/{exp_id}.md`) using standard file I/O.
- Render the text using `st.markdown(file_content)`.

#### Algorithm Tab
- Since the Algorithm section is currently missing from the docs, you could hide this tab dynamically if the data doesn't exist, or manually add the algorithm text to the markdown files later.

#### Results / Output Tab
- The extracted screenshots represent the expected outputs. You can create a sub-section in the **Output** tab (or a brand new "Expected Result" tab) that renders the extracted screenshot using `st.image(f"assets/images/{exp_id}_screenshot.png")`. This allows students to compare their live execution output with the expected document output.

### 3. Dependencies
- If you decide to dynamically parse `.docx` files within the app instead of pre-compiling them to Markdown, you will need to add `python-docx` to `requirements.txt`. However, the **pre-compilation to Markdown** approach is highly recommended for performance and stability.
