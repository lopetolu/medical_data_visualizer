import pandas as pd
import seaborn as sns
import numpy as np

file_data = r"C:\Users\USER\Desktop\PROJECT FILE\medical_examination.csv"
df=pd.read_csv(file_data)
df.set_index("id",inplace=True)

df["overweight"]= ((df["weight"]/(df["height"]/100)**2)>25).astype("int")  #Number 2

df[["cholesterol", "gluc"]] = (df[["cholesterol", "gluc"]]>1).astype("int") #Number 3: Normalizing

#Creating the categorical plot (Q4 to Q9)
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"],value_vars=["cholesterol", "gluc", "smoke", "alco", "active","overweight"])
    fig = sns.catplot(data=df_cat, kind="count", x="variable", col="cardio", hue="value")

### Creating the heatmap
def draw_heat_map():
    df_heat = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"]>=df["height"].quantile(0.025))
    &( df["height"]<=df["height"].quantile(0.975))
    &(df["weight"]>=df["weight"].quantile(0.025) )
    & (df["weight"]<=df["weight"].quantile(0.975))]

    corr = df_heat.corr()
    mask = np.triu(corr)

    sns.heatmap(corr)