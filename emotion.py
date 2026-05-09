import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file):
    data=[]
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            text,label=line.strip().split(';')
            data.append([text,label])
        return pd.DataFrame(data,columns=['text','emotion'])
    
train=load_data('train.txt')
test=load_data('test.txt')
val=load_data('val.txt')

df=pd.concat([train,val],axis=0)

import re
def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-z\s]', '', text)
    return text
df['clean_text']=df['text'].apply(clean_text)
test['clean_text']=test['text'].apply(clean_text)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['emotion']=le.fit_transform(df['emotion'])
test['emotion']=le.transform(test['emotion'])
print(le.classes_)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=10000,ngram_range=(1,2),stop_words='english',min_df=2,max_df=0.9)
X_train=tfidf.fit_transform(df['clean_text'])
y_train=df['emotion']

X_test=tfidf.transform(test['clean_text'])
y_test=test['emotion']

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=2000)
model.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
y_pred=model.predict(X_test)
print("Accuracy : ",accuracy_score(y_test,y_pred))
print("Classification Report :",classification_report(y_test,y_pred))
print("Confusion Matrix :",confusion_matrix(y_test,y_pred))

import pickle
pickle.dump(model,open("emotion_model.pkl",'wb'))
pickle.dump(tfidf,open("tfidf.pkl",'wb'))

print(df['emotion'].unique())
