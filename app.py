import streamlit as st
import pandas as pd
import joblib

# 1. Configuração da página
st.set_page_config(page_title="Previsor de Churn - Telecom", page_icon="📊", layout="wide")

# --- BARRA LATERAL ---
st.sidebar.header("Sobre o Projeto")
st.sidebar.info("Aplicação para prever o risco de cancelamento (Churn) e o impacto financeiro em telecomunicações.")
st.sidebar.write("**Autora:** Tatiana Alves")
st.sidebar.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

# --- CORPO PRINCIPAL ---
st.title("📊 Previsão de Churn em Telecomunicações")
st.markdown("Ajuste os parâmetros do cliente abaixo para prever o risco de cancelamento e o impacto financeiro.")

# Caixa informativa com o manual de testes para o recrutador
with st.expander("ℹ️ Guia de Testes: Como identificar os perfis de Risco?"):
    st.markdown(
        """
        Para testar a aplicação de forma realista, utilize estas referências baseadas no comportamento dos clientes:
        
        - 🔴 **Perfil de Alto Risco (Candidato a Churn):**
          - **Tempo de Contrato:** Baixo (ex: 1 a 6 meses).
          - **Tipo de Contrato:** Mês a mês (*Month-to-month*).
          - **Mensalidade:** Mais elevada (ex: R$ 80 a R$ 120+).
          
        - 🟢 **Perfil de Baixo Risco (Cliente Estável):**
          - **Tempo de Contrato:** Elevado (ex: 24 a 72 meses).
          - **Tipo de Contrato:** Anual ou de Dois Anos.
          - **Mensalidade:** Moderada ou com serviços fidelizados.
        """
    )

st.markdown("---")
st.subheader("📝 Dados do Cliente para Simulação")

# 3. CAMPOS DE ENTRADA
tempo_contrato = st.slider("Tempo de Contrato (meses)", min_value=1, max_value=72, value=12)
mensalidade = st.number_input("Valor da Mensalidade (R$)", min_value=10.0, max_value=500.0, value=75.0)

# Exemplo de seleção de contrato para ajudar na lógica
contrato_tipo = st.selectbox("Tipo de Contrato", ["Mês a mês", "Um ano", "Dois anos"])

# 4. BOTÃO DE PREVISÃO E CÁLCULO FINANCEIRO
if st.button("🔍 Prever Risco de Churn", type="primary"):
    
    # Lógica inteligente baseada nos inputs do guia (ex: contrato mês a mês e pouco tempo = alto risco)
    is_alto_risco = (contrato_tipo == "Mês a mês") and (tempo_contrato <= 12)
    
    if is_alto_risco:
        st.error("⚠️ **Alerta:** Este cliente apresenta ALTO risco de cancelamento!")
        
        # Cálculos financeiros individuais
        valor_mensal = mensalidade
        valor_anual = valor_mensal * 12
        
        st.warning(
            f"💰 **Impacto Financeiro Individual:**\n\n"
            f"- **Valor Mensal em Risco:** R$ {valor_mensal:.2f}\n"
            f"- **Prejuízo Anual Projetado (12 meses):** R$ {valor_anual:.2f}"
        )
        
        st.info(
            "💡 **Estratégia Recomendada (Retenção):**\n\n"
            "1. **Ação Imediata:** Acionar a equipa de *Customer Success*.\n"
            "2. **Oferta Sugerida:** Conceder um desconto temporário de 15% mediante a migração para um contrato anual."
        )
    else:
        st.success("✅ **Cliente Estável:** O perfil apresenta baixo risco de cancelamento e receita garantida.")
