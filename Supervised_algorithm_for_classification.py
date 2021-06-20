import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sb
import matplotlib.pyplot as plt
import scipy.stats as st
import statistics
from sklearn.preprocessing import scale

# Importion des données
df = pd.read_csv('/kaggle/input/titanicdataset-traincsv/train.csv')
df = df.drop(columns = ['PassengerId'])
