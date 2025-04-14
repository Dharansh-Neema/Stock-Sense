news_response = """
symbol='AAPL' 
stock_name='AAPL' 
headline=['Asian tech stocks bounce back after Trump tariff exemptions', 
'Tariffs on imported semiconductor chips coming soon, Trump says', 
'Taiwan tech supply chain stocks bounce back after Trump tariff exemptions',
 'Apple: Tariffs Are Another Nail In The Weak Growth Story', 
 'Trump says chips from China will face national security probe; further tariffs expected', 
 'Wall Street Brunch: Tariffs For Some', 'ClearBridge Large Cap Growth ESG Strategy Q1 2025 Commentary',
   'PFM: Dividend Growth ETF With High Fees And Average Result', 
   'ClearBridge Appreciation ESG Strategy Q1 2025 Commentary', 
   'US Commerce Secretary says exempted electronic products to come under separate tariffs', 
   "SCHD's Portfolio Shake-Up: What It Means For Investors (Rating Downgrade)", 
   'Taiwan Semiconductor Earnings Preview: Despite Risks And Headwinds, Valuation Remains Attractive', 
   'Apple Gains From Trump Tariff Reversal, But Is Still Too Pricey', 
   'Trump Exempts Some Electronics, Including Smartphones, From Tariffs on China', 
   'Apple, Nvidia Score Relief From US Tariffs With Exemptions', 
   'Apple, Nvidia, Dell, and Others Get a Tariffs Exemption Under New Rules', 
   "Apple, Nvidia, and Microsoft can 'breathe a huge sigh of relief' after Trump's China tariff exemptions", 
   'Jim Cramer On Apple Inc. (AAPL): “Own Apple, Don’t Trade It!”', 
   'US exempts smartphones from reciprocal tariffs, seen as positive for Apple', 
   'Smartphones and computers are now exempt from Trump’s latest tariffs',
    "Trump administration says it will exclude some electronics from 'reciprocal' tariffs", 'Apple has experienced significant volatility
"""

graph_output="""
{
     "symbol": "AAPL",
    "price_data": [
        {
            "time": "2025-04-11 13:30:00",
            "close": 188.26
        },
        {
            "time": "2025-04-11 13:35:00",
            "close": 190.24
        },
        {
            "time": "2025-04-11 13:40:00",
            "close": 190.73
        },
        {
            "time": "2025-04-11 13:45:00",
            "close": 191.4
        },
        {
            "time": "2025-04-11 13:50:00",
            "close": 192.7
        },
        {
            "time": "2025-04-11 13:55:00",
            "close": 191.55
        },
        {
            "time": "2025-04-11 14:00:00",
            "close": 191.38
        },
        {
            "time": "2025-04-11 14:05:00",
            "close": 192.49
        },
        {
            "time": "2025-04-11 14:10:00",
            "close": 191.46
        },
        {
            "time": "2025-04-11 14:15:00",
            "close": 190.65
        },
        {
            "time": "2025-04-11 14:20:00",
            "close": 190.33
        },
        {
            "time": "2025-04-11 14:25:00",
            "close": 189.93
        },
        {
            "time": "2025-04-11 14:30:00",
            "close": 191.71
        },
        {
            "time": "2025-04-11 14:35:00",
            "close": 192.02
        },
        {
            "time": "2025-04-11 14:40:00",
            "close": 192.93
        },
        {
            "time": "2025-04-11 14:45:00",
            "close": 193.55
        },
        {
            "time": "2025-04-11 14:50:00",
            "close": 193.03
        },
        {
            "time": "2025-04-11 14:55:00",
            "close": 192.28
        },
        {
            "time": "2025-04-11 15:00:00",
            "close": 192.31
        },
        {
            "time": "2025-04-11 15:05:00",
            "close": 193.66
        },
        {
            "time": "2025-04-11 15:10:00",
            "close": 192.73
        },
        {
            "time": "2025-04-11 15:15:00",
            "close": 192.36
        },
        {
            "time": "2025-04-11 15:20:00",
            "close": 192.52
        },
        {
            "time": "2025-04-11 15:25:00",
            "close": 193.32
        },
        {
            "time": "2025-04-11 15:30:00",
            "close": 193.59
        },
        {
            "time": "2025-04-11 15:35:00",
            "close": 194.68
        },
        {
            "time": "2025-04-11 15:40:00",
            "close": 194.63
        },
        {
            "time": "2025-04-11 15:45:00",
            "close": 194.96
        },
        {
            "time": "2025-04-11 15:50:00",
            "close": 194.78
        },
        {
            "time": "2025-04-11 15:55:00",
            "close": 195.64
        },
        {
            "time": "2025-04-11 16:00:00",
            "close": 196.57
        },
        {
            "time": "2025-04-11 16:05:00",
            "close": 196.22
        },
        {
            "time": "2025-04-11 16:10:00",
            "close": 195.86
        },
        {
            "time": "2025-04-11 16:15:00",
            "close": 197.01
        },
        {
            "time": "2025-04-11 16:20:00",
            "close": 196.1
        },
        {
            "time": "2025-04-11 16:25:00",
            "close": 195.8
        },
        {
            "time": "2025-04-11 16:30:00",
            "close": 197.26
        },
        {
            "time": "2025-04-11 16:35:00",
            "close": 197.51
        },
        {
            "time": "2025-04-11 16:40:00",
            "close": 197.8
        },
        {
            "time": "2025-04-11 16:45:00",
            "close": 199.04
        },
        {
            "time": "2025-04-11 16:50:00",
            "close": 199.17
        },
        {
            "time": "2025-04-11 16:55:00",
            "close": 198.47
        },
        {
            "time": "2025-04-11 17:00:00",
            "close": 198.34
        },
        {
            "time": "2025-04-11 17:05:00",
            "close": 198.37
        },
        {
            "time": "2025-04-11 17:10:00",
            "close": 198.16
        },
        {
            "time": "2025-04-11 17:15:00",
            "close": 197.63
        },
        {
            "time": "2025-04-11 17:20:00",
            "close": 197.26
        },
        {
            "time": "2025-04-11 17:25:00",
            "close": 196.83
        },
        {
            "time": "2025-04-11 17:30:00",
            "close": 196.55
        },
        {
            "time": "2025-04-11 17:35:00",
            "close": 197.79
        },
        {
            "time": "2025-04-11 17:40:00",
            "close": 199.16
        },
        {
            "time": "2025-04-11 17:45:00",
            "close": 198.52
        },
        {
            "time": "2025-04-11 17:50:00",
            "close": 198.67
        },
        {
            "time": "2025-04-11 17:55:00",
            "close": 198.26
        },
        {
            "time": "2025-04-11 18:00:00",
            "close": 198.13
        },
        {
            "time": "2025-04-11 18:05:00",
            "close": 197.97
        },
        {
            "time": "2025-04-11 18:10:00",
            "close": 198.21
        },
        {
            "time": "2025-04-11 18:15:00",
            "close": 197.54
        },
        {
            "time": "2025-04-11 18:20:00",
            "close": 197.55
        },
        {
            "time": "2025-04-11 18:25:00",
            "close": 197.58
        },
        {
            "time": "2025-04-11 18:30:00",
            "close": 197.76
        },
        {
            "time": "2025-04-11 18:35:00",
            "close": 197.93
        },
        {
            "time": "2025-04-11 18:40:00",
            "close": 198.2
        },
        {
            "time": "2025-04-11 18:45:00",
            "close": 198.34
        },
        {
            "time": "2025-04-11 18:50:00",
            "close": 198.04
        },
        {
            "time": "2025-04-11 18:55:00",
            "close": 197.54
        },
        {
            "time": "2025-04-11 19:00:00",
            "close": 198.2
        },
        {
            "time": "2025-04-11 19:05:00",
            "close": 198.5
        },
        {
            "time": "2025-04-11 19:10:00",
            "close": 198.6
        },
        {
            "time": "2025-04-11 19:15:00",
            "close": 198.6
        },
        {
            "time": "2025-04-11 19:20:00",
            "close": 198.84
        },
        {
            "time": "2025-04-11 19:25:00",
            "close": 198.34
        },
        {
            "time": "2025-04-11 19:30:00",
            "close": 198.25
        },
        {
            "time": "2025-04-11 19:35:00",
            "close": 197.98
        },
        {
            "time": "2025-04-11 19:40:00",
            "close": 198.1
        },
        {
            "time": "2025-04-11 19:45:00",
            "close": 198.04
        },
        {
            "time": "2025-04-11 19:50:00",
            "close": 198.81
        },
        {
            "time": "2025-04-11 19:55:00",
            "close": 198.02
        }
    ],
    "volume_data": [
        {
            "time": "2025-04-11 13:30:00",
            "volume": 4890768
        },
        {
            "time": "2025-04-11 13:35:00",
            "volume": 1622041
        },
        {
            "time": "2025-04-11 13:40:00",
            "volume": 1446893
        },
        {
            "time": "2025-04-11 13:45:00",
            "volume": 1248605
        },
        {
            "time": "2025-04-11 13:50:00",
            "volume": 1417228
        },
        {
            "time": "2025-04-11 13:55:00",
            "volume": 990585
        },
        {
            "time": "2025-04-11 14:00:00",
            "volume": 1310267
        },
        {
            "time": "2025-04-11 14:05:00",
            "volume": 1038847
        },
        {
            "time": "2025-04-11 14:10:00",
            "volume": 847444
        },
        {
            "time": "2025-04-11 14:15:00",
            "volume": 688630
        },
        {
            "time": "2025-04-11 14:20:00",
            "volume": 973104
        },
        {
            "time": "2025-04-11 14:25:00",
            "volume": 736015
        },
        {
            "time": "2025-04-11 14:30:00",
            "volume": 1030588
        },
        {
            "time": "2025-04-11 14:35:00",
            "volume": 699817
        },
        {
            "time": "2025-04-11 14:40:00",
            "volume": 869763
        },
        {
            "time": "2025-04-11 14:45:00",
            "volume": 979970
        },
        {
            "time": "2025-04-11 14:50:00",
            "volume": 796882
        },
        {
            "time": "2025-04-11 14:55:00",
            "volume": 665948
        },
        {
            "time": "2025-04-11 15:00:00",
            "volume": 888298
        },
        {
            "time": "2025-04-11 15:05:00",
            "volume": 878417
        },
        {
            "time": "2025-04-11 15:10:00",
            "volume": 960976
        },
        {
            "time": "2025-04-11 15:15:00",
            "volume": 677250
        },
        {
            "time": "2025-04-11 15:20:00",
            "volume": 662416
        },
        {
            "time": "2025-04-11 15:25:00",
            "volume": 668345
        },
        {
            "time": "2025-04-11 15:30:00",
            "volume": 593281
        },
        {
            "time": "2025-04-11 15:35:00",
            "volume": 763767
        },
        {
            "time": "2025-04-11 15:40:00",
            "volume": 764018
        },
        {
            "time": "2025-04-11 15:45:00",
            "volume": 1066156
        },
        {
            "time": "2025-04-11 15:50:00",
            "volume": 770726
        },
        {
            "time": "2025-04-11 15:55:00",
            "volume": 862281
        },
        {
            "time": "2025-04-11 16:00:00",
            "volume": 1106545
        },
        {
            "time": "2025-04-11 16:05:00",
            "volume": 1931928
        },
        {
            "time": "2025-04-11 16:10:00",
            "volume": 1078967
        },
        {
            "time": "2025-04-11 16:15:00",
            "volume": 1003318
        },
        {
            "time": "2025-04-11 16:20:00",
            "volume": 700217
        },
        {
            "time": "2025-04-11 16:25:00",
            "volume": 785085
        },
        {
            "time": "2025-04-11 16:30:00",
            "volume": 871441
        },
        {
            "time": "2025-04-11 16:35:00",
            "volume": 994494
        },
        {
            "time": "2025-04-11 16:40:00",
            "volume": 707494
        },
        {
            "time": "2025-04-11 16:45:00",
            "volume": 1237562
        },
        {
            "time": "2025-04-11 16:50:00",
            "volume": 1321787
        },
        {
            "time": "2025-04-11 16:55:00",
            "volume": 1010517
        },
        {
            "time": "2025-04-11 17:00:00",
            "volume": 715901
        },
        {
            "time": "2025-04-11 17:05:00",
            "volume": 667846
        },
        {
            "time": "2025-04-11 17:10:00",
            "volume": 573801
        },
        {
            "time": "2025-04-11 17:15:00",
            "volume": 769673
        },
        {
            "time": "2025-04-11 17:20:00",
            "volume": 718231
        },
        {
            "time": "2025-04-11 17:25:00",
            "volume": 683772
        },
        {
            "time": "2025-04-11 17:30:00",
            "volume": 834074
        },
        {
            "time": "2025-04-11 17:35:00",
            "volume": 802463
        },
        {
            "time": "2025-04-11 17:40:00",
            "volume": 1277990
        },
        {
            "time": "2025-04-11 17:45:00",
            "volume": 868381
        },
        {
            "time": "2025-04-11 17:50:00",
            "volume": 621559
        },
        {
            "time": "2025-04-11 17:55:00",
            "volume": 614635
        },
        {
            "time": "2025-04-11 18:00:00",
            "volume": 639534
        },
        {
            "time": "2025-04-11 18:05:00",
            "volume": 558388
        },
        {
            "time": "2025-04-11 18:10:00",
            "volume": 547202
        },
        {
            "time": "2025-04-11 18:15:00",
            "volume": 507949
        },
        {
            "time": "2025-04-11 18:20:00",
            "volume": 498277
        },
        {
            "time": "2025-04-11 18:25:00",
            "volume": 433571
        },
        {
            "time": "2025-04-11 18:30:00",
            "volume": 338314
        },
        {
            "time": "2025-04-11 18:35:00",
            "volume": 487243
        },
        {
            "time": "2025-04-11 18:40:00",
            "volume": 448390
        },
        {
            "time": "2025-04-11 18:45:00",
            "volume": 485441
        },
        {
            "time": "2025-04-11 18:50:00",
            "volume": 485261
        },
        {
            "time": "2025-04-11 18:55:00",
            "volume": 374921
        },
        {
            "time": "2025-04-11 19:00:00",
            "volume": 511855
        },
        {
            "time": "2025-04-11 19:05:00",
            "volume": 653095
        },
        {
            "time": "2025-04-11 19:10:00",
            "volume": 502071
        },
        {
            "time": "2025-04-11 19:15:00",
            "volume": 634150
        },
        {
            "time": "2025-04-11 19:20:00",
            "volume": 606591
        },
        {
            "time": "2025-04-11 19:25:00",
            "volume": 702411
        },
        {
            "time": "2025-04-11 19:30:00",
            "volume": 806211
        },
        {
            "time": "2025-04-11 19:35:00",
            "volume": 783067
        },
        {
            "time": "2025-04-11 19:40:00",
            "volume": 762926
        },
        {
            "time": "2025-04-11 19:45:00",
            "volume": 827283
        },
        {
            "time": "2025-04-11 19:50:00",
            "volume": 1799570
        },
        {
            "time": "2025-04-11 19:55:00",
            "volume": 4640429
        }
}

"""