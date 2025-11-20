import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
data = pd.read_excel(r"C:\Users\pranshu bhalja\OneDrive\Desktop\College\Smart Quality Checker\Data.xlsx")
df = pd.DataFrame(data)
cl = {}
for col in df:
    mean = df[col].mean()
    sd = df[col].std()
    ucl = mean + (3 * sd)
    lcl = mean - (3 * sd)
    cl[col] = {"Mean": mean, "SD": sd, "UCL": ucl, "LCL": lcl}
cl_df = pd.DataFrame(cl)
def check(row):
    status_list = []
    severity_list = []
    for col in df:
        if row[col] > cl_df.loc["UCL", col]:
            if row[col] <= cl_df.loc["UCL", col] + cl_df.loc["SD", col]:
                status_list.append(f"Minor high in {col}")
                severity_list.append("Minor")
            else:
                status_list.append(f"Major high in {col}")
                severity_list.append("Major")
        elif row[col] < cl_df.loc["LCL", col]:
            if row[col] >= cl_df.loc["LCL", col] - cl_df.loc["SD", col]:
                status_list.append(f"Minor low in {col}")
                severity_list.append("Minor")
            else:
                status_list.append(f"Major low in {col}")
                severity_list.append("Major")
    if not status_list:
        return "In control", "In control"
    else:
        detail = "; ".join(status_list)
        if "Major" in severity_list:
            severity = "Major"
        else:
            severity = "Minor"
        return detail, severity
df[["Status_Detail", "Severity"]] = df.apply(lambda row: pd.Series(check(row)), axis=1)
df.to_excel(r"C:\Users\pranshu bhalja\OneDrive\Desktop\College\Smart Quality Checker\Data_with_Status.xlsx", index=False)

d_f=pd.read_excel(r"C:\Users\pranshu bhalja\OneDrive\Desktop\College\Smart Quality Checker\Data_with_Status.xlsx")
X=d_f[["Current_Temperature","Temperature_Error","Overshoot","Response_Time","Steady_State_Error","Ambient_Temperature","Humidity"]]
y=d_f["Severity"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scale=StandardScaler()
scale.fit(X_train)
X_train=scale.transform(X_train)
X_test=scale.transform(X_test)
classifier=RandomForestClassifier(n_estimators=100,class_weight='balanced',random_state=42)
classifier.fit(X_train,y_train)
y_predict=classifier.predict(X_test)
print(y_predict)
print(confusion_matrix(y_test,y_predict))
print(classification_report(y_test,y_predict))



