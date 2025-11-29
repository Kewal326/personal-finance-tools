import yfinance as yf
import pandas as pd
import time

# Import the master lists from the file in the same repository
try:
    from ticker_master_list import US_TOP_100, INDIA_TOP_100
except ImportError:
    print("❌ Error: 'ticker_master_list.py' not found. Make sure both files are in the same folder.")
    US_TOP_100 = []
    INDIA_TOP_100 = []

# ==========================================
# 🎛️ SETTINGS
# ==========================================
DROP_THRESHOLD = 0.40   # 0.20 = 20% Drop (Change to 0.40 for 40%)

# ==========================================
# 🛠️ HELPER FUNCTIONS
# ==========================================

def get_single_stock_data(ticker):
    """
    Fallback function: Tries to download a single stock if Batch Download fails.
    Using threads=False is slower but more reliable for Yahoo API.
    """
    try:
        df = yf.download(ticker, period="1y", progress=False, threads=False, ignore_tz=True, auto_adjust=True)
        return df
    except:
        return None

def scan_market(tickers, label):
    count = len(tickers)
    print(f"   🔍 Scanning {count} {label} stocks...")
    
    if count == 0:
        print("      ⚠️ Warning: Ticker list is empty.")
        return []

    # 1. Try Batch Download First (Fastest way)
    try:
        data = yf.download(tickers, period="1y", group_by='ticker', progress=False, threads=False, ignore_tz=True, auto_adjust=True)
    except Exception as e:
        print(f"   ❌ Critical Batch Error: {e}")
        return []

    results = []
    failed_initially = []
    
    # 2. Process Batch Data
    for ticker in tickers:
        try:
            # Handle Dataframe Structure (Single stock vs Batch returns different shapes)
            df = data if count == 1 else data.get(ticker)
            
            # Validation: Check if data exists and has columns
            if df is None or df.empty or 'Close' not in df.columns:
                failed_initially.append(ticker)
                continue
            
            # Get valid close prices (drop NaNs from holidays)
            valid_close = df['Close'].dropna()
            if valid_close.empty:
                failed_initially.append(ticker)
                continue
            
            curr = valid_close.iloc[-1]
            high = df['High'].max()
            
            if high == 0: continue
            
            # Calculate Drop
            drop = (curr - high) / high
            
            # Filter Criteria
            if drop <= -DROP_THRESHOLD:
                results.append({
                    'Market': label,
                    'Ticker': ticker,
                    'Price': round(curr, 2),
                    'High': round(high, 2),
                    'Drop %': round(drop * 100, 2)
                })
        except:
            failed_initially.append(ticker)
            continue
            
    # 3. SELF-HEALING: Retry Failed Tickers Individually
    # This fixes issues where Yahoo rejects specific Indian stocks in batch mode (e.g. Zomato)
    if failed_initially:
        print(f"      ⚠️  Batch fetch missed {len(failed_initially)} stocks. Retrying them individually...")
        
        for ticker in failed_initially:
            try:
                time.sleep(0.5) # Be polite to the API
                df = get_single_stock_data(ticker)
                
                if df is not None and not df.empty and 'Close' in df.columns:
                    valid_close = df['Close'].dropna()
                    if not valid_close.empty:
                        curr = valid_close.iloc[-1]
                        high = df['High'].max()
                        drop = (curr - high) / high
                        
                        if drop <= -DROP_THRESHOLD:
                            results.append({
                                'Market': label,
                                'Ticker': ticker,
                                'Price': round(curr, 2),
                                'High': round(high, 2),
                                'Drop %': round(drop * 100, 2)
                            })
            except:
                pass # If it fails twice, we skip it.
                
    return results

# ==========================================
# 🚀 MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    
    print(f"--- STARTING DEEP VALUE SCAN (Threshold: -{DROP_THRESHOLD*100}%) ---")
    
    # 1. Run Scans using imported lists
    us_results = scan_market(US_TOP_100, "USA")
    in_results = scan_market(INDIA_TOP_100, "INDIA")
    
    # 2. Combine Results
    combined = us_results + in_results
    
    # 3. Output Report
    if combined:
        df = pd.DataFrame(combined).sort_values(by='Drop %', ascending=True)
        
        print(f"\n\n🚨 FINAL REPORT: GIANTS DOWN {DROP_THRESHOLD*100}%+ 🚨")
        print("="*75)
        print(df[['Market', 'Ticker', 'Price', 'High', 'Drop %']].to_string(index=False))
        print("="*75)
        
        # Verify Tata Motors (Just for peace of mind)
        tata = next((item for item in in_results if item["Ticker"] == "TATAMOTORS.NS"), None)
        if tata:
            print(f"\n✅ Verified: Tata Motors found (Down {tata['Drop %']}%)")
    else:
        print(f"\n✅ No top companies are currently down {DROP_THRESHOLD*100}%.")