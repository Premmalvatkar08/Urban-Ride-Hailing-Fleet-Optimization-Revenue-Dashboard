# 🚕 Urban Ride-Hailing Fleet Optimization & Revenue Dashboard

An end-to-end **Power BI Data Analytics project** designed to analyze urban ride-hailing demand, revenue performance, driver operations, cancellations, fleet activity, and geographic demand patterns.

The project demonstrates a complete Data Analyst workflow:

**Raw Data → Data Validation → Power Query → Data Modeling → DAX → Dashboard Development → Advanced Analytics → Business Insights**

> **Dataset:** Synthetic ride-hailing data generated specifically for portfolio and analytical demonstration purposes.

---

## 📌 Project Overview

Ride-hailing businesses generate large volumes of trip data containing information about trips, drivers, vehicles, locations, fares, trip duration, payment methods, and cancellations.

This project transforms trip-level data into an interactive Power BI business intelligence solution to answer questions such as:

- When is ride demand highest?
- Which locations generate the most trips?
- How does demand vary by weekday and weekend?
- What is the overall revenue performance?
- What percentage of trips are cancelled?
- Which cancellation reasons occur most frequently?
- How do vehicle types and fuel types contribute to trip activity?
- Which geographic zones have higher demand?
- How does trip distance relate to fare?
- What happens to projected trip volume under different demand scenarios?

---

## 🎯 Business Objectives

The main objectives of this project are:

1. Analyze overall ride demand.
2. Identify peak demand hours.
3. Analyze demand by day and month.
4. Identify high-demand pickup and drop locations.
5. Compare weekday and weekend demand.
6. Analyze revenue performance and revenue efficiency.
7. Monitor cancellation volume and cancellation rate.
8. Analyze driver and vehicle activity.
9. Understand geographic demand distribution.
10. Build interactive business intelligence dashboards.
11. Apply DAX to create business KPIs.
12. Perform what-if scenario analysis for potential demand changes.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Power BI** | Dashboard development, visualization and data modeling |
| **Power Query** | Data cleaning, transformation and feature creation |
| **DAX** | Measures, KPIs and analytical calculations |
| **Python** | Synthetic dataset generation |
| **CSV** | Source data storage |
| **Git & GitHub** | Version control and project documentation |
| **Markdown** | Project documentation and journals |

---

# 🗂️ Dataset

The project uses a synthetic ride-hailing dataset generated using Python.

## Fact Table

--> **FactTrips**

Contains **10,000 ride transactions** and includes:

- Trip ID
- Date
- Pickup Time
- Pickup Location
- Drop Location
- Driver ID
- Vehicle ID
- Trip Status
- Fare
- Distance
- Duration
- Payment Type
- Cancellation Reason

## Dimension Tables

--> **DimDate**

Contains:

- Date
- Year
- Month
- Quarter
- Day
- Day Name
- Week Number

--> **DimDriver**

Contains:

- Driver ID
- Driver Rating
- Vehicle ID
- Join Date
- City Zone

--> **DimVehicle**

Contains:

- Vehicle ID
- Vehicle Type
- Fuel Type
- Vehicle Age

--> **DimLocation**

Contains:

- Location ID
- Location Name
- Zone
- Latitude
- Longitude

--> **DimDropLocation**

A role-playing copy of the location dimension used to analyze drop locations separately from pickup locations.

---

# 🔄 Data Preparation

The dataset was processed using Power Query.

## Major Transformations

- Corrected column data types
- Trimmed text values
- Cleaned text using `Clean`
- Standardized categorical values
- Created Pickup Hour
- Created Day Name
- Created Day Type
- Created Month Name
- Created Month Number
- Created Distance Category
- Created Duration Category
- Validated numerical columns
- Validated categorical values

## Missing Value Handling

The `Cancellation_Reason` column contains blank values because completed trips do not require a cancellation reason.

This was treated as **structural missingness** rather than automatically replacing the values.

---

# ⭐ Data Model

The project follows a **Star Schema** design.

```text
                         DimDate
                            |
                            |
                       FactTrips
                      /    |    \
                     /     |     \
                    /      |      \
             DimDriver DimLocation DimVehicle
                           |
                           |
                    DimDropLocation
```

--> Relationships

```text
DimDate[Date] → FactTrips[Date]

DimDriver[Driver_ID] → FactTrips[Driver_ID]

DimVehicle[Vehicle_ID] → FactTrips[Vehicle_ID]

DimLocation[Location_ID] → FactTrips[Pickup_Location_ID]

DimDropLocation[Location_ID] → FactTrips[Drop_Location_ID]
```

The dimension tables provide descriptive attributes while `FactTrips` stores transactional ride data.

---

# 📊 DAX Measures

The project contains **15 core DAX measures**, with additional measures added for driver operations, geographic analysis, and scenario planning.

## Demand Metrics

- Total Trips
- Completed Trips
- Cancelled Trips
- Peak Hour Demand
- Weekend Demand %

## Revenue Metrics

- Total Revenue
- Average Fare
- Revenue per Trip
- Revenue per KM
- Completed Trip Revenue

## Operational Metrics

- Average Trip Distance
- Average Trip Duration
- Total Distance
- Average Driver Rating
- Active Drivers

## Geographic & Scenario Metrics

- Active Pickup Locations
- Projected Trips

The complete DAX documentation is available in:

```text
DAX/Measures.md
```

---

# 📈 Power BI Dashboards

The completed Power BI report contains **six analytical dashboard pages**.

---

## 1. Executive Overview

The Executive Overview provides a high-level summary of business performance.

--> KPIs

- Total Trips
- Total Revenue
- Average Fare
- Cancellation Rate
- Average Driver Rating

--> Visualizations

- Monthly Trips Trend — Line Chart
- Monthly Revenue Trend — Line Chart
- Trip Status — Donut Chart
- Trips by Day Type — Clustered Column Chart

--> Slicers

- Trip Status
- Month Name
- Payment Type
- Pickup Location

---

## 2. Demand Intelligence

The Demand Intelligence dashboard focuses on ride demand patterns across time and geography.

--> KPI

- Peak Hour Demand

--> Visualizations

- Trips by Pickup Hour — Line Chart
- Trips by Day of Week — Clustered Column Chart
- Trips by Pickup Location — Clustered Bar Chart
- Monthly Demand Trend — Line Chart
- Trips by Day Type — Clustered Column Chart
- Trips by Zone — Clustered Bar Chart

--> Slicers

- Day Name
- Pickup Hour
- Zone

---

## 3. Driver & Operations

This dashboard analyzes driver activity, vehicle activity and operational performance.

--> KPIs

- Active Drivers
- Average Driver Rating
- Average Trip Duration
- Total Distance

--> Visualizations

- Top 10 Drivers by Trips — Clustered Bar Chart
- Trips by Vehicle Type — Clustered Column Chart
- Trips by Fuel Type — Donut Chart
- Average Trip Duration by Vehicle Type — Clustered Column Chart
- Trips by Zone — Clustered Bar Chart

--> Slicers

- Vehicle Type
- Fuel Type
- Zone

---

## 4. Revenue & Cancellation

This dashboard focuses on revenue performance, payment behavior and cancellation patterns.

--> KPIs

- Total Revenue
- Completed Trip Revenue
- Revenue per Trip
- Cancellation Rate

--> Visualizations

- Monthly Revenue Trend — Line Chart
- Revenue by Vehicle Type — Clustered Column Chart
- Trips by Payment Type — Donut Chart
- Cancellation Reasons — Clustered Bar Chart
- Cancellations by Pickup Location — Clustered Bar Chart

--> Slicers

- Vehicle Type
- Payment Type
- Pickup Location

---

## 5. Advanced Analytics

This dashboard combines demand, revenue efficiency, driver activity and scenario analysis.

--> KPIs

- Peak Hour Demand
- Revenue per KM
- Weekend Demand %
- Active Drivers
- Projected Trips

--> Visualizations

- Trips by Pickup Hour — Line Chart
- Revenue by Pickup Hour — Clustered Column Chart
- Trip Distance vs Fare — Scatter Chart
- Top 10 Drivers by Trips — Clustered Bar Chart
- Monthly Trips vs Revenue — Line and Clustered Column Chart

--> What-If Analysis

A **Demand Increase %** parameter was created to test potential demand scenarios.

Example:

- 0% increase → approximately **10,000 projected trips**
- 10% increase → approximately **11,000 projected trips**

---

## 6. Geographic Analysis

This dashboard focuses on location-level demand, revenue and cancellation patterns.

--> KPIs

- Active Pickup Locations
- Total Revenue
- Cancelled Trips

--> Visualizations

- Trips by Pickup Location — Clustered Bar Chart
- Trips by Drop Location — Clustered Bar Chart
- Trips by Zone — Clustered Column Chart
- Revenue by Pickup Location — Clustered Bar Chart
- Cancelled by Pickup Location — Clustered Bar Chart

This page was intentionally kept clean without additional slicers because the existing analytical visuals already use the available canvas effectively.

---

# 🔍 Business Analysis Areas

The dashboard enables analysis across several important business dimensions.

## ⏰ Time Analysis

Analyze:

- Hourly demand
- Daily demand
- Monthly demand
- Weekday vs weekend demand
- Peak demand periods

## 📍 Geographic Analysis

Analyze:

- Pickup locations
- Drop locations
- Geographic zones
- High-demand areas
- Location-level revenue
- Location-level cancellations

## 💰 Revenue Analysis

Analyze:

- Total revenue
- Completed trip revenue
- Average fare
- Revenue per trip
- Revenue per kilometer
- Revenue by vehicle type
- Monthly revenue trends

## 🚗 Fleet & Driver Analysis

Analyze:

- Active drivers
- Driver ratings
- Vehicle types
- Fuel types
- Driver trip activity
- Vehicle-level trip activity
- Trip duration

## ❌ Cancellation Analysis

Analyze:

- Cancelled trips
- Cancellation rate
- Cancellation reasons
- Cancellation patterns by location

## 🔮 Scenario Analysis

Analyze:

- Projected trips
- Demand increase scenarios
- Potential operational planning requirements

---

# 🧪 Data Validation

Before dashboard development, the dataset was validated for:

- Duplicate records
- Missing values
- Invalid numerical values
- Invalid categorical values
- Primary key uniqueness
- Foreign key consistency
- Trip status consistency
- Cancellation reason consistency

## Dataset Validation Summary

| Table | Rows | Columns | Duplicate Rows |
|---|---:|---:|---:|
| FactTrips | 10,000 | 15 | 0 |
| DimDriver | 300 | 5 | 0 |
| DimVehicle | 300 | 4 | 0 |
| DimLocation | 12 | 5 | 0 |

---

# 📌 Key Dashboard Findings

The completed dashboard produced the following descriptive findings from the synthetic dataset:

| Metric | Result |
|---|---:|
| Total Trips | 10,000 |
| Cancelled Trips | 1,194 |
| Cancellation Rate | 11.94% |
| Active Drivers | 300 |
| Active Pickup Locations | 12 |
| Peak Hour Demand | 935 |
| Revenue per KM | ₹19.77 |
| Weekend Demand | 28.36% |
| Total Revenue | Approximately ₹1.54M |

Additional analysis showed differences in trip activity, revenue and cancellations across vehicle types, locations and geographic zones.

These are **descriptive observations from synthetic data** and should not be interpreted as causal findings without additional operational data.

---

# 💼 Data Analyst Skills Demonstrated

This project demonstrates practical experience in:

- Data Cleaning
- Data Validation
- Power Query
- Data Modeling
- Star Schema
- DAX
- KPI Development
- Data Visualization
- Time-Series Analysis
- Geographic Analysis
- Revenue Analysis
- Cancellation Analysis
- Driver & Fleet Analysis
- What-If Analysis
- Business Intelligence
- Dashboard Design
- Business Problem Solving
- Git & GitHub
- Technical Documentation

---

# 📁 Project Structure

```text
Urban Ride-Hailing Fleet Optimization & Revenue Dashboard
│
├── Dataset
│   ├── Raw
│   │   ├── FactTrips.csv
│   │   ├── DimDriver.csv
│   │   ├── DimVehicle.csv
│   │   └── DimLocation.csv
│   │
│   └── generate_dataset.py
│
├── PowerBI
│   └── Urban_Ride_Hailing_Fleet_Optimization_Revenue_Dashboard.pbix
│
├── DAX
│   └── Measures.md
│
├── Documentation
│
├── Project Journal
│   ├── Day-01-Data-Quality-Validation.md
│   ├── Day-02-Power-Query-Transformations.md
│   ├── Day-03-Power-BI-Data-Modeling.md
│   ├── Day-04-DAX-Measures.md
│   ├── Day-05-Executive-Overview.md
│   ├── Day-06-Demand-Intelligence.md
│   ├── Day-07-Driver-Operations.md
│   ├── Day-08-Revenue-Cancellation.md
│   ├── Day-09-Advanced-Analytics.md
│   └── Day-10-Geographic-Analysis.md
│
├── Screenshots
│   ├── Executive-Overview.png
│   ├── Demand-Intelligence.png
│   ├── Driver-Operations.png
│   ├── Revenue-Cancellation.png
│   ├── Advanced-Analytics.png
│   └── Geographic-Analysis.png
│
└── README.md
```

---

# 📚 Project Development Stages

| Day | Work Completed |
|---|---|
| Day 1 | Data Quality Validation |
| Day 2 | Power Query Transformations |
| Day 3 | Power BI Data Modeling |
| Day 4 | DAX Measures |
| Day 5 | Executive Overview Dashboard |
| Day 6 | Demand Intelligence Dashboard |
| Day 7 | Driver & Operations Dashboard |
| Day 8 | Revenue & Cancellation Dashboard |
| Day 9 | Advanced Analytics Dashboard |
| Day 10 | Geographic Analysis Dashboard |
| Day 11 | Final Dashboard Integration & Advanced Polish |
| Day 12 | Final Validation & Portfolio Preparation |

---

# 🚀 Future Enhancements

Potential future improvements include:

- Connecting the dashboard to a real-world ride-hailing dataset
- Publishing the report to Power BI Service
- Adding automated data refresh
- Adding more detailed driver utilization metrics
- Adding route-level analysis
- Adding customer segmentation
- Adding predictive demand forecasting
- Adding anomaly detection
- Adding additional operational KPIs
- Building automated data pipelines

---

# 👨‍💻 Project Type

**Portfolio Project — Data Analytics / Business Intelligence**

Built using:

**Power BI + Power Query + DAX + Python + GitHub**

---

# 📌 Key Takeaway

This project demonstrates an end-to-end approach to transforming raw ride-hailing data into an interactive business intelligence solution.

The workflow covers the complete analytics lifecycle:

**Data → Validation → Cleaning → Modeling → DAX → Visualization → Advanced Analytics → Business Analysis → Documentation**

The project is designed to demonstrate practical Data Analyst skills rather than only dashboard-building skills.

---

## ✅ Project Status

**Completed — Portfolio Ready**

The repository contains the dataset, Python generator, Power BI report, DAX documentation, project journals, dashboard screenshots, and project README.
