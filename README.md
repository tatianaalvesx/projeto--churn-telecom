# 📊 Previsão de Churn em Telecomunicações (End-toEnd)
Este é um projeto completo de Ciência de Dados desenvolvido com foco em **resolução de problema de negócio**, abrangendo desde a Análise Exploratória de Dados (EDA) e a modelagem estatística até ao *Deploy* de uma aplicação web interativa.

---

## Sobre o Projeto
o objetivo deste projeto é prever o **Churn** (cancelamento do clientes) numa operadora de telecomunicações. Mais do que treinar um algoritmo, o foco foi extrair **insights de negócio acionáveis** e disponibilizar uma ferramenta real para que gestores possam simular o risco de cancelamento de clientes em tempo real.

---

## Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Phyton
* **Manipulação e Análise de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Regressão Logistica)
* **Persistência de Modelos:** Joblib ('.pkl')
* **Interface Web / Deploy:** Streamlit
* **Visualização:** Matplotlib, Seaborn

 ---

 ## Principais Insights de Negócio (Interpretabiliade do Modelo)
 Através da análise dos coeficientes do modelo de Regressão Logística, identificamos os fatores críticos que influenciam o comportamento dos clientes:
 * **🔴 Fatores de Maior Risco (Churn):** Clientes com serviço de **Fibra Óptica**, utilizadores de **Fatura Digital** (*Paperless Billing*)** e pagamento por **Cheque Eletrônico** apresentam maior proprensão ao cancelamento.
 * **🟢 fatores de Retenção (Fidelização):** **Contrato de 2 anos**  e de **1 ano**, aliados ao uso de **Suporte Técnico**, funcionam como âncoras mais poderosas para manter o cliente na base.

 ---

 ## Como Testar a Aplicação Interativa
 Você pode testar a aplicação web de previsão de Churn em tempo real!

 
