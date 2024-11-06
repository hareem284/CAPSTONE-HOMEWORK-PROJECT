

#I THINK THERE IS A PROBLEM IN THIS SITE AS I TRIPLE CHECKED MY CODE IS ABSOULUTLY CORRECT

#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas 
import pandas as pd
#importing seaborn
import seaborn as sb
#reading csv file
rf=pd.read_csv("Penguins Data (4).csv")
print(rf.info()) 
rf.isnull().any()
#making a scatter plot
sb.scatterplot(data=rf,x="studyName",y=" Species",hue="Region",size=" Island",alpha=0.4,palette='viridis')
plt.show()
sb.heatmap(rf.corr())
plt.show()
sb.pairplot(rf,hue="Region")
plt.show()