# 🚕 Urban Ride-Hailing Fleet Optimization & Revenue Dashboard

An end-to-end **Power BI data analytics project** designed to analyze urban ride-hailing demand, revenue performance, driver operations, cancellations, and geographic demand patterns.

The project demonstrates a complete Data Analyst workflow:

**Raw Data → Data Validation → Power Query → Data Modeling → DAX → Dashboard → Business Insights**

---

## 📌 Project Overview

Ride-hailing businesses generate large volumes of trip data containing information about customers, drivers, vehicles, locations, fares, trip duration, and cancellations.

This project analyzes that data to answer important business questions such as:

- When is ride demand highest?
- Which locations generate the most trips?
- How does demand vary by weekday and weekend?
- What is the overall revenue performance?
- What percentage of trips are cancelled?
- How do trip distance and duration affect revenue?
- Which geographic zones have higher demand?
- How can fleet operations be better understood using data?

---

## 🎯 Business Objectives

The main objectives of this project are:

1. Analyze overall ride demand.
2. Identify peak demand hours.
3. Analyze demand by day and month.
4. Identify high-demand pickup locations.
5. Compare weekday and weekend demand.
6. Analyze revenue performance.
7. Monitor cancellation rate.
8. Analyze driver ratings.
9. Understand geographic demand distribution.
10. Build an interactive business intelligence dashboard.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Power BI | Dashboard development and visualization |
| Power Query | Data cleaning and transformation |
| DAX | Measures and KPI calculations |
| Python | Synthetic dataset generation |
| CSV | Data storage |
| Git & GitHub | Version control and project documentation |

---

## 🗂️ Dataset

The project uses a synthetic ride-hailing dataset created using Python.

### Fact Table

**FactTrips**

Contains 10,000 ride transactions and includes:

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

### Dimension Tables

#### DimDate
Contains:

- Date
- Year
- Month
- Quarter
- Day
- Day Name
- Week Number

#### DimDriver

Contains:

- Driver ID
- Driver Rating
- Vehicle ID
- Join Date
- City Zone

#### DimVehicle

Contains:

- Vehicle ID
- Vehicle Type
- Fuel Type
- Vehicle Age

#### DimLocation

Contains:

- Location ID
- Location Name
- Zone
- Latitude
- Longitude

#### DimDropLocation

A role-playing copy of the location dimension used to analyze drop locations separately from pickup locations.

---

## 🔄 Data Preparation

The dataset was processed using Power Query.

### Major transformations

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

### Missing Value Handling

The `Cancellation_Reason` column contains many blank values because completed trips do not require a cancellation reason.

This was treated as **structural missingness** rather than automatically replacing the values.

---

## ⭐ Data Model

The project follows a **Star Schema** design.

```text
                         DimDate
                            |
                            |
DimDriver ----          FactTrips          ---- DimVehicle
                       /    |    \
                      /     |     \
                     /      |      \
            DimLocation   DimDropLocation

Relationships
    DimDate → FactTrips
    DimDriver → FactTrips
    DimVehicle → FactTrips
    DimLocation → FactTrips Pickup Location
    DimDropLocation → FactTrips Drop Location

The dimension tables provide descriptive attributes while FactTrips stores transactional ride data.



📊 DAX Measures

The project contains 15 core DAX measures.

Demand Metrics
    Total Trips
    Completed Trips
    Cancelled Trips
    Peak Hour Demand
    Weekend Demand %
Revenue Metrics
    Total Revenue
    Average Fare
    Revenue per Trip
    Revenue per KM
    Completed Trip Revenue
Operational Metrics
    Average Trip Distance
    Average Trip Duration
    Total Distance
    Cancellation Rate
    Average Driver Rating

The complete DAX documentation is available in:
DAX/Measures.md



📈 Power BI Dashboards

1. Executive Overview
The Executive Overview provides a high-level summary of business performance.

KPIs
    Total Trips
    Total Revenue
    Average Fare
    Cancellation Rate
    Average Driver Rating
Visualizations
    Monthly Trips Trend — Line Chart
    Monthly Revenue Trend — Line Chart
    Trip Status — Donut Chart
    Trips by Day Type — Clustered Column Chart
    Trip Status Slicer
    Month Name Slicer
    Payment Type Slicer
    Pickup Location Slicer
Screenshot

2. Demand Intelligence
The Demand Intelligence dashboard focuses on ride demand patterns across time and geography.

KPI
    Peak Hour Demand
    Visualizations
    Trips by Pickup Hour — Line Chart
    Trips by Day of Week — Clustered Column Chart
    Trips by Pickup Location — Clustered Bar Chart
    Monthly Demand Trend — Line Chart
    Trips by Day Type — Clustered Column Chart
    Trips by Zone — Clustered Bar Chart
Slicers
    Day Name
    Pickup Hour
    Zone
Screenshot


🔍 Business Analysis Areas
The dashboard enables analysis across several important business dimensions.

⏰ Time Analysis
Analyze:
    Hourly demand
    Daily demand
    Monthly demand
    Weekday vs weekend demand

📍 Geographic Analysis
Analyze:
    Pickup locations
    Drop locations
    Geographic zones
    High-demand areas

💰 Revenue Analysis
Analyze:
    Total revenue
    Average fare
    Revenue per trip
    Revenue per kilometer

🚗 Fleet & Driver Analysis
Analyze:
    Driver ratings
    Vehicle information
    Trip activity
    Operational demand

❌ Cancellation Analysis
Analyze:
    Cancelled trips
    Cancellation rate
    Cancellation reasons
    Cancellation patterns



📁 Project Structure
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
├── DAX
│   └── Measures.md
│
├── PowerBI
│   └── Urban_Ride_Hailing_Fleet_Optimization_Revenue_Dashboard.pbix
│
├── Project Journal
│   ├── Day-01-Data-Quality-Validation.md
│   ├── Day-02-Power-Query-Transformations.md
│   ├── Day-03-Power-BI-Data-Modeling.md
│   ├── Day-04-DAX-Measures.md
│   ├── Day-05-Executive-Overview.md
│   └── Day-06-Demand-Intelligence.md
│
├── Screenshots
│   ├── Executive-Overview.png
│   └── Demand-Intelligence.png
│
└── README.md



🧪 Data Validation
Before dashboard development, the dataset was validated for:

Duplicate records
    Missing values
    Invalid numerical values
    Invalid categorical values
    Primary key uniqueness
    Foreign key consistency
    Trip status consistency
    Cancellation reason consistency

Dataset Validation Summary
Table	Rows	Columns	Duplicate Rows
FactTrips	10,000	15	0
DimDriver	300	5	0
DimVehicle	300	4	0
DimLocation	12	5	0



💼 Data Analyst Skills Demonstrated
This project demonstrates practical experience in:
    Data Cleaning
    Data Validation
    Power Query
    Data Modeling
    Star Schema
    DAX
    KPI Development
    Data Visualization
    Time-Series Analysis
    Geographic Analysis
    Business Intelligence
    Dashboard Design
    Git & GitHub
    Business Problem Solving



📚 Project Development Stages
Stage	Work Completed
Day 1	Data Quality Validation
Day 2	Power Query Transformations
Day 3	Power BI Data Modeling
Day 4	DAX Measures
Day 5	Executive Overview Dashboard
Day 6	Demand Intelligence Dashboard



🚀 Future Enhancements
Planned enhancements include:
    Geographic map visualization
    Driver & Operations dashboard
    Revenue & Cancellation dashboard
    Advanced DAX calculations
    What-if analysis
    Demand forecasting
    Additional operational KPIs
    Advanced business insights



👨‍💻 Project Type
Portfolio Project — Data Analytics / Business Intelligence

Built using:
Power BI + Power Query + DAX + Python + GitHub


📌 Key Takeaway

This project demonstrates an end-to-end approach to transforming raw ride-hailing data into an interactive business intelligence solution using Power BI.

The workflow covers the complete analytics lifecycle:
Data → Cleaning → Modeling → DAX → Visualization → Business Analysis