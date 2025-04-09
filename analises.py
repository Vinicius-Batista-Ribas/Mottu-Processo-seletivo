import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Mottu-Processo-seletivo\docs\Base_Completa_Churn_Mottu.xlsx - Base Churn Completa.csv")
motivos_controlaveis = [
    'Custo do plano',
    'Qualidade da moto',
    'Atendimento ao cliente',
    'Falta de manutenção preventiva',
    'Qualidade da moto'
]
df['tipo_churn'] = df["Motivo_do_Churn"].apply(lambda x: 'Controlavel' if x in motivos_controlaveis else "Não controlavel")

def plot(dados,titulo, xlabel):

    plt.figure(figsize=(8,4))
    dados.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel('Quantidade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"Mottu-Processo-seletivo/docs/imgs/{titulo}.png")
    plt.show()
    

churn = df["Motivo_do_Churn"].value_counts()
plot(churn,"Motivos do Churn", "Motivo")

churn_cont = df[df['tipo_churn'] == 'Controlavel'].groupby("Motivo_do_Churn")["Cliente_ID"].count()
plot(churn_cont,"Churn Controlaveis", "Motivo")

regioes = df.groupby("Região")["Motivo_do_Churn"].count()
plot(regioes,"Churn Por Região", "Região")

idade = df.groupby("Idade")["Motivo_do_Churn"].count()
plot(idade,"Churn Por Idade", "Idade")

tempo = df.groupby("Tempo_de_Contrato (meses)")["Motivo_do_Churn"].count()
plot(tempo,"Churn Por tempo de Contrato", "tempo (mêses)")

sazon = df.groupby("Mês_do_Churn")["Motivo_do_Churn"].count()
plot(sazon, "Mês do Churn", "Mês")
