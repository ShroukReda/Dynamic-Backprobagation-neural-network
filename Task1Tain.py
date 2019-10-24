import matplotlib.pyplot as plt
import numpy as np
import glob
FirstFeatC1=[None]*51
SecFeatC1=[None]*51
FirstFeatC2=[None]*51
SecFeatC2=[None]*51
FirstClass=[None]*51
SecClass=[None]*51
def signum(x):
    for i in range(len(x)):
        if x[i] >= 0:
            x[i] = 1
        else:
            x[i] = -1
    return x
def loading():
    MydataSet = open("D:\CS\Semester2/Neural Networks\CI [CS-2019]\IrisData.txt", "r")
    MydatasetLine = MydataSet.readlines()
    i = 1
    C1 = [[None] * 4] * 51
    C2 = [[None] * 4] * 51
    C3 = [[None] * 4] * 51
    # ============================================================
    x11 = [None] * 51
    x21 = [None] * 51
    x31 = [None] * 51
    x41 = [None] * 51

    x12 = [None] * 51
    x22 = [None] * 51
    x32 = [None] * 51
    x42 = [None] * 51

    x13 = [None] * 51
    x23 = [None] * 51
    x33 = [None] * 51
    x43 = [None] * 51
    firstClass = 1
    secClass = 1
    thirdClass = 1
    while (i < MydatasetLine.__len__()):
        feature = MydatasetLine[i].split(',')
        x = i / 50
        if x <= 1:
            C1[firstClass] = feature
            firstClass += 1
        elif x > 1 and x <= 2:
            C2[secClass] = feature
            secClass += 1
        elif x > 2 and x <= 3:
            C3[thirdClass] = feature
            thirdClass += 1
        i = i + 1
    # ==================================================
    z = 1
    for j in range(1, 51):
        x11[z] = C1[j][0]
        x21[z] = C1[j][1]
        x31[z] = C1[j][2]
        x41[z] = C1[j][3]

        x12[z] = C2[j][0]
        x22[z] = C2[j][1]
        x32[z] = C2[j][2]
        x42[z] = C2[j][3]

        x13[z] = C3[j][0]
        x23[z] = C3[j][1]
        x33[z] = C3[j][2]
        x43[z] = C3[j][3]
        z = z + 1
    AllFeatures=[x11,x21,x31,x41,x12,x22,x32,x42,x13,x23,x33,x43] #feature then class
    AllClasses=[C1,C2,C3]
    Plotting(AllFeatures)
    return AllFeatures,AllClasses

def Plotting(Features):
    plt.figure('X1,X2')
    plt.scatter(Features[0],Features[1])
    plt.scatter(Features[4], Features[5])
    plt.scatter(Features[8], Features[9])
    plt.xlabel('X1')
    plt.ylabel('X2')

    plt.figure('X1,X3')
    plt.scatter(Features[0], Features[2])
    plt.scatter(Features[4], Features[6])
    plt.scatter(Features[8], Features[10])
    plt.xlabel('X1')
    plt.ylabel('X3')

    plt.figure('X1,X4')
    plt.scatter(Features[0], Features[3])
    plt.scatter(Features[4], Features[7])
    plt.scatter(Features[8], Features[11])
    plt.xlabel('X1')
    plt.ylabel('X4')

    plt.figure('X2,X3')
    plt.scatter(Features[1],Features[2])
    plt.scatter(Features[5], Features[6])
    plt.scatter(Features[9], Features[10])
    plt.xlabel('X2')
    plt.ylabel('X3')

    plt.figure('X2,X4')
    plt.scatter(Features[1], Features[3])
    plt.scatter(Features[5], Features[7])
    plt.scatter(Features[9], Features[11])
    plt.xlabel('X2')
    plt.ylabel('X4')

    plt.figure('X3,X4')
    plt.scatter(Features[2], Features[3])
    plt.scatter(Features[6], Features[7])
    plt.scatter(Features[10], Features[11])
    plt.xlabel('X3')
    plt.ylabel('X4')
    return

def SetClassesAndFeatures(GUIFeature1,GUIFeature2,GUIClass1,GUIClass2): # btndhy 3la loading fen ? mashy w8 kda
    MyFeature,MyClasses=loading()
    strr1 = str(GUIClass1)#tmam kda y sa7by ? ^_^ aha ha4of aho
    strr2 = str(GUIClass2)
    feat1 = str(GUIFeature1)
    feat2 = str(GUIFeature2)
    F=0
    F2=0
    F3=0
    c=0
    c2=0
    if strr1 == "Iris Setosa":
        for i in range(1, 51):
            MyClasses[0][i][4] = "1"
    elif strr1 == "Iris Versicolor":
        for i in range(1, 51):
            MyClasses[1][i][4] = "1"
    elif strr1 == "Iris Virginica":
        for i in range(1, 51):
            MyClasses[2][i][4] = "1"

    if strr2 == "Iris Setosa":
        for i in range(1, 51):
            MyClasses[0][i][4] = "-1"
    elif strr2 == "Iris Versicolor":
        for i in range(1, 51):
            MyClasses[1][i][4] = "-1"
    elif strr2 == "Iris Virginica":
        for i in range(1, 51):
            MyClasses[2][i][4] = "-1"
#===============================================
    if strr1 == "Iris Setosa" or strr2 == "Iris Setosa":
        if (feat1 == "X1" or feat2 == "X1"):
            FirstFeatC1 = MyFeature[0]  # wda
            FirstClass = MyClasses[0]  # tyb e2fl eshta w lw 3zty tndhy ay 7aga mn l gui
            F = F + 1
            c = 1
        if (feat1 == "X2" or feat2 == "X2"):
            if F == 0 and c == 0:
                FirstFeatC1 = MyFeature[1]
                FirstClass = MyClasses[0]
                F = F + 1
                c = 1
            elif F == 1 and c == 1:
                SecFeatC1 = MyFeature[1]
                FirstClass = MyClasses[0]
        if (feat1 == "X3" or feat2 == "X3"):
            if F == 0 and c == 0:
                FirstFeatC1 = MyFeature[2]
                FirstClass = MyClasses[0]
                F = F + 1
                c = 1
            elif F == 1 and c == 1:
                SecFeatC1 = MyFeature[2]
                FirstClass = MyClasses[0]

        if (feat1 == "X4" or feat2 == "X4"):
            if F == 0 and c == 0:
                FirstFeatC1 = MyFeature[3]
                FirstClass = MyClasses[0]
                F = F + 1
                c = 1
            elif F == 1 and c == 1:
                SecFeatC1 = MyFeature[3]
                FirstClass = MyClasses[0]
    if strr1 == "Iris Versicolor" or strr2 == "Iris Versicolor":
        if (feat1 == "X1" or feat2 == "X1"):
            if F2 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[4]
                FirstClass = MyClasses[1]
                F2 = F2 + 1
                c = 2
            if F2 == 0 and c != 2 and c2 == 0:
                FirstFeatC2 = MyFeature[4]
                SecClass = MyClasses[1]
                F2 = F2 + 1
                c2 = 2
        if (feat1 == "X2" or feat2 == "X2"):
            if F2 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[5]
                FirstClass = MyClasses[1]
                F2 = F2 + 1
                c = 2
            elif F2 == 1 and c == 2:
                SecFeatC1 = MyFeature[5]
                FirstClass = MyClasses[1]
            if F2 == 0 and c != 2 and c2 == 0:
                FirstFeatC2 = MyFeature[5]
                SecClass = MyClasses[1]
                F2 = F2 + 1
                c2 = 2
            elif F2 == 1 and c2 == 2:
                SecFeatC2 = MyFeature[5]
                SecClass = MyClasses[1]
        if (feat1 == "X3" or feat2 == "X3"):
            if F2 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[6]
                FirstClass = MyClasses[1]
                F2 = F2 + 1
                c = 2
            elif F2 == 1 and c == 2:
                SecFeatC1 = MyFeature[6]
                FirstClass = MyClasses[1]
            if F2 == 0 and c != 2 and c2 == 0:
                FirstFeatC2 = MyFeature[6]
                SecClass = MyClasses[1]
                F2 = F2 + 1
                c2 = 2
            elif F2 == 1 and c2 == 2:
                SecFeatC2 = MyFeature[6]
                SecClass = MyClasses[1]
        if (feat1 == "X4" or feat2 == "X4") :
            if F2 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[7]
                FirstClass = MyClasses[1]
                F2 = F2 + 1
                c = 2
            elif F2 == 1 and c == 2:
                SecFeatC1 = MyFeature[7]
                FirstClass = MyClasses[1]
            if F2 == 0 and c != 2 and c2 == 0:
                FirstFeatC2 = MyFeature[7]
                SecClass = MyClasses[1]
                F2 = F2 + 1
                c2 = 2
            elif F2 == 1 and c2 == 2:
                SecFeatC2 = MyFeature[7]
                SecClass = MyClasses[1]
    if strr1 == "Iris Virginica" or strr2 == "Iris Virginica":
        if (feat1 == "X1" or feat2 == "X1"):
            if F3 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[8]
                FirstClass = MyClasses[2]
                F3 = F3 + 1
                c = 3
            if F3 == 0 and c != 3 and c2 == 0:
                FirstFeatC2 = MyFeature[8]
                SecClass = MyClasses[2]
                F3 = F3 + 1
                c2 = 3
        if (feat1 == "X2" or feat2 == "X2"):
            if F3 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[9]
                FirstClass = MyClasses[2]
                F3 = F3 + 1
                c = 3
            elif F3 == 1 and c == 3:
                SecFeatC1 = MyFeature[9]
                FirstClass = MyClasses[2]
            if F3 == 0 and c != 3 and c2 == 0:
                FirstFeatC2 = MyFeature[9]
                SecClass = MyClasses[2]
                F3 = F3 + 1
                c2 = 3
            elif F3 == 1 and c2 == 3:
                SecFeatC2 = MyFeature[9]
                SecClass = MyClasses[2]
        if (feat1 == "X3" or feat2 == "X3"):
            if F3 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[10]
                FirstClass = MyClasses[2]
                F3 = F3 + 1
                c = 3
            elif F3 == 1 and c == 3:
                SecFeatC1 = MyFeature[10]
                FirstClass = MyClasses[2]
            if F3 == 0 and c != 3 and c2 == 0:
                FirstFeatC2 = MyFeature[10]
                SecClass = MyClasses[2]
                F3 = F3 + 1
                c2 = 3
            elif F3 == 1 and c2 == 3:
                SecFeatC2 = MyFeature[10]
                SecClass = MyClasses[2]
        if (feat1 == "X4" or feat2 == "X4"):
            if F3 == 0 and c == 0 and c2 == 0:
                FirstFeatC1 = MyFeature[11]
                FirstClass = MyClasses[2]
                F3 = F3 + 1
                c = 3
            elif F3 == 1 and c == 3:
                SecFeatC1 = MyFeature[11]
                FirstClass = MyClasses[2]
            if F3 == 0 and c != 3 and c2 == 0:
                FirstFeatC2 = MyFeature[11]
                SecClass = MyClasses[2]
                F3 = F3 + 1
                c2 = 3
            elif F3 == 1 and c2 == 3:
                SecFeatC2 = MyFeature[11]
                SecClass = MyClasses[2]
    return FirstFeatC1,SecFeatC1,FirstFeatC2,SecFeatC2,FirstClass,SecClass

def Train(F11,F22,F33,F4,C1,C2,Epoch,Rate,B):
    w = np.random.rand(1, 3)
    if B == "With Bias":
        w=w
    else:
        w[0][0]=0
    Epoch=int(Epoch)
    Rate=float(Rate)
    while  Epoch!=0:
        for i in range(1, 31):
            Class1 = np.array([1, float(F11[i]), float(F22[i])])
            Class2 = np.array([1, float(F33[i]), float(F4[i])])
            NetVal1 = np.dot(w, Class1)
            Yhat1 = signum(NetVal1)
            if Yhat1 != int(C1[i][4]):
                Loss1 = (int(C1[i][4]) - Yhat1)
                w = w + (Rate * Loss1 * Class1)

            NetVal2 = np.dot(w, Class2)
            Yhat2 = signum(NetVal2)
            if Yhat2 != int(C2[i][4]):
                Loss2 = (int(C2[i][4]) - Yhat2)
                w = w + (Rate * Loss2 * Class2)
        Epoch=Epoch-1
    return w

def MSETrain(F11,F22,F33,F4,C1,C2,Error,Rate,B):
    w = np.random.rand(1, 3)
    if B == "With Bias":
        w=w
    else:
        w[0][0]=0
    Error=float(Error)
    Rate=float(Rate)
    MSE=100
    while  (MSE > Error):
        for i in range(1, 31):
            Class1 = np.array([1, float(F11[i]), float(F22[i])])
            Class2 = np.array([1, float(F33[i]), float(F4[i])])
            NetVal1 = np.dot(w, Class1)
            Yhat1 = NetVal1
            Loss1 = (int(C1[i][4]) - Yhat1)
            w = w + (Rate * Loss1 * Class1)
            NetVal2 = np.dot(w, Class2)
            Yhat2 = NetVal2
            Loss2 = (int(C2[i][4]) - Yhat2)
            w = w + (Rate * Loss2 * Class2)
        MSE=MSEComp(F11,F22,F33,F4,C1,C2,w)
    return w

def MSEComp(F11,F22,F33,F4,C1,C2,w):
    ErrorList=[]
    SquareSum=0
    for i in range(1, 31):
        Class1 = np.array([1, float(F11[i]), float(F22[i])])
        Class2 = np.array([1, float(F33[i]), float(F4[i])])
        NetVal1 = np.dot(w, Class1)
        Yhat1 = NetVal1
        Loss1 = (int(C1[i][4]) - Yhat1)
        ErrorList.append(Loss1)
        NetVal2 = np.dot(w, Class2)
        Yhat2 = NetVal2
        Loss2 = (int(C2[i][4]) - Yhat2)
        ErrorList.append(Loss2)
    for i in range(0,60):
        SquareSum+=(ErrorList[i][0]*ErrorList[i][0])
    M=0.5*(SquareSum/60)

    return M

def Draw(F1C1,F2C1,F1C2,F2C2,W):
    plt.figure('After Training')
    intlist=[None]*51
    intlist2 = [None] * 51
    intlist11=[None]*51
    intlist22 = [None] * 51
    for i in range(1, 51):
        intlist[i]=float(F1C1[i])
        intlist2[i] = float(F1C2[i])
        intlist11[i]=float(F2C1[i])
        intlist22[i] = float(F2C2[i])
    intlist[0]=3
    intlist2[0] = 3
    X1 = max(intlist)
    X2 = min(intlist)
    X3 = max(intlist2)
    X4 = min(intlist2)
    Xmax=max(X1,X3)
    Xmin=min(X2,X4)
    Y1=(-(W[0][1]*Xmax)-W[0][0])/W[0][2]
    Y2=(-(W[0][1]*Xmin)-W[0][0])/W[0][2]
    plt.scatter(intlist[31:],intlist11[31:])
    plt.scatter(intlist2[31:],intlist22[31:])
    plt.xlabel('F1')
    plt.ylabel('F2')
    plt.plot([Xmin, Xmax], [Y2, Y1])
    plt.show()
    return

def Test (F11,F22,F33,F4,C1,C2,w):
    Right1=0
    wrong1=0
    Right2=0
    wrong2=0
    for i in range(31, 51):
        Class1 = np.array([1, float(F11[i]), float(F22[i])])
        Class2 = np.array([1, float(F33[i]), float(F4[i])])
        NetVal1 = np.dot(w, Class1)
        Yhat1 = signum(NetVal1)
        if Yhat1 == int(C1[i][4]):
            Right1=Right1+1
        else:
            wrong1=wrong1+1
        NetVal2 = np.dot(w, Class2)
        Yhat2 = signum(NetVal2)
        if Yhat2 == int(C2[i][4]):
            Right2 = Right2 + 1
        else:
            wrong2=wrong2+1
        sum=Right1+Right2
    accuracy=(sum/40)*100
    M=ConMatrix(Right1,wrong1,Right2,wrong2)
    return accuracy,M

def ConMatrix(R1,W1,R2,W2):
    C1=[R1,W2]
    C2=[W1,R2]
    Mat=[C1,C2]
    return Mat