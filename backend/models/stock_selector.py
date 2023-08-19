import yfinance as yf
import pandas as pd

import yfinance as yf

def filter_companies(tickers):
    results = []
    for ticker in tickers:
        ticker_data = yf.Ticker(ticker)
        if passes_model(ticker_data):
            results.append(ticker)
    return results

def passes_model(ticker_data):
    def selector(companies):

        # Create an empty DataFrame to store the results
        results = pd.DataFrame(columns=['Company', 'Undervalued', 'Ratio', 'Debt/Equity', 'Return on Equity'])

        # Set the discount rate
        discount_rate = 0.1

        for company in companies:
            # Create a Ticker object for the company
            ticker = yf.Ticker(company)

            # Get the cash flow data
            cashflow = ticker.get_cashflow()

            # Check if 'FreeCashFlow' is in the index of the cashflow DataFrame
            if 'FreeCashFlow' in cashflow.index:
                # Convert 'FreeCashFlow' values to numbers
                fcf = pd.to_numeric(cashflow.loc['FreeCashFlow'], errors='coerce')

                # Ensure there are at least 4 years of data
                if len(fcf) < 4:
                    print(f"Not enough data to calculate CAGR for {ticker.ticker}.")
                    continue  # Skip to the next iteration

                start_value = fcf.iloc[-1]
                end_value = fcf.iloc[0]
                n = len(fcf) - 1

                # Skip if growth is negative
                if end_value < start_value:
                    print(f"Negative growth for {ticker.ticker}. Skipping...")
                    continue  # Skip to the next iteration

                # Calculate CAGR
                growth_rate = (end_value/start_value) ** (1/n) - 1

                print(f"CAGR for {ticker.ticker}: {growth_rate*100:.2f}%")

                # Get the FCF from last year
                last_year_fcf = fcf.iloc[0]

                # Calculate the discounted FCF for the next 10 years
                dcf = [last_year_fcf * (1 + growth_rate) ** year / (1 + discount_rate) ** year for year in range(1, 11)]

                # Calculate the intrinsic value and apply the margin of safety
                intrinsic_value = sum(dcf) * 0.65

                # Get the market capitalization
                market_cap = ticker.info['marketCap']

                # Determine whether the stock is undervalued or overvalued
                undervalued = 'Yes' if intrinsic_value > market_cap else 'No'

                value_ratio = market_cap / intrinsic_value 

                # Get the Debt/Equity ratio and Return on Equity
                debt_equity = ticker.info.get('debtToEquity', None)
                roe = ticker.info.get('returnOnEquity', None)

                # Append the results to the DataFrame
                df = pd.DataFrame({'Company': [company], 'Undervalued': [undervalued], 'Ratio': [value_ratio], 'Debt/Equity': [debt_equity], 'Return on Equity': [roe]})
                results = pd.concat([results, df], ignore_index=True)

            else:
                print(f"Unable to calculate Free Cash Flow for {company}.")

    print(results)

    # Filter the DataFrame for undervalued companies with a Debt/Equity ratio less than 2 and a Return on Equity over 10%
    filtered_results = results[(results['Undervalued'] == 'Yes') & (results['Debt/Equity'] < 200) & (results['Return on Equity'] > 0.10)]

    print(filtered_results)
    return True








### -------------------------BELOW GIVES MORE DETAILS AND IS SLIGHTLY DIFFERENT-------------------------- ###

# # Create an empty DataFrame to store the results
# results = pd.DataFrame(columns=['Company', 'Intrinsic Value', 'Market Cap', 'Undervalued', 'Ratio'])

# # Set the discount rate
# discount_rate = 0.1

# for company in companies:

#     # Create a Ticker object for the company
#     ticker = yf.Ticker(company)
#     # Get the cash flow data
#     cashflow = ticker.get_cashflow()
#     # print(cashflow.index)
#     # print(cashflow)

#     if 'FreeCashFlow' in cashflow.index:

#         # Convert 'FreeCashFlow' values to numbers
#         fcf = pd.to_numeric(cashflow.loc['FreeCashFlow'], errors='coerce')
#         # print(fcf.dtype)
    
#         # Ensure there are at least 5 years of data
#         if len(fcf) < 4:
#             print(f"Not enough data to calculate CAGR for {ticker.ticker}.")
#             continue
            
#         start_value = fcf.iloc[-1]
#         end_value = fcf.iloc[0]
#         n = len(fcf) - 1

#         if end_value < start_value:
#             print(f"Negative growth for {ticker.ticker}. Skipping...")
#             continue

#         # Calculate CAGR
#         growth_rate = (end_value/start_value) ** (1/n) - 1

#         print(f"CAGR for {ticker.ticker}: {growth_rate*100:.2f}%")

#         # Calculate the growth rate for each year
#         # growth_rate = (cashflow.loc['FreeCashFlow'] / cashflow.loc['FreeCashFlow'].shift(-1)) - 1
#         #print("Growth rate by year\n",growth_rate)

#         # # Convert to numeric and drop NaNs
#         # growth_rate = pd.to_numeric(cagr, errors='coerce').dropna()

#         # Calculate the geometric mean of the growth rate
#         #### average_growth_rate = gmean(growth_rate + 1) -1 
    
#         #mean_growth_rate = mean(growth_rate) 

#         #print("Average growth rate: ", average_growth_rate)

#         # Get the FCF from last year
#         last_year_fcf = cashflow.loc['FreeCashFlow'].iloc[0]
#         #print("Last year cash flow:", last_year_fcf)

#         # Calculate the discounted FCF for the next 10 years
#         dcf = [last_year_fcf * (1 + growth_rate) ** year / (1 + discount_rate) ** year for year in range(1, 11)]
#         #print(dcf)

#         # Calculate the intrinsic value and apply the margin of safety
#         intrinsic_value = sum(dcf) * 0.65

#         #print("Intrinsic value: ", intrinsic_value)

#         # Get the market capitalization
#         market_cap = ticker.info['marketCap']

#         # Determine whether the stock is undervalued or overvalued
#         undervalued = 'Yes' if intrinsic_value > market_cap else 'No'

#         value_ratio = market_cap / intrinsic_value 

#         #print("Market Cap / Intrinsic Value (should be less than 1)", value_ratio)

#         #print("Is the stock undervalued? ", undervalued)

#         df = pd.DataFrame({'Company': [company], 'Intrinsic Value': [intrinsic_value], 'Market Cap': [market_cap], 'Undervalued': [undervalued], 'Ratio': [value_ratio]})
#         results = pd.concat([results, df], ignore_index=True)
        
#     else:
#         print(f"Unable to calculate Free Cash Flow for {company}.")


# print(results)