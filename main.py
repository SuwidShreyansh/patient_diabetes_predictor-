import pandas as pd 
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("data.csv")
x=df.drop("Outcome",axis=1)
y=df["Outcome"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print()
print("MODEL ACCURACY : ", round(accuracy*100,2),"%")
while True:
    print("\n ENTER THE PATIENT DETAILS OR TYPE 'EXIT' : ")
    user_input=input("Pregnancies,Glucose ,Blood Pressure,SkinThickness , Insulin,BMI,DPF,Age:\n>")
    if user_input.lower()=="exit" :
        print("EXITING PROGRAM  : ")
        print("thank you !!!!")
        break
    try :
            values = list(map(float,user_input.split(",")))
            if len(values) !=8 :
                print("please enter exactly 8 values !")
                continue
            # prediction = model.predict(values)[0]
            input_df = pd.DataFrame([values], columns=x.columns)
            prediction = model.predict(input_df)[0]
            if prediction == 1 :
                print("===================")
                print("RESULT : DIABETIC ")
                print("===================")
            else :
                print("======================")
                print("RESULT : NOT DIABETIC ")
                print("======================")
    except ValueError :
        print("INVALID INPUT PLEASE ENTER NUMBER CORRECTLY")
