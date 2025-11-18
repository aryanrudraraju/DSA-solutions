"""

Homework 2

"""

def buy_and_hold(prices, start_index=0, starting_money=100.0):
    """
    Buy and hold strategy


    Parameters:
        prices (list): stock prices
        start_index (positive integer, optional): index from which to start the strategy
        starting_money (float, optional): starting cash position. Defaults to 100.0.

    Returns:
        list containing value of position using buy and hold strategy

    Example use:
    >>> res = buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5])
    >>> [round(x, 1) for x in res]
    [100.0, 75.0, 90.0, 115.0, 125.0]
    >>> [round(x, 2) for x in buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5], start_index=2)]
    [100.0, 100.0, 100.0, 127.78, 138.89]
    """
    # Your code here. Don't change anything above.
    if start_index >= len(prices):
        return []

    value = [starting_money] * start_index

    shares = starting_money / prices[start_index]
    value += [shares * price for price in prices[start_index:]]

    return value


def moving_average(prices, n):
    """
    Calculates n-period moving average of a list of floats/integers.

    Parameters:
        prices: list of values (ordered in time),
        n: integer moving-average parameter

    Returns:
        list with None for the first n-1 values in prices and the appropriate moving average for the rest

    Example use:
    >>> ma = moving_average([2,3,4,5,8,5,4,3,2,1], 3)
    >>> [round(m, 2) if m is not None else None for m in ma]
    [None, None, 3.0, 4.0, 5.67, 6.0, 5.67, 4.0, 3.0, 2.0]
    >>> moving_average([2,3,4,5,8,5,4,3,2,1], 2)
    [None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5]
    """
    # Your code here. Don't change anything above.
    ma = [None] * (n - 1)
    
    for i in range(n - 1, len(prices)):
        window = prices[i - n + 1 : i + 1]
        ma.append(sum(window) / n)
    
    return ma


def compare_mas(ma1, ma2):
    """
    Compare two moving averages.

    Compares values in ma1 and ma2 pairwise to create a list of indicators such that
    - If ma1 > ma2, indicator = 1
    - Otherwise indicator = 0
    - The moving averages may contain None-values in the beginning. If either value is None, the indicator is None

    Parameters:
        ma1 (list): moving average (list of prices)
        ma2 (list): moving average (list of prices)

    Returns:
        list: binary indicators for which moving average value is greater

    Example use:
    >>> p1 = [1, 2, 4, 5]
    >>> p2 = [0, 2.5, 5, 3]
    >>> compare_mas(p1, p2)
    [1, 0, 0, 1]
    >>> p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
    >>> p2 = [None, None, 3.0, 4.0, 4.33, 4.0, 3.0, 2.0, 3.0, 2.66]
    >>> compare_mas(p1, p2)
    [None, None, 1, 1, 1, 0, 0, 0, 1, 1]
    """
    # Your code here. Don't change anything above.
    if len(ma1) != len(ma2):
        return []

    result = []
    for i in range(len(ma1)):
        if ma1[i] is None or ma2[i] is None:
            result.append(None)
        elif ma1[i] > ma2[i]:
            result.append(1)
        else:
            result.append(0)

    return result

def ma_strategy(prices, comparisons, starting_cash=100.0):
    """
    Trade based on moving average crossovers

    Parameters:
        prices: list if stock prices
        comparisons: list of comparisons from compare_mas
        starting_cash (float, optional): Starting cash position, defaults to 100.0.

    Returns:
        list of values of the current position: either cash position or the market value of stock position
    
    We initially hold cash, and buy when we first get a signal to buy.

    More specifically, a change from value 0 to 1 in comparisons signals there's a crossover in moving averages, so we want to buy stock. A move from 1 to 0 signals that we want to sell stock.

    Whenever we trade, we buy with our entire cash position, or sell our entire stock position.
    We will therefore always hold either stock or cash, but never both.
    
    Assume we can hold fractional stock quantities, and there are no transaction fees.

    Example use:
    >>> starting_cash = 1.0
    >>> prices = [2,4,6,5,1]
    >>> cos = [0, 1, 1, 0, 0] # not real indicators, just to illustrate portfolio value when trading
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> values
    [1.0, 1.0, 1.5, 1.25, 1.25]
    >>> starting_cash = 1000.0
    >>> prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
    >>> cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> [round(v, 2) for v in values] # round every value of the returned list using list comprehension
    [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
    """
    # Your code here. Don't change anything above.
    value = []
    cash = starting_cash
    stock_quantity = 0
    has_stock = False

    for i in range(len(prices)):
        current_price = prices[i]
        signal = comparisons[i]

        if signal is None:
            if has_stock:
                value.append(stock_quantity * current_price)
            else:
                value.append(cash)
            continue

        if i > 0 and comparisons[i - 1] == 0 and signal == 1 and not has_stock:
            stock_quantity = cash / current_price
            cash = 0
            has_stock = True

        elif i > 0 and comparisons[i - 1] == 1 and signal == 0 and has_stock:
            cash = stock_quantity * current_price
            stock_quantity = 0
            has_stock = False

        if has_stock:
            value.append(stock_quantity * current_price)
        else:
            value.append(cash)

    return value


def trading_floor(visits, option=2):
    """
    Produce summary statistics of trading desk utilisation.

    Parameters:
        visits: list of visits (see also HTML instructions):
            Each visit is a tuple (desk number (str), trader ID (str), time (str)) (all elements are integers in string format)
            Each trader starts outside any desk, and they leave all desks at the end of the day.
            The visits are not necessarily in chronological order.
        option (int, optional): determines what to return, see below
            
    Returns:
        a list containing tuples for each trading desk (sorted in increasing order by desk number (1, 2, 3, ...)):
        - if option = 0, (desk number, number of distinct traders)
        - if option = 1, (desk number, number of distinct traders, average visit duration)
        - if option = 2, (desk number, number of distinct traders, average visit duration, longest total time spent at the desk by a single trader)
        - the average visit duration is rounded to the nearest minute.

    Example use:
    >>> visits = [('0', '0', '20'), ('0', '0', '25'), ('1', '1', '74'), ('1', '1', '2')]
    >>> trading_floor(visits)
    [('0', 1, 5, 5), ('1', 1, 72, 72)]
    >>> trading_floor(visits, 0)
    [('0', 1), ('1', 1)]
    >>> trading_floor(visits, 1)
    [('0', 1, 5), ('1', 1, 72)]
    >>> trading_floor(visits, 1)[0]
    ('0', 1, 5)
    >>> visits = [('15', '3', '61'), ('15', '3', '45'), ('6', '0', '91'), ('10', '4', '76'), ('6', '0', '86'), ('6', '4', '2'), ('10', '1', '47'), ('6', '3', '17'), ('6', '4', '41'), ('15', '3', '36'), ('6', '2', '97'), ('15', '4', '58'), ('6', '0', '16'), ('10', '2', '21'), ('10', '4', '75'), ('6', '0', '76'), ('15', '4', '50'), ('10', '1', '64'), ('6', '3', '3'), ('15', '3', '35'), ('6', '2', '96'), ('10', '2', '35'), ('10', '2', '77'), ('10', '2', '48')]
    >>> trading_floor(visits)
    [('6', 4, 24, 65), ('10', 3, 15, 43), ('15', 2, 8, 17)]
    """
    # Your code here. Don't change anything above.
    desk_data = {}

    for desk, trader, time in visits:
        if desk not in desk_data:
            desk_data[desk] = {}
        
        if trader not in desk_data[desk]:
            desk_data[desk][trader] = []
        
        desk_data[desk][trader].append(int(time))

    results = []
    
    for desk in sorted(desk_data.keys(), key=int):
        trader_count = len(desk_data[desk])
        all_durations = []
        trader_totals = {}
        
        for trader, times in desk_data[desk].items():
            times.sort()
            total_duration = 0
            
            for i in range(0, len(times), 2):
                if i+1 < len(times):
                    duration = times[i+1] - times[i]
                    all_durations.append(duration)
                    total_duration += duration
            
            trader_totals[trader] = total_duration

        avg_duration = round(sum(all_durations) / len(all_durations)) if all_durations else 0
        max_trader_time = max(trader_totals.values()) if trader_totals else 0
        
        if option == 0:
            results.append((desk, trader_count))
        elif option == 1:
            results.append((desk, trader_count, avg_duration))
        else:
            results.append((desk, trader_count, avg_duration, max_trader_time))
    
    return results
