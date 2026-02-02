import numpy as np 
# Example dataset: products and sales
products = ["Shampoo","Soap","Toothpaste","Oil","Rice"]
sales = np.array([120,200,150,80,300])

# Basic Analysis
total_sales = np.sum(sales)
average_sales = np.mean(sales)
best_selling = products[np.argmax(sales)]
worst_selling = products[np.argmin(sales)]

#Output
print("Total Sales: ",total_sales)
print("Average sales: ",average_sales)
print("Best-selling product: ",best_selling)
print("Worst-selling Product: ",worst_selling)

import matplotlib.pyplot as plt 
 
plt.bar(products,sales,color='lightgreen')
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.show()