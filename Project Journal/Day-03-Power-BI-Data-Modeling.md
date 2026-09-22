# Day 03 — Power BI Data Modeling & Star Schema

--> Objective

Build and validate a professional star-schema data model for the urban ride-hailing analytics project.

--> 1. Tables Used

- FactTrips
- DimDate
- DimDriver
- DimVehicle
- DimLocation
- DimDropLocation

--> 2. Date Dimension

Created a dedicated `DimDate` table containing:

- Date
- Year
- Month Number
- Month Name
- Quarter
- Day
- Day Name
- Day Number
- Week Number

`DimDate` was marked as the official Power BI Date Table.

--> 3. Relationships

Created the following active relationships:

- DimDate → FactTrips
- DimDriver → FactTrips
- DimVehicle → FactTrips
- DimLocation → FactTrips through Pickup_Location_ID
- DimDropLocation → FactTrips through Drop_Location_ID

All relationships use:

- One-to-many cardinality
- Single cross-filter direction
- Active status

--> 4. Role-Playing Location Dimension

Because FactTrips contains both pickup and drop location keys, a separate `DimDropLocation` table was created.

This avoids ambiguous filtering and allows pickup and drop locations to be analyzed independently.

--> 5. Model Validation

The model was tested using report visuals.

The following relationships were successfully validated:

- Date filtering
- Driver filtering
- FactTrips interaction with dimension tables

No relationship errors were identified.

--> 6. Star Schema Structure

The final model follows a star-schema design with:

**FactTrips** as the central fact table and dimension tables surrounding it.

--> 7. Conclusion

The Power BI data model has been successfully created and validated.

The model is now ready for the next stage:

**DAX Measures and Business KPI Development.**

--> Skills Demonstrated

- Power BI Data Modeling
- Star Schema Design
- Relationship Management
- Date Dimension
- Role-Playing Dimensions
- Cardinality
- Cross-Filter Direction
- Data Model Validation