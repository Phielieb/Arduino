import pandas as pd
value_set =pd.read_csv("/home/pi/Arduino/Data/Moist_Val.csv")
print(value_set)
value_set = value_set[['Timestamp','Moist_Val']]
print(value_set)
