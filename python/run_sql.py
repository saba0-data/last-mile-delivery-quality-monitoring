import sqlite3
from pathlib import Path

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

database_file = (
    project_root /
    "data" /
    "delivery_quality.db"
)

connection = sqlite3.connect(database_file)

cursor = connection.cursor()


# --------------------------------------------------
# QUERY 1 — TOTAL DELIVERIES
# --------------------------------------------------

query = """
SELECT
    COUNT(*) AS total_deliveries,
    SUM(
        CASE
            WHEN Exception_Flag = 'Yes'
            THEN 1
            ELSE 0
        END
    ) AS total_exceptions
FROM delivery_quality;
"""

cursor.execute(query)

result = cursor.fetchone()

total_deliveries = result[0]
total_exceptions = result[1]
print("=" * 60)
print("SQL QUALITY ANALYSIS")
print("=" * 60)

print("\n1. OVERALL QUALITY METRICS")




print("Total deliveries:", total_deliveries)

print("Total exceptions:", total_exceptions)

exception_rate = (
    total_exceptions / total_deliveries
) * 100

print(
    f"Exception rate: {exception_rate:.2f}%"
)

# --------------------------------------------------
# QUERY 2 — CITY LEVEL QUALITY ANALYSIS
# --------------------------------------------------

query = """
SELECT
    City,
    COUNT(*) AS total_deliveries,
    SUM(
        CASE
            WHEN Exception_Flag = 'Yes'
            THEN 1
            ELSE 0
        END
    ) AS total_exceptions,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN Exception_Flag = 'Yes'
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS exception_rate
FROM delivery_quality
GROUP BY City
ORDER BY exception_rate DESC;
"""

cursor.execute(query)

city_results = cursor.fetchall()

print("\n" + "=" * 60)
print("2. CITY-LEVEL QUALITY ANALYSIS")
print("=" * 60)

print(
    f"{'City':<15}"
    f"{'Deliveries':>12}"
    f"{'Exceptions':>12}"
    f"{'Rate %':>10}"
)

print("-" * 50)

for row in city_results:
    city = row[0]
    deliveries = row[1]
    exceptions = row[2]
    rate = row[3]

    print(
        f"{city:<15}"
        f"{deliveries:>12}"
        f"{exceptions:>12}"
        f"{rate:>10.2f}"
    )

# --------------------------------------------------
# QUERY 3 — DRIVER PERFORMANCE ANALYSIS
# --------------------------------------------------

query = """
SELECT
    Driver_ID,

    COUNT(*) AS total_deliveries,

    SUM(
        CASE
            WHEN Exception_Flag = 'Yes'
            THEN 1
            ELSE 0
        END
    ) AS total_exceptions,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN Exception_Flag = 'Yes'
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS exception_rate,

    SUM(
        CASE
            WHEN Exception_Type = 'SLA Breach'
            THEN 1
            ELSE 0
        END
    ) AS sla_breaches,

    ROUND(
        AVG(Customer_Rating),
        2
    ) AS avg_customer_rating

FROM delivery_quality

GROUP BY Driver_ID

HAVING total_deliveries >= 20

ORDER BY exception_rate DESC

LIMIT 10;
"""

cursor.execute(query)

driver_results = cursor.fetchall()

print("\n" + "=" * 70)
print("3. TOP 10 DRIVERS BY EXCEPTION RATE")
print("=" * 70)

print(
    f"{'Driver':<12}"
    f"{'Deliveries':>12}"
    f"{'Exceptions':>12}"
    f"{'Rate %':>10}"
    f"{'SLA':>8}"
    f"{'Rating':>10}"
)

print("-" * 70)

for row in driver_results:

    driver = row[0]
    deliveries = row[1]
    exceptions = row[2]
    exception_rate = row[3]
    sla_breaches = row[4]
    rating = row[5]

    print(
        f"{driver:<12}"
        f"{deliveries:>12}"
        f"{exceptions:>12}"
        f"{exception_rate:>10.2f}"
        f"{sla_breaches:>8}"
        f"{rating:>10.2f}"
    )

# --------------------------------------------------
# QUERY 4 — SLA PERFORMANCE
# --------------------------------------------------

query = """
SELECT

    COUNT(*) AS total_deliveries,

    SUM(
        CASE
            WHEN Delivery_Time_Minutes <= SLA_Minutes
            THEN 1
            ELSE 0
        END
    ) AS sla_met,

    SUM(
        CASE
            WHEN Delivery_Time_Minutes > SLA_Minutes
            THEN 1
            ELSE 0
        END
    ) AS sla_breached,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN Delivery_Time_Minutes <= SLA_Minutes
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS sla_compliance_rate

FROM delivery_quality;
"""

cursor.execute(query)

sla_result = cursor.fetchone()

print("\n" + "=" * 60)
print("4. SLA PERFORMANCE")
print("=" * 60)

print(
    "Total deliveries:",
    sla_result[0]
)

print(
    "SLA met:",
    sla_result[1]
)

print(
    "SLA breached:",
    sla_result[2]
)

print(
    f"SLA compliance rate: "
    f"{sla_result[3]:.2f}%"
)

# --------------------------------------------------
# QUERY 5 — EXCEPTION TYPE ANALYSIS
# --------------------------------------------------

query = """
SELECT
    Exception_Type,
    COUNT(*) AS exception_count,

    ROUND(
        100.0 * COUNT(*) /
        (
            SELECT COUNT(*)
            FROM delivery_quality
            WHERE Exception_Flag = 'Yes'
        ),
        2
    ) AS exception_percentage

FROM delivery_quality

WHERE Exception_Flag = 'Yes'

GROUP BY Exception_Type

ORDER BY exception_count DESC;
"""

cursor.execute(query)

exception_results = cursor.fetchall()

print("\n" + "=" * 65)
print("5. EXCEPTION TYPE ANALYSIS")
print("=" * 65)

print(
    f"{'Exception Type':<30}"
    f"{'Count':>12}"
    f"{'Percentage':>15}"
)

print("-" * 65)

for row in exception_results:

    exception_type = row[0]
    count = row[1]
    percentage = row[2]

    print(
        f"{exception_type:<30}"
        f"{count:>12}"
        f"{percentage:>14.2f}%"
    )

# --------------------------------------------------
# QUERY 6 — PRIORITY ESCALATION ANALYSIS
# --------------------------------------------------

query = """
SELECT
    Severity,
    COUNT(*) AS exception_count,

    ROUND(
        100.0 * COUNT(*) /
        (
            SELECT COUNT(*)
            FROM delivery_quality
            WHERE Exception_Flag = 'Yes'
        ),
        2
    ) AS percentage

FROM delivery_quality

WHERE Exception_Flag = 'Yes'

GROUP BY Severity

ORDER BY
    CASE Severity
        WHEN 'Critical' THEN 1
        WHEN 'High' THEN 2
        WHEN 'Medium' THEN 3
        WHEN 'Low' THEN 4
        ELSE 5
    END;
"""

cursor.execute(query)

severity_results = cursor.fetchall()

print("\n" + "=" * 60)
print("6. PRIORITY ESCALATION ANALYSIS")
print("=" * 60)

print(
    f"{'Severity':<15}"
    f"{'Exceptions':>15}"
    f"{'Percentage':>15}"
)

print("-" * 45)

for row in severity_results:

    severity = row[0]
    count = row[1]
    percentage = row[2]

    print(
        f"{severity:<15}"
        f"{count:>15}"
        f"{percentage:>14.2f}%"
    )

# --------------------------------------------------
# CLOSE CONNECTION
# --------------------------------------------------

connection.close()
