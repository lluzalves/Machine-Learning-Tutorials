#Data Preprocessing 

#Importing dataset
dataset = read.csv('Data.csv')
 
#Handling missing data 
# we will take the column of Age of the dataset and we use a ifelse condition to check for missing values 
# if the condition is true we get the mean of the collumn to add it in the missing value else it should returns 
# the value of the observation
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(replaceMissingAgeValues) mean(replaceMissingAgeValues,na.rm = TRUE)),
                     dataset$Age) 

# we applied the same strategy to replace the missing salary values from the dataset
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(replaceMissingSalaryValues) mean(replaceMissingSalaryValues, na.rm = TRUE)),
                        dataset$Salary)
                        )