"""
ticker_master_list.py

This file contains the hardcoded master lists of Top 100 companies 
for US (Nasdaq/S&P mixed) and INDIA (Nifty 100).

These symbols are pre-formatted for Yahoo Finance:
- US symbols use hyphens for classes (e.g., BRK-B)
- Indian symbols use the .NS suffix (e.g., RELIANCE.NS)
"""

# ==========================================
# 🇺🇸 USA: TOP 100 BY MARKET CAP
# ==========================================
US_TOP_100 = [
    'AAPL', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'BRK-B', 'LLY', 'TSM', 
    'AVGO', 'JPM', 'V', 'NVO', 'WMT', 'XOM', 'MA', 'UNH', 'PG', 'JNJ', 
    'HD', 'ORCL', 'COST', 'MRK', 'ABBV', 'BAC', 'CVX', 'CRM', 'KO', 'NFLX', 
    'AMD', 'PEP', 'ADBE', 'LIN', 'TMO', 'DIS', 'MCD', 'ACN', 'CSCO', 'WFC', 
    'ABT', 'INTC', 'QCOM', 'TM', 'CAT', 'INTU', 'DHR', 'VZ', 'AMAT', 'IBM', 
    'GE', 'CMCSA', 'AXP', 'UBER', 'PFE', 'NKE', 'TXN', 'AMGN', 'UNP', 'PM', 
    'NOW', 'SPGI', 'LOW', 'ISRG', 'COP', 'HON', 'RTX', 'GS', 'UPS', 'T', 
    'BKNG', 'ELV', 'NEE', 'SYK', 'PLD', 'MS', 'BA', 'MDT', 'BMY', 'TJX', 
    'LRCX', 'BLK', 'PGR', 'DE', 'ADP', 'ADI', 'MMC', 'LMT', 'CB', 'VRTX', 
    'MDLZ', 'REGN', 'C', 'BSX', 'PANW', 'MU', 'KLAC', 'FI', 'ETN', 'GILD'
]

# ==========================================
# 🇮🇳 INDIA: TOP 100 (NIFTY 100 CONSTITUENTS)
# ==========================================
INDIA_TOP_100 = [
    # --- Top 50 Giants ---
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'BHARTIARTL.NS', 'SBIN.NS', 
    'INFY.NS', 'LICI.NS', 'ITC.NS', 'HINDUNILVR.NS', 'LT.NS', 'BAJFINANCE.NS', 
    'HCLTECH.NS', 'MARUTI.NS', 'SUNPHARMA.NS', 'ADANIENT.NS', 'KOTAKBANK.NS', 
    'TITAN.NS', 'ONGC.NS', 'TATAMOTORS.NS', 'NTPC.NS', 'AXISBANK.NS', 'ADANIPORTS.NS',
    'ULTRACEMCO.NS', 'M&M.NS', 'ASIANPAINT.NS', 'BAJAJFINSV.NS', 'POWERGRID.NS',
    'COALINDIA.NS', 'WIPRO.NS', 'NESTLEIND.NS', 'IOC.NS', 'JSWSTEEL.NS', 'DLF.NS',
    'ADANIGREEN.NS', 'TATASTEEL.NS', 'SIEMENS.NS', 'IRFC.NS', 'VBL.NS', 'ETERNAL.NS',
    'HAL.NS', 'TRENT.NS', 'BEL.NS', 'PFC.NS', 'RECLTD.NS', 'PNB.NS', 'GAIL.NS',
    'BANKBARODA.NS', 'ADANIPOWER.NS', 'JIOFIN.NS', 'TATACONSUM.NS',
    
    # --- Next 50 Major Players ---
    'CHOLAFIN.NS', 'HAVELLS.NS', 'DABUR.NS', 'ABB.NS', 'GODREJCP.NS',
    'DIVISLAB.NS', 'BPCL.NS', 'INDUSINDBK.NS', 'SHREECEM.NS', 'TVSMOTOR.NS', 
    'LTIM.NS', 'AMBUJACEM.NS', 'VEDL.NS', 'HINDALCO.NS', 'PIDILITIND.NS', 
    'EICHERMOT.NS', 'GRASIM.NS', 'TECHM.NS', 'CIPLA.NS', 'BRITANNIA.NS', 
    'DRREDDY.NS', 'HEROMOTOCO.NS', 'APOLLOHOSP.NS', 'SBICARD.NS', 'BOSCHLTD.NS',
    'SRF.NS', 'ICICIPRULI.NS', 'ICICIGI.NS', 'CANBK.NS', 'BERGEPAINT.NS', 
    'MOTHERSON.NS', 'NAUKRI.NS', 'ZYDUSLIFE.NS', 'LODHA.NS', 'UNIONBANK.NS', 
    'IOB.NS', 'NHPC.NS', 'INDIGO.NS', 'JINDALSTEL.NS', 'TORNTPHARM.NS', 
    'MANKIND.NS', 'JSWINFRA.NS', 'POLICYBZR.NS', 'DMART.NS',
    
    # --- Added to reach exactly 100 count ---
    'OFSS.NS', 'LUPIN.NS', 'VOLTAS.NS', 'PERSISTENT.NS', 'MUTHOOTFIN.NS'
]