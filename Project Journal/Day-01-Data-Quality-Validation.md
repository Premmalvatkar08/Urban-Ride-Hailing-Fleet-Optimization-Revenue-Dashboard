# Day 01 — Data Quality & Validation

>> Objective

Validate the raw urban ride-hailing datasets before importing them into Power BI.

---

>> 1. Dataset Summary

| Dataset | Rows | Columns |
|---|---:|---:|
| FactTrips | 10,000 | 15 |
| DimDriver | 300 | 5 |
| DimVehicle | 300 | 4 |
| DimLocation | 12 | 5 |

---

>> 2. Duplicate Check

All four datasets were checked for duplicate records.

**Result:** No duplicate records were found.

---

>> 3. Missing Value Check

The datasets were checked for missing values.

>> FactTrips

`Cancellation_Reason` contains blank values for completed trips.

This is expected because a completed trip does not require a cancellation reason.

>> Dimension Tables

- DimDriver → No missing values
- DimVehicle → No missing values
- DimLocation → No missing values

---

>> 4. Business Rule Validation

The relationship between `Trip_Status` and `Cancellation_Reason` was validated.

Expected business rule:

- **Completed trip → Cancellation reason should be blank**
- **Cancelled trip → Cancellation reason should be populated**

The validation confirmed that the cancellation information follows the expected business logic.

---

>> 5. Numeric Value Validation

The following fields were checked for invalid values:

- Fare
- Distance_KM
- Duration_Minutes
- Driver_Rating
- Vehicle_Age

**Result:** No invalid values were identified.

---

>> 6. Relationship / Key Validation

The following relationships were checked:

- FactTrips → DimDriver
- FactTrips → DimVehicle
- FactTrips → DimLocation (Pickup)
- FactTrips → DimLocation (Drop)

All referenced IDs were validated against their corresponding dimension tables.

**Result:** No missing foreign-key references were identified.

---

>> 7. Conclusion

The raw datasets passed the initial data-quality and relational-integrity checks.

The data is ready for the next stage:

**Power Query transformation and cleaning.**

---

>> Skills Demonstrated

- Data Quality Assessment
- Missing Value Analysis
- Duplicate Detection
- Business Rule Validation
- Referential Integrity Validation
- Python
- Pandas
- Data Preparation for Power BI