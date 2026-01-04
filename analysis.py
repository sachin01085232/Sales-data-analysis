import pandas as pd 
import numpy as np 

df = pd.read_csv('clean_dataset.csv')


# Region-wise total & avg sales

region_wise_avg_sales = df.groupby('region')['sales_amount'].mean('sales_amount')
print(region_wise_avg_sales)

# quantity wise order
quantity_wise = df.groupby('product_category')['quantity'].count()
print(quantity_wise.sort_values(ascending=False))

# Top 5 highest revenue orders

top_5 = df.sort_values(by='sales_amount',ascending=False).head(5)[
   ['order_id', 'sales_amount', 'region', 'order_date']
]
print(top_5)
# Q Sales trend (monthly / yearly)    
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# exclulde month 
df['order_month'] = df['order_date'].dt.to_period('M')

monthly_sales = df.groupby('order_month')['sales_amount'].sum().reset_index() 
print(monthly_sales)

# yearly salary exclude from order date
df['order_year'] = df['order_date'].dt.to_period('Y')

yearly_sales = df.groupby('order_year')['sales_amount'].sum().reset_index() 
print(yearly_sales)

# Which product category performs best?

best_performs =  df.groupby('product_category')['sales_amount'].sum().round().astype('int64').sort_values(ascending=False)
print(best_performs) 

   # Returned orders % and impact on revenue 

total_revenue = df['sales_amount'].sum()

Returned_revenue= df.loc[df['returned'] == "Yes",'sales_amount'].sum().round()
print('return order',Returned_revenue)  

impact_percentage = ((Returned_revenue/total_revenue)*100).round()
# 2f ko 2 decial point tk rhkega 
print(f"Impact on revenue (%): {impact_percentage:.2f}%")

