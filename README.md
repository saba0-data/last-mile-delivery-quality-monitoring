# Last-Mile Delivery Quality & Exception Analytics

## Overview

A data quality and operational analytics project simulating a
last-mile delivery quality monitoring workflow.

The project audits delivery records, identifies operational
exceptions, assigns severity levels, recommends corrective actions,
and analyzes quality patterns using Python and SQL.

---

## Business Problem

Last-mile delivery operations generate large volumes of
transactional and operational data.

Quality teams need to identify:

- Address and geocode issues
- SLA breaches
- Excessive delivery attempts
- Route anomalies
- Customer experience issues
- Recurring operational patterns
- High-priority exceptions requiring escalation

This project simulates such a quality-monitoring workflow.

---

## Project Objectives

- Perform systematic quality audits
- Identify data-quality and operational exceptions
- Classify exceptions by type
- Assign severity levels
- Recommend corrective actions
- Analyze city-level performance
- Analyze driver-level performance
- Measure SLA compliance
- Identify recurring exception patterns
- Prioritize issues for escalation

---

## Dataset

The project uses a synthetic dataset containing:

- 10,100 delivery records
- 14 original attributes
- Delivery information
- Driver information
- Geographic information
- SLA information
- Customer ratings
- Address quality
- Route status

Additional analytical fields are generated during the
quality-audit process.

---

## Quality Audit Rules

The audit evaluates:

1. Duplicate orders
2. Invalid latitude
3. Invalid longitude
4. Missing addresses
5. SLA breaches
6. Excessive delivery attempts
7. Low customer ratings
8. Route anomalies

---

## Exception Classification

Detected issues are classified into:

- Geocode Issue
- Address Issue
- SLA Breach
- Driver/Attempt Issue
- Route Issue
- Customer Experience Issue

---

## Severity Classification

| Severity | Description |
|---|---|
| Critical | Immediate operational/data-quality attention |
| High | Requires timely investigation or escalation |
| Medium | Requires operational review |
| None | No exception detected |

---

## Key Results

### Overall Quality

- Records audited: 10,100
- Total exceptions: 2,304
- Exception rate: 22.81%

### SLA Performance

- SLA compliance: 95%
- SLA breaches: 505

### Exception Patterns

| Exception Type | Count | Share |
|---|---:|---:|
| Geocode Issue | 599 | 26.00% |
| Address Issue | 473 | 20.53% |
| SLA Breach | 462 | 20.05% |
| Driver/Attempt Issue | 268 | 11.63% |
| Route Issue | 258 | 11.20% |
| Customer Experience Issue | 244 | 10.59% |

### Priority Analysis

| Severity | Exceptions | Share |
|---|---:|---:|
| Critical | 599 | 26.00% |
| High | 1,179 | 51.17% |
| Medium | 526 | 22.83% |

77.17% of identified exceptions were classified as
Critical or High priority.

---

## City-Level Analysis

The SQL analysis compares cities based on:

- Total deliveries
- Total exceptions
- Exception rate

Mumbai recorded the highest exception rate at 23.60%,
while Hyderabad recorded the lowest at 21.69%.

The relatively narrow difference suggests that quality
issues are distributed across the network rather than
being concentrated in a single city.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Power BI
- Git
- GitHub

---

## Project Workflow

Raw Delivery Data

↓

Quality Audit

↓

Exception Detection

↓

Severity Classification

↓

Recommended Action

↓

SQLite Database

↓

SQL Analysis

↓

Power BI Dashboard

---

## Business Impact

The analysis identifies address and geocode quality as a
major operational improvement opportunity.

Geocode and address issues together represented 46.53%
of classified exceptions.

Improving location and address data quality could therefore
help reduce a significant portion of operational exceptions.

---

## Future Improvements

- Power BI operational dashboard
- Automated exception monitoring
- Trend analysis over time
- Root-cause analysis
- Automated escalation workflows
- Real-time operational monitoring
