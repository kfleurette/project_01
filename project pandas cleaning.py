import pandas as pd

df = pd.read_excel(r"C:\Users\user\Documents\Customer Call List.xlsx")


df = df.drop_duplicates()

df = df.drop(columns= "Not_Useful_Column")

#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")

df["Last_Name"] = df["Last_Name"].str.strip("123._/")


#this line is not working

#df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('[^a-zA-Z0-9]','')



df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('|','')
df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('/','')
df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('-','')
df["Phone_Number"] = df["Phone_Number"].astype(str).apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('N/a--','')
df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('Na--','')

df[["Street_Address","State","Zip_Code"]] = df["Address"].str.split(',', expand=True)


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')

df = df.fillna('')

for x in df.index :
    if df.loc[x,"Do_Not_Contact" ] == 'Y' :
        df.drop(x, inplace=True)

for x in df.index :
    if df.loc[x,"Phone_Number" ] == '' :
        df.drop(x, inplace=True)

for x in df.index :
    if df.loc[x,"Do_Not_Contact" ] == '' :
        df.drop(x, inplace=True) 

df = df.reset_index(drop=True)

print(df)


