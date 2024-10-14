import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import random
import tkinter as tk
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

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


"""  
sns.barplot(x=tt.index , y=tt['yüzde değişimi'], palette='viridis')
plt.xticks(rotation=90)
plt.show()


sns.lineplot(x=tt.index, y=tt['bu gün'], palette='viridis')
sns.lineplot(x=tt.index, y=tt['yıl bası'], palette='viridis')
plt.show()

"""




ana.mainloop()

sto='TSLA'
ff=yf.download(sto, start='2022-01-01', end='2024-01-01')

kapaa=ff['Close']




plt.figure(figsize=(10,6))
plt.plot(kapaa.index, kapaa, label='Geçmiş Fiyat')

forecast_data=pd.date_range(start=kapaa.index[-1],periods=180, freq='D')
plt.title(f'{sto} 6 ay sonrası ')
plt.xlabel('Tarih')
plt.ylabel('fiyat')
plt.legend()
plt.grid(True)
plt.show()

mdo=ARIMA(kapaa,order=(5, 1, 0))
egıt=mdo.fit()


forecast, stderr,conf_int=egıt.forecast(steps=180)
forecast_data=pd.date_range(start=kapaa.index[-1],periods=180, freq='D')



plt.plot(forecast_data, forecast, label="tahmin edilen fiyat", color='red')
plt.fill_between(forecast_data, conf_int[:, 0], conf_int[:, 1],color='gray', alpha=0.3 )

plt.title(f'{sto} 6 Ay Sonrası Fiyat Tahmini (ARIMA)')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (USD)')
plt.legend()
plt.grid(True)
plt.show()


