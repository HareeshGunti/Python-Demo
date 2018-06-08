# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

#####
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)

print('##########')
# Print out country column as Pandas Series
print(cars['country'])

print('##########')
# Print out country column as Pandas DataFrame
print(cars[['country']])

print('##########')
# Print out observation for Japan
print(cars.loc['JAP'])

print('##########')
# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])

print('##########')
# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

print('##########')
# Print sub-DataFrame for Morocco and Russia, both country and drives right
print(cars.loc[['RU','MOR'],['country','drives_right']])
