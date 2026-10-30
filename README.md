# 📊 Previsão de Churn em Telecomunicações (End-to-End)

Este é um projeto completo de Ciência de Dados desenvolvido com foco em **resolução de problemas de negócio**, abrangendo desde a Análise Exploratória de Dados (EDA) e modelagem estatística até ao *Deploy* de uma aplicação web interativa na nuvem.

---

## 🚀 Sobre o Projeto
O objetivo deste projeto é prever o **Churn** (cancelamento de clientes) numa operadora de telecomunicações. Mais do que apenas treinar um algoritmo de Machine Learning (Regressão Logística), o foco foi extrair **insights de negócio acionáveis** e disponibilizar uma ferramenta real e interativa para que gestores possam simular o risco de clientes em tempo real.

- **🔗 Link de acesso à aplicação online:** [projeto-churn-telecom.streamlit.app](https://projeto--churn-telecom.streamlit.app)

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python 🐍
* **Manipulação e Análise de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Regressão Logística)
* **Persistência de Modelos:** Joblib (`.pkl`)
* **Interface Web / Deploy:** Streamlit & Streamlit Cloud
* **Visualização:** Matplotlib, Seaborn

---

## 📈 Principais Insights de Negócio e Perfis Comportamentais
Através da Análise Exploratória de Dados (EDA) e da interpretabilidade dos coeficientes do modelo, mapeámos os fatores críticos que influenciam o comportamento dos clientes:

* **🔴 Perfil de Alto Risco (Quem Cancela / Churn):**
  * **Tempo de Casa (*Tenure*):** Clientes recém-chegados, com poucos meses de relacionamento (ainda não criaram vínculo com a marca).
  * **Tipo de Contrato:** Contratos flexíveis **Mês a mês (*Month-to-month*)**, que facilitam a troca de operadora por terem barreiras de saída nulas.
  * **Mensalidade (*MonthlyCharges*):** Faturas mensais mais elevadas, gerando maior sensibilidade ao preço e frustração.
  * **Suporte Técnico:** **Ausência de suporte técnico**, agravando a insatisfação perante problemas operacionais.
  * **Tecnologia e Pagamento:** Utilizadores de **Fibra Óptica**, adesão a fatura digital (*Paperless Billing*) e pagamento por **Cheque Eletrónico**.

* **🟢 Perfil de Baixo Risco (Cliente Seguro / Retido):**
  * **Tempo de Casa (*Tenure*):** Clientes antigos com forte longevidade e estabilidade na base.
  * **Tipo de Contrato:** Contratos de longo prazo (**1 ano** ou **2 anos**), funcionando como âncoras de retenção.
  * **Suporte Técnico:** Presença ativa de **Suporte Técnico contratado**, garantindo assistência rápida e reduzindo o atrito.
  * **Pagamento:** Métodos de pagamento mais estáveis e automáticos.

---

## 🕹️ Como Testar a Aplicação Web
Pode testar a aplicação interativa de duas formas:

 **Diretamente na nuvem (Recomendado):** 
   Acesso ao link oficial: **[projeto-churn-telecom.streamlit.app](https://projeto--churn-telecom.streamlit.app)**

    
### 💡 Cenários de Teste Sugeridos na Aplicação:
* **Perfil de Alto Risco (Simulação de Alerta):**
  * *Tempo de casa:* 1 a 6 meses
  * *Contrato:* Mês a mês (*Month-to-month*)
  * *Internet:* Fibra Óptica (*Fiber optic*)
  * *Suporte Técnico:* Não (*No*)
  * *Método de pagamento:* Cheque Eletrónico (*Electronic check*)
* **Perfil de Baixo Risco (Cliente Seguro):**
  * *Tempo de casa:* 36 a 72 meses
  * *Contrato:* Dois anos (*Two year*)
  * *Suporte Técnico:* Sim (*Yes*)

 
