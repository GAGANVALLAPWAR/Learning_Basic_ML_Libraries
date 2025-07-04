import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#sample dataframe
df = pd.DataFrame({'Student' : ['Harish','Atul','Anup','Abhay'],
                   'CGPA' : [68,70,65,78],
                    'Branch' : ['ENTC','CSE','ENTC','MECH'] })

#plot a  boxplot
sns.boxplot(x='Branch', y='CGPA', data=df)
plt.show()
