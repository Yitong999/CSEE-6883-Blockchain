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
   python fecth_save_data.py
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

## Contributing

Feel free to submit issues and enhancement requests! 