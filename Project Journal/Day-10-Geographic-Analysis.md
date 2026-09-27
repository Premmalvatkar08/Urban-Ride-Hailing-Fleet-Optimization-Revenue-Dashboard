## Phase: Dashboard Development & Business Intelligence


## 1. Objective

The objective of Day 10 was to develop a Geographic Analysis dashboard to evaluate ride-hailing activity across pickup locations, drop locations, and operational zones.

The analysis focuses on identifying geographic patterns in trip demand, revenue generation, and cancellation activity. These insights can support management in understanding demand concentration and identifying locations that may require greater operational attention.

--

## 2. Business Requirements
The dashboard was designed to address the following business questions:

1. Which locations generate the highest pickup demand?
2. Which locations receive the highest number of trips?
3. Which zones contribute the most to overall trip activity?
4. Which pickup locations generate the highest revenue?
5. Where are cancellations most concentrated?
6. Do high-demand locations also contribute significantly to revenue?
7. Which locations may require further investigation from an operational perspective?

--

## 3. Data Model Used
The geographic analysis was implemented using the existing Power BI star-schema model.

Fact Table - FactTrips
Relevant fields:
    Pickup_Location_ID
    Drop_Location_ID
    Fare
    Trip_Status

Dimension Tables - DimLocation
    Location_ID
    Location_Name
    Zone
    Latitude
    Longitude

DimDropLocation

A role-playing copy of the location dimension used specifically for analyzing drop locations independently from pickup locations.

Relevant Relationships
DimLocation
     │
     │ Pickup Location
     ▼
  FactTrips
     ▲
     │ Drop Location
     │
DimDropLocation

This structure allows pickup and drop locations to be analyzed independently while maintaining the existing star-schema architecture.

--

## 4. DAX Development
A new measure was created to determine the number of locations actively represented in the trip data.

Active Pickup Locations =
DISTINCTCOUNT(FactTrips[Pickup_Location_ID])

Existing measures reused in the dashboard included:

Total Revenue =
SUM(FactTrips[Fare])

and

Cancelled Trips =
CALCULATE(
    [Total Trips],
    FactTrips[Trip_Status] = "Cancelled"
)

Using existing measures instead of creating duplicate calculations ensured consistency across dashboard pages.

--

## 5. Key Findings
The completed dashboard produced the following observations from the project dataset.

7.1 Geographic Coverage
The dashboard contains 12 active pickup locations, providing coverage across multiple urban areas represented in the dataset.

7.2 Pickup Demand
Airoli recorded the highest pickup activity, followed by locations including Ghansoli, Ghatkopar, and Powai.
This indicates that these locations represent important trip-origin points within the dataset.

7.3 Drop Demand
Airoli also recorded the highest number of drop-offs, while Bandra, Ghatkopar, and Thane were among the other high-volume destinations.
Comparing pickup and drop distributions provides a better understanding of movement patterns across the service network.

7.4 Zone-Level Demand
The zone analysis shows approximately:
Central: 3.4K trips
Navi Mumbai: 3.4K trips
North: 1.6K trips
West: 1.6K trips
This indicates that trip activity is concentrated more heavily in the Central and Navi Mumbai zones within the generated dataset.

7.5 Revenue Distribution
Airoli generated approximately ₹143K in revenue, followed by Ghansoli and Ghatkopar at approximately ₹136K each.
This demonstrates that several high-volume pickup locations also make substantial contributions to revenue.

7.6 Cancellation Distribution
Airoli recorded the highest cancellation count at approximately 112, followed by Bandra and Dadar.
Locations with relatively high cancellation volumes can be investigated further using additional operational information such as driver availability, waiting time, and cancellation reasons.

--

## 6. Business Interpretation

The geographic analysis demonstrates that ride demand and revenue are not distributed uniformly across all locations.

High-activity areas can potentially require greater attention when planning:
    - Driver allocation
    - Fleet positioning
    - Demand monitoring
    - Operational capacity
    - Service availability

However, the dashboard identifies patterns rather than causes. Additional operational data would be required to determine why particular locations experience higher demand or cancellation activity.

--

## 7. Final Outcome
The Geographic Analysis dashboard successfully adds a location-focused analytical layer to the Urban Ride-Hailing project.
The page integrates:

Demand → Geography → Revenue → Cancellations

This allows users to move from identifying high-demand locations to understanding their revenue contribution and cancellation activity.
The completed dashboard strengthens the overall portfolio project by demonstrating practical application of Power BI data modeling, DAX, dimensional analysis, visualization design, and business insight generation.

--

## 8. Deliverables

- Geographic Analysis Power BI dashboard page
- Day-10-Geographic-Analysis.md
- Geographic-Analysis.png
- Active Pickup Locations DAX measure
- Geographic business insights
- Dashboard validation