import os
import sys
import streamlit as st

# Make sure the repo root is on the Python path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from fetch.fetch_value_factors import fetch_value_factors


st.title("Small-Cap Lab – Value / Mispricing Engine")

st.write(
    "Enter one or more stock tickers (comma-separated) "
    "and I'll fetch the core value factors from Yahoo Finance."
)

# Text box for tickers
tickers_input = st.text_input(
    "Tickers (comma-separated):",
    value="TWST, ENSG, SPXC",
)

if st.button("Fetch value factors"):
    # Turn "TWST, ENSG, SPXC" into ["TWST", "ENSG", "SPXC"]
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

    if not tickers:
        st.warning("Please enter at least one ticker.")
    else:
        with st.spinner("Fetching data from Yahoo Finance..."):
            df = fetch_value_factors(tickers)

        st.subheader("Raw value factors")
        st.dataframe(df)
