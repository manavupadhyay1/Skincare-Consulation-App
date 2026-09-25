import streamlit as st
import pandas as pd

# --- Configuration & Data Loading ---
st.set_page_config(page_title="AI Skin Consultant", layout="centered")

@st.cache_data
def load_data():
    # Load the new dataset (make sure the filename matches your saved file)
    df = pd.read_csv('indian_skincare_dataset.csv')
    
    # Standardize column names to remove hidden spaces
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# --- Minimalist Sidebar ---
st.sidebar.header("✨ Your Skin Profile")

# Extract unique values for dropdowns to ensure they match the dataset
skin_types = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
concerns = ["Acne", "Pigmentation", "Hydration", "Sun protection", "Dark Spots"]

stype = st.sidebar.selectbox("Skin Type", skin_types)
sconcern = st.sidebar.selectbox("Main Concern", concerns)

# --- Main App ---
st.title("AI Skin Consultant")
st.markdown("Scientific recommendations for your unique skin needs.")

if st.button("Generate My Routine"):
    # AI Logic: Filtering based on the specific columns in your CSV
    # We search the 'Skin type' and 'Concern' columns directly
    filtered = df[
        (df['Skin type'].str.contains(stype, case=False, na=False)) & 
        (df['Concern'].str.contains(sconcern, case=False, na=False))
    ]

    # --- Routine Builder ---
    st.subheader("Your Personalized Recommendations")
    
    if not filtered.empty:
        # Displaying results in a clean grid
        for index, row in filtered.head(6).iterrows():
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    # Display product picture if URL exists
                    if pd.notnull(row['product_pic']):
                        st.image(row['product_pic'], width=100)
                with col2:
                    st.write(f"### {row['Product']}")
                    st.write(f"**Best For:** {row['Concern']}")
                    st.write(f"[View Product Page]({row['product_url']})")
                st.divider()
    else:
        st.error(f"No products found specifically for {stype} skin with {sconcern.lower()} concerns. Try a different category!")

st.markdown("---")
st.caption("AI suggestions based on categorized Indian skincare data.")

#to run the code paste this in the terminal- python -m streamlit run app.py