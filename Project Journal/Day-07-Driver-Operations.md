# Day 07 — Driver & Operations Dashboard

## Objective

Analyze driver performance, vehicle activity, trip efficiency, and operational demand to understand fleet operations and identify important performance patterns.

## Business Questions

1. How many active drivers are handling trips?
2. Which drivers handle the highest number of trips?
3. What is the average driver rating?
4. Which vehicle types have the highest trip activity?
5. How does average trip duration vary by vehicle type?
6. Which fuel types account for the most trips?
7. Which zones have the highest operational activity?

## Data Model Used

The dashboard uses the Power BI star schema created during Day 3:

- FactTrips
- DimDriver
- DimVehicle
- DimLocation
- DimDate
- DimDropLocation

Important relationships used:

- DimDriver[Driver_ID] → FactTrips[Driver_ID]
- DimVehicle[Vehicle_ID] → FactTrips[Vehicle_ID]
- DimLocation[Location_ID] → FactTrips[Pickup_Location_ID]

## DAX Measure Added

### Active Drivers

```DAX
Active Drivers =
DISTINCTCOUNT(FactTrips[Driver_ID])
```

This measure counts unique drivers appearing in the trip fact table.

## KPI Cards

Four KPI cards were created:

1. Active Drivers — 300
2. Average Driver Rating — 4.24
3. Average Trip Duration — 48.77 minutes
4. Total Distance — 77.71K km

## Dashboard Visuals

### 1. Trips by Driver
**Visual Type:** Clustered Bar Chart

Shows the highest-trip-volume drivers using a Top 10 filter.

The visible dashboard screenshot shows D0277 with 51 trips, followed by D0078 and D0204 with 47 trips each, and D0140 with 45 trips.

### 2. Trips by Fuel Type
**Visual Type:** Donut Chart

Shows trip distribution across Electric, CNG, and Petrol.

Visible values are approximately:

- Electric — 3.46K (34.64%)
- CNG — 3.43K (34.31%)
- Petrol — 3.11K (31.05%)

### 3. Trips by Zone
**Visual Type:** Clustered Bar Chart

Shows operational trip volume by zone.

Visible values:

- Central — 3,394
- Navi Mumbai — 3,381
- North — 1,626
- West — 1,599

### 4. Average Trip Duration by Vehicle Type
**Visual Type:** Clustered Column Chart

Visible rounded values:

- Sedan — 49 minutes
- SUV — 49 minutes
- Hatchback — 48 minutes

### 5. Trips by Vehicle Type
**Visual Type:** Clustered Column Chart

Visible approximate values:

- Hatchback — 3.5K
- SUV — 3.4K
- Sedan — 3.1K

## Slicers

Three interactive slicers were added:

- Vehicle Type
- Fuel Type
- Zone

These allow users to filter the dashboard and analyze operational performance across different fleet segments and geographic zones.

## Business Insights

Based on the completed dashboard screenshot:

1. **Fleet activity is spread across all three vehicle types.** Hatchbacks show the highest trip volume at approximately 3.5K trips, followed by SUVs at approximately 3.4K and Sedans at approximately 3.1K.

2. **Average trip duration is very similar across vehicle types.** Sedan and SUV trips are approximately 49 minutes on average, while Hatchback trips are approximately 48 minutes. This indicates only a small difference in average duration between the displayed vehicle categories.

3. **Central and Navi Mumbai show the highest operational activity.** They record 3,394 and 3,381 trips respectively, substantially above the North and West zones shown in the dashboard.

4. **Fuel-type demand is relatively balanced.** Electric and CNG account for approximately 34.64% and 34.31% of trips respectively, while Petrol accounts for approximately 31.05%.

5. **The highest-volume drivers in the visible Top 10 chart have around 45–51 trips.** D0277 is the highest visible driver at 51 trips, followed by D0078 and D0204 at 47 trips each. The chart is filtered to Top 10 drivers, so the screenshot does not represent all 300 drivers individually.

## Validation

- Active Drivers measure validated: 300.
- Average Driver Rating validated: 4.24.
- Average Trip Duration validated: 48.77 minutes.
- Total Distance validated: 77.71K km.
- Driver chart uses Top 10 filtering and descending trip count.
- Vehicle and zone charts are sorted by trip volume.
- Fuel-type distribution is displayed as a percentage-based donut chart.
- Vehicle Type, Fuel Type, and Zone slicers were tested for interaction.
- Dashboard visuals were checked for overlap, clipping, alignment, and consistent formatting.

## Dashboard Design

The dashboard follows the project's established visual theme:

- Background: #F7F9FC
- Primary: #2F80ED
- Dark text: #17365D
- Secondary: #9CC3E6
- Highlight: #F2994A
- Visual backgrounds: White
- Font: Segoe UI

## Skills Practiced

- Power BI dashboard design
- DAX DISTINCTCOUNT
- KPI design
- Driver performance analysis
- Fleet utilization analysis
- Vehicle-type analysis
- Fuel-type analysis
- Geographic/zone analysis
- Interactive slicers
- Top N filtering
- Data visualization and business insight generation

## Conclusion

The Driver & Operations dashboard provides an operational view of driver activity, fleet composition, trip duration, fuel usage, and zone-level demand. It converts the underlying ride-hailing dataset into interactive performance indicators that can support operational analysis and further investigation.

## Screenshot

Save the completed dashboard screenshot in the project repository as:

`Screenshots/Driver-Operations.png`
