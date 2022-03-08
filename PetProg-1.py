#!/usr/bin/env python
# coding: utf-8

# In[259]:


import pandas as pd


# Запись датасета "bookings.csv", находящийся по ссылке из источника
# Запись первых семи строк в переменную "bookings_head "

# In[64]:


bookings = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', sep=';')
bookings_head = bookings.head(7)


# Узнаем размер таблицы

# In[65]:


bookings.shape


# Узнаем тип переменных в таблице

# In[66]:


bookings.dtypes


# Привидем названия столбцов к однородному виду

# In[67]:


bookings.columns = bookings.columns.str.replace(' ', '_').str.lower()


# Найдем пользователи каких стран (топ-5) совершили наибольшее число успешных бронирований

# In[68]:


bookings .query('is_canceled == 0') .country .value_counts() .head(5)


# Найдем на сколько ночей в среднем бронируют отели типа "City Hotel" и "Resort Hotel"

# In[85]:


bookings .groupby(['hotel'], as_index=False) .aggregate({'stays_total_nights':'mean'}) .round(decimals=2)


# Найдем колличество случаев, когда тип номера клиента отличается от изначально забронированного 

# In[91]:


bookings     .query('assigned_room_type != reserved_room_type')     .shape[0]


# Узнаем на какой месяц чаще всего оформляли бронь в 2016 году

# In[107]:


bookings     .query('arrival_date_year == 2016')     .value_counts('arrival_date_month')     .idxmax()


# Проверим изменился ли самый популярный месяц в 2017 году

# In[101]:


bookings     .query('arrival_date_year == 2017')     .value_counts('arrival_date_month')     .idxmax()


# Сгруппируем данные по годам, а затем проверим, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего

# In[289]:


bookings     .query('hotel == "City Hotel" and is_canceled == 1')     .groupby('arrival_date_year', as_index=False)     .arrival_date_month     .value_counts()
    


# Проверим какая из числовых характеристик имеет наибольшее занчение

# In[128]:


bookings[['adults', 'children', 'babies']]     .mean()     .round(decimals=2)


# Создадим колонку total_kids, объединив столбцы children и babies
# 
# Найдем для отелей какого типа среднее значение переменной оказалось наибольшим. В ответ укажем наибольшее среднее число

# In[145]:


bookings['total_kids'] = bookings['children'] + bookings['babies']


# In[146]:


bookings     .groupby('hotel', as_index=False)     .aggregate({'total_kids':'mean'}, )     .sort_values('total_kids', ascending=False)     .round(decimals=2)


# Создадим переменную "has_kids", которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка, в противном случае – False

# In[258]:


bookings['has_kids'] = bookings['total_kids'] > 0


# Найдем сколько клиентов было потеряно в процессе бронирования, процент оттока плиентов

# In[294]:


churn_rate = (
    bookings.query('is_canceled == 1').shape[0] 
    / bookings.shape[0]
)
churn_rate = round(churn_rate * 100, 2)


# In[295]:


churn_rate


# Проверим среди какой группы пользователей (с детьми или без) показатель оттока выше

# Найдем ооток пользователей без детей

# In[290]:


no_kids_churn_rate = (
    bookings.query('is_canceled == 1 and has_kids == False').shape[0] 
    / bookings.query('has_kids == False').shape[0]
)
no_kids_churn_rate = round(no_kids_churn_rate * 100, 2)


# In[291]:


no_kids_churn_rate


# Найдем оттот среди пользователей с детьми

# In[285]:


kids_churn_rate = (
    bookings.query('is_canceled == 1 and has_kids == True').shape[0] 
    / bookings.query('has_kids == True').shape[0]
)
kids_churn_rate = round(kids_churn_rate * 100, 2)


# In[286]:


kids_churn_rate

