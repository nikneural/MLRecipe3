import pandas as pd

employee_data = {'employee_id': ['1', '2', '3', '4'],
                 'name': ['Amy Jones', 'Allen Keys', 'Alice Bees', 'Tim Hotron']}
dataframe_employees = pd.DataFrame(employee_data, columns=['employee_id', 'name'])

sales_data = {'employee_id': ['3', '4', '5', '6'],
              'total_sales': [23456, 2512, 2345, 1455]}
dataframe_sales = pd.DataFrame(sales_data, columns=['employee_id', 'total_sales'])

print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id')) # внутренее соединение
print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer'))
