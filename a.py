import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas
import pandas as pd
import seaborn as sns


df = pd.DataFrame({'Сумма кредита': [100, 400, 200, 500],
                   'Название банка': ['Бром', 'Авто', 'Дрен', 'Гоап'],
                   'Процент годовых': [8, 4, 5, 3]
                   })
df['Название банка'] = df['Название банка'].apply(lambda x: 1 if x =='Бром' else 0)
plt.Figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot = True, cmap = 'Blues')
plt.title('Корреляция')
#plt.show()
print(df)
shape_df = df.shape[1]
print(shape_df)
num = 1
for i in range(shape_df - 1):
    for j in range(i + 1, shape_df):
        for k in range(3):
            match k:
                case 0:
                    marker = '+'
                case 1:
                    marker = 'o'
                case 2:
                    marker = 'x'
plt.scatter(df['Название банка'][class_indices, i], ds['Название банка'][class_indices, j],
            label = f'Класс {df['targe]}')