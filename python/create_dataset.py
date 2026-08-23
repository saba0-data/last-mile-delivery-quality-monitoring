import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# --------------------------------------------------
# 1. Reproducibility
# --------------------------------------------------

np.random.seed(42)
random.seed(42)

# --------------------------------------------------
# 2. Basic configuration
# --------------------------------------------------

NUM_RECORDS = 10000

# Indian cities for the synthetic dataset
cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi",
    "Kolkata",
    "Ahmedabad"
]

# Approximate city coordinates
city_coordinates = {
    "Hyderabad": (17.3850, 78.4867),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Mumbai": (19.0760, 72.8777),
    "Pune": (18.5204, 73.8567),
    "Delhi": (28.6139, 77.2090),
    "Kolkata": (22.5726, 88.3639),
    "Ahmedabad": (23.0225, 72.5714)
}

delivery_statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Failed",
    "Returned"
]

address_quality_options = [
    "Good",
    "Good",
    "Good",
    "Good",
    "Poor"
]

route_status_options = [
    "Normal"
]
# --------------------------------------------------
# 3. Generate base delivery records
# --------------------------------------------------

records = []

start_date = datetime(2026, 1, 1)

for i in range(NUM_RECORDS):

    order_id = f"ORD{i + 1:06d}"
    driver_id = f"DRV{random.randint(1, 250):04d}"

    city = random.choice(cities)

    base_lat, base_lon = city_coordinates[city]

    # Generate coordinates around the city
    latitude = round(base_lat + np.random.normal(0, 0.05), 6)
    longitude = round(base_lon + np.random.normal(0, 0.05), 6)

    delivery_date = start_date + timedelta(
        days=random.randint(0, 180)
    )

    pincode = str(random.randint(500000, 799999))

    delivery_status = random.choice(delivery_statuses)

    attempt_count = random.choices(
        [1, 2, 3],
        weights=[75, 20, 5]
    )[0]

    sla_minutes = random.choice([
        30, 45, 60, 90, 120
    ])

    delivery_time = random.randint(
    max(10, int(sla_minutes * 0.5)),
    max(10, int(sla_minutes * 0.95))
    )

    customer_rating = round(
        np.random.uniform(2.5, 5.0),
        1
    )

    address_quality = random.choice(
        address_quality_options
    )

    route_status = random.choice(
        route_status_options
    )

    records.append([
        order_id,
        driver_id,
        delivery_date.strftime("%Y-%m-%d"),
        city,
        pincode,
        latitude,
        longitude,
        delivery_status,
        attempt_count,
        delivery_time,
        sla_minutes,
        customer_rating,
        address_quality,
        route_status
    ])

# --------------------------------------------------
# 4. Create DataFrame
# --------------------------------------------------

columns = [
    "Order_ID",
    "Driver_ID",
    "Delivery_Date",
    "City",
    "Pincode",
    "Latitude",
    "Longitude",
    "Delivery_Status",
    "Attempt_Count",
    "Delivery_Time_Minutes",
    "SLA_Minutes",
    "Customer_Rating",
    "Address_Quality",
    "Route_Status"
]

df = pd.DataFrame(records, columns=columns)

# --------------------------------------------------
# 5. Inject intentional data-quality issues
# --------------------------------------------------

# 5% missing addresses
missing_address_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.05),
    replace=False
)

df.loc[missing_address_indices, "Address_Quality"] = "Missing"

# 3% invalid latitude values
invalid_lat_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.03),
    replace=False
)

df.loc[invalid_lat_indices, "Latitude"] = np.random.choice(
    [-95, 95, 150, -150],
    size=len(invalid_lat_indices)
)

# 3% invalid longitude values
invalid_lon_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.03),
    replace=False
)

df.loc[invalid_lon_indices, "Longitude"] = np.random.choice(
    [-200, 200, 250, -250],
    size=len(invalid_lon_indices)
)

# 5% SLA breaches
sla_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.05),
    replace=False
)

df.loc[sla_indices, "Delivery_Time_Minutes"] = (
    df.loc[sla_indices, "SLA_Minutes"] +
    np.random.randint(10, 90, size=len(sla_indices))
)

# 3% excessive delivery attempts
attempt_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.03),
    replace=False
)

df.loc[attempt_indices, "Attempt_Count"] = np.random.choice(
    [4, 5, 6],
    size=len(attempt_indices)
)

# 3% low customer ratings
rating_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.03),
    replace=False
)

df.loc[rating_indices, "Customer_Rating"] = np.round(
    np.random.uniform(1.0, 2.4, size=len(rating_indices)),
    1
)

# 3% route anomalies
route_indices = np.random.choice(
    df.index,
    size=int(NUM_RECORDS * 0.03),
    replace=False
)

df.loc[route_indices, "Route_Status"] = "Anomaly"

# --------------------------------------------------
# 6. Create duplicate orders
# --------------------------------------------------

duplicate_indices = np.random.choice(
    df.index,
    size=100,
    replace=False
)

duplicates = df.loc[duplicate_indices].copy()

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# --------------------------------------------------
# 7. Save dataset
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

data_folder = project_root / "data"

data_folder.mkdir(
    exist_ok=True
)

output_file = data_folder / "delivery_data_raw.csv"

df.to_csv(
    output_file,
    index=False
)

# --------------------------------------------------
# 8. Display summary
# --------------------------------------------------

print("=" * 50)
print("LAST-MILE DELIVERY DATASET CREATED")
print("=" * 50)

print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"Saved to: {output_file}")

print("\nDataset preview:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nDelivery status distribution:")
print(df["Delivery_Status"].value_counts())

print("\nAddress quality distribution:")
print(df["Address_Quality"].value_counts())

print("\nRoute status distribution:")
print(df["Route_Status"].value_counts())

print("\nDataset creation completed successfully!")
