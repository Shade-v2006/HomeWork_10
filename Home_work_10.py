
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит 
# всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd

# Генерация данных
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные категории
categories = data['whoAmI'].unique()

# Создаем новые столбцы для каждой категории и заполняем нулями
for category in categories:
    data[category] = 0

# Заполняем единицами соответствующие столбцы для каждой категории
for i, row in data.iterrows():
    category = row['whoAmI']
    data.at[i, category] = 1

#data.drop(columns=['whoAmI'], inplace=True) # Удаляем исходный столбец 'whoAmI'

print(data.head())
