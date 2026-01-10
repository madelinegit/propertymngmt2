import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f9f6fc;
    }

    /* Primary buttons */
    .stButton > button {
        background-color: #cdb4db;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5em 1.2em;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #b296c9;
        color: white;
    }

    /* Radio buttons & multiselect highlight */
    div[role="radiogroup"] > label > div:first-child,
    .stMultiSelect div[data-baseweb="tag"] {
        background-color: #e6d9f2 !important;
        color: #4b2c5e !important;
    }

    /* Input box focus */
    input:focus, textarea:focus {
        border-color: #cdb4db !important;
        box-shadow: 0 0 0 0.2rem rgba(205, 180, 219, 0.25) !important;
    }

    /* Headers */
    h1, h2, h3 {
        color: #5e3a7d;
    }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Property Distance Sorter", layout="wide")
st.title("Property Distance Sorter")

uploaded = st.file_uploader("Upload your property distance Excel file", type=["xlsx"])

if uploaded:
    df = pd.read_excel(uploaded)

    # Auto-detect columns
    name_col = "Property Name" if "Property Name" in df.columns else st.selectbox("Property name column", df.columns)
    dist_col = "Distance" if "Distance" in df.columns else st.selectbox("Distance column", df.columns)

    # Ensure numeric distance
    df[dist_col] = pd.to_numeric(df[dist_col], errors="coerce")

    st.subheader("Select Properties")
    st.write("Start typing a property name and press **Enter** to add it.")

    selected = st.multiselect(
        "Properties",
        options=df[name_col].dropna().tolist(),
        default=[],
        placeholder="Type a property name…"
    )

    order = st.radio(
        "Sort order",
        ["Closest → Farthest", "Farthest → Closest"],
        horizontal=True
    )
    ascending = order == "Closest → Farthest"

    if st.button("Sort & Analyze", type="primary"):
        if not selected:
            st.warning("Please select at least one property.")
        else:
            result = (
                df[df[name_col].isin(selected)]
                .sort_values(by=dist_col, ascending=ascending)
                .reset_index(drop=True)
            )

            st.subheader("Sorted Results")

            # Clean display
            for i, row in result.iterrows():
                st.write(f"**{i+1}. {row[name_col]}** — {row[dist_col]} miles")
