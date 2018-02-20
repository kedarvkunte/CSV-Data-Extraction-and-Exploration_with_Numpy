import numpy as np

####################################################
# Problem 1: Data filtering
####################################################
housing_data = np.loadtxt("boston.csv",delimiter=',')

print("Shape of housing data\n")
print(housing_data.shape)
#print((np.isnan(housing_data)).astype(int).ravel())
count_of_nans = np.bincount((np.isnan(housing_data)).astype(int).ravel())
print("Percentage of entries in the matrix have the value NaN ", count_of_nans[1]/sum(count_of_nans))

nans_matrix = (np.isnan(housing_data)).astype(int)

print("\nRows containing at least one NaN value? ",sum(np.count_nonzero(nans_matrix,axis = 1)))


print("\nArray of NaN values each column has is ",(np.count_nonzero(nans_matrix,axis = 0)))


#print((~np.isnan(housing_data)).astype(int))

without_nan_rows = housing_data[~np.isnan(housing_data).any(axis=1)]
#print(without_nan_rows.shape)

print("\nAverage value of each column, ignoring all rows containing at least one NaN value?\n")
print(np.mean(without_nan_rows, axis=0))

print("\nAverage value of each column, ignoring NaN values, but including other features in the same row as a NaN value \ n")
print(np.nanmean(housing_data, axis=0))


## Add code here ##





####################################################
# Problem 2: Data exploration
####################################################

iris_data = np.loadtxt("iris.csv",delimiter=',',skiprows=1)
    
## Add code here ##



#np.bincount(iris_data[:,4].astype(int), weights = iris_data[:,2])

print("Average petal length for each iris species \ n")
print(np.bincount(iris_data[:,4].astype(int), weights = iris_data[:,2])/np.bincount(iris_data[:,4].astype(int)))


print("Sepal width for the ve data cases with the largest sepal length \ n")
print(iris_data[(iris_data[:,0]).argsort()[-5:],1])

print("Sepal measurements for the three data cases with the largest petal area according to this approximation. \n")
area_array = 0.25*np.pi*(iris_data[:,2]*iris_data[:,3])

#np.array(iris_data[((iris_data[:,0]).argsort()[-3:],0)],iris_data[((iris_data[:,0]).argsort()[-3:],0)])


print("4 by 4 Pearson correlation matrix\n")
#print(np.array([iris_data[area_array.argsort()[-3:],0],iris_data[area_array.argsort()[-3:],1]]).T)

features = iris_data[:,:4]

print(np.corrcoef(features.T))


#
#from scipy import stats as st

print("Z-score")
mu = np.mean(features,axis=0)
sigma = np.std(features,axis=0)
Z_score = (features - mu)/sigma
print(np.max(Z_score,axis=0))





