
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит 
# всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import random
import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot = pd.get_dummies(data['whoAmI']) # Преобразование в one hot вид
data = pd.concat([data, one_hot], axis=1)
# data.drop(columns=['whoAmI'], inplace=True) # Удаление исходного столбца 'whoAmI'

print(data.head())