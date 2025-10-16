from datetime import time

# --- Define locations ---
locations = [
      {"name": "Naperville Metra", "lat": 41.779533, "lon": -88.146133},
      {"name": "Naperville Downtown", "lat": 41.767281, "lon": -88.155243},
      {"name": "Naperville East", "lat": 41.743500, "lon": -88.097485},
      {"name": "Chicago Union Station", "lat": 41.878679, "lon": -87.640132},
      {"name": "Mokena", "lat": 41.544891, "lon": -87.853366},
]

# --- Define time windows (local time) ---
time_windows = [
    (time(6, 30), time(9, 0)),      
    (time(17, 30), time(19, 0)), 
]

timewca = [
    (time(7, 30), time(8, 0)),      
    (time(17, 30), time(18, 0)), 
]
timewh = [
    (time(6, 30), time(7, 0)),
    (time(8, 20), time(9, 0)),      
    (time(15, 30), time(16, 0)), 
]
timewm = [
    (time(6, 30), time(7, 0)),      
    (time(18, 30), time(19, 0)), 
]
timewc = [
    (time(6, 30), time(7, 0)),  
    (time(8, 20), time(9, 0)),    
    (time(15, 30), time(16, 0)), 
]
timewmo = [
    (time(7, 30), time(9, 0)),      
    (time(16, 0), time(18, 0)), 
]

# --- Define thresholds ---
rain_threshold = 40
snow_threshold = 0.4  