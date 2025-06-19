# Solana Staking Rewards to Koinly CSV

A web-based application that fetches Solana staking rewards and exports them in Koinly-compatible CSV format for tax reporting.

## Features

- 🔍 **Smart Epoch Processing**: Automatically detects and processes staking rewards from your Solana wallet
- 💾 **Local Database Storage**: Uses IndexedDB to store results locally, allowing incremental data building across sessions
- 🔄 **Smart Retry System**: Automatically retries failed epochs with intelligent error categorization
- 🎯 **Manual Epoch Check**: Target specific epochs for checking (useful for finding missing rewards)
- 📊 **Multiple Time Ranges**: From recent epochs to full historical data
- 🌐 **Multiple RPC Endpoints**: Fallback system with Alchemy, Helius, and public Solana RPC endpoints
- 📈 **Real-time Progress**: Live status updates and progress tracking
- 🛑 **Stop/Resume**: Ability to stop long-running processes and resume later
- 📄 **Koinly CSV Export**: Direct export in Koinly-compatible format for tax reporting

## How It Works

1. **Enter your Solana wallet address** (the withdrawer authority for your stake accounts)
2. **Select network** (Mainnet or Devnet)
3. **Choose time range** or enter specific epochs manually
4. **Generate report** - the app will:
   - Find all stake accounts associated with your wallet
   - Scan epochs for staking rewards
   - Store results in local database
   - Display rewards in a table
5. **Download CSV** for import into Koinly

## Smart Retry System

The application includes an intelligent retry system that:
- **Categorizes failures** by type (rate limits, network issues, RPC errors)
- **Tracks retry attempts** for each epoch
- **Automatically retries** failed epochs on subsequent runs
- **Provides manual retry** options for specific epochs
- **Prevents data loss** due to temporary RPC issues

## Database Storage

- **Local Storage**: All data is stored locally in your browser using IndexedDB
- **Persistent**: Data survives browser restarts and is private to your browser
- **Incremental**: Only processes new/failed epochs, building your complete history over time
- **Location**: Browser → Developer Tools → Application → Storage → IndexedDB → SolanaRewardsDB

## Files

- `SolanaStaking.html` - Main application (single HTML file with embedded CSS/JS)
- `CursorChat.md` - Development log and conversation history

## Usage

1. Open `SolanaStaking.html` in your web browser
2. (Optional) Enter your Alchemy API key for better reliability
3. Enter your Solana wallet public key
4. Configure your preferred settings
5. Click "Generate Report"
6. Download the CSV when complete

## Configuration

- **API Key**: Optional Alchemy API key for improved reliability and rate limits
- **Wallet Address**: Your Solana wallet public key (withdrawer authority)
- **Settings**: Saved automatically in browser localStorage

## API Requirements

The application works with:
- **Alchemy API** (essential - get free key at [alchemy.com](https://alchemy.com))
- **Public Solana RPC endpoints** (free but may have rate limits)
- **Helius RPC** (demo access available)

Sign up for a free Alchemy account and use your API key.

## Branch Structure

- `main` - Production-ready releases
- `develop` - Development branch for integration
- `feature/*` - Feature development branches

## Technical Details

- **Frontend**: Pure HTML/CSS/JavaScript (no build process required)
- **Storage**: IndexedDB for local data persistence
- **API**: Solana JSON-RPC for blockchain data
- **Export**: CSV format compatible with Koinly tax software

## Contributing

1. Fork the repository
2. Create a feature branch from `develop`
3. Make your changes
4. Submit a pull request to `develop`

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on GitHub or check the `CursorChat.md` file for development history and troubleshooting information. 