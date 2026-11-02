import streamlit as st
import pandas as pd
import joblib

# 1. Configuração da página
st.set_page_config(page_title="Previsor de Churn - Telecom", page_icon="📊", layout="wide")

# --- BARRA LATERAL ---
st.sidebar.header("Sobre o Projeto")
st.sidebar.info("Aplicação interativa para prever o risco de cancelamento (Churn), o impacto financeiro individual e estratégias de retenção em telecomunicações.")
st.sidebar.write("**Autora:** Tatiana Alves")
st.sidebar.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com/tatianaalvesx/projeto-churn-telecom)")

# --- CORPO PRINCIPAL ---
st.title("📊 Previsão de Churn em Telecomunicações")
st.markdown("Ajuste os parâmetros do cliente abaixo para simular o risco de cancelamento, o impacto financeiro e a estratégia comercial recomendada.")

# Guia Completo com todos os Perfis Validados na Análise Exploratória
with st.expander("ℹ️ Guia de Análise: Perfis de Alto Risco vs. Baixo Risco (Baseado em EDA)"):
    st.markdown(
        """
        Através da nossa Análise Exploratória de Dados (EDA) e interpretabilidade do modelo, mapeámos os seguintes padrões comportamentais:
        
        - 🔴 **Perfil de Alto Risco (Candidato a Churn):**
          - **Tempo de Contrato (*Tenure*):** Baixo (1 a 6 meses), clientes recém-chegados sem vínculo firme.
          - **Tipo de Contrato:** Flexível, do tipo **Mês a mês (*Month-to-month*)** (sem barreiras de saída).
          - **Mensalidade (*MonthlyCharges*):** Valores mais elevados (faturas mais pesadas).
          - **Suporte Técnico:** **Ausência de suporte técnico**, agravando a insatisfação perante problemas.
          - **Tecnologia:** Utilização de **Fibra Óptica**.
          - **Pagamento:** pagamente por **Cheque Eletrônico**.
          ---
          
        - 🟢 **Perfil de Baixo Risco (Cliente Estável / Retido):**
          - **Tempo de Contrato (*Tenure*):** Elevado (longevidade e estabilidade na base).
          - **Tipo de Contrato:** Fidelização de longo prazo (**1 ano** ou **2 anos**).
          - **Suporte Técnico:** Presença ativa de **Suporte Técnico contratado**, garantindo assistência rápida.
          - **Pagamento:** Métodos de pagamento mais estáveis como **Debito Automaatico**,**Cartão de Credito** e **Faturas via Corrreio**
        """
    )

st.markdown("---")
st.subheader("📝 Parâmetros para Simulação do Cliente")

# Organização em 3 colunas para separar claramente Contrato, Tecnologia e Pagamento
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("##### 📄 Contrato e Custos")
    tempo_contrato = st.slider("Tempo de Contrato (meses)", min_value=1, max_value=72, value=6)
    mensalidade = st.number_input("Valor da Mensalidade (R$)", min_value=10.0, max_value=500.0, value=85.0)
    contrato_tipo = st.selectbox("Tipo de Contrato", ["Mês a mês", "Um ano", "Dois anos"])

with col2:
    st.markdown("##### 🌐 Tecnologia e Serviços")
    internet_servico = st.selectbox("Tipo de Internet", ["Fiber optic", "DSL", "No"])
    suporte_tecnico = st.selectbox("Possui Suporte Técnico?", ["No", "Yes", "No internet service"])

with col3:
    st.markdown("##### 💳 Faturação e Pagamento")
    pagamento_metodo = st.selectbox("Método de Pagamento", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    fatura_digital = st.selectbox("Fatura Digital (Paperless)?", ["Yes", "No"])

st.markdown("---")

# 4. BOTÃO DE PREVISÃO E CÁLCULO FINANCEIRO
if st.button("🔍 Prever Risco de Churn e Impacto Financeiro", type="primary"):
    
    # Lógica inteligente refletindo o perfil de risco mapeado na análise de negócio
    is_alto_risco = (contrato_tipo == "Mês a mês") and (tempo_contrato <= 12) and (internet_servico == "Fiber optic") and (pagamento_metodo == "Electronic check")
    
    if is_alto_risco:
        st.error("⚠️ **Alerta de Negócio:** Este cliente apresenta perfil de ALTO risco de cancelamento!")
        
        # Cálculos financeiros individuais (Mensal e Anual)
        valor_mensal = mensalidade
        valor_anual = valor_mensal * 12
        
        st.warning(
            f"💰 **Impacto Financeiro Individual:**\n\n"
            f"- **Valor Mensal em Risco:** R$ {valor_mensal:.2f}\n"
            f"- **Prejuízo Anual Projetado (12 meses):** R$ {valor_anual:.2f}"
        )
        
        st.info(
            "💡 **Estratégia Recomendada (Retenção):**\n\n"
            "1. **Ação Imediata:** Acionar a equipa de *Retenção* para acompanhamento proativo.\n"
            "2. **Oferta Comercial Sugerida:** Oferecer um desconto temporário de **15%** condicionado à migração imediata para um contrato anual, associado à ativação gratuita de suporte técnico prioritário."
        )
    else:
        st.success("✅ **Cliente Estável:** O perfil apresenta baixo risco de cancelamento, demonstrando forte retenção e receita garantida.")
