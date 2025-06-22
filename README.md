# 🌟 Solana Staking Rewards to Koinly CSV

> **Free, open-source tool to fetch your Solana staking rewards and convert them to CSV format for tax reporting with Koinly**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Koderalus/SolanaStakingRewards.svg?style=social&label=Star)](https://github.com/Koderalus/SolanaStakingRewards)
[![GitHub forks](https://img.shields.io/github/forks/Koderalus/SolanaStakingRewards.svg?style=social&label=Fork)](https://github.com/Koderalus/SolanaStakingRewards/fork)

## 🚀 What This Does

**TL;DR**: Automatically finds all your Solana staking rewards and exports them as a CSV file that Koinly (and other tax software) can understand. No more manual tracking! 

**Perfect for**:
- 📊 Tax season preparation
- 🔍 Tracking staking performance
- 💰 Portfolio management
- 🛡️ Audit trail creation

## ✨ Features

- 🔍 **Smart Epoch Processing**: Automatically detects and processes staking rewards from your Solana wallet
- 💾 **Local Database Storage**: Uses IndexedDB to store results locally, allowing incremental data building across sessions  
- 🔄 **Smart Retry System**: Automatically retries failed epochs with intelligent error categorization
- 🎯 **Manual Epoch Check**: Target specific epochs for checking (useful for finding missing rewards)
- 📊 **Multiple Time Ranges**: From recent epochs to full historical data
- 🌐 **Multiple RPC Endpoints**: Fallback system with Alchemy, Helius, and public Solana RPC endpoints
- 📈 **Real-time Progress**: Live status updates and progress tracking
- 🛑 **Stop/Resume**: Ability to stop long-running processes and resume later
- 📄 **Koinly CSV Export**: Direct export in Koinly-compatible format for tax reporting
- 🔒 **Privacy First**: All data stays in your browser - nothing sent to external servers
- 🆓 **Completely Free**: No subscriptions, no limits, open source

## 🎯 Quick Start

1. **Download**: Clone this repo or download `SolanaStaking.html`
2. **Open**: Open the HTML file in any modern web browser
3. **Enter**: Your Solana wallet address (the one that controls your stake accounts)
4. **Generate**: Click "Generate Report" and wait for processing
5. **Download**: Export your CSV for Koinly import

**That's it!** No installation, no setup, no API keys required (though recommended for better performance).

## 🛠️ How It Works

1. **Enter your Solana wallet address** (the withdrawer authority for your stake accounts)
2. **Select network** (Mainnet or Devnet)  
3. **Choose time range** or enter specific epochs manually
4. **Generate report** - the app will:
   - Find all stake accounts associated with your wallet
   - Scan epochs for staking rewards
   - Store results in local database
   - Display rewards in a table
5. **Download CSV** for import into Koinly

## 🧠 Smart Retry System

The application includes an intelligent retry system that:
- **Categorizes failures** by type (rate limits, network issues, RPC errors)
- **Tracks retry attempts** for each epoch
- **Automatically retries** failed epochs on subsequent runs
- **Provides manual retry** options for specific epochs  
- **Prevents data loss** due to temporary RPC issues

## 💾 Database Storage

- **Local Storage**: All data is stored locally in your browser using IndexedDB
- **Persistent**: Data survives browser restarts and is private to your browser
- **Incremental**: Only processes new/failed epochs, building your complete history over time
- **Location**: Browser → Developer Tools → Application → Storage → IndexedDB → SolanaRewardsDB

## 📁 Files

- `SolanaStaking.html` - Main application (single HTML file with embedded CSS/JS)
- `CursorChat.md` - Development log and conversation history

## ⚙️ Configuration

- **API Key**: Optional Alchemy API key for improved reliability and rate limits
- **Wallet Address**: Your Solana wallet public key (withdrawer authority)
- **Settings**: Saved automatically in browser localStorage

## 🔌 API Requirements

The application works with:
- **Alchemy API** (recommended - get free key at [alchemy.com](https://alchemy.com))
- **Public Solana RPC endpoints** (free but may have rate limits)
- **Helius RPC** (demo access available)

💡 **Pro tip**: Sign up for a free Alchemy account and use your API key for the best experience.

## 🌿 Branch Structure

- `main` - Production-ready releases
- `develop` - Development branch for integration  
- `feature/*` - Feature development branches (cleaned for security)

## 🔧 Technical Details

- **Frontend**: Pure HTML/CSS/JavaScript (no build process required)
- **Storage**: IndexedDB for local data persistence
- **API**: Solana JSON-RPC for blockchain data
- **Export**: CSV format compatible with Koinly tax software

## 🤝 Contributing

We welcome contributions! 

1. Fork the repository
2. Create a feature branch from `develop`
3. Make your changes
4. Submit a pull request to `develop`

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

- 🐛 **Issues**: [Open an issue](https://github.com/Koderalus/SolanaStakingRewards/issues) on GitHub
- 📖 **Documentation**: Check `CursorChat.md` for development history and troubleshooting
- 💬 **Discussions**: Use GitHub Discussions for questions and feature requests

## 🌟 Show Your Support

If this tool helped you with your Solana tax reporting, consider:
- ⭐ Starring this repository
- 🍴 Forking for your own modifications  
- 📢 Sharing with the Solana community
- 🐛 Reporting bugs or suggesting features

---

**Made with ❤️ for the Solana community** | **Built with security and privacy in mind** 