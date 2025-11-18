# Intraday prices (15min interval) on 27 January 2025
aapl = [
   226.75, 225.66, 225.19, 227.30, 227.88, 227.81, 227.83, 228.49, 229.60,
   228.42, 229.14, 230.08, 230.30, 230.16, 230.67, 231.32, 231.35, 231.48,
   231.15, 232.04, 231.20, 231.58, 231.01, 230.68, 230.88, 229.99
]

nvda = [
   126.89, 126.88, 124.58, 124.03, 124.57, 123.00, 121.60, 119.15, 118.50,
   120.25, 120.17, 119.76, 119.98, 118.50, 118.84, 117.87, 119.13, 117.83,
   117.83, 118.81, 117.63, 117.92, 117.99, 117.77, 118.39, 118.52
]

def count_bull_traps(prices):
    """Count bull traps in a list of prices
    
    Bull trap is identified  by:
    - price rise
    - price declines to the new daily low later
    """

    #Counter variable
    traps = 0

    for i in range(1, len(prices) - 1):
        
        if prices[i] > prices[i - 1]:
            
            low_before = min(prices[:i])
            low_after = min(prices[i + 1:])
            if low_after < low_before:
                traps += 1

    return traps

print("NVDA Traps:", count_bull_traps(nvda))
print("AAPL Traps:", count_bull_traps(aapl))
            