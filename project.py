import numpy as np
import matplotlib.pyplot as plt

def step_gradient(b_current, w_current, w1_current, w2_current, w3_current, train_x, train_y, train_x1, train_x2, train_x3, learning_rate):
    b = 0
    w = 0
    w1=0
    w2=0
    w3=0
    m = len(train_y)
    global K
    global B
    global K1
    global K2
    global K3
    for i in range(m):
        x = train_x[i]
        y = train_y[i]
        x1=train_x1[i]
        x2=train_x2[i]
        x3=train_x3[i]
        b += (1/m) * (((w_current * x) +(w1_current * x1)+(w2_current * x2)+(w3_current * x3) + b_current) - y)
        w += (1/m) * x * (((w_current * x) + (w1_current * x1)+(w2_current * x2)+(w3_current * x3) + b_current) - y)
        w1 += (1/m) * x1 * (((w_current * x) + (w1_current * x1)+(w2_current * x2)+(w3_current * x3) + b_current) - y)
        w2 += (1/m) * x2 * (((w_current * x) + (w1_current * x1)+(w2_current * x2)+(w3_current * x3) + b_current) - y)
        w3 += (1/m) * x3 * (((w_current * x) + (w1_current * x1)+(w2_current * x2)+(w3_current * x3) + b_current) - y)
        b_new = b_current - (learning_rate * b)
        w_new = w_current - (learning_rate * w)
        w1_new = w1_current - (learning_rate * w1)
        w2_new = w2_current - (learning_rate * w2)
        w3_new = w3_current - (learning_rate * w3)
        B=b_new
        K=w_new
        K1=w1_new
        K2=w2_new
        K3=w3_new*10000
    return [b_new, w_new, w1_new, w2_new, w3_new]


def run_descent(train_x, train_y,train_x1,train_x2,train_x3, init_b, init_w,init_w1,init_w2,init_w3, epochs, learning_rate):
    b = init_b
    w = init_w
    w1=init_w1
    w2=init_w2
    w3=init_w3
    for i in range(epochs):
        b, w,w1,w2,w3 = step_gradient(b, w, w1, w2, w3, train_x, train_y, train_x1, train_x2, train_x3, learning_rate)
    return [b, w,w1,w2,w3]



def drawPlot(train_x, train_y, m, b):
    plt.plot(train_x, train_y, 'ro')
    plt.plot([0, 7000], [0 + b, 7000*m + b], color='b', linestyle='-', linewidth=2)
    plt.xlabel('Size')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.show()


def run():
    file = 'houses.csv'
    points = np.array(np.genfromtxt(file, delimiter=',', skip_header=1))
                      
    learning_rate = 0.0000001  

    train_x = points[:,0]  
    train_y = points[:,1]  
    train_x1=points[:,2]
    train_x2=points[:,3]
    train_x3=points[:,4]
    init_b = 0
    init_w = 0
    init_w1=0
    init_w2=0
    init_w3=0

    print('{} - number of training examples'.format(len(train_y)))
    print('k = 0, b = 0 | initial parameters')

    epochs = 10
    [b, w, w1, w2, w3] = run_descent(train_x, train_y,train_x1,train_x2,train_x3, init_b, init_w,init_w1,init_w2,init_w3, epochs, learning_rate)

    print('k = {}, b = {}, k1 = {}, k2 = {}, k3 = {} | final parameters'.format(w, b, w1, w2, w3*100))
    m = len(train_y)
    drawPlot(train_x, train_y, w, b)


if __name__ == '__main__':
    run()

from tkinter import *
def prePrice():
    amt=float(amount.get())
    itrt=float(intRate.get())
    lo=float(ty.get())
    yrs=float(years.get())
    y=((K*amt)+(K1*itrt)+(K2*yrs)+(K3*lo)+B)
    lblMonthly=Label(main, text = 'Rs %.2f' % y).grid(row=5,column=1,padx=0,pady=10)
    return
main = Tk()
main.title("House Price Prediction")
main.geometry('700x700')
 
amount = StringVar()
intRate = StringVar()
years = StringVar()
ty = StringVar()
 
lblAmount = Label(main, text = 'Enter the size of house :').grid(row = 0, column = 0, padx = 0, pady = 10)
entAmount = Entry(main, textvariable = amount).grid(row = 0, column = 1)
 
lblIntRate = Label(main, text = 'Enter the number of bedroom :').grid(row = 1, column = 0, padx = 0, pady = 10)
entIntRate = Entry(main, textvariable = intRate).grid(row = 1, column = 1)
 
lblYears = Label(main, text = 'Enter the number of bolcony :').grid(row = 2, column = 0, padx = 0, pady = 10)
entYears = Entry(main, textvariable = years).grid(row = 2, column = 1)  

city = Label(main, text = ' The number for corresponding city Hydrabad=1, Kolkata=2, Bengaluru=3, Delhi=4, Mumbai=5:').grid(row = 3, column = 0, padx = 0, pady = 10)
cityName = Label(main, text = 'Enter the number of City :').grid(row = 4, column = 0, padx = 0, pady = 10)
cityNo = Entry(main, textvariable = ty).grid(row = 4, column = 1)

btn= Button(main,text='calculate', command= prePrice).grid(row=6, column=1)

lblMonthly = Label(main, text ='Predict Price is : ').grid(row=5,column=0,padx=0,pady=10)

main.mainloop()
