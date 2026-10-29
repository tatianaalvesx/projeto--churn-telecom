import streamlit as st
import joblib
import pandas as pd

# 1. Carregar o modelo treinado e a lista de colunas oficiais
modelo = joblib.load('modelo_churn.pkl')
colunas_modelo = joblib.load('colunas_modelo.pkl')

# 2. Configurar o design da página web
st.set_page_config(page_title="Previsor de Churn - Telecom", page_icon="📊", layout="centered")

st.title("📊 Simulador de Risco de Churn (Cancelamento)")
st.write("Esta aplicação utiliza Machine Learning (Regressão Logística) para prever se um cliente da operadora tem probabilidade de cancelar o serviço.")

st.markdown("---")

# 3. Criar os campos de entrada (Inputs) para o utilizador na barra lateral ou na tela principal
st.subheader("📝 Insira os dados do cliente:")

# Inputs interativos
tenure = st.slider("Tempo de relacionamento com a empresa (em meses):", 1, 72, 12)
monthly_charges = st.number_input("Valor da Mensalidade Atual ($):", min_value=0.0, max_value=200.0, value=70.0)
total_charges = st.number_input("Valor Total Pago até o momento ($):", min_value=0.0, max_value=10000.0, value=800.0)

contract = st.selectbox("Tipo de Contrato:", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Tipo de Internet:", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Método de Pagamento:", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
paperless_billing = st.selectbox("Fatura Digital (Paperless Billing):", ["Yes", "No"])
tech_support = st.selectbox("Suporte Técnico:", ["Yes", "No", "No internet service"])

# 4. Botão para efetuar a previsão
if st.button("🔮 Calcular Risco de Churn", type="primary"):
    
    # Criar um DataFrame em branco com todas as colunas que o modelo espera (preenchidas com 0)
    entrada_usuario = pd.DataFrame(0, index=[0], columns=colunas_modelo)
    
    # Preencher as colunas numéricas diretas
    if 'tenure' in entrada_usuario.columns:
        entrada_usuario['tenure'] = tenure
    if 'MonthlyCharges' in entrada_usuario.columns:
        entrada_usuario['MonthlyCharges'] = monthly_charges
    if 'TotalCharges' in entrada_usuario.columns:
        entrada_usuario['TotalCharges'] = total_charges
        
    # Preencher as variáveis categóricas usando a lógica do One-Hot Encoding (colunas de texto transformadas)
    # Exemplo: Contract_One year, Contract_Two year, InternetService_Fiber optic, etc.
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
        st.error(f"⚠️ **ALERTA DE ALTO RISCO DE CHURN!**")
        st.write(f" embora o modelo aponte cancelamento, a probabilidade calculada é de **{probabilidade * 100:.2f}%**.")
        st.info("💡 **Ação Recomendada:** Ofereça imediatamente uma migração para contrato anual ou um desconto no suporte técnico para reter este cliente.")
    else:
        st.success(f"✅ **CLIENTE SEGURO (Baixo risco de Churn)**")
        st.write(f"A probabilidade calculada de cancelamento é de apenas **{probabilidade * 100:.2f}%**.")
        st.info("💡 **Ação Recomendada:** Manter o bom atendimento habitual. O cliente demonstra forte estabilidade na base.")