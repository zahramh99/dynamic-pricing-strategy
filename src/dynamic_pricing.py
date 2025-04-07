import numpy as np

def calculate_dynamic_pricing(data):
    """Calculate dynamic pricing based on demand and supply"""
    # Calculate demand multipliers
    high_demand_percentile = 75
    low_demand_percentile = 25
    
    data['demand_multiplier'] = np.where(
        data['Number_of_Riders'] > np.percentile(data['Number_of_Riders'], high_demand_percentile),
        data['Number_of_Riders'] / np.percentile(data['Number_of_Riders'], high_demand_percentile),
        data['Number_of_Riders'] / np.percentile(data['Number_of_Riders'], low_demand_percentile)
    )
    
    # Calculate supply multipliers
    high_supply_percentile = 75
    low_supply_percentile = 25
    
    data['supply_multiplier'] = np.where(
        data['Number_of_Drivers'] > np.percentile(data['Number_of_Drivers'], low_supply_percentile),
        np.percentile(data['Number_of_Drivers'], high_supply_percentile) / data['Number_of_Drivers'],
        np.percentile(data['Number_of_Drivers'], low_supply_percentile) / data['Number_of_Drivers']
    )
    
    # Define thresholds
    demand_threshold_high = 1.2
    demand_threshold_low = 0.8
    supply_threshold_high = 0.8
    supply_threshold_low = 1.2
    
    # Calculate adjusted price
    data['adjusted_ride_cost'] = data['Historical_Cost_of_Ride'] * (
        np.maximum(data['demand_multiplier'], demand_threshold_low) *
        np.maximum(data['supply_multiplier'], supply_threshold_high)
    )
    
    return data