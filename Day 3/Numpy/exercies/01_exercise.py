import numpy as np

np.random.seed(42)
base = np.linspace(100000, 200000, 24)  # 2 years of data
seasonal = 50000 * np.sin(np.arange(24) * 2 * np.pi / 12)
noise = np.random.normal(0, 10000, 24)
revenue = base + seasonal + noise


def analyze_revenue_trends(monthly_revenue):
    """
    Analyze revenue trends and calculate key metrics.
    
    Args:
        monthly_revenue: NumPy array of monthly revenue values
    
    Returns:
        tuple: (growth_rates, seasonality, trend)
    """
    # TODO: Calculate month-over-month growth rates
    # Hint: Use np.diff() and array operations
    growth_rates = None
    
    # TODO: Extract seasonality by subtracting 12-month moving average
    # Hint: Use np.convolve() for moving average
    seasonality = None
    
    # TODO: Calculate linear trend
    # Hint: Use np.linspace() and basic array operations
    trend = None
    
    return growth_rates, seasonality, trend


def forecast_revenue(historical_revenue, months_ahead):
    """
    Forecast revenue for future months using historical data.
    
    Args:
        historical_revenue: NumPy array of historical monthly revenue
        months_ahead: Number of months to forecast
    
    Returns:
        array: Forecasted revenue values
    """
    # TODO: Implement simple forecasting using trend and seasonality
    # 1. Calculate average growth rate
    # 2. Project trend forward
    # 3. Add seasonal factors
    # Hint: Use array operations and broadcasting
    
    forecast = None
    
    return forecast

print(analyze_revenue_trends(revenue))
