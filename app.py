# Botão de Previsão
if st.button("🔍 Prever Risco de Churn", type="primary"):
    
    # Simulação da previsão do modelo (substitua pela lógica real do seu modelo)
    # Exemplo: se o modelo prever churn (1), exibe o alerta financeiro e estratégico
    risco_churn = True  # Altere para a variável real da previsão do seu modelo
    
    if risco_churn:
        st.error("⚠️ **Alerta:** Este cliente apresenta ALTO risco de cancelamento!")
        
        # Cálculos financeiros individuais
        valor_mensal = mensalidade
        valor_anual = valor_mensal * 12
        
        # Exibição do Impacto Financeiro
        st.warning(
            f"💰 **Impacto Financeiro Individual:**\n\n"
            f"- **Valor Mensal:** R$ {valor_mensal:.2f}\n"
            f"- **Prejuízo Anual Projetado (12 meses):** R$ {valor_anual:.2f}"
        )
        
        # Sugestão Estratégica de Ação
        st.info(
            "💡 **Estratégia Recomendada (Retenção):**\n\n"
            "1. **Acionamento Imediato:** Direcionar o perfil para a equipa de *Customer Success*.\n"
            "2. **Oferta Comercial Sugerida:** Conceder um desconto temporário de 15% condicionado à renovação de um contrato anual, ou realizar um *upgrade* de benefícios para aumentar o LTV (*Lifetime Value*) do cliente."
        )
    else:
        st.success("✅ **Cliente Estável:** O cliente apresenta baixo risco de cancelamento. Perfil saudável.")
