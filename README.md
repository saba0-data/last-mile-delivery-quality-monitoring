#  Last-Mile Delivery Quality & Exception Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black)

A data quality and operational analytics project that simulates a
**last-mile delivery quality monitoring workflow** using **Python, SQL, SQLite, and Power BI**.

The project audits delivery records, identifies operational exceptions,
assigns severity levels, recommends corrective actions, performs SQL-based
analysis, and presents key findings through an interactive Power BI dashboard.

---

##  Dashboard Preview

![Last-Mile Delivery Quality Dashboard](screenshots/dashboard.png)

### Dashboard KPIs

| KPI | Result |
|---|---:|
| Total Deliveries | **10,100** |
| Total Exceptions | **2,304** |
| Exception Rate | **22.81%** |
| SLA Compliance | **95.00%** |

---

##  Business Problem

Last-mile delivery operations generate large volumes of transactional and
operational data.

Quality and operations teams need to identify:

- Address and geocoding problems
- SLA breaches
- Excessive delivery attempts
- Route anomalies
- Customer experience issues
- High-priority operational exceptions
- City-level quality differences
- Driver-level exception patterns

This project simulates a data-driven quality monitoring workflow to identify
these issues and prioritize corrective action.

---

##  Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **SQL**
- **SQLite**
- **Power BI**
- **Git & GitHub**

---

##  Project Workflow

```text
Raw Delivery Data
        ↓
Data Quality Audit
        ↓
Exception Detection
        ↓
Exception Classification
        ↓
Severity Assignment
        ↓
Recommended Action
        ↓
SQLite Database
        ↓
SQL Analysis
        ↓
Power BI Dashboard
```

---

##  Dataset

The project uses a synthetic last-mile delivery dataset containing:

- **10,100 delivery records**
- **14 original attributes**
- Driver information
- Delivery information
- Geographic information
- SLA information
- Customer ratings
- Address quality
- Route status

Additional analytical fields are generated during the quality-audit process.

### Original Dataset Columns

| Column | Description |
|---|---|
| `Order_ID` | Unique delivery order identifier |
| `Driver_ID` | Delivery driver identifier |
| `Delivery_Date` | Date of delivery |
| `City` | Delivery city |
| `Pincode` | Delivery location pincode |
| `Latitude` | Delivery latitude |
| `Longitude` | Delivery longitude |
| `Delivery_Status` | Delivery outcome |
| `Attempt_Count` | Number of delivery attempts |
| `Delivery_Time_Minutes` | Actual delivery time |
| `SLA_Minutes` | Target delivery time |
| `Customer_Rating` | Customer rating |
| `Address_Quality` | Address quality classification |
| `Route_Status` | Route status |

---

##  Data Quality Audit

The Python audit evaluates delivery records using multiple quality rules:

1. Duplicate orders
2. Invalid latitude
3. Invalid longitude
4. Missing addresses
5. SLA breaches
6. Excessive delivery attempts
7. Low customer ratings
8. Route anomalies

### Audit Results

| Metric | Result |
|---|---:|
| Records Audited | **10,100** |
| Total Exceptions | **2,304** |
| Exception Rate | **22.81%** |

---

##  Exception Analysis

Detected issues are classified into six operational categories.

| Exception Type | Count | Percentage |
|---|---:|---:|
| Geocode Issue | 599 | 26.00% |
| Address Issue | 473 | 20.53% |
| SLA Breach | 462 | 20.05% |
| Driver/Attempt Issue | 268 | 11.63% |
| Route Issue | 258 | 11.20% |
| Customer Experience Issue | 244 | 10.59% |

### Key Finding

**Geocode and address issues together account for 46.53% of classified exceptions.**

This indicates that address and location data quality represents a major
operational improvement opportunity.

---

##  Priority & Severity Analysis

Exceptions were assigned three operational severity levels.

| Severity | Exceptions | Percentage |
|---|---:|---:|
| Critical | 599 | 26.00% |
| High | 1,179 | 51.17% |
| Medium | 526 | 22.83% |

### Key Finding

**77.17% of exceptions were classified as Critical or High priority.**

This highlights the importance of prioritizing operational exceptions rather
than treating every issue equally.

---

##  SLA Performance

| Metric | Result |
|---|---:|
| Total Deliveries | **10,100** |
| SLA Met | **9,595** |
| SLA Breached | **505** |
| SLA Compliance | **95.00%** |

The delivery network achieved **95% SLA compliance**, while 505 deliveries
breached their target delivery time.

---

##  City-Level Analysis

Exception rates were analyzed across eight cities.

| City | Deliveries | Exceptions | Exception Rate |
|---|---:|---:|---:|
| Mumbai | 1,212 | 286 | 23.60% |
| Pune | 1,300 | 303 | 23.31% |
| Ahmedabad | 1,254 | 292 | 23.29% |
| Kolkata | 1,281 | 297 | 23.19% |
| Bengaluru | 1,221 | 277 | 22.69% |
| Delhi | 1,286 | 290 | 22.55% |
| Chennai | 1,241 | 276 | 22.24% |
| Hyderabad | 1,305 | 283 | 21.69% |

### Key Finding

Mumbai recorded the highest exception rate at **23.60%**, while Hyderabad
recorded the lowest at **21.69%**.

The relatively narrow difference suggests that quality issues are distributed
across the delivery network rather than being concentrated in one city.

---

## Driver-Level Analysis

SQL analysis was used to identify drivers with higher exception counts.

The analysis considers:

- Total deliveries
- Exception count
- SLA breaches
- Average customer rating

This provides an operational view of driver-level quality patterns and helps
identify records requiring further investigation.

---

##  Power BI Dashboard

The Power BI dashboard provides an executive-level view of delivery quality
and operational exceptions.

### Dashboard Components

- **Total Deliveries** KPI
- **Total Exceptions** KPI
- **Exception Rate** KPI
- **SLA Compliance** KPI
- **Exceptions by Type**
- **Exception Rate by City**
- **SLA Performance**
- **Exception Priority Distribution**

The dashboard helps operations teams quickly identify major sources of
delivery-quality issues and prioritize investigation.

---

##  Business Insights

### 1. Location data is a major quality concern

Geocode and address issues together represent **46.53% of classified
exceptions**.

Improving address validation and geocoding processes could reduce a
significant portion of operational exceptions.

### 2. Most exceptions require attention

More than **77% of exceptions are classified as Critical or High priority**,
indicating that exception prioritization is important for operational teams.

### 3. SLA performance is strong but not perfect

The network achieves **95% SLA compliance**, with 505 deliveries breaching
the SLA.

### 4. Quality issues are network-wide

City exception rates range from **21.69% to 23.60%**, suggesting that the
quality problem is not isolated to a single city.

---

##  SQL Analysis

The project stores the audited delivery data in a **SQLite database** and
uses SQL queries for operational analysis.

SQL analysis includes:

- Overall quality metrics
- Exception rate by city
- Driver exception analysis
- SLA performance
- Exception type distribution
- Priority escalation analysis
- Operational KPI calculations

The SQL queries are available in:

```text
python/quality_analysis.sql
```

---

##  Python Analysis

Python is used for:

- Synthetic dataset generation
- Data validation
- Quality-rule implementation
- Exception detection
- Exception classification
- Severity assignment
- Recommended-action assignment
- Database loading

### Python Scripts

```text
python/
├── create_dataset.py
├── quality_audit.py
├── load_database.py
├── run_sql.py
└── quality_analysis.sql
```

---

##  Project Structure

```text
last-mile-delivery-quality-monitoring/
│
├── README.md
│
├── python/
│   ├── create_dataset.py
│   ├── quality_audit.py
│   ├── load_database.py
│   ├── run_sql.py
│   └── quality_analysis.sql
│
├── data/
│   ├── delivery_data_raw.csv
│   ├── delivery_exceptions.csv
│   ├── quality_audit_results.csv
│   └── delivery_quality.db
│
├── dashboard/
│   └── Last_Mile_Delivery_Quality_Analytics.pbix
│
└── screenshots/
    └── dashboard.png
```

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/saba0-data/last-mile-delivery-quality-monitoring.git
cd last-mile-delivery-quality-monitoring
```

### 2. Install dependencies

```bash
pip install pandas numpy
```

### 3. Generate the delivery dataset

```bash
python python/create_dataset.py
```

### 4. Run the data quality audit

```bash
python python/quality_audit.py
```

### 5. Load the database

```bash
python python/load_database.py
```

### 6. Run SQL analysis

```bash
python python/run_sql.py
```

### 7. Open the Power BI dashboard

Open:

```text
dashboard/Last_Mile_Delivery_Quality_Analytics.pbix
```

---

##  Skills Demonstrated

### Data Analytics

- Data quality auditing
- Data validation
- Exception detection
- Exploratory data analysis
- KPI analysis
- Operational analytics
- Business insights

### Python

- Pandas
- NumPy
- Data transformation
- Rule-based validation
- Automated quality checks

### SQL

- SELECT statements
- WHERE conditions
- GROUP BY
- Aggregations
- CASE statements
- KPI calculations
- City-level analysis
- Driver-level analysis
- Exception analysis

### Power BI

- KPI cards
- Bar charts
- Donut charts
- Dashboard design
- Operational reporting
- Data visualization

### Database

- SQLite
- Data loading
- Structured analytical storage

### Development Tools

- Git
- GitHub
- VS Code

---

##  Future Improvements

Potential extensions to the project include:

- Automated daily quality monitoring
- Time-series exception trend analysis
- Root-cause analysis
- Automated exception alerts
- Real-time operational monitoring
- Driver performance scoring
- Predictive SLA breach detection
- Automated Power BI refresh

## Power BI Dashboard

An interactive Power BI dashboard was developed to monitor:

- Overall delivery volume
- Total exceptions
- Exception rate
- SLA compliance
- Exception types
- Exception rate by city
- SLA performance
- Exception severity distribution

Dashboard file:

`dashboard/Last_Mile_Delivery_Quality_Analytics.pbix`

Dashboard preview:

![Power BI Dashboard](screenshots/dashboard.png)
---

##  Author

**Saba Sultana**

**Data Science | Data Analytics | Python | SQL | Power BI**

---

⭐ If you found this project useful, consider giving the repository a star.
