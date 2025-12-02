import yfinance as yf
import pandas as pd
import numpy as np

def fetch_value_factors(tickers):
  """
  Fetch value and mispricing factors from Yahoo Finance
  for a list of tickers.
  """
  rows = []

  for ticker in tickers:
      t = yf.Ticker(ticker)
      info = t.info

      ev = info.get("enterpriseValue",np.nan)
      ebit = info.get("ebit", info.get("operatingIncome", np.nan))
      ps = info.get("priceToSalesTrailing12Months", np.nan)
      sector = info.get("sector", None)
      market_cap = info.get("marketCap", np.nan)
      total_debt = info.get("totalDebt", np.nan)
      total_equity = info.get("totalStockholderEquity", np.nan)
      free_cash_flow = info.get("freeCashflow", np.nan)
        # Compute EV/EBIT safely
        if ebit not in (0, None, np.nan):
            ev_ebit = ev / ebit
        else:
            ev_ebit = np.nan
          
        # Compute Debt-to-Equity safely
        if total_equity not in (0, None, np.nan):
            de_ratio = total_debt / total_equity
        else:
            de_ratio = np.nan
          
        # Compute Free Cash Flow Yield safely
        if market_cap not in (0, None, np.nan) and free_cash_flow not in (None, np.nan):
            fcf_yield = free_cash_flow / market_cap
        else:
            fcf_yield = np.nan

        row = {
            "ticker": ticker,
            "sector": sector,
            "enterprise_value": ev,
            "ebit": ebit,
            "ev_ebit": ev_ebit,
            "price_sales_ttm": ps,
            "total_debt": total_debt,
            "total_equity": total_equity,
            "de_ratio": de_ratio,
            "free_cash_flow": free_cash_flow,
            "market_cap": market_cap,
            "fcf_yield": fcf_yield,
        }

        rows.append(row)
  df = pd.DataFrame(rows)
  df = df.set_index("ticker")
  return df








