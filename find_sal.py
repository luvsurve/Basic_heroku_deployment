import pickle
import numpy as np
def find_saly(age, workclass, education, race, sex, hpw,country):
    encode = pickle.load(open('encode.pkl','rb'))
    sex = encode.fit_transform([sex]) 
    workclass = encode.fit_transform([workclass])
    race = encode.fit_transform([race])
    country = encode.fit_transform([country])
    input = np.array([age,workclass,education,race,sex,hpw,country]).reshape(1,7)
    log = pickle.load(open('logreg.pkl','rb'))
    op = log.predict(input)[0]
    return op

#print(find_saly(35,'Fedral-gov',12,'White','Male',45,'United-States'))

