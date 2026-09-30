Project: Urban Ride-Hailing Fleet Optimization & Revenue Dashboard
Phase: Advanced Analytics & Scenario Analysis


## 1. Objective

The objective of Day 9 was to enhance the ride-hailing analytics solution with advanced analytical capabilities focused on demand patterns, revenue efficiency, driver performance, and scenario-based demand forecasting.

The dashboard was designed to move beyond descriptive reporting and provide business users with analytical insights that can support operational planning and decision-making.

## 2. Business Objectives

The Advanced Analytics dashboard was developed to analyze:

Hourly ride demand
Revenue generated throughout the day
Revenue efficiency per kilometer
Weekend demand contribution
Active driver participation
Relationship between trip distance and fare
Driver workload distribution
Monthly trips and revenue patterns
Potential impact of increased demand
3. KPI Development

The following KPI cards were included in the dashboard.

Peak Hour Demand

Existing DAX measure:

Peak Hour Demand =
MAXX(
    VALUES(FactTrips[Pickup_Hour]),
    [Total Trips]
)

Observed value: 935 trips

Revenue per KM
Revenue per KM =
DIVIDE(
    [Total Revenue],
    SUM(FactTrips[Distance_KM]),
    0
)

Observed value: ₹19.77 per KM

Weekend Demand %
Weekend Demand % =
DIVIDE(
    CALCULATE(
        [Total Trips],
        FactTrips[Day_Type] = "Weekend"
    ),
    [Total Trips],
    0
)

Observed value: 28.36%

Active Drivers
Active Drivers =
DISTINCTCOUNT(FactTrips[Driver_ID])

Observed value: 300 drivers

4. Advanced Visualizations
4.1 Trips by Pickup Hour

Visual Type: Line Chart

Fields:

X-axis: FactTrips[Pickup_Hour]
Y-axis: [Total Trips]

The Pickup Hour field was sorted in ascending order.

Purpose:
To identify hourly demand patterns and determine periods of relatively high and low ride activity.

4.2 Revenue by Pickup Hour

Visual Type: Clustered Column Chart

Fields:

X-axis: FactTrips[Pickup_Hour]
Y-axis: [Total Revenue]

Purpose:
To analyze revenue generation across different hours of the day and compare revenue patterns with trip demand.

4.3 Trip Distance vs Fare

Visual Type: Scatter Chart

Fields:

X-axis: FactTrips[Distance_KM]
Y-axis: FactTrips[Fare]
Details: FactTrips[Trip_ID]

A visual-level filter was applied:

Trip_Status = Completed

Purpose:
To examine the relationship between trip distance and fare while excluding cancelled trips from the analysis.

4.4 Top 10 Drivers by Trips

Visual Type: Clustered Bar Chart

Fields:

Y-axis: DimDriver[Driver_ID]
X-axis: [Total Trips]

A Top N = 10 filter was applied using [Total Trips].

Purpose:
To identify drivers handling the highest number of trips and provide a view of workload concentration across the driver fleet.

4.5 Monthly Trips vs Revenue

Visual Type: Line and Clustered Column Chart

Fields:

X-axis: DimDate[Month Name]
Column Y-axis: [Total Trips]
Line Y-axis: [Total Revenue]

The month field was arranged chronologically using the previously configured month-number sorting.

Purpose:
To compare monthly ride volume and revenue performance within a single visual.

5. What-If Analysis

A Demand Increase % What-If parameter was introduced to support scenario analysis.

Parameter configuration
Setting	Value
Parameter	Demand Increase %
Data Type	Decimal Number
Minimum	0
Maximum	0.50
Increment	0.05
Default	0

A slicer was automatically added to the dashboard to allow users to adjust the demand-growth assumption.

6. Projected Trips Measure

The following DAX measure was created:

Projected Trips =
[Total Trips] *
(
    1 +
    SELECTEDVALUE(
        'Demand Increase %'[Demand Increase %],
        0
    )
)
Scenario interpretation

At 0% demand increase:

Projected Trips = 10,000

At 10% demand increase:

Projected Trips ≈ 11,000

This provides a simple scenario-planning mechanism that allows users to examine how changes in demand assumptions could affect expected trip volume.

7. Dashboard Design

The Advanced Analytics page followed the established project design system.

Color Palette
Dark Navy: #17365D
Primary Blue: #2F80ED
Secondary Blue: #9CC3E6
Highlight Orange: #F2994A
Background: #F7F9FC
Visual Background: #FFFFFF
Typography
Font: Segoe UI
Main title: 20–22 pt, Bold
Subtitle: 10–11 pt
Dark navy used for headings and important KPI values

The dashboard was designed with minimal borders and consistent spacing to maintain visual consistency with the other report pages.

8. Business Insights

The completed analysis generated the following observations:

8.1 Peak Demand

The highest hourly demand reached 935 trips, highlighting the importance of identifying peak operating periods.

8.2 Hourly Demand Pattern

Trip demand was relatively lower during early hours and increased during later daytime and evening periods.

8.3 Revenue Efficiency

The dashboard recorded approximately ₹19.77 revenue per kilometer, providing a useful measure of revenue efficiency.

8.4 Weekend Contribution

Weekend trips represented approximately 28.36% of total demand in the dataset.

8.5 Driver Activity

All 300 drivers were represented in trip activity, indicating broad participation across the modeled driver fleet.

8.6 Distance and Fare Relationship

The scatter analysis showed a generally positive relationship between trip distance and fare, indicating that longer completed trips tend to be associated with higher fares in the generated dataset.

8.7 Driver Workload

The Top 10 driver analysis highlights differences in trip volumes across drivers and provides a basis for examining workload distribution.

8.8 Scenario Planning

The What-If analysis allows management to test hypothetical demand-growth scenarios. For example, a 10% increase applied to the baseline of 10,000 trips produces approximately 11,000 projected trips.

9. Validation

The following validation activities were completed:

Verified KPI measures against existing DAX calculations.
Confirmed Pickup Hour was sorted chronologically.
Verified the Top 10 driver filter.
Confirmed the scatter chart uses completed trips.
Checked the monthly trips and revenue comparison.
Tested the What-If parameter at different demand assumptions.
Verified the Projected Trips calculation.
Checked visual titles and formatting.
Confirmed consistent colors and typography.
Reviewed the final dashboard for alignment and readability.
10. Final Outcome

The Advanced Analytics dashboard successfully extends the project from descriptive reporting to more analytical and scenario-based reporting.

The page combines:

Demand Analysis → Revenue Efficiency → Driver Performance → Relationship Analysis → Scenario Planning

The What-If parameter adds an interactive planning component, while the advanced visuals provide a more detailed understanding of demand and operational performance.

11. Portfolio Skills Demonstrated

This stage demonstrates practical experience with:

Advanced Power BI visualization
DAX measure development
What-If parameters
Scenario analysis
Top N analysis
Scatter plot analysis
Time-series analysis
KPI development
Business-oriented dashboard design
Analytical storytelling
12. Deliverables
Advanced Analytics Power BI dashboard
Advanced DAX measures
Demand Increase % What-If parameter
Projected Trips measure
Business insights
Dashboard screenshot
Day 9 project journal