import requests
import json

# Using public Solana mainnet endpoint
url = "https://api.mainnet-beta.solana.com"

# Using a well-known address that should have transaction history
# This is a popular Solana address (you can replace with any address you want to check)
address = "DpobReDm34nGXfGhDDRHhbgCXWNibUs7ZvmrmSECf4LT"

# Using standard Solana RPC method
payload = {
    "jsonrpc": "2.0",
    "method": "getSignaturesForAddress",
    "params": [
        address,
        {
            "limit": 5  # Reduced to 5 for cleaner output
        }
    ],
    "id": 1
}

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

try:
    print(f"Fetching transaction signatures for address: {address}")
    print(f"Using endpoint: {url}")
    print("-" * 60)
    
    response = requests.post(url, json=payload, headers=headers)
    print("Status Code:", response.status_code)
    
    if response.status_code == 200:
        result = response.json()
        if 'error' in result:
            print("API Error:", result['error'])
        else:
            print(f"Success! Found {len(result.get('result', []))} transaction signatures:")
            
            # Pretty print the JSON response
            if result.get('result'):
                for i, tx in enumerate(result['result'], 1):
                    print(f"\nTransaction {i}:")
                    print(f"  Signature: {tx.get('signature', 'N/A')}")
                    print(f"  Slot: {tx.get('slot', 'N/A')}")
                    print(f"  Block Time: {tx.get('blockTime', 'N/A')}")
                    print(f"  Confirmation Status: {tx.get('confirmationStatus', 'N/A')}")
                    if tx.get('err'):
                        print(f"  Error: {tx.get('err')}")
            else:
                print("No transactions found for this address.")
                
            print("\nFull JSON Response:")
            print(json.dumps(result, indent=2))
    else:
        print("HTTP Error:", response.status_code)
        print(response.text)
        
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except Exception as e:
    print("An error occurred:", e)