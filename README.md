
# RISKA

## Authors

- [@chuklee](https://github.com/chuklee)


## Project Overview

This code is a simple trading bot that uses an agent-based approach to trade on financial markets. The bot is written in Python and uses the following libraries:

- pandas
- json
- binance

The bot uses a set of technical indicators to make buy and sell decisions, and it is trained on historical data. The bot tries to maximize its profit while minimizing its risk.

## Getting Started
To use the trading bot, you need to run the **riska.py** script. Before running the script, you need to make sure that you have the necessary libraries installed. You can install the libraries using pip:
```bash
    pip install pandas
    pip install python-binance
```
To run the script, use the following command:
```bash
    python riska.py
```
And also save your credentials for the binance api into a json file name **credentials.json** in the root project folder. With this format:
```json
{
    "api_key": "TOSET",
    "api_secret": "TOSET"
}
```
The script will train the trading bot on historical data and save the parameters of the best agent in a parameters.json file.

## Files
The code consists of three files:
- **riska.py**: This file contains the main code for the trading bot. It loads the historical data, trains the agents, and saves the parameters of the best agent.
- **agent.py**: This file contains the **agent** class, which represents an agent that trades on the financial market.
- **get_data.py**: This Python file contains functions to retrieve cryptocurrency data from Binance, create a Pandas DataFrame, add technical indicators to the data, and save the resulting DataFrame to a CSV file. The file imports the following modules.

## Parameters
The riska.py file contains several parameters that you can adjust to change the behavior of the trading bot:

- **cut**: The number of parts to split the data into. The bot will train an agent on each part.
- **cash**: The amount of cash that the agent starts with.
- **nb_agents**: The number of agents to use in the training process.
- **generation_nb**: The number of generations to train the agents.


## Disclaimer
This trading bot is provided for educational purposes only. It should not be used for real trading without proper testing and validation. The author of this code is not responsible for any losses that may result from using this trading bot.