# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data_sample.csv")
df_gb = df.groupby(["technology"]).sum('f0_')
df_sorted = df_gb.sort_values(by='f0_', ascending=False)
df_10 = df_sorted.head(10)
df_baru = df.loc[df['technology'].isin(df_10.index)]
df_pivot = df_baru.pivot(index="date", columns='technology', values='f0_')
df_filled = df_pivot.fillna('0')

fig2 = go.Figure()
for col in df_pivot.columns:
    fig2.add_trace(go.Scatter(x=df_pivot.index, y=df_pivot[col], mode='lines+markers', name=col))
    
fig2.update_layout(
    title="Perkembangan 10 teknologi populer",
    xaxis_title="Tanggal",
    yaxis_title="Penggunaan",
    template="plotly_white"
)
fig2.show()
fig2.write_html("sample.html")




