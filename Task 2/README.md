# Task 2: Exploratory Data Analysis (EDA)

## 🎯 Objective
Perform exploratory data analysis on the cleaned Airbnb NYC dataset to identify trends, distributions, relationships, and patterns.

## 📊 Dataset
**cleaned_airbnb_nyc.csv** (cleaned in Task 1)

## 🔍 Analysis Performed

### 1. Basic Statistics
- Checked dataset shape, columns, and data types
- Generated numerical summary (`describe()`)
- Verified missing values (none remaining)

### 2. Univariate Analysis
- **Room Type Distribution:** Count and percentage of each room type
- **Neighbourhood Group Distribution:** Listings by borough
- **Price Statistics:** Mean, median, std dev, min, max
- **Price Distribution:** Histogram with KDE + Box plot

### 3. Bivariate Analysis
- **Average Price by Room Type:** Compared mean prices across room types
- **Average Price by Neighbourhood Group:** Compared mean prices across boroughs
- **Room Type vs Neighbourhood:** Stacked bar chart showing distribution

### 4. Geospatial Analysis
- Scatter plot of listings across NYC using longitude/latitude
- Size of points = price, color = neighbourhood group

### 5. Correlation Analysis
- Correlation matrix of numerical features:
  `price`, `minimum_nights`, `number_of_reviews`, `reviews_per_month`, `calculated_host_listings_count`, `availability_365`
- Heatmap visualization

### 6. Top Performers
- **Top 10 Neighbourhoods** by number of listings
- **Top 10 Hosts** by number of listings

## 📈 Visualizations Created
| # | Chart | File |
|---|-------|------|
| 1 | Room Type Distribution | `Distribution by Room_Types.png` |
| 2 | Listings by Neighbourhood Group | `Distribution by Neighbourhood Group.png` |
| 3 | Price Distribution (Histogram + Box) | `Distribution of Price.png` |
| 4 | Average Price by Room Type | `Price by Room Type.png` |
| 5 | Average Price by Borough | `Price by Borough.png` |
| 6 | Room Type by Borough (Stacked) | `Room Type by Borough.png` |
| 7 | Geospatial Distribution | `Geospatial Distribution.png` |
| 8 | Correlation Matrix | `Correlation_Matrix.png` |
| 9 | Top 10 Neighbourhoods | `Top 10 Neighbourhood.png` |
| 10 | Top 10 Hosts | `Top Host.png` |

## 💡 Key Insights
- **Room type** and **neighbourhood group** significantly impact price
- **Manhattan** has the highest average price among boroughs
- **Entire home/apt** listings are priced higher than private/shared rooms
- Most listings are concentrated in **Manhattan and Brooklyn**
- Weak correlation between price and most numerical features
- A few hosts own a large number of listings (top hosts dominate)

## 🛠️ Tools Used
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

## 📁 Files
- `task2_swynex.ipynb` — Full EDA code
- `Charts/` — All visualization PNGs
- `cleaned_airbnb_nyc.csv` — Dataset used
