import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment")

# Initialize client
client = OpenAI(api_key=api_key)

# Read transaction data
df = pd.read_csv("opensea_sales.csv")

# Read prompt
with open("nft_trend_analysis_prompt.txt", "r") as f:
    prompt = f.read()

# Prepare data summary
data_summary = f"""
Data Summary:
Total transactions: {len(df)}
Time range: {df['blockTimestamp'].min()} to {df['blockTimestamp'].max()}
Price range: {df['price_eth'].min():.4f} to {df['price_eth'].max():.4f} ETH
Average price: {df['price_eth'].mean():.4f} ETH

First 10 transactions:
{df.head(10).to_string()}
"""

# Combine prompt
full_prompt = prompt + "\n\n" + data_summary

# Create chat completion (v1-style)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert NFT market analyst."},
        {"role": "user", "content": full_prompt}
    ],
    temperature=0.7
)

# Write result to file
with open("nft_market_analysis.txt", "w") as f:
    f.write(response.choices[0].message.content)

print("✅ Analysis saved to nft_market_analysis.txt")
