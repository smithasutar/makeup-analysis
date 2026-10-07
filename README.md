# Makeup Data Analysis: Professional vs. Drugstore

## Project Overview

This project analyzes makeup products to determine whether professional makeup is worth the additional cost compared to drugstore makeup.

Using Python, SQL, and Power BI, I analyzed product prices, ratings, market segments, and makeup categories to identify pricing patterns and determine which products and categories provide the best value.

## Business Questions

The analysis focuses on the following questions:

* Is professional makeup significantly more expensive than drugstore makeup?
* Does a higher price generally correspond to a higher product rating?
* Which makeup categories provide the best value?
* How large is the price premium for professional makeup?
* Does professional makeup provide enough additional value to justify its higher price?

## Tools & Technologies

* **Python** — Data cleaning and analysis
* **Pandas** — Data manipulation and analysis
* **SQL / SQLite** — Data querying and analysis
* **Power BI** — Data visualization and dashboard development
* **Git & GitHub** — Version control and project documentation

## Data Preparation

The dataset was cleaned and prepared for analysis by:

* Inspecting and cleaning the raw dataset
* Handling relevant data inconsistencies
* Converting product prices from USD to CAD
* Creating a `Market_Segment` classification for Professional and Drugstore products
* Preparing the data for SQL and Power BI analysis

## Analysis

The analysis compares Professional and Drugstore makeup using:

### Price Analysis

* Average drugstore product price
* Average professional product price
* Professional price premium

### Rating Analysis

* Average product ratings
* Relationship between product price and rating

### Value Analysis

A value score was calculated by comparing product ratings relative to price.

Higher value scores indicate products that provide a higher rating relative to their price.

### Category Analysis

Makeup categories were compared to identify which categories provide the best value for consumers.

## Power BI Dashboard

The Power BI dashboard provides an interactive overview of the analysis, including:

* Average Drugstore Price
* Average Professional Price
* Professional Price Premium
* Best Value Category
* Price vs. Rating Scatter Plot
* Professional vs. Drugstore comparisons

### Dashboard Preview

*Add a screenshot of the completed Power BI dashboard here.*

## Project Structure

```text
makeup-data-analysis/
│
├── data/
│   ├── raw_makeup.csv
│   └── cleaned_makeup.csv
│
├── python/
│   └── makeup_analysis.py
│
├── sql/
│   └── makeup_analysis.sql
│
├── powerbi/
│   ├── makeup_dashboard.pbix
│   └── powerbi_dashboard.png
│
├── README.md
└── requirements.txt
```

## Key Skills Demonstrated

This project demonstrates experience with:

* Data cleaning
* Exploratory data analysis
* Data manipulation with Pandas
* SQL querying
* Data aggregation
* Data visualization
* Business problem solving
* Comparative analysis
* KPI development
* Dashboard development
* Data-driven decision making
* Git/GitHub

## Conclusion

The goal of this project is to use data to evaluate whether the higher price of professional makeup is supported by higher ratings and better overall value.

The analysis demonstrates how raw product data can be transformed into meaningful insights that can support consumer and business decision-making.

To answer the main question no drugstore makeup is not worth the cost because when comparing the premium prices and ratings there is a much larginer price margin compared to ratings.
