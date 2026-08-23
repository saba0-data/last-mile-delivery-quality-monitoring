import pandas as pd
from pathlib import Path

# Find the project folder
project_root = Path(__file__).resolve().parent.parent

# Location of the raw dataset
data_file = project_root / "data" / "delivery_data_raw.csv"

# Load the dataset
df = pd.read_csv(data_file)

print("=" * 60)
print("LAST-MILE DELIVERY QUALITY AUDIT")
print("=" * 60)

print("\n1. Dataset shape:")
print(df.shape)

print("\n2. Column names:")
print(df.columns.tolist())

print("\n3. First 5 records:")
print(df.head())

print("\n4. Missing values:")
print(df.isnull().sum())

print("\n5. Duplicate Order IDs:")
print(df["Order_ID"].duplicated().sum())

print("\n6. Data types:")
print(df.dtypes)



# --------------------------------------------------
# QUALITY AUDIT RULES
# --------------------------------------------------

print("\n" + "=" * 60)
print("QUALITY AUDIT RESULTS")
print("=" * 60)

# Rule 1: Duplicate orders
duplicate_orders = df["Order_ID"].duplicated().sum()

print("\nRule 1 - Duplicate Orders:")
print(f"Duplicate records: {duplicate_orders}")


# Rule 2: Invalid latitude
invalid_latitude = (
    (df["Latitude"] < -90) |
    (df["Latitude"] > 90)
).sum()

print("\nRule 2 - Invalid Latitude:")
print(f"Invalid latitude records: {invalid_latitude}")


# Rule 3: Invalid longitude
invalid_longitude = (
    (df["Longitude"] < -180) |
    (df["Longitude"] > 180)
).sum()

print("\nRule 3 - Invalid Longitude:")
print(f"Invalid longitude records: {invalid_longitude}")


# Rule 4: Missing address
missing_address = (
    df["Address_Quality"] == "Missing"
).sum()

print("\nRule 4 - Missing Address:")
print(f"Missing address records: {missing_address}")


# Rule 5: SLA breach
sla_breach = (
    df["Delivery_Time_Minutes"] >
    df["SLA_Minutes"]
).sum()

print("\nRule 5 - SLA Breach:")
print(f"SLA breach records: {sla_breach}")


# Rule 6: Excessive delivery attempts
excessive_attempts = (
    df["Attempt_Count"] > 3
).sum()

print("\nRule 6 - Excessive Attempts:")
print(f"Excessive attempt records: {excessive_attempts}")


# Rule 7: Low customer rating
low_rating = (
    df["Customer_Rating"] < 2.5
).sum()

print("\nRule 7 - Low Customer Rating:")
print(f"Low rating records: {low_rating}")


# Rule 8: Route anomaly
route_anomaly = (
    df["Route_Status"] == "Anomaly"
).sum()

print("\nRule 8 - Route Anomaly:")
print(f"Route anomaly records: {route_anomaly}")


# --------------------------------------------------
# EXCEPTION DETECTION
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXCEPTION DETECTION")
print("=" * 60)


def identify_exception(row):
    """
    Identify the main quality/operational issue
    for each delivery record.
    """

    # Check for invalid geographical coordinates
    if row["Latitude"] < -90 or row["Latitude"] > 90:
        return "Geocode Issue"

    if row["Longitude"] < -180 or row["Longitude"] > 180:
        return "Geocode Issue"

    # Check for missing address
    if row["Address_Quality"] == "Missing":
        return "Address Issue"

    # Check for SLA breach
    if row["Delivery_Time_Minutes"] > row["SLA_Minutes"]:
        return "SLA Breach"

    # Check for excessive attempts
    if row["Attempt_Count"] > 3:
        return "Driver/Attempt Issue"

    # Check for route anomaly
    if row["Route_Status"] == "Anomaly":
        return "Route Issue"

    # Check for low customer rating
    if row["Customer_Rating"] < 2.5:
        return "Customer Experience Issue"

    # No issue found
    return "No Exception"


# Apply the exception detection rules
df["Exception_Type"] = df.apply(
    identify_exception,
    axis=1
)


# --------------------------------------------------
# EXCEPTION FLAG
# --------------------------------------------------

df["Exception_Flag"] = df["Exception_Type"].apply(
    lambda x: "Yes" if x != "No Exception" else "No"
)


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

print("\nException distribution:")

print(
    df["Exception_Type"]
    .value_counts()
)


print("\nTotal exceptions:")

total_exceptions = (
    df["Exception_Flag"] == "Yes"
).sum()

print(total_exceptions)


print("\nException rate:")

exception_rate = (
    total_exceptions / len(df)
) * 100

print(f"{exception_rate:.2f}%")




# --------------------------------------------------
# SAVE AUDIT RESULTS
# --------------------------------------------------

audit_file = (
    project_root /
    "data" /
    "quality_audit_results.csv"
)

df.to_csv(
    audit_file,
    index=False
)

print("\nAudit results saved to:")
print(audit_file)




# --------------------------------------------------
# SEVERITY CLASSIFICATION
# --------------------------------------------------

def assign_severity(exception_type):

    severity_map = {
        "Geocode Issue": "Critical",
        "Address Issue": "High",
        "SLA Breach": "High",
        "Driver/Attempt Issue": "Medium",
        "Route Issue": "Medium",
        "Customer Experience Issue": "High",
        "No Exception": "None"
    }

    return severity_map.get(
        exception_type,
        "Medium"
    )


df["Severity"] = df["Exception_Type"].apply(
    assign_severity
)


# --------------------------------------------------
# RECOMMENDED ACTION
# --------------------------------------------------

def recommended_action(exception_type):

    action_map = {
        "Geocode Issue":
            "Review and correct coordinates",

        "Address Issue":
            "Verify delivery address",

        "SLA Breach":
            "Escalate to operations",

        "Driver/Attempt Issue":
            "Investigate delivery attempts",

        "Route Issue":
            "Review route assignment",

        "Customer Experience Issue":
            "Investigate customer issue",

        "No Exception":
            "No action required"
    }

    return action_map.get(
        exception_type,
        "Review exception"
    )


df["Recommended_Action"] = df[
    "Exception_Type"
].apply(
    recommended_action
)


# --------------------------------------------------
# DISPLAY SEVERITY SUMMARY
# --------------------------------------------------

print("\nSeverity distribution:")

print(
    df["Severity"]
    .value_counts()
)


print("\nRecommended action distribution:")

print(
    df["Recommended_Action"]
    .value_counts()
)


# --------------------------------------------------
# SAVE FINAL AUDIT DATA
# --------------------------------------------------

df.to_csv(
    audit_file,
    index=False
)

print("\nFinal audit dataset saved successfully!")




# --------------------------------------------------
# IDENTIFY ALL EXCEPTIONS
# --------------------------------------------------

def identify_all_exceptions(row):

    issues = []

    if row["Latitude"] < -90 or row["Latitude"] > 90:
        issues.append("Geocode Issue")

    if row["Longitude"] < -180 or row["Longitude"] > 180:
        issues.append("Geocode Issue")

    if row["Address_Quality"] == "Missing":
        issues.append("Address Issue")

    if row["Delivery_Time_Minutes"] > row["SLA_Minutes"]:
        issues.append("SLA Breach")

    if row["Attempt_Count"] > 3:
        issues.append("Driver/Attempt Issue")

    if row["Route_Status"] == "Anomaly":
        issues.append("Route Issue")

    if row["Customer_Rating"] < 2.5:
        issues.append("Customer Experience Issue")

    if len(issues) == 0:
        return "No Exception"

    # Remove duplicate issue names
    issues = list(dict.fromkeys(issues))

    return "; ".join(issues)


df["All_Exceptions"] = df.apply(
    identify_all_exceptions,
    axis=1
)




# --------------------------------------------------
# CREATE EXCEPTION QUEUE
# --------------------------------------------------

exceptions_df = df[
    df["Exception_Flag"] == "Yes"
].copy()

# Select the most useful columns for an analyst
exception_columns = [
    "Order_ID",
    "Driver_ID",
    "Delivery_Date",
    "City",
    "Pincode",
    "Delivery_Status",
    "Attempt_Count",
    "Delivery_Time_Minutes",
    "SLA_Minutes",
    "Customer_Rating",
    "Address_Quality",
    "Route_Status",
    "Exception_Type",
    "Severity",
    "Recommended_Action"
]

exceptions_df = exceptions_df[
    exception_columns
]

# --------------------------------------------------
# SORT BY SEVERITY
# --------------------------------------------------

severity_order = {
    "Critical": 1,
    "High": 2,
    "Medium": 3,
    "Low": 4,
    "None": 5
}

exceptions_df["Severity_Rank"] = (
    exceptions_df["Severity"]
    .map(severity_order)
)

exceptions_df = exceptions_df.sort_values(
    by="Severity_Rank"
)

# Remove helper column
exceptions_df = exceptions_df.drop(
    columns=["Severity_Rank"]
)

# --------------------------------------------------
# SAVE EXCEPTION QUEUE
# --------------------------------------------------

exception_file = (
    project_root /
    "data" /
    "delivery_exceptions.csv"
)

exceptions_df.to_csv(
    exception_file,
    index=False
)

# --------------------------------------------------
# EXCEPTION QUEUE SUMMARY
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXCEPTION QUEUE")
print("=" * 60)

print(
    f"\nTotal exception records: {len(exceptions_df)}"
)

print("\nExceptions by severity:")
print(
    exceptions_df["Severity"]
    .value_counts()
)

print("\nExceptions by type:")
print(
    exceptions_df["Exception_Type"]
    .value_counts()
)

print("\nException queue saved to:")
print(exception_file)