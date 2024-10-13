import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import random
import tkinter as tk

ana=tk.Tk()
ana.title("hisse inceleme")
ana.geometry("500x500")

def all():
    verial=ara.get()
    s.append(verial)
    label.config(text=f"alındı: {verial}   ")

    labelhisse.config(text=f"{tt}")
    


btn=tk.Button(ana, text="incele", command=all)
btn.pack()

ara=tk.Entry(ana)
ara.pack()

label=tk.Label(ana,text="")
label.pack(pady=10)

labelhisse=tk.Label(ana)
labelhisse.pack(pady=10)




s=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX', 'NVDA', 'PYPL', 'BABA','GARAN.IS']


strt="2024-01-01"
ennd=pd.Timestamp.today().strftime('%Y-%m-%d')
prct={}
for hss in s:
    aa=yf.download(hss ,start=strt , end=ennd)

    bsl=aa['Close'].iloc[0]
    snn=aa['Close'].iloc[-1]

    yuzdee=((snn-bsl)/bsl)*100
    print(yuzdee)

    prct[hss]={

        'bu gün': bsl,
        'yıl bası':snn ,
        'yüzde değişimi': yuzdee



    }
tt=pd.DataFrame(prct).T

print(tt)



sns.barplot(x=tt.index , y=tt['yüzde değişimi'], palette='viridis')
plt.xticks(rotation=90)
plt.show()


sns.lineplot(x=tt.index, y=tt['bu gün'], palette='viridis')
sns.lineplot(x=tt.index, y=tt['yıl bası'], palette='viridis')
plt.show()

ana.mainloop()