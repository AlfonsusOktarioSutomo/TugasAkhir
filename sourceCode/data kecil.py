# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data_sample2.csv") 
df_gb = df.groupby(["technology"]).sum('f0_')
jumlah = df_gb['f0_'].sum()
df_sorted = df_gb.sort_values(by='f0_', ascending=False)
df_sorted['f0_'] = df_sorted['f0_'] / jumlah
df_10 = df_sorted.head(10)
df_baru = df.loc[df['technology'].isin(df_10.index)]
df_baru = df_baru[['date','technology','f0_']]
df_baru['f0_'] = df_baru['f0_']/jumlah
df_baru.drop_duplicates(subset='date')      
df_pivot = df_baru.pivot_table(index="date", columns='technology', values='f0_')
df_pivot['jumlah'] = df_pivot.sum(axis=1)
df_pivot.to_excel("10 teknologi populer.xlsx")
for i in df_pivot.columns:
      df_pivot[i] = df_pivot[i]/df_pivot['jumlah']
df_pivot = df_pivot.drop(columns = 'jumlah')
df_filled = df_pivot.fillna('0')

fig2 = go.Figure()
for col in df_pivot.columns:
    fig2.add_trace(go.Scatter(x=df_pivot.index, y=df_pivot[col], mode='lines+markers', name=col))
    
fig2.update_layout(
    title="Perkembangan 10 teknologi populer",
    xaxis_title="Tanggal",
    yaxis_title="Peresentase penggunaan",
    template="plotly_white"
)
fig2.show()
fig2.write_html("sample.html")

##Data Mobile
df_mobile = df[df['client'] == 'mobile']
df_mobile_gb = df_mobile.groupby(["technology"]).sum('f0_')
jumlah_mobile = df_mobile_gb['f0_'].sum()
df_mobile_gb['f0_'] = df_mobile_gb['f0_']/jumlah_mobile
df_sorted_mobile = df_mobile_gb.sort_values(by='f0_', ascending=False)
df_10mobile = df_sorted_mobile.head(10)
df_baru_mobile = df_mobile.loc[df_mobile['technology'].isin(df_10mobile.index)]
df_baru_mobile = df_baru_mobile[['date','technology','f0_']]
df_baru_mobile['f0_'] = df_baru_mobile['f0_']/jumlah_mobile
#df_baru.drop_duplicates(subset='date')
df_pivot_mobile = df_baru_mobile.pivot_table(index="date", columns='technology', values='f0_')

fig3 = go.Figure()
for col in df_pivot_mobile.columns:
    fig3.add_trace(go.Scatter(x=df_pivot_mobile.index, y=df_pivot_mobile[col], mode='lines+markers', name=col))
    
fig3.update_layout(
    title="Perkembangan 10 teknologi populer pada client mobile",
    xaxis_title="Tanggal",
    yaxis_title="Peresentase penggunaan",
    template="plotly_white"
)
fig3.show()
fig3.write_html('sample_mobile.html')


##Data Desktop
df_desktop = df[df['client'] == 'desktop']
df_desktop_gb = df_desktop.groupby(["technology"]).sum('f0_')
jumlah_desktop = df_desktop_gb['f0_'].sum()
df_desktop_gb['f0_'] = df_desktop_gb['f0_']/jumlah_desktop
df_sorted_desktop = df_desktop_gb.sort_values(by='f0_', ascending=False)
df_10desktop = df_sorted_desktop.head(10)
df_baru_desktop = df_desktop.loc[df_desktop['technology'].isin(df_10desktop.index)]
df_baru_desktop = df_baru_desktop[['date','technology','f0_']]
df_baru_desktop['f0_'] = df_baru_desktop['f0_']/jumlah_desktop
#df_baru.drop_duplicates(subset='date')
df_pivot_desktop = df_baru_desktop.pivot_table(index="date", columns='technology', values='f0_')

fig3 = go.Figure()
for col in df_pivot_desktop.columns:
    fig3.add_trace(go.Scatter(x=df_pivot_desktop.index, y=df_pivot_desktop[col], mode='lines+markers', name=col))
    
fig3.update_layout(
    title="Perkembangan 10 teknologi populer pada client desktop",
    xaxis_title="Tanggal",
    yaxis_title="Peresentase penggunaan",
    template="plotly_white"
)
fig3.show()
fig3.write_html('sample_desktop.html')
