import requests
import pandas as pd

def get_weather_data(lat: float, lon: float, location_name: str) -> pd.DataFrame:
    """
    Fetch 15-minute weather forecast data from Open-Meteo API for a given location.

    Args:
        lat (float): Latitude of location.
        lon (float): Longitude of location.
        location_name (str): Name of the location (for labeling).

    Returns:
        pd.DataFrame: DataFrame containing timestamps, rain/snow probabilities, and precipitation.
    """

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude={lat}&longitude={lon}"
        "&minutely_15=precipitation_probability,precipitation,snowfall"
        "&forecast_days=1&timezone=auto"
    ).format(lat=lat, lon=lon)

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        minutely = data.get("minutely_15", {})
        if not minutely or "time" not in minutely:
            print(f"⚠️ No forecast data for {location_name}")
            return pd.DataFrame()

        df = pd.DataFrame({
            "time": pd.to_datetime(minutely["time"]),
            "rain_probability(%)": minutely.get("precipitation_probability", [0]*len(minutely["time"])),
            "snowfall(mm)": minutely.get("snowfall", [0]*len(minutely["time"])),
        })
        
        df["location"] = location_name
        return df

    except Exception as e:
        print(f"❌ Error fetching data for {location_name}: {e}")
        return pd.DataFrame()
