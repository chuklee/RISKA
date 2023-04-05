class agent:
    def __init__(self, dataframe_train, parameters, cash, id, df):
        self.id = id # Represent the id of the agent
        self.dataframe_train = dataframe_train # Represent the dataframe of the currency
        self.parameters = parameters # Represent the parameters of the agent
        self.cash = cash # Represent the cash of the agent
        self.total = cash # Represent the total cash and trade of the agent
        self.buying = 0 #If > 0, the agent is buying at the price buying
        self.df = df
        self.indice = 0 # Represent the indice of the dataframe
        self.cash_test = cash
        self.total_test = cash

    def trade(self):
        # Trade with the agent
        sell_or_buy = 0
        #print(self.id)
        columns_length = len(self.dataframe_train.columns)
        for i in range(len(self.dataframe_train)):
            for j in range(columns_length):
                sell_or_buy += self.parameters[j] * self.dataframe_train.iloc[i][j] # Define if the agent buy or sell
            if sell_or_buy > 0 and self.buying == 0 and self.cash > 0:
                self.buy()
            elif sell_or_buy < 0 and self.buying > 0:
                self.sell()
            sell_or_buy = 0
            self.indice += 1

    
    def buy(self):
        # Buy with the agent
        self.cash = 0
        self.buying = self.df.iloc[self.indice][0]


    def sell(self):
        # Sell with the agent
        self.cash = ((self.total / self.buying) * self.df.iloc[self.indice][0]) * 0.97
        self.total = self.cash
        self.buying = 0
     
    def test(self, parts, normal):
        self.buying = 0
        self.indice = 0
        columns_length = len(parts[0].columns)
        for i in range(len(parts)):
            sell_or_buy = 0
            for j in range(len(parts[i])):
                for k in range(columns_length):
                    sell_or_buy += self.parameters[k] * parts[i].iloc[j][k]
                if sell_or_buy > 0 and self.buying == 0 and self.cash_test > 0:
                    self.buy_test(normal[i])
                elif sell_or_buy < 0 and self.buying > 0:
                    self.sell_test(normal[i])
                sell_or_buy = 0
                self.indice += 1
            self.indice = 0

            
    def buy_test(self, df):
        self.cash_test = 0
        self.buying = df.iloc[self.indice][0]
    
    def sell_test(self, df):
        self.cash_test = ((self.total_test / self.buying) * df.iloc[self.indice][0]) * 0.97
        self.total_test = self.cash_test
        self.buying = 0