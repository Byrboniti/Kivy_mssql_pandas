import pandas as pd
from connection_db import Connection
from datetime import date, timedelta

start_date = date(2022,1,1)
end_date = start_date + timedelta(days=30)

query = "SELECT sales_date, article, sales FROM sales WHERE sales_date BETWEEN @start_date AND @end_date"

df = pd.read_sql(query, Connection, params={'start_date': start_date, 'end_date': end_date})

df['year'] = df['sales_date'].dt.year
df['month'] = df['sales_date'].dt.month
df['avg_sales_per_month'] = df.groupby(['year', 'month', 'article'])['sales'].transform('mean')
df['sales_share'] = df.groupby(['year', 'month', 'article'])['sales'].transform(lambda x: x / x.sum())

df = df[['year', 'month', 'article', 'avg_sales_per_month', 'sales_share']]
df.to_excel("sales_report.xlsx", index=False)
