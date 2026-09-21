import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# Configuration
# -----------------------------
np.random.seed(42)
random.seed(42)

NUM_TRIPS = 10000

# -----------------------------
# Locations
# -----------------------------
locations = [
    ("L001", "Andheri", "West", 19.1197, 72.8468),
    ("L002", "Bandra", "West", 19.0607, 72.8362),
    ("L003", "Powai", "Central", 19.1176, 72.9060),
    ("L004", "Kurla", "Central", 19.0726, 72.8845),
    ("L005", "Thane", "North", 19.2183, 72.9781),
    ("L006", "Dadar", "Central", 19.0178, 72.8478),
    ("L007", "Borivali", "North", 19.2307, 72.8567),
    ("L008", "Ghatkopar", "Central", 19.0860, 72.9081),
    ("L009", "Vashi", "Navi Mumbai", 19.0771, 72.9988),
    ("L010", "Nerul", "Navi Mumbai", 19.0330, 73.0297),
    ("L011", "Airoli", "Navi Mumbai", 19.1590, 72.9986),
    ("L012", "Ghansoli", "Navi Mumbai", 19.1260, 73.0050),
]

# -----------------------------
# Drivers
# -----------------------------
drivers = [f"D{str(i).zfill(4)}" for i in range(1, 301)]

# -----------------------------
# Vehicles
# -----------------------------
vehicles = []

for i in range(1, 301):
    vehicles.append({
        "Vehicle_ID": f"V{str(i).zfill(4)}",
        "Vehicle_Type": random.choice(
            ["Hatchback", "Sedan", "SUV"]
        ),
        "Fuel_Type": random.choice(
            ["Petrol", "CNG", "Electric"]
        ),
        "Vehicle_Age": random.randint(1, 8)
    })

vehicle_df = pd.DataFrame(vehicles)

# -----------------------------
# Generate Trips
# -----------------------------
start_date = datetime(2026, 1, 1)

trip_data = []

for i in range(1, NUM_TRIPS + 1):

    trip_id = f"T{str(i).zfill(6)}"

    date = start_date + timedelta(
        days=random.randint(0, 180)
    )

    hour = random.choices(
        range(24),
        weights=[
            1, 1, 1, 1, 1, 2,
            4, 6, 7, 5, 4, 4,
            4, 4, 4, 5, 6, 8,
            10, 9, 7, 5, 3, 2
        ]
    )[0]

    minute = random.randint(0, 59)

    pickup_time = date.replace(
        hour=hour,
        minute=minute,
        second=0
    )

    pickup = random.choice(locations)
    drop = random.choice(locations)

    while drop[0] == pickup[0]:
        drop = random.choice(locations)

    driver_id = random.choice(drivers)
    vehicle_id = f"V{str(random.randint(1, 300)).zfill(4)}"

    status = random.choices(
        ["Completed", "Cancelled"],
        weights=[88, 12]
    )[0]

    distance = round(
        np.random.gamma(shape=2.2, scale=3.5),
        2
    )

    distance = min(max(distance, 1.0), 35.0)

    duration = round(
        distance * random.uniform(3.5, 6.5)
        + random.randint(5, 15)
    )

    fare = round(
        50 + distance * random.uniform(12, 20),
        2
    )

    payment_type = random.choice(
        ["UPI", "Cash", "Credit Card", "Debit Card", "Wallet"]
    )

    cancellation_reason = None

    if status == "Cancelled":
        cancellation_reason = random.choice([
            "Driver unavailable",
            "Customer cancelled",
            "Long waiting time",
            "Driver cancelled",
            "Wrong pickup location"
        ])

        fare = 0

    trip_data.append([
        trip_id,
        date.date(),
        pickup_time.strftime("%H:%M:%S"),
        pickup[0],
        pickup[1],
        drop[0],
        drop[1],
        driver_id,
        vehicle_id,
        status,
        fare,
        distance,
        duration,
        payment_type,
        cancellation_reason
    ])

# -----------------------------
# Create DataFrame
# -----------------------------
columns = [
    "Trip_ID",
    "Date",
    "Pickup_Time",
    "Pickup_Location_ID",
    "Pickup_Location",
    "Drop_Location_ID",
    "Drop_Location",
    "Driver_ID",
    "Vehicle_ID",
    "Trip_Status",
    "Fare",
    "Distance_KM",
    "Duration_Minutes",
    "Payment_Type",
    "Cancellation_Reason"
]

trips_df = pd.DataFrame(
    trip_data,
    columns=columns
)

# -----------------------------
# Save FactTrips
# -----------------------------
trips_df.to_csv(
    "Dataset/Raw/FactTrips.csv",
    index=False
)

# -----------------------------
# Save DimVehicle
# -----------------------------
vehicle_df.to_csv(
    "Dataset/Raw/DimVehicle.csv",
    index=False
)

# -----------------------------
# Create DimDriver
# -----------------------------
driver_data = []

for driver in drivers:

    driver_data.append([
        driver,
        round(random.uniform(3.5, 5.0), 2),
        f"V{str(random.randint(1, 300)).zfill(4)}",
        (
            start_date
            - timedelta(days=random.randint(30, 1500))
        ).date(),
        random.choice([
            "West",
            "Central",
            "North",
            "Navi Mumbai"
        ])
    ])

driver_df = pd.DataFrame(
    driver_data,
    columns=[
        "Driver_ID",
        "Driver_Rating",
        "Vehicle_ID",
        "Join_Date",
        "City_Zone"
    ]
)

driver_df.to_csv(
    "Dataset/Raw/DimDriver.csv",
    index=False
)

# -----------------------------
# Create DimLocation
# -----------------------------
location_df = pd.DataFrame(
    locations,
    columns=[
        "Location_ID",
        "Location_Name",
        "Zone",
        "Latitude",
        "Longitude"
    ]
)

location_df.to_csv(
    "Dataset/Raw/DimLocation.csv",
    index=False
)

print("Dataset generated successfully!")
print(f"Trips: {len(trips_df)}")
print(f"Drivers: {len(driver_df)}")
print(f"Vehicles: {len(vehicle_df)}")
print(f"Locations: {len(location_df)}")