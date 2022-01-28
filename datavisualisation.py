import csv
import pandas as p
import plotly.express as pe

d = p.read_csv("data.csv")

mean = d.groupby( ["student_id","level"] , as_index = False)["attempt"].mean()

print(mean)

Plot = pe.scatter(mean , x="student_id",y="level", size = "attempt" , color="attempt" , title = "Scatter Graph Of Different Students")

Plot.show()