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
    # Calculate month-over-month growth rates
    growth_rates = np.diff(monthly_revenue) / monthly_revenue[:-1] * 100
    
    # Calculate 12-month moving average (trend)
    window = 12
    weights = np.ones(window) / window
    trend = np.convolve(monthly_revenue, weights, mode='valid')
    
    # Pad trend to match original length
    pad_start = window // 2
    pad_end = window - 1 - pad_start
    trend = np.pad(trend, (pad_start, pad_end), mode='edge')
    
    # Extract seasonality by subtracting trend
    seasonality = monthly_revenue - trend
    
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
    # Calculate average growth rate
    growth_rates = np.diff(historical_revenue) / historical_revenue[:-1]
    avg_growth_rate = np.mean(growth_rates)
    
    # Calculate seasonal factors (assume 12-month seasonality)
    n_seasons = len(historical_revenue) // 12
    seasonal_pattern = np.zeros(12)
    for i in range(12):
        seasonal_pattern[i] = np.mean(historical_revenue[i::12])
    seasonal_pattern = seasonal_pattern - np.mean(seasonal_pattern)
    
    # Project trend forward
    last_value = historical_revenue[-1]
    trend = last_value * (1 + avg_growth_rate) ** np.arange(1, months_ahead + 1)
    
    # Add seasonal factors
    seasonal_indices = np.arange(len(historical_revenue), 
                               len(historical_revenue) + months_ahead) % 12
    forecast = trend + seasonal_pattern[seasonal_indices]
    
    return forecast


print(analyze_revenue_trends(revenue))
print(forecast_revenue(revenue, 12))
