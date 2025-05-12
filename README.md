# NFT Market Analysis with GraphQL and LLM

This project analyzes NFT trading data from OpenSea's Seaport protocol using GraphQL queries and Large Language Models (LLMs) for market trend analysis.

## Project Structure

```
subgraph/
├── fecth_save_data.py      # Script to fetch NFT trading data using GraphQL
├── analyze_nft_trends.py   # Script to analyze data using GPT-4
├── nft_trend_analysis_prompt.txt  # Prompt template for LLM analysis
├── opensea_sales.csv       # Generated trading data
└── nft_market_analysis.txt # Generated market analysis
```

## Features

- **Data Collection**: Fetches 1000 recent NFT transactions from OpenSea's Seaport protocol
- **Data Processing**: Converts prices from Wei to ETH and handles timestamps
- **Market Analysis**: Uses GPT-4 to analyze trading patterns and predict trends
- **Risk Assessment**: Identifies potential market risks and provides recommendations

## Prerequisites

- Python 3.8+
- Required Python packages:
  ```bash
  pip install pandas requests openai
  ```
- OpenAI API key (for GPT-4 analysis)

## Usage

1. **Fetch Trading Data**
   ```bash
   python fetch_save_data.py
   ```
   This will generate `opensea_sales.csv` with the latest trading data.

2. **Analyze Market Trends**
   ```bash
   # Set your OpenAI API key
   export OPENAI_API_KEY='your-api-key-here'
   
   # Run the analysis
   python analyze_nft_trends.py
   ```
   This will generate `nft_market_analysis.txt` with the market analysis.

## Analysis Components

The analysis includes:
1. **Price Trends**
   - Price movement patterns
   - Average price calculations
   - Significant price changes

2. **Trading Activity**
   - Volume patterns
   - Activity periods
   - Unusual patterns

3. **Market Predictions**
   - 30-day price trend forecast
   - Confidence levels
   - Influencing factors

4. **Risk Assessment**
   - Market risks
   - Concerning patterns
   - Risk mitigation strategies

## Data Format

The generated CSV file includes:
- Transaction ID
- Buyer address (offerer)
- Seller address (recipient)
- Price (in ETH)
- Transaction timestamp
- Transaction hash

## Notes

- The analysis is based on the most recent 1000 transactions
- Prices are converted from Wei to ETH for better readability
- The LLM analysis provides both quantitative and qualitative insights

## A Sample Prediction towards a NFT asset class.
```
1. EXECUTIVE SUMMARY

The data shows a total of 1000 transactions from June 15, 2022, to August 20, 2023. The price range of the transactions is from 0 to 22.8 ETH, with an average price of 0.1427 ETH. Analysis of the data reveals fluctuating price trends, varying trading volumes, and several potential market risks. Market predictions have been made based on historical data and trends observed.

2. DETAILED ANALYSIS

Price Trends:
The average price of transactions is 0.1427 ETH. There are fluctuations in the prices, indicating a volatile market condition. Significant price spikes and drops are observed, which could be attributed to market sentiment, demand and supply, and other market factors.

Trading Activity:
Trading volume patterns reveal periods of high and low activity. Unusual trading patterns such as sudden spikes or drops in trading volumes are observed. These could be due to specific events or market news causing increased buying or selling activity.

3. PREDICTIONS

Based on historical data, the price trend for the next 30 days could be volatile given the fluctuations observed in the data. However, as the market for NFTs continues to grow, a general upward trend in prices can be expected. Key influencing factors could include market sentiment, demand and supply, and overall market conditions. The confidence level for this prediction is moderate given the volatility of the NFT market.

4. RISK ASSESSMENT

Potential market risks include price volatility, which could lead to significant losses for traders. Concerning patterns such as sudden spikes or drops in trading volumes suggest possible market manipulation or the impact of market news. To mitigate these risks, traders should diversify their portfolios, stay updated with market news, and use stop-loss orders to limit potential losses.

Please note that this analysis is based on historical data and may not accurately predict future market behavior. Always consult with a financial advisor before making investment decisions.
```
