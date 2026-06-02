import streamlit as st
import importlib
import contextlib
import io
import matplotlib.pyplot as plt
import os

EXPERIMENT_MAP = {
    "1 Basic Graphs": "exp1",
    "2 Graph Isomorphism": "exp2",
    "3 Subgraphs": "exp3",
    "4 Havel-Hakimi": "exp4",
    "5 Line Graph": "exp5",
    "6 Kruskal MST": "exp6",
    "7 Dijkstra": "exp7",
    "8 Closed Walks Trails Paths": "exp8",
    "9 Eulerian Circuit": "exp9",
    "10 Hamiltonian Circuit": "exp10",
    "11 Greedy Graph Colouring": "exp11"
}

def mock_show(*args, **kwargs):
    st.pyplot(plt.gcf())
    plt.clf()

def render(experiment_name):
    exp_id = EXPERIMENT_MAP.get(experiment_name)
    if not exp_id:
        st.error("Experiment not found mapping.")
        return

    aim_text = ""
    theory_file = os.path.join("theory", f"{exp_id}.md")
    if os.path.exists(theory_file):
        with open(theory_file, "r", encoding="utf-8") as f:
            content = f.read()
            if "# Aim" in content:
                aim_part = content.split("# Aim")[1].split("#")[0].strip()
                aim_text = aim_part

    is_dark = st.session_state.get('theme') == 'Dark'
    text_col = '#F8FAFC' if is_dark else '#111827'
    muted_col = '#CBD5E1' if is_dark else '#6B7280'
    theme_accent = '#10B981'

    st.markdown("<div style='margin-bottom: 30px;'>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color: {muted_col}; font-weight: 600; margin-bottom: 8px; letter-spacing: 1px; text-transform: uppercase;'>Graph Theory Laboratory</h4>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='margin-top: 0; font-size: 38px; margin-bottom: 20px; color: {text_col};'>{experiment_name}</h1>", unsafe_allow_html=True)
    
    if aim_text:
        st.markdown(f"""
        <div class="premium-card" style="padding: 20px 24px; border-left: 4px solid {theme_accent}; margin-bottom: 30px;">
            <p style='font-size: 17px; color: {muted_col}; font-weight: 500; margin: 0; line-height: 1.6;'>{aim_text}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Theory", 
        "⚙ Algorithm", 
        "💻 Code", 
        "▶ Run", 
        "📊 Output"
    ])
    
    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        if os.path.exists(theory_file):
            with open(theory_file, "r", encoding="utf-8") as f:
                content = f.read()
                st.markdown(f"<div class='premium-card'>\n\n{content}\n\n</div>", unsafe_allow_html=True)
        else:
            st.info("Theory documentation not available.")
        
    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        algo_file = os.path.join("algorithms", f"{exp_id}.md")
        if os.path.exists(algo_file):
            with open(algo_file, "r", encoding="utf-8") as f:
                content = f.read()
                st.markdown(f"<div class='premium-card'>\n\n{content}\n\n</div>", unsafe_allow_html=True)
        else:
            st.info("Algorithm documentation not available.")
        
    with tab3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='premium-card' style='padding-bottom: 10px; margin-bottom: 15px;'>
            <h3 style='margin-top:0; font-size: 20px; color: {text_col};'>Implementation Source</h3>
            <p style='color:{muted_col}; font-size: 15px; margin-bottom: 0;'>Python script representing the actual executed logic.</p>
        </div>
        """, unsafe_allow_html=True)
        
        file_path = os.path.join("lab_experiments", f"{exp_id}.py")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                code_content = f.read()
            st.code(code_content, language='python')
        else:
            st.error(f"Source file not found: {file_path}")
            
    with tab4:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='premium-card'>
            <h3 style='margin-top:0; font-size: 22px; margin-bottom: 10px; color: {text_col};'>Execution Engine</h3>
            <p style='color:{muted_col}; font-size: 16px; margin-bottom: 25px;'>
                Ready to execute the environment script in an isolated runtime. Results will be piped directly to the Output tab.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Execute Experiment", type="primary", use_container_width=True):
                st.session_state[f'run_{exp_id}'] = True
                st.success("Execution triggered! Navigate to the 📊 Output tab to view results.")
            
    with tab5:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.session_state.get(f'run_{exp_id}'):
            with st.spinner("Executing..."):
                original_show = plt.show
                plt.show = mock_show
                f_out = io.StringIO()
                
                try:
                    with contextlib.redirect_stdout(f_out):
                        module = importlib.import_module(f"lab_experiments.{exp_id}")
                        importlib.reload(module)
                        
                        if hasattr(module, "run"):
                            module.run()
                        else:
                            st.warning("No 'run()' function found in the module.")
                except Exception as e:
                    st.error(f"Execution Error: {e}")
                finally:
                    plt.show = original_show
                
                text_output = f_out.getvalue()
                if text_output.strip():
                    st.markdown(f"""
                    <div class='premium-card' style='padding-bottom: 10px; margin-bottom: 15px;'>
                        <h3 style='margin-top:0; font-size: 19px; color: {text_col};'>💻 Console Output</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    st.code(text_output, language='text')
                
                images_dir = os.path.join("assets", "images")
                if os.path.exists(images_dir):
                    expected_images = [img for img in os.listdir(images_dir) if img.startswith(f"{exp_id}_screenshot_")]
                    if expected_images:
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.markdown(f"""
                        <div class='premium-card' style='padding-bottom: 10px; margin-bottom: 15px;'>
                            <h3 style='margin-top:0; font-size: 19px; color: {text_col};'>📸 Expected Lab Record Output</h3>
                            <p style='color:{muted_col}; font-size: 15px; margin-bottom: 0;'>Reference imagery extracted from documentation.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        for img in sorted(expected_images):
                            st.image(os.path.join(images_dir, img), use_container_width=True)
        else:
            st.info("Run the experiment from the ▶ Run tab to view the captured output and figures.")
