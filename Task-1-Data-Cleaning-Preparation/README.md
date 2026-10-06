# Task 1: Data Cleaning & Preparation

## 📌 Task Overview
This folder contains **Task 1** of my Data Analyst Internship at **SWYNEX Technologies** — Data Cleaning & Preparation.

## 📂 Dataset
- **Source:** Airbnb in NYC (public dataset)
- **Raw file:** `Airbnb_in_NYC.csv`
- **Cleaned file:** `cleaned_airbnb_nyc.csv`

## 🧹 Cleaning Steps Performed

| Issue | Solution |
|---|---|
| Missing `name` values (2 rows) | Filled with "Unnamed Listing" |
| Missing `host_name` (1 row) | Filled with "Unknown Host" |
| Missing `reviews_per_month` (~200 rows) | Filled with 0 (no reviews yet) |
| Missing `last_review` | Kept as NaT + created `has_review` flag |
| `last_review` wrong data type | Converted to datetime |
| `id`, `host_id` wrong type | Converted to string (identifiers) |
| `room_type`, `neighbourhood_group` | Converted to category |
| Price = 0 (invalid listing) | Row removed |
| `minimum_nights` > 365 (unrealistic) | Rows removed |
| Price outliers | Capped using IQR method |

## 🛠️ Tools Used
- Python 3
- Pandas, NumPy

## ▶️ How to Run
```bash
pip install pandas numpy
python data_cleaning.py
```

## 📊 Results
- **Before:** 1000 rows, 16 columns, 400+ missing values  
- **After:** ~994 rows, 19 columns, 0 missing values  

---

## 👤 Author
**Waseque Ahmad** — Data Analyst Intern @ SWYNEX Technologies  
Intern ID: `SWX-2026-001813`

