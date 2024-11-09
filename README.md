# Reddit DM Automation Bot

## Overview
The **Reddit DM Automation Bot** is a straightforward yet powerful Python script that uses [**ReddAPI**](https://reddapi.online) to send automated messages on Reddit. With this bot, you can quickly send custom messages to multiple Reddit users using rotating proxies and multiple accounts, making large-scale messaging easier and more efficient.

With the help of [**ReddAPI**](https://reddapi.online), you can achieve high messaging success rates while adhering to Reddit’s guidelines. The setup includes random message selection, proxy management, and multithreaded execution, making it a flexible and efficient solution for outreach on Reddit.

Ready to get started? [**Subscribe to ReddAPI**](https://rapidapi.com/SeasonedCode/api/reddapi) and try it out for free!

## Prerequisites

To get the bot up and running, ensure you have the following:

1. **Python**: Make sure Python 3.7 or higher is installed on your machine. You can download it [here](https://www.python.org/downloads/).
2. **API Key**: Sign up at [ReddAPI](https://rapidapi.com/SeasonedCode/api/reddapi) to get your API key for Reddit API access.

## Getting Started

### Step 1: Clone or Download the Repository
- Clone the repo or download it as a ZIP file and extract it to your desired location.

### Step 2: Install Required Packages
- Open a terminal, navigate to the project folder, and install the required packages:

  ```bash
  pip install -r requirements.txt
  
### Step 3: Set Up API Configuration

1. Open `config.ini`
2. Replace `"API"` with your actual ReddAPI key.

### Step 4: Prepare Your Proxies, Messages, and Accounts

- **Proxies**: List your proxies in `data/proxies.txt`, one per line. For example:
  ```plaintext
  proxy1:port or username:password@ip:port
  proxy2:port
  
- **Messages**: Add messages to `data/msgs.txt`, one message per line. The bot will randomly select from these messages.

- **Accounts**: Add bearer tokens (one per line) to `data/accounts.txt` to allow the bot to rotate accounts when sending messages.

- **Usernames**: Add usernames to `data/usernames.txt`, one username per line, for the bot to message.

### Step 5: Run the Script
Start the bot by running:
```bash
  python main.py
```
The bot will send messages to each username, rotating proxies and accounts as configured.

## Output

- **Success Logs**: Successful DMs are logged in the console.
- **Error Logs**: Errors, such as invalid proxies or failed requests, are logged for troubleshooting.

## Important Notes

- **Proxy Validation**: Ensure proxies are correctly listed in `data/proxies.txt`.
- **Compliance**: Follow Reddit’s guidelines to prevent account suspension. Use this bot responsibly and respectfully.

## Troubleshooting

- **Invalid API Key**: Verify your ReddAPI key if you experience authorization errors.
- **Connection Issues**: Confirm that proxies are valid and review logs for any network-related errors.

## Support

For Support Joing our telegram group at: https://t.me/reddapi_support
