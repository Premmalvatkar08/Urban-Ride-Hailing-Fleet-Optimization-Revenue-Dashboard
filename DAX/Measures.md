# DAX Measures — Urban Ride-Hailing Fleet Optimization & Revenue Dashboard

This document contains the DAX measures used to calculate the key performance indicators and analytical metrics in the Urban Ride-Hailing Fleet Optimization & Revenue Dashboard.

---

## 1. Total Trips

```DAX
Total Trips =
COUNTROWS(FactTrips)
```

**Purpose:** Calculates the total number of trips in the fact table.

**Business use:** Used as the primary trip-volume KPI across the dashboard.

---

## 2. Completed Trips

```DAX
Completed Trips =
CALCULATE(
    [Total Trips],
    FactTrips[Trip_Status] = "Completed"
)
```

**Purpose:** Calculates the number of successfully completed trips.

**Business use:** Helps measure successful trip fulfillment.

---

## 3. Cancelled Trips

```DAX
Cancelled Trips =
CALCULATE(
    [Total Trips],
    FactTrips[Trip_Status] = "Cancelled"
)
```

**Purpose:** Calculates the total number of cancelled trips.

**Business use:** Used to monitor service cancellations and operational issues.

---

## 4. Total Revenue

```DAX
Total Revenue =
SUM(FactTrips[Fare])
```

**Purpose:** Calculates total fare revenue recorded in the dataset.

**Business use:** Core revenue KPI used for financial performance analysis.

---

## 5. Average Fare

```DAX
Average Fare =
AVERAGE(FactTrips[Fare])
```

**Purpose:** Calculates the average fare per trip.

**Business use:** Helps understand typical customer transaction value.

---

## 6. Average Trip Distance

```DAX
Average Trip Distance =
AVERAGE(FactTrips[Distance_KM])
```

**Purpose:** Calculates the average distance travelled per trip.

**Business use:** Supports trip-efficiency and demand analysis.

---

## 7. Average Trip Duration

```DAX
Average Trip Duration =
AVERAGE(FactTrips[Duration_Minutes])
```

**Purpose:** Calculates the average duration of trips.

**Business use:** Helps evaluate operational efficiency and travel-time patterns.

---

## 8. Cancellation Rate

```DAX
Cancellation Rate =
DIVIDE(
    [Cancelled Trips],
    [Total Trips],
    0
)
```

**Purpose:** Calculates the percentage of trips that were cancelled.

**Business use:** Measures service reliability and cancellation performance.

**Format:** Percentage.

---

## 9. Revenue per Trip

```DAX
Revenue per Trip =
DIVIDE(
    [Total Revenue],
    [Total Trips],
    0
)
```

**Purpose:** Calculates average revenue generated per recorded trip.

**Business use:** Provides a normalized revenue-efficiency metric.

---

## 10. Revenue per KM

```DAX
Revenue per KM =
DIVIDE(
    [Total Revenue],
    SUM(FactTrips[Distance_KM]),
    0
)
```

**Purpose:** Calculates revenue generated per kilometre travelled.

**Business use:** Helps evaluate revenue efficiency relative to distance.

---

## 11. Peak Hour Demand

```DAX
Peak Hour Demand =
MAXX(
    VALUES(FactTrips[Pickup_Hour]),
    [Total Trips]
)
```

**Purpose:** Identifies the maximum number of trips recorded in any pickup hour.

**Business use:** Supports peak-demand identification and fleet planning.

---

## 12. Weekend Demand %

```DAX
Weekend Demand % =
DIVIDE(
    CALCULATE(
        [Total Trips],
        FactTrips[Day_Type] = "Weekend"
    ),
    [Total Trips],
    0
)
```

**Purpose:** Calculates the proportion of total trips occurring on weekends.

**Business use:** Helps compare weekday and weekend demand patterns.

**Format:** Percentage.

---

## 13. Total Distance

```DAX
Total Distance =
SUM(FactTrips[Distance_KM])
```

**Purpose:** Calculates the total distance covered by recorded trips.

**Business use:** Used to evaluate overall fleet travel activity.

---

## 14. Completed Trip Revenue

```DAX
Completed Trip Revenue =
CALCULATE(
    [Total Revenue],
    FactTrips[Trip_Status] = "Completed"
)
```

**Purpose:** Calculates revenue associated with completed trips.

**Business use:** Separates completed-trip revenue from cancelled-trip records.

---

## 15. Average Driver Rating

```DAX
Average Driver Rating =
AVERAGE(DimDriver[Driver_Rating])
```

**Purpose:** Calculates the average rating across drivers.

**Business use:** Provides a high-level indicator of driver rating performance.

---

## 16. Active Drivers

```DAX
Active Drivers =
DISTINCTCOUNT(FactTrips[Driver_ID])
```

**Purpose:** Counts the distinct drivers associated with recorded trips.

**Business use:** Measures the active driver base contributing to trip activity.

---

## 17. Active Pickup Locations

```DAX
Active Pickup Locations =
DISTINCTCOUNT(FactTrips[Pickup_Location_ID])
```

**Purpose:** Counts the distinct pickup locations appearing in trip activity.

**Business use:** Measures geographic coverage of pickup operations.

---

## 18. Projected Trips

```DAX
Projected Trips =
[Total Trips] *
(
    1 +
    SELECTEDVALUE(
        'Demand Increase %'[Demand Increase %],
        0
    )
)
```

**Purpose:** Calculates projected trip volume based on the selected demand-increase scenario.

**Business use:** Supports what-if scenario analysis for potential changes in demand.

**Example:**
- 0% increase → approximately 10,000 projected trips
- 10% increase → approximately 11,000 projected trips

---

# DAX Techniques Demonstrated

- `COUNTROWS()`
- `SUM()`
- `AVERAGE()`
- `DISTINCTCOUNT()`
- `CALCULATE()`
- `DIVIDE()`
- `MAXX()`
- `VALUES()`
- `SELECTEDVALUE()`
- Filter context
- KPI calculations
- Percentage calculations
- Conditional aggregation
- What-if parameter analysis

# Measure Categories

| Category | Measures |
|---|---|
| Trip Volume | Total Trips, Completed Trips, Cancelled Trips |
| Revenue | Total Revenue, Completed Trip Revenue, Revenue per Trip, Revenue per KM |
| Trip Efficiency | Average Fare, Average Trip Distance, Average Trip Duration, Total Distance |
| Operations | Active Drivers, Average Driver Rating, Peak Hour Demand |
| Cancellation | Cancellation Rate |
| Demand | Weekend Demand %, Peak Hour Demand |
| Geography | Active Pickup Locations |
| Scenario Analysis | Projected Trips |

# Validation Summary

The measures were tested against the dashboard and dataset during development.

Key validated outputs include:

- Total Trips: 10,000
- Cancelled Trips: 1,194
- Cancellation Rate: approximately 11.94%
- Active Drivers: 300
- Active Pickup Locations: 12
- Peak Hour Demand: 935
- Revenue per KM: approximately ₹19.77
- Weekend Demand: approximately 28.36%
- Projected Trips at 0% demand increase: approximately 10,000
- Projected Trips at 10% demand increase: approximately 11,000

> Note: The project uses a synthetic ride-hailing dataset created for portfolio and analytical demonstration purposes.
