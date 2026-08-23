import pandas as pd
import sqlite3
from pathlib import Path

# Project root
project_root = Path(__file__).resolve().parent.parent

# File paths
csv_file = project_root / "data" / "quality_audit_results.csv"
database_file = project_root / "data" / "delivery_quality.db"

# Load audit data
df = pd.read_csv(csv_file)

# Connect to SQLite
connection = sqlite3.connect(database_file)

# Create table
df.to_sql(
    "delivery_quality",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("=" * 60)
print("DATABASE CREATED SUCCESSFULLY")
print("=" * 60)

print(f"\nRecords loaded: {len(df)}")
print(f"Columns loaded: {len(df.columns)}")

print("\nDatabase:")
print(database_file)

print("\nTable:")
print("delivery_quality")