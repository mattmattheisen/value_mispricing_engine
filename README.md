# value_mispricing_engine
A quantitative value and mispricing engine for the Small-Cap Lab. Computes EV/EBIT, Relative P/S, Debt-to-Equity, FCF Yield, Piotroski F-Score, and a unified Value Score for integration with momentum, HMM regimes, and Kelly sizing.
## Project Structure

```text
small-cap-lab-value-module/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── sector_medians.csv          # optional storage for sector P/S medians
│
├── fetch/
│   └── fetch_value_factors.py      # pulls EV/EBIT, P/S, D/E, FCF, sector, etc.
│
├── scoring/
│   ├── ev_ebit_score.py            # normalization function
│   ├── relative_ps_score.py
│   ├── de_score.py
│   ├── fcf_yield_score.py
│   └── piotroski_score.py          # optional (we’ll add later)
│
├── value_module/
│   └── compute_value_score.py      # combines all the factors into Value_Score
│
├── dual_engine/
│   └── dual_score.py               # 0.60 momentum + 0.40 value
│
└── streamlit_app/
    └── app.py                      # optional UI integration

