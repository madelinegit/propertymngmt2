import streamlit as st
import pandas as pd

st.markdown("""
<style>
/* --- overall vibe --- */
.stApp { background-color: #f9f6fc; }

/* Headings */
h1, h2, h3 { color: #5e3a7d; }

/* Buttons */
.stButton > button {
  background: #cdb4db !important;
  color: white !important;
  border: 0 !important;
  border-radius: 10px !important;
  font-weight: 600 !important;
}
.stButton > button:hover { background: #b296c9 !important; }

/* Radio accents (dot + hover) */
div[role="radiogroup"] * {
  accent-color: #cdb4db !important;
}

/* --- MULTISELECT FIXES --- */
/* The outer input border */
div[data-baseweb="select"] > div {
  border-color: #cdb4db !important;
}

/* Focus/active border + glow */
div[data-baseweb="select"] > div:focus-within {
  border-color: #cdb4db !important;
  box-shadow: 0 0 0 0.2rem rgba(205, 180, 219, 0.25) !important;
}

/* The selected “chips/tags” background (yours are red right now) */
div[data-baseweb="tag"] {
  background-color: #e6d9f2 !important;
  color: #4b2c5e !important;
  border: 1px solid #cdb4db !important;
}

/* The little “x” close icon inside the chips */
div[data-baseweb="tag"] span {
  color: #4b2c5e !important;
}

/* Placeholder / typed text color */
div[data-baseweb="select"] input {
  color: #4b2c5e !important;
}
div[data-baseweb="select"] input::placeholder {
  color: rgba(75, 44, 94, 0.55) !important;
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
