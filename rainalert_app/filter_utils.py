import pandas as pd
from datetime import time
from typing import List, Tuple

def filter_weather(
    df: pd.DataFrame,
    time_windows: List[Tuple[time, time]],
    rain_threshold: float = 40,
    snow_threshold: float = None
) -> pd.DataFrame:
    """
    Filter weather DataFrame for given time windows and probability thresholds.

    Args:
        df (pd.DataFrame): DataFrame from get_weather_data()
        time_windows (List[Tuple[time, time]]): List of (start_time, end_time) tuples
        rain_threshold (float): Minimum rain probability (%) to keep
        snow_threshold (float, optional): Minimum snow probability (%) to keep

    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    if df.empty:
        return pd.DataFrame()

    # Ensure local_time column exists
    df = df.copy()
    df["local_time"] = df["time"].dt.time

    # Create mask for time windows
    mask = pd.Series(False, index=df.index)
    for start, end in time_windows:
        mask |= df["local_time"].between(start, end)

    # Apply rain threshold
    rain_mask = df["rain_probability(%)"] >= rain_threshold

    # Apply snow threshold if provided
    if snow_threshold is not None:
        snow_mask = df["snowfall(mm)"] >= snow_threshold
        combined_mask = mask & (rain_mask | snow_mask)
    else:
        combined_mask = mask & rain_mask

    filtered_df = df[combined_mask].copy()

    # Sort by time for clarity
    filtered_df.sort_values(by=["time"], inplace=True)
    filtered_df.reset_index(drop=True, inplace=True)
    return filtered_df
