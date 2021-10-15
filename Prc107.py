import pandas as pd
from pandas.core import groupby
import plotly.express as px
import statistics

df=pd.read_csv("Prc107.csv")

mean =df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(mean)
fig =px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
fig.show()