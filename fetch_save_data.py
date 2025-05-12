import requests
import pandas as pd

# GraphQL query
query = """
{
  orderFulfillments(first: 1000) {
    id
    offerer
    recipient
    price
    transactionHash
    blockTimestamp
  }
}
"""

# Subgraph endpoint
SUBGRAPH_URL = "https://api.studio.thegraph.com/query/110798/6883-seaport-test/v0.2.2"

# Fetch data
response = requests.post(SUBGRAPH_URL, json={"query": query})

if response.status_code != 200:
    raise Exception(f"GraphQL query failed: {response.text}")

print("Status code:", response.status_code)
data = response.json()["data"]["orderFulfillments"]
df = pd.DataFrame(data)

# Convert timestamps and prices
df["blockTimestamp"] = pd.to_datetime(df["blockTimestamp"], unit='s')
df["price"] = pd.to_numeric(df["price"], errors='coerce')

# Calculate price in ETH (assuming price is in Wei)
df["price_eth"] = df["price"] / 1e18

# Drop any rows with NaN values
df = df.dropna()

# Save to CSV
df.to_csv("opensea_sales.csv", index=False)
print("✅ Data saved to opensea_sales.csv")
print(f"Total transactions processed: {len(df)}")
print(f"Price range: {df['price_eth'].min():.4f} to {df['price_eth'].max():.4f} ETH")