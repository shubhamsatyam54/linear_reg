import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('automobileEDA.csv')

X = df['highway-mpg']
Y = df['price']
x_mean=X.mean()
y_mean=Y.mean()


def main():
    xy_cal=0
    x2_cal=0
    for i in range(len(df)):
        xy_cal+=(X[i]-x_mean)*(Y[i]-y_mean)
        x2_cal+=((X[i]-x_mean)**2)
    m=(xy_cal)/x2_cal
    c=y_mean-(m*x_mean)
    print("On applying linear regression we get m={0}, c={1}, error={2}".format(m,c,error(m,c)))
                                                                                
def error(m,c):
    y2_cal=0
    yp2_cal=0
    for i in range(len(df)):
        yp=m*X[i]+c
        yp2_cal+=(yp-y_mean)**2
        y2_cal+=(Y[i]-y_mean)**2
    err=(yp2_cal/y2_cal)
    return err

if __name__ == '__main__':
    main()





