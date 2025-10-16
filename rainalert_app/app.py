import streamlit as st
import pandas as pd
from datetime import time
from config import (locations, time_windows, timewm,
                    timewca, timewh, timewc, timewmo,
                    rain_threshold, snow_threshold)
from weather_fetch import get_weather_data
from filter_utils import filter_weather
from email_utils import send_email_alert


def main():
    st.set_page_config(page_title="Weather Alert Dashboard", layout="wide")
    st.title("🌧️ ❄️ ChicagoLand Weather Alert Dashboard")

    all_alerts = []

    for loc in locations:
        st.subheader(f"📍 {loc['name']}")
        df = get_weather_data(loc["lat"], loc["lon"], loc["name"])
        
        #time based on location
        if loc["name"] == "Naperville Metra":
            time_windows = timewm
        elif loc["name"] == "Naperville Downtown":
            time_windows = timewc
        elif loc["name"] == "Naperville East":
            time_windows = timewh
        elif loc["name"] == "Chicago Union Station":
            time_windows = timewca
        elif loc["name"] == "Mokena":
            time_windows = timewmo
        
         # Filter for rain and snow alerts
        filtered = filter_weather(df, time_windows, rain_threshold)
        snow_alerts = df[(df["snowfall(mm)"] > snow_threshold)]
        combined = pd.concat([filtered, snow_alerts]).drop_duplicates()
        
        
        if not combined.empty:
            snownz_tval = df[df["snowfall(mm)"] >= snow_threshold][["time", "snowfall(mm)"]]
            rainnz_tval = df[df["rain_probability(%)"] >= rain_threshold][["time", "rain_probability(%)"]]
            if not snownz_tval.empty:
                st.warning(f" ❄️ Snow 🚨 Alerts At {loc['name']}:")
                st.dataframe(snownz_tval)
            if not rainnz_tval.empty:
                st.warning(f" 🌧️ Rain 🚨 Alerts At {loc['name']}:")
                st.dataframe(rainnz_tval)
            #st.dataframe(combined)
            all_alerts.append(combined)
        else:
            st.success(f"No Worries about Rain/Snow 🌧️ ❄️ Today At {loc['name']}.")

    # if all_alerts:
    #     final_df = pd.concat(all_alerts)
    #     st.download_button("📥 Download Alerts CSV", final_df.to_csv(index=False), file_name="alerts.csv")
    #     if st.button("📧 Send Email Alerts"):
    #         send_email_alert(final_df)
    # else:
    #     st.info("No alerts found across all locations.")

if __name__ == "__main__":
    main()
