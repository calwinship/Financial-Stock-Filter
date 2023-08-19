### --------------------------------------------STOCK SELECTOR-----------------------------------------------------###

# import selector from models/stock_selector

# # Define the Tickers
# SnP500 = ['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'TSLA', 'BRK.B', 'NVDA', 'JPM', 'JNJ', 'V', 'PG', 'UNH', 'DIS', 'HD', 'MA', 'PYPL', 'BAC', 'INTC', 'CMCSA', 'VZ', 'XOM', 'ADBE', 'CRM', 'NFLX', 'KO', 'NKE', 'MRK', 'PEP', 'PFE', 'WMT', 'CSCO', 'ABT', 'T', 'ORCL', 'CVX', 'LLY', 'MCD', 'ABBV', 'ACN', 'DHR', 'AVGO', 'QCOM', 'TXN', 'COST', 'HON', 'AMGN', 'NEE', 'UNP', 'MDT', 'BMY', 'LIN', 'MMM', 'LOW', 'UPS', 'IBM', 'BA', 'SBUX', 'RTX', 'GE', 'CAT', 'GS', 'INTU', 'TMO', 'CVS', 'BKNG', 'CHTR', 'ISRG', 'GILD', 'SPGI', 'BLK', 'AXP', 'FIS', 'SYK', 'NOW', 'MDLZ', 'ZTS', 'ANTM', 'C', 'ADP', 'TJX', 'AMAT', 'LMT', 'MO', 'USB', 'PNC', 'DUK', 'MU', 'PLD', 'CCI', 'CB', 'SO', 'D', 'CL', 'BDX', 'EOG', 'ITW', 'MS', 'DE']
# SnP5002 = ['CMS', 'CNC', 'CNP', 'COF', 'COG', 'COO', 'COP', 'COST', 'COTY', 'CPB', 'CPRT', 'CRM', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTVA', 'CTXS', 'CVS', 'CVX', 'CXO', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS', 'DISCA', 'DISCK', 'DISH', 'DLR', 'DLTR', 'DOV', 'DOW', 'DRE', 'DRI', 'DTE', 'DUK', 'DVA', 'DVN', 'DXC', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'ES', 'ESS', 'ETFC', 'ETN', 'ETR', 'EVRG', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR', 'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLS', 'FLT', 'FMC', 'FOX', 'FOXA', 'FRC', 'FRT', 'FTI', 'FTNT', 'FTV', 'GD', 'GE', 'GILD', 'GIS', 'GL', 'GLW', 'GM', 'GOOG', 'GOOGL']
# SnP5003= ['GPC', 'GPN', 'GPS', 'GRMN', 'GS', 'GWW', 'HAL', 'HAS', 'HBAN', 'HBI', 'HCA', 'HD', 'HES', 'HFC', 'HIG', 'HII', 'HLT', 'HOG', 'HOLX', 'HON', 'HP', 'HPE', 'HPQ', 'HRB', 'HRL', 'HSIC', 'HST', 'HSY', 'HUM', 'IBM', 'ICE', 'IDXX', 'IEX', 'IFF', 'ILMN', 'INCY', 'INFO', 'INTC', 'INTU', 'IP', 'IPG', 'IPGP', 'IQV', 'IR', 'IRM', 'ISRG', 'IT', 'ITW', 'IVZ', 'J', 'JBHT', 'JCI', 'JEC', 'JKHY', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY', 'KEYS', 'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LDOS', 'LEG', 'LEN', 'LH', 'LHX', 'LIN', 'LKQ', 'LLY', 'LMT', 'LNC', 'LNT', 'LOW', 'LRCX', 'LUV', 'LVS', 'LW', 'LYB', 'M', 'MA', 'MAA', 'MAC', 'MAR', 'MAS', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MGM', 'MHK', 'MKC', 'MKTX', 'MLM', 'MMC', 'MMM', 'MNST', 'MO', 'MOS']
# SnP5004= ['MPC', 'MRK', 'MRO', 'MS', 'MSCI', 'MSFT', 'MSI', 'MTB', 'MTD', 'MU', 'MXIM', 'MYL', 'NBL', 'NCLH', 'NDAQ', 'NEE', 'NEM', 'NFLX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV', 'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'ODFL', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PCAR', 'PEAK', 'PEG', 'PEP', 'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKG', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PXD', 'PYPL', 'QCOM', 'QRVO', 'RCL', 'RE', 'REG', 'REGN', 'RF', 'RHI', 'RJF', 'RL', 'RMD', 'ROK', 'ROL', 'ROP', 'ROST', 'RSG', 'RTN', 'SBAC', 'SBUX', 'SCHW', 'SEE', 'SHW', 'SIVB', 'SJM', 'SLB', 'SLG', 'SNA', 'SNPS', 'SO', 'SPG', 'SPGI', 'SRE', 'STE', 'STT', 'STX', 'STZ', 'SWK', 'SWKS', 'SYF', 'SYK', 'SYY', 'T', 'TAP', 'TDG', 'TEL', 'TFX', 'TGT', 'TIF', 'TJX', 'TMO', 'TMUS', 'TPR', 'TROW', 'TRV', 'TSCO', 'TSN', 'TTWO', 'TWTR', 'TXN', 'TXT', 'UA', 'UAA', 'UAL', 'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URI', 'USB', 'UTX', 'V', 'VAR', 'VFC', 'VIAC', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ', 'WAB', 'WAT', 'WBA', 'WCG', 'WDC', 'WEC', 'WELL', 'WFC', 'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRB', 'WRK', 'WU', 'WY', 'WYNN', 'XEC', 'XEL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL', 'YUM', 'ZBH', 'ZBRA', 'ZION', 'ZTS']
# LSE = ['III', 'ADM', 'AAL', 'ANTO', 'AHT', 'ABF', 'AZN', 'AUTO', 'AVV', 'AV.', 'BA.', 'BARC', 'BDEV', 'BKG', 'BHP', 'BP.', 'BATS', 'BLND', 'BT.A', 'BNZL', 'BRBY', 'CCL', 'CNA', 'CCH', 'CPG', 'CRH', 'CRDA', 'DCC', 'DGE', 'EZJ', 'EXPN', 'FERG', 'FLTR', 'FRES', 'GSK', 'GLEN', 'HLMA', 'HL.', 'HSBA', 'IMB', 'INF', 'IHG', 'IAG', 'ITRK', 'JD.', 'JMAT', 'KGF', 'LAND', 'LGEN', 'LLOY']
# NASDAQ = ['ATVI', 'ADBE', 'AMD', 'ALXN', 'ALGN', 'GOOGL', 'GOOG', 'AMZN', 'AEP', 'AMGN', 'ADI', 'ANSS', 'AAPL', 'AMAT', 'ASML', 'ADSK', 'ADP', 'BIDU', 'BIIB', 'BMRN', 'BKNG', 'AVGO', 'CDNS', 'CELG', 'CERN', 'CHTR', 'CHKP', 'CTAS', 'CSCO', 'CTXS', 'CTSH', 'CMCSA', 'COST', 'CSX', 'CTRP', 'DLTR', 'EBAY', 'EA', 'EXC', 'FB', 'FAST', 'FISV', 'GILD', 'HAS', 'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU']
# ISEQ = ['AIBG', 'APGN', 'BKIR', 'CRG', 'DCC', 'DOY', 'DRS', 'GL9', 'GNC', 'GRN', 'HBRN', 'IRES', 'KRX', 'MIO', 'ORP', 'RY4C', 'SGRO', 'SMH', 'T7O', 'YEW']
# Euronext100 = ['ABI', 'AD', 'ADYEN', 'AI', 'AIR', 'ALO', 'AMS', 'ATO', 'BB', 'BIM', 'BN', 'BNP', 'CA', 'CAP', 'CS', 'DG', 'DSY', 'EL', 'ENGI', 'ENX']
# Eurostoxx50 = ['ABI', 'AD', 'AI', 'AIR', 'ALV', 'ASML', 'BBVA', 'SAN', 'BAS', 'BAYN', 'BMW', 'BNP', 'CRG', 'CS', 'DTE', 'ENEL', 'ENGI', 'ENI', 'EOAN', 'EL', 'FRE', 'IBE', 'INGA', 'ISP', 'ITX', 'KER', 'LIN', 'MC', 'MUV2', 'NOKIA', 'OR', 'ORA', 'PHIA', 'SAF', 'SAN', 'SAP', 'SIE', 'SU', 'TEF', 'FP', 'URW', 'VIV', 'VOW3', 'DG', 'DPW', 'SIE', 'DAI']

# # Define the exchange
# companies = SnP500

# # Call the function
# selector(companies)

from flask import Flask, request, jsonify
import stock_selector

app = Flask(__name__)

@app.route('/filter_companies', methods=['POST'])
def filter_companies():
    tickers = request.json['tickers']
    results = stock_selector.filter_companies(tickers)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)