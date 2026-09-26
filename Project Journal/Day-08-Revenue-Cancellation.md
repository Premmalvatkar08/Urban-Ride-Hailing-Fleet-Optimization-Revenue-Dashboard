# Day 08 — Revenue & Cancellation Dashboard

## Objective
Analyze revenue performance, payment behavior, cancellation patterns, and location-level cancellation activity using Power BI.

## Business Questions
1. How much revenue is generated?
2. How much revenue comes from completed trips?
3. What is the revenue generated per trip?
4. What is the cancellation rate?
5. How does revenue change month by month?
6. Which vehicle types generate the most revenue?
7. How are trips distributed across payment types?
8. What are the major cancellation reasons?
9. Which pickup locations have the highest cancellation activity?

## DAX Measures Used
- Total Revenue
- Completed Trip Revenue
- Revenue per Trip
- Cancellation Rate
- Cancelled Trips
- Total Trips

## KPI Cards
- Total Revenue — ₹1.54M
- Completed Trip Revenue — ₹1.54M
- Revenue per Trip — ₹153.64
- Cancellation Rate — 11.94%

## Dashboard Visuals

### Monthly Revenue Trend
**Visual Type:** Line Chart
Revenue falls from January to February, rises in March, dips slightly in April, reaches the highest visible level in May, and dips slightly in June.

### Revenue by Vehicle Type
**Visual Type:** Clustered Column Chart
- Hatchback — approximately ₹0.52M
- SUV — approximately ₹0.50M
- Sedan — approximately ₹0.48M

### Trips by Payment Type
**Visual Type:** Donut Chart
The displayed payment methods have a relatively balanced trip distribution, with each category contributing roughly one-fifth of trips.

### Cancelled Trips by Cancellation Reason
**Visual Type:** Clustered Bar Chart
- Driver Cancelled — approximately 245
- Driver Unavailable — approximately 236
- Customer Cancelled — approximately 224

### Cancelled Trips by Location
**Visual Type:** Clustered Bar Chart
- Airoli — approximately 112
- Bandra — approximately 108
- Dadar — approximately 108

## Slicers
- Vehicle Type
- Payment Type
- Location Name

## Business Insights
1. Total revenue is approximately ₹1.54M and completed-trip revenue is also approximately ₹1.54M.
2. Revenue per trip is approximately ₹153.64.
3. May has the highest visible monthly revenue, while February has the lowest visible level.
4. Hatchbacks generate the highest visible revenue at approximately ₹0.52M, followed by SUVs at approximately ₹0.50M and Sedans at approximately ₹0.48M.
5. The overall cancellation rate is 11.94%. Driver Cancelled is the largest displayed cancellation-reason category.
6. Airoli has the highest visible cancellation count at approximately 112, followed by Bandra and Dadar at approximately 108 each.
7. Payment methods are relatively balanced in the displayed trip distribution.

## Validation
- KPI values checked.
- Monthly revenue sorted chronologically.
- Vehicle revenue sorted descending.
- Blank cancellation reasons excluded.
- Cancellation charts sorted by count.
- Vehicle Type, Payment Type, and Location slicers tested.
- Visual alignment, readability, and clipping checked.

## Dashboard Design
- Background: #F7F9FC
- Primary: #2F80ED
- Dark text: #17365D
- Secondary: #9CC3E6
- Highlight: #F2994A
- Visual backgrounds: White
- Font: Segoe UI

## Skills Practiced
Power BI dashboard design, revenue analysis, cancellation analysis, DAX, KPI creation, time-series analysis, payment analysis, vehicle revenue comparison, location analysis, interactive slicers, and business insight generation.

## Conclusion
The Revenue & Cancellation dashboard provides a focused view of financial performance and operational losses associated with cancelled trips through interactive revenue, payment, cancellation-reason, and location analyses.

## Screenshot
Save as: `Screenshots/Revenue-Cancellation.png`
