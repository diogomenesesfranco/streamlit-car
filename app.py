import pandas as pd
import streamlit as st
import joblib
import numpy as np
import streamlit.components.v1 as components
from PIL import Image
import base64
import requests
from io import BytesIO
import locale

def prever_preco(modelo, dados):
    preco = modelo.predict(dados)
    return preco

def preprocessamento(valores_x):    
    valores_x['PRE_make_Kia'] = [1 if x=='KIA'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Nissan'] = [1 if x=='NISSAN'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Chevrolet'] = [1 if x=='CHEVROLET'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Ford'] = [1 if x=='FORD'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Hyundai'] = [1 if x=='HYUNDAI'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_BMW'] = [1 if x=='BMW'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Toyota'] = [1 if x=='TOYOTA'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Dodge'] = [1 if x=='DODGE'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Chrysler'] = [1 if x=='CHRYSLER'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Honda'] = [1 if x=='HONDA'   else 0 for x in valores_x['make']]

    valores_x['PRE_body_SUV'] = [1 if x=='SUV'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_SEDAN'] = [1 if x=='SEDAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CONVERTIBLE'] = [1 if x=='CONVERTIBLE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_COUPE'] = [1 if x=='COUPE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_HATCHBACK'] = [1 if x=='HATCHBACK'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CREW CAB'] = [1 if x=='CREW CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_ELANTRA COUPE'] = [1 if x=='ELANTRA COUPE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_GENESIS COUPE'] = [1 if x=='GENESIS COUPE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_WAGON'] = [1 if x=='WAGON'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_MINIVAN'] = [1 if x=='MINIVAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_VAN'] = [1 if x=='VAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_DOUBLE CAB'] = [1 if x=='DOUBLE CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CREWMAX CAB'] = [1 if x=='CREWMAX CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_ACCESS CAB'] = [1 if x=='ACCESS CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_KING CAB'] = [1 if x=='KING CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_SUPERCREW'] = [1 if x=='SUPERCREW'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_EXTENDED CAB'] = [1 if x=='EXTENDED CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_E-SERIES VAN'] = [1 if x=='E-SERIES VAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_SUPERCAB'] = [1 if x=='SUPERCAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_REGULAR CAB'] = [1 if x=='REGULAR CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_KOUP'] = [1 if x=='KOUP'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_QUAD CAB'] = [1 if x=='QUAD CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CLUB CAB'] = [1 if x=='CLUB CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_MEGA CAB'] = [1 if x=='MEGA CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_TRANSIT VAN'] = [1 if x=='TRANSIT VAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_REGULAR-CAB'] = [1 if x=='REGULAR-CAB'   else 0 for x in valores_x['body']]
        
    valores_x['PRE_state_CA'] = [1 if x=='CA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_WI'] = [1 if x=='WI'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_FL'] = [1 if x=='FL'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_PA'] = [1 if x=='PA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NV'] = [1 if x=='NV'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NJ'] = [1 if x=='NJ'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NC'] = [1 if x=='NC'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_VA'] = [1 if x=='VA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_IN'] = [1 if x=='IN'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_IL'] = [1 if x=='IL'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_TN'] = [1 if x=='TN'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MN'] = [1 if x=='MN'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MI'] = [1 if x=='MI'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_OH'] = [1 if x=='OH'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_TX'] = [1 if x=='TX'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_AZ'] = [1 if x=='AZ'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_CO'] = [1 if x=='CO'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_UT'] = [1 if x=='UT'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_GA'] = [1 if x=='GA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MO'] = [1 if x=='MO'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MD'] = [1 if x=='MD'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_LA'] = [1 if x=='LA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NY'] = [1 if x=='NY'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NE'] = [1 if x=='NE'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_WA'] = [1 if x=='WA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_SC'] = [1 if x=='SC'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_PR'] = [1 if x=='PR'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MA'] = [1 if x=='MA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_OR'] = [1 if x=='OR'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_QC'] = [1 if x=='QC'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_AB'] = [1 if x=='AB'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_HI'] = [1 if x=='HI'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_ON'] = [1 if x=='ON'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_OK'] = [1 if x=='OK'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MS'] = [1 if x=='MS'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NM'] = [1 if x=='NM'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_AL'] = [1 if x=='AL'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NS'] = [1 if x=='NS'   else 0 for x in valores_x['state']]

    valores_x['PRE_color_WHITE'] = [1 if x=='WHITE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_GRAY'] = [1 if x=='GRAY'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BLACK'] = [1 if x=='BLACK'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_RED'] = [1 if x=='RED'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_SILVER'] = [1 if x=='SILVER'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BLUE'] = [1 if x=='BLUE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_PURPLE'] = [1 if x=='PURPLE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BURGUNDY'] = [1 if x=='BURGUNDY'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_GOLD'] = [1 if x=='GOLD'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BEIGE'] = [1 if x=='BEIGE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_YELLOW'] = [1 if x=='YELLOW'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_GREEN'] = [1 if x=='GREEN'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_NÃOESPECIFICADO'] = [1 if x=='NÃO ESPECIFICADO'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BROWN'] = [1 if x=='BROWN'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_CHARCOAL'] = [1 if x=='CHARCOAL'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_ORANGE'] = [1 if x=='ORANGE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_TURQUOISE'] = [1 if x=='TURQUOISE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_PINK'] = [1 if x=='PINK'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_OFF-WHITE'] = [1 if x=='OFF-WHITE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_LIME'] = [1 if x=='LIME'   else 0 for x in valores_x['color']]	
        
    valores_x['PRE_interior_BLACK'] = [1 if x=='BLACK'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BEIGE'] = [1 if x=='BEIGE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_TAN'] = [1 if x=='TAN'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_GRAY'] = [1 if x=='GRAY'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BROWN'] = [1 if x=='BROWN'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BURGUNDY'] = [1 if x=='BURGUNDY'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_WHITE'] = [1 if x=='WHITE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_SILVER'] = [1 if x=='SILVER'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_OFF-WHITE'] = [1 if x=='OFF-WHITE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_RED'] = [1 if x=='RED'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_YELLOW'] = [1 if x=='YELLOW'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BLUE'] = [1 if x=='BLUE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_PURPLE'] = [1 if x=='PURPLE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_NÃOESPECIFICADO'] = [1 if x=='NÃO ESPECIFICADO'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_GREEN'] = [1 if x=='GREEN'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_ORANGE'] = [1 if x=='ORANGE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_GOLD'] = [1 if x=='GOLD'   else 0 for x in valores_x['interior']]
        
    valores_x['PRE_model_ALTIMA'] = [1 if x=='ALTIMA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FUSION'] = [1 if x=='FUSION'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ESCAPE'] = [1 if x=='ESCAPE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAMRY'] = [1 if x=='CAMRY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_F-150'] = [1 if x=='F-150'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FOCUS'] = [1 if x=='FOCUS'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_GRAND_CARAVAN'] = [1 if x=='GRAND CARAVAN'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_IMPALA'] = [1 if x=='IMPALA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SONATA'] = [1 if x=='SONATA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACCORD'] = [1 if x=='ACCORD'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_MALIBU'] = [1 if x=='MALIBU'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_COROLLA'] = [1 if x=='COROLLA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CRUZE'] = [1 if x=='CRUZE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_3_SERIES'] = [1 if x=='3 SERIES'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELANTRA'] = [1 if x=='ELANTRA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CIVIC'] = [1 if x=='CIVIC'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_EDGE'] = [1 if x=='EDGE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ROGUE'] = [1 if x=='ROGUE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_TOWN_AND_COUNTRY'] = [1 if x=='TOWN AND COUNTRY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPLORER'] = [1 if x=='EXPLORER'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SENTRA'] = [1 if x=='SENTRA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_1500'] = [1 if x=='SILVERADO 1500'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_EQUINOX'] = [1 if x=='EQUINOX'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CHARGER'] = [1 if x=='CHARGER'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_OPTIMA'] = [1 if x=='OPTIMA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_200'] = [1 if x=='200'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_MUSTANG'] = [1 if x=='MUSTANG'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVENGER'] = [1 if x=='AVENGER'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_TAURUS'] = [1 if x=='TAURUS'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_300'] = [1 if x=='300'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_R4V4'] = [1 if x=='R4V4'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_JOURNEY'] = [1 if x=='JOURNEY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_VERSA'] = [1 if x=='VERSA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FORTE'] = [1 if x=='FORTE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SOUL'] = [1 if x=='SOUL'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CR-V'] = [1 if x=='CR-V'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ODYSSEY'] = [1 if x=='ODYSSEY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FIESTA'] = [1 if x=='FIESTA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_MURANO'] = [1 if x=='MURANO'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_5_SERIES'] = [1 if x=='5 SERIES'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SIENNA'] = [1 if x=='SIENNA'   else 0 for x in valores_x['model']]
        
    valores_x['PRE_trim_SE'] = [1 if x=='SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LX'] = [1 if x=='LX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS'] = [1 if x=='LS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLT'] = [1 if x=='XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED'] = [1 if x=='LIMITED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BASE'] = [1 if x=='BASE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT'] = [1 if x=='LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GLS'] = [1 if x=='GLS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE'] = [1 if x=='LE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5 S'] = [1 if x=='2.5 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEXT'] = [1 if x=='SEXT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEL'] = [1 if x=='SEL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S'] = [1 if x=='S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING'] = [1 if x=='TOURING' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_V-6'] = [1 if x=='EX V-6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5'] = [1 if x=='2.5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX'] = [1 if x=='EX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SV'] = [1 if x=='SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX-L'] = [1 if x=='EX-L' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5_SV'] = [1 if x=='3.5 SV' else 0 for x in valores_x['trim']]

    return valores_x

def coletar_dados_usuario():
    
        # Inputs numéricos
    with st.sidebar.expander("Condição do Veículo"):
        idade_carro = st.number_input("Idade do Veículo", min_value=0, step=1, value=0, key="idade_carro_input")
        mmr = st.number_input("Preço da Tabela Fipe", min_value=0, step=1, value=0, key="mmr_input")
        condition = st.number_input("Estado do Veículo ( 0 - 100) ", min_value=0, step=1, value=0, key="condition_input")
        odometer = st.number_input("Kilometragem", min_value=0, step=1, value=0, key="odometer_input")  
    
    # Inputs categóricos
    with st.sidebar.expander("Especificação Técnica do Veículo"):
        make = st.selectbox("Fabricante", ['KIA', 'BMW', 'NISSAN', 'CHEVROLET', 'FORD', 'HYUNDAI', 'TOYOTA', 'DODGE', 'CHRYSLER', 'HONDA'], key="make_input")
        body = st.selectbox("Categoria", ['SUV', 'SEDAN', 'CONVERTIBLE', 'COUPE', 'HATCHBACK', 'CREW CAB', 'ELANTRA COUPE', 'GENESIS COUPE', 'WAGON', 'MINIVAN', 'VAN', 'DOUBLE CAB', 'CREWMAX CAB', 'ACCESS CAB', 'KING CAB', 'SUPERCREW', 'EXTENDED CAB', 'E-SERIES VAN', 'SUPERCAB', 'REGULAR CAB', 'KOUP', 'QUAD CAB', 'CLUB CAB', 'MEGA CAB', 'TRANSIT VAN', 'REGULAR-CAB'], key="body_input")
        state = st.selectbox("Estado", ['CA', 'TX', 'PA', 'MN', 'AZ', 'WI', 'TN', 'MD', 'FL', 'NE', 'NV', 'OH', 'MI', 'NJ', 'SC', 'NC', 'VA', 'IN', 'IL', 'CO', 'UT', 'GA', 'MO', 'NY', 'LA', 'WA', 'PR', 'MA', 'HI', 'OR', 'QC', 'AB', 'ON', 'OK', 'MS', 'NM', 'AL', 'NS'], key="state_input")
        color = st.selectbox("Cor", ['WHITE', 'GRAY', 'BLACK', 'RED', 'SILVER', 'BLUE', 'PURPLE', 'BURGUNDY', 'GOLD', 'BEIGE', 'YELLOW', 'GREEN', 'NÃO ESPECIFICADO', 'BROWN', 'CHARCOAL', 'ORANGE', 'TURQUOISE', 'PINK', 'OFF-WHITE', 'LIME'], key="color_input")
        interior = st.selectbox("Cor Interior", ['BLACK', 'BEIGE', 'TAN', 'GRAY', 'BROWN', 'BURGUNDY', 'WHITE', 'SILVER', 'OFF-WHITE', 'RED', 'YELLOW', 'BLUE', 'NÃO ESPECIFICADO', 'PURPLE', 'GREEN', 'ORANGE', 'GOLD'], key="interior_input")
        trim = st.selectbox("Tipo", ['SE', 'LX', 'LS', 'XLT', 'LIMITED', 'BASE', 'LT', 'GLS', 'LE', '2.5 S', 'SEXT', 'SEL', 'S', 'TOURING', 'EX V-6', '2.5', 'EX', 'SV', 'EX-L', '3.5 SV'], key="trim_input")
        model = st.selectbox("Modelo", ['ALTIMA', 'FUSION', 'ESCAPE', 'CAMRY', 'F-150', 'FOCUS', 'GRAND CARAVAN', 'IMPALA', 'SONATA', 'ACCORD', 'MALIBU', 'COROLLA', 'CRUZE', '3 SERIES', 'ELANTRA', 'CIVIC', 'EDGE', 'ROGUE', 'TOWN AND COUNTRY', 'EXPLORER', 'SENTRA', 'SILVERADO 1500', 'EQUINOX', 'CHARGER', 'OPTIMA', '200', 'MUSTANG', 'AVENGER', 'TAURUS', '300', 'R4V4', 'JOURNEY', 'VERSA', 'FORTE', 'SOUL', 'CR-V', 'ODYSSEY', 'FIESTA', 'MURANO', '5 SERIES', 'SIENNA'], key="model_input")

    return {
        'condition': condition,
        'odometer': odometer,
        'mmr': mmr,
        'idade_carro': idade_carro,
        'make': make,
        'body': body,
        'state': state,
        'color': color,
        'interior': interior,
        'model': model,
        'trim': trim
    }
import streamlit as st

def pagina_intro():
    st.title("Bem-vindo ao Sistema de Previsão de Preços de Veículos")
    st.write("Esta aplicação prevê o preço de um veículo com base em várias características.")
    st.write("Por favor, selecione a página que deseja acessar:")

    pagina_selecionada = st.selectbox("Selecione a Página", ["Página Inicial", "Previsão de Preço"])
    return pagina_selecionada

def prever_preco(modelo, dados):
    preco = modelo.predict(dados)
    return preco

def preprocessamento(valores_x):    
    valores_x['PRE_make_Kia'] = [1 if x=='KIA'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Nissan'] = [1 if x=='NISSAN'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Chevrolet'] = [1 if x=='CHEVROLET'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Ford'] = [1 if x=='FORD'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Hyundai'] = [1 if x=='HYUNDAI'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_BMW'] = [1 if x=='BMW'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Toyota'] = [1 if x=='TOYOTA'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Dodge'] = [1 if x=='DODGE'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Chrysler'] = [1 if x=='CHRYSLER'   else 0 for x in valores_x['make']]
    valores_x['PRE_make_Honda'] = [1 if x=='HONDA'   else 0 for x in valores_x['make']]

    valores_x['PRE_body_SUV'] = [1 if x=='SUV'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_SEDAN'] = [1 if x=='SEDAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CONVERTIBLE'] = [1 if x=='CONVERTIBLE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_COUPE'] = [1 if x=='COUPE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_HATCHBACK'] = [1 if x=='HATCHBACK'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CREW CAB'] = [1 if x=='CREW CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_ELANTRA COUPE'] = [1 if x=='ELANTRA COUPE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_GENESIS COUPE'] = [1 if x=='GENESIS COUPE'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_WAGON'] = [1 if x=='WAGON'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_MINIVAN'] = [1 if x=='MINIVAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_VAN'] = [1 if x=='VAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_DOUBLE CAB'] = [1 if x=='DOUBLE CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CREWMAX CAB'] = [1 if x=='CREWMAX CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_ACCESS CAB'] = [1 if x=='ACCESS CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_KING CAB'] = [1 if x=='KING CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_SUPERCREW'] = [1 if x=='SUPERCREW'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_EXTENDED CAB'] = [1 if x=='EXTENDED CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_E-SERIES VAN'] = [1 if x=='E-SERIES VAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_SUPERCAB'] = [1 if x=='SUPERCAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_REGULAR CAB'] = [1 if x=='REGULAR CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_KOUP'] = [1 if x=='KOUP'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_QUAD CAB'] = [1 if x=='QUAD CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_CLUB CAB'] = [1 if x=='CLUB CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_MEGA CAB'] = [1 if x=='MEGA CAB'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_TRANSIT VAN'] = [1 if x=='TRANSIT VAN'   else 0 for x in valores_x['body']]
    valores_x['PRE_body_REGULAR-CAB'] = [1 if x=='REGULAR-CAB'   else 0 for x in valores_x['body']]
        
    valores_x['PRE_state_CA'] = [1 if x=='CA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_WI'] = [1 if x=='WI'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_FL'] = [1 if x=='FL'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_PA'] = [1 if x=='PA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NV'] = [1 if x=='NV'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NJ'] = [1 if x=='NJ'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NC'] = [1 if x=='NC'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_VA'] = [1 if x=='VA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_IN'] = [1 if x=='IN'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_IL'] = [1 if x=='IL'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_TN'] = [1 if x=='TN'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MN'] = [1 if x=='MN'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MI'] = [1 if x=='MI'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_OH'] = [1 if x=='OH'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_TX'] = [1 if x=='TX'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_AZ'] = [1 if x=='AZ'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_CO'] = [1 if x=='CO'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_UT'] = [1 if x=='UT'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_GA'] = [1 if x=='GA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MO'] = [1 if x=='MO'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MD'] = [1 if x=='MD'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_LA'] = [1 if x=='LA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NY'] = [1 if x=='NY'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NE'] = [1 if x=='NE'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_WA'] = [1 if x=='WA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_SC'] = [1 if x=='SC'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_PR'] = [1 if x=='PR'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MA'] = [1 if x=='MA'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_OR'] = [1 if x=='OR'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_QC'] = [1 if x=='QC'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_AB'] = [1 if x=='AB'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_HI'] = [1 if x=='HI'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_ON'] = [1 if x=='ON'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_OK'] = [1 if x=='OK'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_MS'] = [1 if x=='MS'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NM'] = [1 if x=='NM'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_AL'] = [1 if x=='AL'   else 0 for x in valores_x['state']]
    valores_x['PRE_state_NS'] = [1 if x=='NS'   else 0 for x in valores_x['state']]

    valores_x['PRE_color_WHITE'] = [1 if x=='WHITE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_GRAY'] = [1 if x=='GRAY'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BLACK'] = [1 if x=='BLACK'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_RED'] = [1 if x=='RED'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_SILVER'] = [1 if x=='SILVER'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BLUE'] = [1 if x=='BLUE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_PURPLE'] = [1 if x=='PURPLE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BURGUNDY'] = [1 if x=='BURGUNDY'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_GOLD'] = [1 if x=='GOLD'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BEIGE'] = [1 if x=='BEIGE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_YELLOW'] = [1 if x=='YELLOW'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_GREEN'] = [1 if x=='GREEN'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_NÃOESPECIFICADO'] = [1 if x=='NÃO ESPECIFICADO'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_BROWN'] = [1 if x=='BROWN'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_CHARCOAL'] = [1 if x=='CHARCOAL'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_ORANGE'] = [1 if x=='ORANGE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_TURQUOISE'] = [1 if x=='TURQUOISE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_PINK'] = [1 if x=='PINK'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_OFF-WHITE'] = [1 if x=='OFF-WHITE'   else 0 for x in valores_x['color']]
    valores_x['PRE_color_LIME'] = [1 if x=='LIME'   else 0 for x in valores_x['color']]	
        
    valores_x['PRE_interior_BLACK'] = [1 if x=='BLACK'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BEIGE'] = [1 if x=='BEIGE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_TAN'] = [1 if x=='TAN'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_GRAY'] = [1 if x=='GRAY'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BROWN'] = [1 if x=='BROWN'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BURGUNDY'] = [1 if x=='BURGUNDY'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_WHITE'] = [1 if x=='WHITE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_SILVER'] = [1 if x=='SILVER'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_OFF-WHITE'] = [1 if x=='OFF-WHITE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_RED'] = [1 if x=='RED'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_YELLOW'] = [1 if x=='YELLOW'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_BLUE'] = [1 if x=='BLUE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_PURPLE'] = [1 if x=='PURPLE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_NÃOESPECIFICADO'] = [1 if x=='NÃO ESPECIFICADO'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_GREEN'] = [1 if x=='GREEN'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_ORANGE'] = [1 if x=='ORANGE'   else 0 for x in valores_x['interior']]
    valores_x['PRE_interior_GOLD'] = [1 if x=='GOLD'   else 0 for x in valores_x['interior']]
        
    valores_x['PRE_model_ALTIMA'] = [1 if x=='ALTIMA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FUSION'] = [1 if x=='FUSION'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ESCAPE'] = [1 if x=='ESCAPE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAMRY'] = [1 if x=='CAMRY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_F-150'] = [1 if x=='F-150'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FOCUS'] = [1 if x=='FOCUS'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_GRAND_CARAVAN'] = [1 if x=='GRAND CARAVAN'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_IMPALA'] = [1 if x=='IMPALA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SONATA'] = [1 if x=='SONATA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACCORD'] = [1 if x=='ACCORD'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_MALIBU'] = [1 if x=='MALIBU'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_COROLLA'] = [1 if x=='COROLLA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CRUZE'] = [1 if x=='CRUZE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_3_SERIES'] = [1 if x=='3 SERIES'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELANTRA'] = [1 if x=='ELANTRA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CIVIC'] = [1 if x=='CIVIC'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_EDGE'] = [1 if x=='EDGE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ROGUE'] = [1 if x=='ROGUE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_TOWN_AND_COUNTRY'] = [1 if x=='TOWN AND COUNTRY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPLORER'] = [1 if x=='EXPLORER'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SENTRA'] = [1 if x=='SENTRA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_1500'] = [1 if x=='SILVERADO 1500'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_EQUINOX'] = [1 if x=='EQUINOX'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CHARGER'] = [1 if x=='CHARGER'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_OPTIMA'] = [1 if x=='OPTIMA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_200'] = [1 if x=='200'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_MUSTANG'] = [1 if x=='MUSTANG'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVENGER'] = [1 if x=='AVENGER'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_TAURUS'] = [1 if x=='TAURUS'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_300'] = [1 if x=='300'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_R4V4'] = [1 if x=='R4V4'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_JOURNEY'] = [1 if x=='JOURNEY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_VERSA'] = [1 if x=='VERSA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FORTE'] = [1 if x=='FORTE'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SOUL'] = [1 if x=='SOUL'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_CR-V'] = [1 if x=='CR-V'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_ODYSSEY'] = [1 if x=='ODYSSEY'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_FIESTA'] = [1 if x=='FIESTA'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_MURANO'] = [1 if x=='MURANO'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_5_SERIES'] = [1 if x=='5 SERIES'   else 0 for x in valores_x['model']]
    valores_x['PRE_model_SIENNA'] = [1 if x=='SIENNA'   else 0 for x in valores_x['model']]
        
    valores_x['PRE_trim_SE'] = [1 if x=='SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LX'] = [1 if x=='LX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS'] = [1 if x=='LS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLT'] = [1 if x=='XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED'] = [1 if x=='LIMITED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BASE'] = [1 if x=='BASE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT'] = [1 if x=='LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GLS'] = [1 if x=='GLS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE'] = [1 if x=='LE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5 S'] = [1 if x=='2.5 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEXT'] = [1 if x=='SEXT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEL'] = [1 if x=='SEL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S'] = [1 if x=='S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING'] = [1 if x=='TOURING' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_V-6'] = [1 if x=='EX V-6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5'] = [1 if x=='2.5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX'] = [1 if x=='EX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SV'] = [1 if x=='SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX-L'] = [1 if x=='EX-L' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5_SV'] = [1 if x=='3.5 SV' else 0 for x in valores_x['trim']]

    return valores_x

def coletar_dados_usuario():
    st.sidebar.title("Dados do Veículo")

    # Inputs numéricos
    #with st.sidebar.expander("Condição do Veículo"):
    idade_carro = st.sidebar.number_input("Idade do Veículo", min_value=0, step=1, value=0, key="idade_carro_input")
    mmr = st.sidebar.number_input("Preço da Tabela Fipe", min_value=0, step=1, value=0, key="mmr_input")
    condition = st.sidebar.number_input("Estado do Veículo ( 0 - 100) ", min_value=0, step=1, value=0, key="condition_input")
    odometer = st.sidebar.number_input("Kilometragem", min_value=0, step=1, value=0, key="odometer_input")  

# Inputs categóricos
#with st.sidebar.expander("Especificação Técnica do Veículo"):
    make = st.sidebar.selectbox("Fabricante", ['KIA', 'BMW', 'NISSAN', 'CHEVROLET', 'FORD', 'HYUNDAI', 'TOYOTA', 'DODGE', 'CHRYSLER', 'HONDA'], key="make_input")
    body = st.sidebar.selectbox("Categoria", ['SUV', 'SEDAN', 'CONVERTIBLE', 'COUPE', 'HATCHBACK', 'CREW CAB', 'ELANTRA COUPE', 'GENESIS COUPE', 'WAGON', 'MINIVAN', 'VAN', 'DOUBLE CAB', 'CREWMAX CAB', 'ACCESS CAB', 'KING CAB', 'SUPERCREW', 'EXTENDED CAB', 'E-SERIES VAN', 'SUPERCAB', 'REGULAR CAB', 'KOUP', 'QUAD CAB', 'CLUB CAB', 'MEGA CAB', 'TRANSIT VAN', 'REGULAR-CAB'], key="body_input")
    state = st.sidebar.selectbox("Estado", ['CA', 'TX', 'PA', 'MN', 'AZ', 'WI', 'TN', 'MD', 'FL', 'NE', 'NV', 'OH', 'MI', 'NJ', 'SC', 'NC', 'VA', 'IN', 'IL', 'CO', 'UT', 'GA', 'MO', 'NY', 'LA', 'WA', 'PR', 'MA', 'HI', 'OR', 'QC', 'AB', 'ON', 'OK', 'MS', 'NM', 'AL', 'NS'], key="state_input")
    color = st.sidebar.selectbox("Cor", ['WHITE', 'GRAY', 'BLACK', 'RED', 'SILVER', 'BLUE', 'PURPLE', 'BURGUNDY', 'GOLD', 'BEIGE', 'YELLOW', 'GREEN', 'NÃO ESPECIFICADO', 'BROWN', 'CHARCOAL', 'ORANGE', 'TURQUOISE', 'PINK', 'OFF-WHITE', 'LIME'], key="color_input")
    interior = st.sidebar.selectbox("Cor Interior", ['BLACK', 'BEIGE', 'TAN', 'GRAY', 'BROWN', 'BURGUNDY', 'WHITE', 'SILVER', 'OFF-WHITE', 'RED', 'YELLOW', 'BLUE', 'NÃO ESPECIFICADO', 'PURPLE', 'GREEN', 'ORANGE', 'GOLD'], key="interior_input")
    trim = st.sidebar.selectbox("Tipo", ['SE', 'LX', 'LS', 'XLT', 'LIMITED', 'BASE', 'LT', 'GLS', 'LE', '2.5 S', 'SEXT', 'SEL', 'S', 'TOURING', 'EX V-6', '2.5', 'EX', 'SV', 'EX-L', '3.5 SV'], key="trim_input")
    model = st.sidebar.selectbox("Modelo", ['ALTIMA', 'FUSION', 'ESCAPE', 'CAMRY', 'F-150', 'FOCUS', 'GRAND CARAVAN', 'IMPALA', 'SONATA', 'ACCORD', 'MALIBU', 'COROLLA', 'CRUZE', '3 SERIES', 'ELANTRA', 'CIVIC', 'EDGE', 'ROGUE', 'TOWN AND COUNTRY', 'EXPLORER', 'SENTRA', 'SILVERADO 1500', 'EQUINOX', 'CHARGER', 'OPTIMA', '200', 'MUSTANG', 'AVENGER', 'TAURUS', '300', 'R4V4', 'JOURNEY', 'VERSA', 'FORTE', 'SOUL', 'CR-V', 'ODYSSEY', 'FIESTA', 'MURANO', '5 SERIES', 'SIENNA'], key="model_input")

    if st.sidebar.button('Enviar'): 
        return {
                    'condition': condition,
                    'odometer': odometer,
                    'mmr': mmr,
                    'idade_carro': idade_carro,
                    'make': make,
                    'body': body,
                    'state': state,
                    'color': color,
                    'interior': interior,
                    'model': model,
                    'trim': trim
            }
    else:
        # retorna valor 0
        return {
            'condition': 0,
            'odometer': 0,
            'mmr': 0,
            'idade_carro': 0,
            'make': 0,
            'body': 0,
            'state': 0,
            'color': 0,
            'interior': 0,
            'model': 0,
            'trim': 0
        }


def interface_previsao():
    # Interface para entrada de dados
    dados_usuario = coletar_dados_usuario()

    # Converter os dados do usuário para DataFrame
    dados_entrada = pd.DataFrame(dados_usuario, index=[0])

    # Pré-processar os dados de entrada
    preprocessamento(dados_entrada)
    dados_entrada = dados_entrada.drop(columns=['make', 'model', 'trim', 'body', 'state', 'color', 'interior'])
    dados_entrada.to_csv('dados_entrada.csv')

    # Carregar o modelo treinado
    modelo = joblib.load('modelo.joblib')

    # Prever o preço do veículo
    preco = prever_preco(modelo, dados_entrada)
    
    # Exibir o preço previsto com uma formatação melhor em reias
    preco_formatado = locale.format_string("%.2f", preco.item(), grouping=True)
    st.markdown(f'<p style="font-size: 25px; font-weight: bold;">Preço Previsto do Veículo: R$ {preco_formatado}</p>', unsafe_allow_html=True)
       
def main(): 
    st.set_page_config(page_title="Motor Web", page_icon="🚗")
    
    st.sidebar.image('transferir.png', use_column_width=True)

    # Criação do navbar
    navbar = st.sidebar.selectbox('Navegação', ['Página Inicial', 'Previsão de Preço'])

    if navbar == "Página Inicial":
        st.markdown("<h2 style='text-left: center; color: yellow;'>MOTOR WEB</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-left: center; color: white;'>Bem-vindo ao Sistema de Previsão de Preço de Veículos!</h3>", unsafe_allow_html=True)
        st.write("""
            Este sistema foi desenvolvido para oferecer uma estimativa do valor de mercado de veículos com base em diversas variáveis do mercado automotivo. Nossa tecnologia utiliza algoritmos avançados para analisar as tendências atuais do mercado e considerar fatores importantes, como:

            - Idade do Veículo
            - Preço da Tabela Fipe
            - Estado do Veículo
            - Kilometragem
            - Fabricante
            - Categoria
            - Estado
            - Cor
            - Tipo
            - Modelo do veículo

            Para começar, vá até navegação e na caixa de seleção, escolha a página Previsão de Preço.
            """)
                    
    elif navbar == "Previsão de Preço":
        st.markdown("<h2 style='text-left: center; color: yellow;'>Previsão de Preço do Veículo</h2>", unsafe_allow_html=True)
        st.write("Nossa plataforma analisa cuidadosamente os dados do seu veículo para prever seu valor de mercado. Com base nas informações fornecidas, oferecemos uma estimativa precisa do preço do seu veículo. Nosso objetivo é ajudá-lo a entender o valor atual do seu veículo no mercado automotivo. Após fornecer todas as informações necessárias, clique no botão Enviar para gerar a estimativa de preço do veículo.")
        interface_previsao()

if __name__ == "__main__":
    main()
