#Memanggil Library di Python
import numpy as np
import pandas as pd

#Exploratory Data Analysis dengan Pandas - Part 1
order_df = pd.read_csv("D:/DQLab/DATA/Python/order.csv")

#Melihat struktur kolom dan baris dari data frame
print(order_df.shape)

#Melihat preview data dari data frame
print(order_df.head(10))

#Exploratory Data Analysis dengan Pandas - Part 1
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())

#Exploratory Data Analysis dengan Pandas - Part 2
#Tugas Praktek
import matplotlib.pyplot as plt
# plot histogram kolom: price
order_df[["price"]].hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()  # Untuk menampilkan histogram plot

#Standar Deviasi dan Varians pada Pandas
# Standar variasi kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].std())
# Varians kolom product_weight_gram
print(order_df.loc[:, "product_weight_gram"].var())

#Menemukan Outliers Menggunakan Pandas
# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1
print(IQR)

#Rename Kolom Data Frame
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={ "freight_value" : "shipping_cost"}, inplace=True)
print(order_df)

#.groupby menggunakan Pandas
# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)

#Sorting Menggunakan Pandas
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=False)
print(sort_harga)

# Mini Project
# Median price yang dibayar customer dari masing-masing metode pembayaran. 
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print(median_price)
# Ubah freight_value menjadi shipping_cost dan cari shipping_cost 
# termahal dari data penjualan tersebut menggunakan sort.
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)
# Untuk product_category_name, berapa  rata-rata weight produk tersebut 
# dan standar deviasi mana yang terkecil dari weight tersebut, 
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())
# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity 
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()