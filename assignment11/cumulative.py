import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query to get order_id and total_price per order
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

# Load query results into DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Add cumulative revenue column using cumsum()
df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs order_id
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', color='blue')
plt.title("Cumulative Revenue by Order ID")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
