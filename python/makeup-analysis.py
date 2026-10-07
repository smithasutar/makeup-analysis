import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

df = pd.read_csv("data/raw_makeup.csv")

drugstore_brands = [
    "Milk Makeup",
    "E.l.f.",
    "IT Cosmetics",
    "ColourPop",
]

professional_brands = [
    "Make Up For Ever",
    "Kiehl’s",
    "NARS",
    "Farsali",
    "Yves Saint Laurent",
    "Morphe",
    "Bite Beauty",
    "Sisley",
    "KVD Beauty",
    "Glossier",
    "Becca",
    "Huda Beauty",
    "RMS Beauty",
    "Bobby Brown",
    "Ilia Beauty",
    "Clinique",
    "Rare Beauty",
    "Tatcha",
    "Too Faced",
    "Kylie Cosmetics",
    "Shiseido",
    "Anastasia Beverly Hills",
    "Juvia’s Place",
    "Drunk Elephant",
    "Hourglass",
    "Natasha Denona",
    "Fenty Beauty",
    "Charlotte Tilbury",
    "Tarte",
    "Danessa Myricks",
    "Bourjois",
    "Urban Decay",
    "Laura Mercier",
    "Perricone MD",
    "Patrick Ta",
    "Pat McGrath Labs",
]

brand_segment = {
    "Make Up For Ever": "Professional",
    "Kiehl’s": "Professional",
    "NARS": "Professional",
    "Farsali": "Professional",
    "Yves Saint Laurent": "Professional",
    "Morphe": "Professional",
    "Bite Beauty": "Professional",
    "Sisley": "Professional",
    "KVD Beauty": "Professional",
    "Glossier": "Professional",
    "Becca": "Professional",
    "Huda Beauty": "Professional",
    "RMS Beauty": "Professional",
    "Bobby Brown": "Professional",
    "Ilia Beauty": "Professional",
    "Clinique": "Professional",
    "Rare Beauty": "Professional",
    "Tatcha": "Professional",
    "Too Faced": "Professional",
    "Kylie Cosmetics": "Professional",
    "Shiseido": "Professional",
    "Anastasia Beverly Hills": "Professional",
    "Juvia’s Place": "Professional",
    "Drunk Elephant": "Professional",
    "Hourglass": "Professional",
    "Natasha Denona": "Professional",
    "Fenty Beauty": "Professional",
    "Charlotte Tilbury": "Professional",
    "Tarte": "Professional",
    "Danessa Myricks": "Professional",
    "Bourjois": "Professional",
    "Urban Decay": "Professional",
    "Laura Mercier": "Professional",
    "Perricone MD": "Professional",
    "Patrick Ta": "Professional",
    "Pat McGrath Labs": "Professional",
    "Milk Makeup": "Drugstore",
    "E.l.f.": "Drugstore",
    "IT Cosmetics": "Drugstore",
    "ColourPop": "Drugstore",
}

df["Market_Segment"] = df["Brand"].map(brand_segment)
df["Price_CAD"] = df["Price_USD"]*1.43

#Mean of professional makeup - mean of drugstore makeup
# print(df.groupby("Market_Segment")["Rating"].mean().round(2))
mean_r_dm = df[df["Market_Segment"] == "Drugstore"]["Rating"].mean().round(2)
mean_r_pm = df[df["Market_Segment"] == "Professional"]["Rating"].mean().round(2)

# print("The ratings difference is: ", ((mean_r_dm-mean_r_pm)/mean_r_dm).round(2)*100, "%");

#Calculate price premium
mean_p_dm = df[df["Market_Segment"] == "Drugstore"]["Price_CAD"].mean().round(2)
mean_p_pm = df[df["Market_Segment"] == "Professional"]["Price_CAD"].mean().round(2)
# print("The price premium is: ", (((mean_p_dm-mean_r_pm)/mean_p_dm).round(2))*100, "%")

#Check each category rating value score
category_price_means = df.groupby(["Category","Market_Segment"])["Price_CAD"].mean().unstack().round(2)
category_rating_means = df.groupby(["Category","Market_Segment"])["Rating"].mean().unstack().round(2)

value_scores = pd.DataFrame()
value_scores["Drugstore Value Score"] = ((category_rating_means["Drugstore"] / category_price_means["Drugstore"])*100).round(0)
value_scores["Professional Value Score"] = ((category_rating_means["Professional"] / category_price_means["Professional"])*100).round(0)

# print(value_scores["Professional Value Score"]-value_scores["Drugstore Value Score"])

#Does rating increase as price increases?
correlation = df["Price_CAD"].corr(df["Rating"])
# print(correlation)

avg_price = df.groupby("Market_Segment")["Price_CAD"].mean()

avg_price.plot(kind="bar")

plt.title("Average Makeup Price: Professional vs Drugstore")
plt.ylabel("Average Price ($)")
plt.xlabel("Makeup Segment")
plt.xticks(rotation=0)

plt.show()

for segment in df["Market_Segment"].unique():

    subset = df[df["Market_Segment"] == segment]

    plt.scatter(
        subset["Price_CAD"],
        subset["Rating"],
        label=segment
    )

plt.xlabel("Price ($)")
plt.ylabel("Rating")
plt.title("Price vs Customer Rating")
plt.legend()

plt.show()


conn = sqlite3.connect("makeup.db")
df.to_sql("products", conn, if_exists="replace", index=False)


#Average price by market segment
query = """
SELECT Market_Segment, ROUND(AVG(Price_CAD), 2) AS "Average_Price" FROM products GROUP BY Market_Segment
"""
result = pd.read_sql_query(query, conn)
print(result)

#Average rating by segment
query = """
SELECT Market_Segment, ROUND(AVG(Rating), 2) AS "Average_Rating" FROM products GROUP BY Market_Segment
"""
result = pd.read_sql_query(query, conn)
print(result)

#Count the Products
query = """
SELECT Market_Segment, COUNT(*) AS "Num_of_Products" FROM products GROUP BY Market_Segment
"""
result = pd.read_sql_query(query, conn)
print(result)

#Find the highest-rated products
query = """
SELECT Product_Name, Brand, Rating FROM products ORDER BY Rating DESC LIMIT 10
"""
result = pd.read_sql_query(query, conn)
print(result)

#Find highly-rated AND cheap products
query = """
SELECT 
    Product_Name, Brand, Rating, Price_CAD
FROM products 
WHERE Rating >= 4.5 
ORDER BY Price_CAD 
LIMIT 10
"""
result = pd.read_sql_query(query, conn)
print(result)

#Compare by category and market segment
query = """
SELECT
    Category,
    Market_Segment,
    ROUND(AVG(Price_CAD), 2) AS Average_Price,
    ROUND(AVG(Rating), 1) AS Average_Rating,
    COUNT(*) AS Product_Count
FROM products
GROUP BY Category, Market_Segment
ORDER BY Category, Market_Segment;
"""
result = pd.read_sql_query(query, conn)
print(result)

conn.close()

df.to_csv("cleaned_makeup.csv", index=False)