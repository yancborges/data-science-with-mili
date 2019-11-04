from lyrics import lyrics
from data_set import data_set
import pandas as pd
from nltk.tokenize import word_tokenize

ds = data_set()
ds.load_objects()

word_lists = []
names = []
for item in ds.obj_list:
    names.append(item.name)
    #word_lists.append(word_tokenize(item.content))
    word_lists.append(item.content)
print(names)
zippedList =  list(zip(names,word_lists))
df = pd.DataFrame(zippedList, columns = ['song_name' , 'word_list']) 

print(df.shape)

with open('all_songs_cleaned.csv', 'w', encoding="utf-8") as f:
    f.write(df.to_csv(index=True))


