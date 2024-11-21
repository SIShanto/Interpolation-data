import pandas as pd

df=pd.read_csv("cvs.csv",parse_dates=["Date"])
df.set_index("Date",inplace=True)
new_fd= df.interpolate(method="linear")
dt= pd.date_range("2001-06-07", "2021-12-31")
idx= pd.DatetimeIndex(dt)
df= df.reindex(idx)
df.to_csv("Interpolated_MDD_Data_1.csv")
