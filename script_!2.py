import pandas as pd
import random
from faker import Faker

fake = Faker('es_ES')

datos=[]

for i in range(5000):
    datos.append({
        "FechaRegistro": fake.date_this_year(),
        "Especialidad": random.choice([
            "Cardiología",
            "Pediatría",
            "Dermatología",
            "Traumatología"
        ]),
        "TipoEvento": random.choice([
            "Reserva",
            "Cancelación",
            "Reprogramación"
        ]),
        "TiempoEspera": random.randint(5,120),
        "Sede": random.choice([
            "Los Olivos",
            "Comas",
            "Independencia"
        ]),
        "Costo": random.randint(80,500)
    })

df=pd.DataFrame(datos)
df.to_csv("citas_bigdata.csv",index=False)
print(df.head())
