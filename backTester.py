# -*- coding: utf-8 -*-
"""
main back-testing script
Created on Wed May  5 18:15:23 2021
@author: keill
"""

"""
Gets data from yfinance
    -> this will need the ticker, interval and date range.
    -> will give it a single stock to check and backtest so that
    later we can just call this class multiple times to cover multiple watch lists

Need a way for it to use a strategy and to call it from another class
what sort of data will be given to the strategy ect
back tester should just give OCHL data one at a time until the strat tells it otherwise
backtester will keep track of the open position of the stock and the value and number 
of stock


might have to manually import the file name of strategy
 strategy class which stores data and analyses it

"""
import matplotlib.pyplot as plt
import pandas as pd
from StockData import StockData
from DadsStrategy import DadsStrategy
from Plotter import Plotter

class BackTester:

    """
    BackTester todo:
        - Need to impliment the ability to send stuff to broker, like quantity and amount
        - Need to write some more stategies
    
    """    
    
    def __init__(self,data):
        """
        Expecting to take a StockData object and run the backtest on it
        """
        self.data = data
        self.position = {'long':False, 'short':False, 'quantity':0, 'makePrice':None}
        self.profit = {'value':1000}
        self.buySignals = []
        self.sellSignals = []
        self.strategy = DadsStrategy()
        self.plotter = Plotter(self.data)
        return

        
    def run(self):
        for indexs, row in self.data.marketData.iterrows():
            #Need to make this able to integrate with a broker where it will send
            #buy or sell signals
            self.strategy.update(Open  = row['Open'],
                            Close = row['Close'],
                            Low   = row['Low'],
                            High  = row['High'])
            signal = self.strategy.signal()
            if signal == 'buy':
                #append into buySignals
                self.buySignals.append([len(self.strategy.Ks)-1,self.strategy.Ks[-1]])
                if self.position['long']==False:
                    #Check to see an open position exists
                    self.buy('max', indexs)
                    
            elif signal == 'sell':
                #append into sellSignals
                self.sellSignals.append([len(self.strategy.Ks)-1,self.strategy.Ks[-1]])
                if self.position['long'] == True:
                    #Check to see if an open position exists
                    self.sell('all',indexs)      
        return
    
    def buy(self,quant,indexs):
        #Update the backtester position dict
        #Send a signal to a broker
        #will assume to buy at the next open
        self.position['makePrice']=\
            self.data.marketData['Open'][self.data.marketData.index.get_loc(str(indexs))+1]
        self.position['long'] = True
        
        return
    
    def sell(self,quant,indexs):
        #Uses next open as buy amount
        percentChange = (self.data.marketData['Open'][self.data.marketData.index.get_loc(str(indexs))+1]-self.position['makePrice'])/(self.position['makePrice'])
        self.profit['value'] *=1+percentChange
        self.position['long']=False
        self.position['makePrice'] = None
        print(percentChange*100)
        
        return
    
    
    
if __name__ =='__main__':
    """
    Plotting to do:
        - Want to have a large amount of the plotting done in the strat class.
        - This should just pass through relavant data and the strat plots
        the specific type of plot needed.
        - Have it set up so that depending on the interval the bounds thing
        changes with it
        - Title at the top of the page outlines the ticker and interval info
        as well as the strat being used
    """
    sampleData = StockData('AAPL')
    sampleData.get_market_data(period='1y',
                               interval ="1d")
    
    sampleTester = BackTester(sampleData)
    sampleTester.run()
    sampleTester.plotter.addEMA(20)
    #sampleTester.plotter.addEMA(2)
    #sampleTester.plotter.addTrendLines(10)
    #sampleTester.plotter.addRSI(14,30,70)
    sampleTester.plotter.addStochOsil(14,30,70)
    sampleTester.plotter.plotIndicators()

    #print(sampleTester.data.sckOpen)
    #print(sampleTester.profit['value'])
    

    