# Day 02 — Power Query Data Transformations

--> Objective

Transform and standardize the raw ride-hailing datasets in Power Query before building the Power BI data model.

---

--> 1. Tables Imported

The following datasets were imported into Power BI:

- FactTrips
- DimDriver
- DimVehicle
- DimLocation

---

--> 2. Data Type Standardization

Correct data types were applied to identifiers, dates, times, numeric measures, and categorical fields.

Identifiers such as Trip_ID, Driver_ID, Vehicle_ID, and Location_ID were stored as text because they are keys rather than numerical measures.

---

--> 3. FactTrips Transformations

The following transformations were performed:

- Trimmed and cleaned text fields
- Standardized categorical text values
- Created Pickup_Hour
- Created Day_Name
- Created Day_Type
- Created Month_Name
- Created Month_Number
- Created Distance_Category
- Created Duration_Category

--># Analytical Categories

**Day_Type**
- Weekday
- Weekend

**Distance_Category**
- Short
- Medium
- Long

**Duration_Category**
- Short
- Medium
- Long

---

--> 4. Dimension Transformations

--># DimDriver

- Standardized data types
- Trimmed and cleaned text fields
- Validated driver-related fields

--> DimVehicle

- Standardized data types
- Trimmed and cleaned text fields
- Validated vehicle-related fields

--># DimLocation

- Standardized data types
- Trimmed and cleaned text fields
- Validated geographic numeric fields

---

--> 5. Missing Value Handling

`Cancellation_Reason` contains blank values for completed trips.

These values were intentionally retained because the field is only applicable to cancelled trips.

Cancelled trips were validated to ensure that cancellation reasons are populated.

---

--> 6. Validation

The transformed datasets were validated for:

- Correct data types
- Valid categorical values
- Analytical categories
- Date and time-derived columns
- Query errors
- Expected number of FactTrips columns

FactTrips contains the original 15 columns plus 7 analytical columns.

---

--> 7. Conclusion

The raw ride-hailing datasets were successfully transformed and standardized using Power Query.

The data is now ready for the next stage:

**Power BI Data Modeling and Star Schema Design.**

---

--> Skills Demonstrated

- Power Query
- Data Cleaning
- Data Transformation
- Data Type Management
- Conditional Columns
- Feature Engineering
- Data Validation
- Power BI Data Preparation