import pandas
import pandasql

library_inventory = pandas.read_csv('Library Inventory.csv')
sample_customer_inventory = pandas.read_csv("1234567890987 Customer Inventory.csv")

# This query shows what books/games we have in our library has and how many copies of each. This can show the popularity of each item
# and whether we should get more copies of specific items, depending on demand. This also shows customers what we have.
query1 = """
SELECT Title, "Total Copies"
FROM library_inventory
"""
print("Query 1: The title of each book/game in our inventory and how many we have.")
result1 = pandasql.sqldf(query1)
print(result1)

# This query shows what this specific sample user has checked out, sorted by type. This way they can see what kinds of things
# they must return and what fees are associated with them.
query2 = """
SELECT "Item Name", Type
FROM sample_customer_inventory
ORDER BY Type
"""

print("Query 2: The items this user has checked sorted by type")
result2 = pandasql.sqldf(query2)
print(result2)

# This shows the library staff which book is the most sought after so they know to increase it's stock when they can.
query3 = """
SELECT Title, MAX("Copies Checked Out")
FROM library_inventory
"""

print("Query 3: The most popular item in terms of having the most copies checked out.")
result3 = pandasql.sqldf(query3)
print(result3)

# This shows whether the books or games are more checked out so the library knows where to put their attention
query4 = """
SELECT "Item Type", AVG("Copies Checked Out")
FROM library_inventory
GROUP BY "Item Type"
"""

print("Query 4: Each item type and the average number of copies checked out")
result4 = pandasql.sqldf(query4)
print(result4)
