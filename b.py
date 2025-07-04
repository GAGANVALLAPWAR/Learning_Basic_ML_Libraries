import pandas as pd

#create a simple dataframe
data = {
    'Name': ['Alice','Bob','Charlie',"Shri",'Rise'],
    'Age' : [25,30,35,27,34],
    'City' : ['New York','Paris','London','India','USA'],
    'College' : ['JDIET','IIT','YCCE','VNIT','PRMCMR']
}
df = pd.DataFrame(data)

#display the dataframe
print(df)

#access a column
print(df['Name'])

#basic statistics
print(df['Age'].mean()) #averege age

#filter row
print(df[df['Age'] > 28])

print(df['College'])