import streamlit as st
import pandas as pd
import numpy as np
from questions import Question


#heading da página da Calculadora de Orçamento



abertura=st.sidebar
abertura.image('./assets/logomicroduino.png')
abertura.title('Calculadora Investimento')
abertura.header('Olá, vou te dar uma ideia do investimento para mudar a sua escola!')
abertura.write('São apenas 3 perguntas, não tomarei nem 5 min do seu tempo :) Ao fim do questionário, se tiver interesse podemos colocar um consultor em contato.')
abertura.write('Aproveite!')
Resultado1=0
Resultado2=0
Resultado3=0

     
     
st.title('Para quais níveis você quer orçar nossas soluções?')
nivelFund1= st.checkbox('Fundamental I') 
nivelFund2= st.checkbox('Fundamental II')
nivelMedio= st.checkbox('Ensino Médio')

#Coluna 1 - Alunos por Nível de Ensino
col1, col2 = st.beta_columns(2)
if nivelFund1 or nivelFund2 or nivelMedio:
    col1.write('Quantos alunos há em cada nível?')
if nivelFund1:
    alunosFund1= col1.number_input('Fundamental I', value=0, key='alunosFund1')
if nivelFund2:
    alunosFund2= col1.number_input('Fundamental II', value=0, key='alunosFund2')
if nivelMedio: 
    alunosMedio= col1.number_input('Ensino Médio', value=0, key='alunosMedio')


#Coluna 2 - Turmas por Nível de Ensino
if nivelFund1 or nivelFund2 or nivelMedio:
    col2.write('Quantas turmas há em cada nível?')
if nivelFund1:
    turmasFund1= col2.number_input('Fundamental I', value=0)
if nivelFund2:
    turmasFund2= col2.number_input('Fundamental II', value=0)
if nivelMedio:
    turmasMedio= col2.number_input('Ensino Médio', value=0)



if (nivelFund1 and turmasFund1!=0 and alunosFund1!=0):
    Resultado1 = alunosFund1*199
    st.write('Seu investimento para o Fundamental I será: R$', Resultado1)
if (nivelFund2 and turmasFund2!=0 and alunosFund2!=0):
    Resultado2 = turmasFund2*1299*8
    st.write('Seu investimento para o Fundamental I será: R$', Resultado2)
if (nivelMedio and turmasMedio!=0 and alunosMedio!=0):
    Resultado3 = turmasMedio*12900
    st.write('Seu investimento para o Fundamental I será: R$', Resultado3)

if (Resultado1!=0 or Resultado2!=0 or Resultado3!=0):
    somaTotal= st.write('Investimento Total: R$', Resultado1+Resultado2+Resultado3)