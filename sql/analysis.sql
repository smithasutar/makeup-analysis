
SELECT Market_Segment, ROUND(AVG(Price_CAD), 2) AS "Average_Price" FROM products GROUP BY Market_Segment

SELECT Market_Segment, ROUND(AVG(Rating), 2) AS "Average_Rating" FROM products GROUP BY Market_Segment

SELECT Market_Segment, COUNT(*) AS "Num_of_Products" FROM products GROUP BY Market_Segment

SELECT Product_Name, Brand, Rating FROM products ORDER BY Rating DESC LIMIT 10

SELECT 
    Product_Name, Brand, Rating, Price_CAD
FROM products 
WHERE Rating >= 4.5 
ORDER BY Price_CAD 
LIMIT 10

SELECT
    Category,
    Market_Segment,
    ROUND(AVG(Price_CAD), 2) AS Average_Price,
    ROUND(AVG(Rating), 1) AS Average_Rating,
    COUNT(*) AS Product_Count
FROM products
GROUP BY Category, Market_Segment
ORDER BY Category, Market_Segment;
