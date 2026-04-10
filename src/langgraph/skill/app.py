import streamlit as st
import json
import os

st.set_page_config(page_title="Paper2Code Debugger", layout="wide")

st.title("🧠 Paper2Code Agent Debugger")

# Load traces
trace_files = os.listdir("traces") if os.path.exists("traces") else []

selected_file = st.selectbox("Select run", trace_files)

if selected_file:
    with open(f"traces/{selected_file}") as f:
        data = json.load(f)

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Paper Text")
        st.text_area("", data.get("paper_text", ""), height=400)

        st.subheader("🧠 Spec")
        st.text_area("", data.get("spec", ""), height=300)

    with col2:
        st.subheader("💻 Generated Code")
        st.code(data.get("code", ""), language="python")

        st.subheader("❌ Error (if any)")
        st.text_area("", data.get("error", ""), height=200)

    st.divider()

    # Trace timeline
    st.subheader("📊 Execution Trace")

    trace = data.get("trace", [])

    for i, event in enumerate(trace):
        with st.expander(f"{i+1}. {event['event']}"):
            st.json(event["data"])