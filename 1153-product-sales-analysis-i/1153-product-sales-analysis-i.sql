# Time: O(n) as we're iterating over all the rows of Sales Table
# Space: O(1) as we're not using any extra memory 
SELECT
    p.product_name, s.year, s.price
FROM
    Sales s
JOIN 
    Product p
ON

    s.product_id = p.product_id;