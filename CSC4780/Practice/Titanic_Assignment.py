import matplotlib.pyplot as plt
import sys
import pandas as pd

#Opening the file with data
file_handle = open(sys.argv[1])

#Read all the data in the file into a dataframe in Pandas
data = pd.read_csv(file_handle)

#Plot a histogram with the ages of passengers
ages = data['Age'].tolist()
ages_set = {ind_age for ind_age in ages}
ages_count = [] 
for each in ages_set:
	ages_count.append(ages.count(each))
plt.hist(ages_count)
print(ages_set)

#Adding attributes to the plot
plt.title('Age distribution of passengers in the Titanic')

#Showing the plot
plt.show()