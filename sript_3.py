import pandas as pd
from sqlalchemy import create_engine

# Aqui tus constraints
USER = "sa"
PASSWORD = "753159852"
SERVER = "localhost"
DATABASE = "ClinicaBigData"
DRIVER = "ODBC+Driver+17+for+SQL+Server"

engine = create_engine(f"mssql+pyodbc://{USER}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}")

query="""
SELECT * FROM citas_bigdata
"""

df=pd.read_sql(query,engine)

cancelaciones = len(
    df[df["TipoEvento"]=="Cancelación"]
)

total=len(df)

kpi_cancelacion=(cancelaciones/total)*100
print(kpi_cancelacion)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X=df[["TiempoEspera"]]
y=df["Costo"]

X_train,X_test,y_train,y_test= train_test_split(
X,y,test_size=0.2
)

modelo=LinearRegression()
modelo.fit(X_train,y_train)

pred=modelo.predict(X_test)

print("Precisión:",modelo.score(X_test,y_test))
