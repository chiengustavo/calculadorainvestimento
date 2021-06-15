import streamlit as st
import pandas as pd
import numpy as np

#heading da página da Calculadora de Orçamento
st.image('./assets/logomicroduino.png')
st.title('Calculadora Investimento')
st.header("Olá, vou te dar uma ideia do investimento para mudar a sua escola!")
caixaPerguntas = st.empty()
caixaResultado= st.empty()

#aqui começa a captura de informações

#Níveis de Ensino que a escola deseja orçar

formQuotation=caixaPerguntas.form(key='formQuotation')
formQuotation.header("Primeiro preciso saber para quais níveis de ensino você precisa encontrar soluções.")
nivelFund1=formQuotation.checkbox('Ensino Fundamental I')
nivelFund2=formQuotation.checkbox('Ensino Fundamental II')
nivelMedio=formQuotation.checkbox('Ensino Médio')
formQuotation.text_input('Quantos alunos no Fundamental I?')
formQuotation.text_input('E quantas turmas do Fundamental I?')
formQuotation.text_input('Quantos alunos no Fundamental II?')
formQuotation.text_input('E quantas turmas do Fundamental II?')
formQuotation.text_input('Quantos alunos no Ensino Médio?')
formQuotation.text_input('E quantas turmas do Ensino Médio?')

respostaForm=formQuotation.form_submit_button(label='Enviar informações!')
if respostaForm:
    st.success('Feito! Seu orçamento será enviado por email :)')








        


