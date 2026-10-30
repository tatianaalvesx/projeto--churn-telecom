import streamlit as st
import joblib
import pandas as pd

# 1. Configurar o design da página web (Deve ser sempre a primeira linha do Streamlit)
st.set_page_config(page_title="Previsor de Churn - Telecom", page_icon="📊", layout="wide")

# 2. Carregar o modelo treinado e a lista de colunas oficiais
modelo = joblib.load('modelo_churn.pkl')
colunas_modelo = joblib.load('colunas_modelo.pkl')

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.header("Sobre o Projeto")
st.sidebar.info(
    "Esta aplicação utiliza Machine Learning (Regressão Logística) para prever "
    "a probabilidade de um cliente cancelar os serviços (Churn) numa operadora de telecomunicações."
)
st.sidebar.write("**Autora:** Tatiana Alves")
st.sidebar.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

# --- CORPO PRINCIPAL ---
st.title("📊 Simulador de Risco de Churn (Cancelamento)")
st.markdown("Bem-vindo(a)! Esta ferramenta interativa permite testar o modelo preditivo baseado na análise de comportamento dos clientes.")

# --- CAIXA 1: COMO INTERPRETAR ESTA APLICAÇÃO ---
with st.expander("ℹ️ Como interpretar esta aplicação?"):
    st.write(
        """
        - **O que é Churn?** É a taxa de cancelamento de clientes numa operadora.
        - **Como testar:** Preencha os dados do perfil do cliente nos seletores e cursores abaixo e clique no botão de cálculo.
        - **Resultado:** O modelo indicará se o cliente apresenta alto ou baixo risco de abandonar a empresa, exibindo a probabilidade exata e recomendações práticas de negócio.
        """
    )

# --- CAIXA 2: PERFIS COMPORTAMENTAIS E HIPÓTESES DE NEGÓCIO ---
with st.expander("📊 Perfis Comportamentais (Análise de Negócio e EDA)"):
    st.markdown(
        """
        Com base na nossa Análise Exploratória de Dados (EDA) e nos coeficientes do modelo preditivo, mapeámos o comportamento que diferencia os clientes:
        
        *   🔴 **Perfil de Alto Risco (Quem Cancela / Churn):**
            *   **Tempo de Casa (*Tenure*):** Clientes recém-chegados, com poucos meses de relacionamento (ainda não criaram vínculo com a marca).
            *   **Tipo de Contrato:** Contratos flexíveis **Mês a mês (*Month-to-month*)**, que facilitam a troca de operadora por terem barreiras de saída nulas.
            *   **Mensalidade (*MonthlyCharges*):** Faturas mensais mais elevadas, gerando maior sensibilidade ao preço e frustração quando ocorrem falhas.
            *   **Suporte Técnico:** **Ausência de suporte técnico**, agravando a insatisfação perante problemas operacionais.
            *   **Tecnologia e Pagamento:** Utilizadores de **Fibra Óptica**, adesão a fatura digital (*Paperless Billing*) e pagamento por **Cheque Eletrónico**.

            ***
        *   🟢 **Perfil de Baixo Risco (Cliente Seguro / Retido):**
            *   **Tempo de Casa (*Tenure*):** Clientes antigos com forte longevidade e estabilidade na base.
            *   **Tipo de Contrato:** Contratos de longo prazo (**1 ano** ou **2 anos**), que funcionam como uma âncora de retenção.
            *   **Suporte Técnico:** Presença ativa de **Suporte Técnico contratado**, garantindo assistência rápida e reduzindo o atrito.
            *   **Pagamento:** Métodos de pagamento estáveis e automáticos (transferência bancária ou cartão de crédito).
        """
    )

st.markdown("---")
st.subheader("📝 Insira os dados do cliente para simulação:")

# 3. Criar os campos de entrada (Inputs) estruturados em colunas para melhor organização
col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tempo de relacionamento com a empresa (em meses):", 1, 72, 12)
    monthly_charges = st.number_input("Valor da Mensalidade Atual ($):", min_value=0.0, max_value=200.0, value=70.0)
    total_charges = st.number_input("Valor Total Pago até o momento ($):", min_value=0.0, max_value=10000.0, value=800.0)
    contract = st.selectbox("Tipo de Contrato:", ["Month-to-month", "One year", "Two year"])

with col2:
    internet_service = st.selectbox("Tipo de Internet:", ["DSL", "Fiber optic", "No"])
    payment_method = st.selectbox("Método de Pagamento:", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    paperless_billing = st.selectbox("Fatura Digital (Paperless Billing):", ["Yes", "No"])
    tech_support = st.selectbox("Suporte Técnico:", ["Yes", "No", "No internet service"])

# 4. Botão para efetuar a previsão
if st.button("🔮 Calcular Risco de Churn", type="primary", use_container_width=True):
    
    # Criar um DataFrame em branco com todas as colunas que o modelo espera (preenchidas com 0)
    entrada_usuario = pd.DataFrame(0, index=[0], columns=colunas_modelo)
    
    # Preencher as colunas numéricas diretas
    if 'tenure' in entrada_usuario.columns:
        entrada_usuario['tenure'] = tenure
    if 'MonthlyCharges' in entrada_usuario.columns:
        entrada_usuario['MonthlyCharges'] = monthly_charges
    if 'TotalCharges' in entrada_usuario.columns:
        entrada_usuario['TotalCharges'] = total_charges
        
    # Preencher as variáveis categóricas usando a lógica do One-Hot Encoding
    col_contract = f"Contract_{contract}"
    if col_contract in entrada_usuario.columns:
        entrada_usuario[col_contract] = 1
        
    col_internet = f"InternetService_{internet_service}"
    if col_internet in entrada_usuario.columns:
        entrada_usuario[col_internet] = 1
        
    col_payment = f"PaymentMethod_{payment_method}"
    if col_payment in entrada_usuario.columns:
        entrada_usuario[col_payment] = 1
        
    if paperless_billing == "Yes" and "PaperlessBilling_Yes" in entrada_usuario.columns:
        entrada_usuario["PaperlessBilling_Yes"] = 1
        
    if tech_support == "Yes" and "TechSupport_Yes" in entrada_usuario.columns:
        entrada_usuario["TechSupport_Yes"] = 1
    elif tech_support == "No internet service" and "TechSupport_No internet service" in entrada_usuario.columns:
        entrada_usuario["TechSupport_No internet service"] = 1

    # 5. Executar a previsão com o modelo carregado
    probabilidade = modelo.predict_proba(entrada_usuario)[0][1] # Probabilidade de Churn (classe 1)
    previsao = modelo.predict(entrada_usuario)[0]
    
    st.markdown("---")
    st.subheader("🎯 Resultado da Análise:")
    
    # Exibir o resultado visualmente com cores e alertas
    if previsao == 1:
        st.error(f"⚠️ **ALERTA DE ALTO RISCO DE CHURN!** (Probabilidade: **{probabilidade * 100:.2f}%**)")
        st.info("💡 **Ação Recomendada:** Ofereça imediatamente uma migração para contrato anual ou um desconto no suporte técnico para reter este cliente.")
    else:
        st.success(f"✅ **CLIENTE SEGURO / BAIXO RISCO** (Probabilidade de Churn: **{probabilidade * 100:.2f}%**)")
        st.info("💡 **Ação Recomendada:** Manter o bom atendimento habitual. O cliente demonstra forte estabilidade na base.")
