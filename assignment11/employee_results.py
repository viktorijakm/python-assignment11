import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database (relative path from assignment11)
conn = sqlite3.connect("../db/lesson.db")

# SQL query to calculate revenue per employee
query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

# Load query results into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(employee_results['last_name'], employee_results['revenue'], color='teal')
plt.title("Employee Revenue")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()