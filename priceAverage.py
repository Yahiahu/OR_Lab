import numpy as np
import pandas as pd
from tqdm import tqdm 
import math

df = pd.read_csv('product demand.csv')

df.columns

print(df.head())
all_products = set(df['Product_Num'].tolist())
results_dictionary = {}
# took 253 seconds to run -- approximately 4.2 minutes

# Loop over all products to calculate the demand
for prod in tqdm(all_products, desc="Processing Products"):
    # Initialize a variable to store the sum of demands for the product
    sum_demand = 0

    # Iterate over the years from 1997 to 2003
    for year in range(1997, 2004):  # Note the range is 1997 to 2004 because the upper bound is exclusive
        # Filter DataFrame for the specific product, in February, and in the specific year
        df_specific_product = df[(df['Product_Num'] == prod) & (df['Month'] == 2) & (df['Year'] == year)]

        # Add the demand for the specific year to the sum
        sum_demand += df_specific_product['Demand'].sum()

    # Multiply the total demand by 2
    total_demand = 2/6 * sum_demand
    
    # Store the result in the dictionary
    results_dictionary[prod] = total_demand
data = []
# Looping over all products
for prod in all_products:
  data.append([prod,math.ceil(results_dictionary[prod])])

    
collected_data = pd.DataFrame(data, columns=['Product_Num', 'Est_Demand_All_Years'])
collected_data.to_csv('double_demand.csv')

collected_data.head(50)
