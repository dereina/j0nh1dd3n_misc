
import pandas as pd
  
  
# creating a dataframe
df = pd.DataFrame([('Bike', 'Kawasaki', 186),
                   ('Bike', 'Ducati Panigale', 202),
                   ('Car', 'Bugatti Chiron', 304), 
                   ('Car', 'Jaguar XJ220', 210),
                   ('Bike', 'Lightning LS-218', 218), 
                   ('Car', 'Hennessey Venom GT', 270),
                   ('Bike', 'BMW S1000RR', 188)],
                  columns =('Type', 'Name', 'top_speed(mph)'))

print(df)

# using groupby function with aggregation
# to get mean, min and max values
result = df.groupby('Type').agg({'top_speed(mph)': ['mean', 'min', 'max']})
  
print("Mean, min, and max values of Top Speed grouped by Vehicle Type")
print(result)






# creating a dataframe
sales_data = pd.DataFrame({
'customer_id':[3005, 3001, 3002, 3009, 3005, 3007,
               3002, 3004, 3009, 3008, 3003, 3002],
      
'salesman_id': [102, 105, 101, 103, 102, 101, 101,
                106, 103, 102, 107, 101],
  
'purchase_amt':[1500, 2700, 1525, 1100, 948, 2400,
                5700, 2000, 1280, 2500, 750, 5050]})
  
print(sales_data)

# using groupby function with aggregation 
# to get mean, min and max values
result = sales_data.groupby('salesman_id').agg({'purchase_amt': ['mean', 'min', 'max']})
  
print("Mean, min, and max values of Purchase Amount grouped by Salesman id")
print(result)








# creating a dataframe
df = pd.DataFrame({"Team": ["Radisson", "Radisson", "Gladiators",
                            "Blues", "Gladiators", "Blues", 
                            "Gladiators", "Gladiators", "Blues", 
                            "Blues", "Radisson", "Radisson"],
                     
        "Position": ["Player", "Extras", "Player", "Extras",
                     "Extras", "Player", "Player", "Player",
                     "Extras", "Player", "Player", "Extras"],
                     
        "Age": [22, 24, 21, 29, 32, 20, 21, 23, 30, 26, 20, 31],
        "Age2": [22, 24, 21, 29, 32, 20, 21, 23, 30, 26, 20, 31]})
print(df)

# using groupby function with aggregation 
# to get mean, min and max values
result = df.groupby('Team').agg({'Age': ['std', 'median','mean', 'min', 'max','sum', 'count'], 'Age2': ['mean', 'min', 'max','sum']})
result =result.reset_index()
print("Mean, min, and max values of Age grouped by Team")
print(result)

df = pd.DataFrame(
    {
        "A": [1, 1, 2, 2],
        "B": [1, 2, 3, 4],
        "C": [0.362838, 0.227877, 1.267767, -0.562860],
    }
)
print(df)
print(df.groupby(["A", "B"])[["B"]].agg(lambda x: x.astype(float).min()))