import numpy as np

sales = np.array(
    [
        [200, 300, 250, 400],
        [150, 220, 300, 310],
        [400, 500, 450, 600],
        [100, 150, 200, 180],
    ]
)

print("Original sales dataset:\n", sales)

total_sales = np.sum(sales, axis=0)
print("Total sales per product:\n", total_sales)

average_sales_per_month = np.mean(sales, axis=1)
print("Average sales per month:\n", average_sales_per_month)

max_over_all_sales = np.argmax(total_sales) + 1
print("Product having Maximum overall sales is number", max_over_all_sales, "product")

lowest_total_sales_month = np.argmin(np.sum(sales, axis=1)) + 1
print("Month having lowest average sales is number", lowest_total_sales_month, "month")
