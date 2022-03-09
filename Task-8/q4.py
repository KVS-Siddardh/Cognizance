import pandas as pd
import string

ser = pd.Series(['amrita', 'school', 'of', 'engineering'])
str = " ".join(ser)
print(string.capwords(str))
print(str.upper())