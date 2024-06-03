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
        
    valores_x['PRE_model_ALTIMA'] = [1 if x == 'ALTIMA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FUSION'] = [1 if x == 'FUSION' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SORENTO'] = [1 if x == 'SORENTO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CRUZE'] = [1 if x == 'CRUZE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAMARO'] = [1 if x == 'CAMARO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_OPTIMA'] = [1 if x == 'OPTIMA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SONATA'] = [1 if x == 'SONATA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_IMPALA'] = [1 if x == 'IMPALA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MALIBU'] = [1 if x == 'MALIBU' else 0 for x in valores_x['model']]
    valores_x['PRE_model_VERSA'] = [1 if x == 'VERSA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELANTRA'] = [1 if x == 'ELANTRA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_VERSA_NOTE'] = [1 if x == 'VERSA NOTE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_X1'] = [1 if x == 'X1' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_1500'] = [1 if x == 'SILVERADO 1500' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SANTA_FE'] = [1 if x == 'SANTA FE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_GENESIS'] = [1 if x == 'GENESIS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SONATA_HYBRID'] = [1 if x == 'SONATA HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACCENT'] = [1 if x == 'ACCENT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_VELOSTER'] = [1 if x == 'VELOSTER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELANTRA_COUPE'] = [1 if x == 'ELANTRA COUPE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AZERA'] = [1 if x == 'AZERA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TUCSON'] = [1 if x == 'TUCSON' else 0 for x in valores_x['model']]
    valores_x['PRE_model_GENESIS_COUPE'] = [1 if x == 'GENESIS COUPE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RIO'] = [1 if x == 'RIO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SOUL'] = [1 if x == 'SOUL' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FORTE'] = [1 if x == 'FORTE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_370Z'] = [1 if x == '370Z' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SPORTAGE'] = [1 if x == 'SPORTAGE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_COROLLA'] = [1 if x == 'COROLLA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SIENNA'] = [1 if x == 'SIENNA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_JUKE'] = [1 if x == 'JUKE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_YARIS'] = [1 if x == 'YARIS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SENTRA'] = [1 if x == 'SENTRA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ROGUE'] = [1 if x == 'ROGUE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_NV'] = [1 if x == 'NV' else 0 for x in valores_x['model']]
    valores_x['PRE_model_LEAF'] = [1 if x == 'LEAF' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAMRY'] = [1 if x == 'CAMRY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TACOMA'] = [1 if x == 'TACOMA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FJ_CRUISER'] = [1 if x == 'FJ CRUISER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVALON'] = [1 if x == 'AVALON' else 0 for x in valores_x['model']]
    valores_x['PRE_model_NV200'] = [1 if x == 'NV200' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RAV4'] = [1 if x == 'RAV4' else 0 for x in valores_x['model']]
    valores_x['PRE_model_QUEST'] = [1 if x == 'QUEST' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TUNDRA'] = [1 if x == 'TUNDRA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MAXIMA'] = [1 if x == 'MAXIMA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_XTERRA'] = [1 if x == 'XTERRA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PRIUS'] = [1 if x == 'PRIUS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FRONTIER'] = [1 if x == 'FRONTIER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAMRY_HYBRID'] = [1 if x == 'CAMRY HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CUBE'] = [1 if x == 'CUBE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ARMADA'] = [1 if x == 'ARMADA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_VENZA'] = [1 if x == 'VENZA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MURANO'] = [1 if x == 'MURANO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PATHFINDER'] = [1 if x == 'PATHFINDER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_HIGHLANDER'] = [1 if x == 'HIGHLANDER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_5_SERIES'] = [1 if x == '5 SERIES' else 0 for x in valores_x['model']]
    valores_x['PRE_model_3_SERIES'] = [1 if x == '3 SERIES' else 0 for x in valores_x['model']]
    valores_x['PRE_model_1_SERIES'] = [1 if x == '1 SERIES' else 0 for x in valores_x['model']]
    valores_x['PRE_model_X3'] = [1 if x == 'X3' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVENGER'] = [1 if x == 'AVENGER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_E_SERIES_WAGON'] = [1 if x == 'E-SERIES WAGON' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ESCAPE'] = [1 if x == 'ESCAPE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EDGE'] = [1 if x == 'EDGE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FOCUS'] = [1 if x == 'FOCUS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FLEX'] = [1 if x == 'FLEX' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TRAVERSE'] = [1 if x == 'TRAVERSE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_2500HD'] = [1 if x == 'SILVERADO 2500HD' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FIESTA'] = [1 if x == 'FIESTA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_200'] = [1 if x == '200' else 0 for x in valores_x['model']]
    valores_x['PRE_model_JOURNEY'] = [1 if x == 'JOURNEY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EQUINOX'] = [1 if x == 'EQUINOX' else 0 for x in valores_x['model']]
    valores_x['PRE_model_300'] = [1 if x == '300' else 0 for x in valores_x['model']]
    valores_x['PRE_model_F_150'] = [1 if x == 'F-150' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPLORER'] = [1 if x == 'EXPLORER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAPTIVA_SPORT'] = [1 if x == 'CAPTIVA SPORT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_GRAND_CARAVAN'] = [1 if x == 'GRAND CARAVAN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TOWN_AND_COUNTRY'] = [1 if x == 'TOWN AND COUNTRY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_E_SERIES_VAN'] = [1 if x == 'E-SERIES VAN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_VOLT'] = [1 if x == 'VOLT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPRESS_CARGO'] = [1 if x == 'EXPRESS CARGO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CHARGER'] = [1 if x == 'CHARGER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPEDITION'] = [1 if x == 'EXPEDITION' else 0 for x in valores_x['model']]
    valores_x['PRE_model_COLORADO'] = [1 if x == 'COLORADO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPRESS'] = [1 if x == 'EXPRESS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SONIC'] = [1 if x == 'SONIC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACCORD'] = [1 if x == 'ACCORD' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CR_V'] = [1 if x == 'CR-V' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MUSTANG'] = [1 if x == 'MUSTANG' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CIVIC'] = [1 if x == 'CIVIC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FIT'] = [1 if x == 'FIT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PILOT'] = [1 if x == 'PILOT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ODYSSEY'] = [1 if x == 'ODYSSEY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CROSSTOUR'] = [1 if x == 'CROSSTOUR' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TRANSIT_CONNECT'] = [1 if x == 'TRANSIT CONNECT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TAURUS'] = [1 if x == 'TAURUS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_VERACRUZ'] = [1 if x == 'VERACRUZ' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SEDONA'] = [1 if x == 'SEDONA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_7_SERIES'] = [1 if x == '7 SERIES' else 0 for x in valores_x['model']]
    valores_x['PRE_model_5_SERIES_GRAN_TURISMO'] = [1 if x == '5 SERIES GRAN TURISMO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_HIGHLANDER_HYBRID'] = [1 if x == 'HIGHLANDER HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PRIUS_PLUG_IN'] = [1 if x == 'PRIUS PLUG-IN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CR_Z'] = [1 if x == 'CR-Z' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SUBURBAN'] = [1 if x == 'SUBURBAN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_HHR'] = [1 if x == 'HHR' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACCORD_CROSSTOUR'] = [1 if x == 'ACCORD CROSSTOUR' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EQUUS'] = [1 if x == 'EQUUS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_NITRO'] = [1 if x == 'NITRO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TAHOE'] = [1 if x == 'TAHOE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CHALLENGER'] = [1 if x == 'CHALLENGER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ESCAPE_HYBRID'] = [1 if x == 'ESCAPE HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RANGER'] = [1 if x == 'RANGER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_X5'] = [1 if x == 'X5' else 0 for x in valores_x['model']]
    valores_x['PRE_model_INSIGHT'] = [1 if x == 'INSIGHT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FUSION_HYBRID'] = [1 if x == 'FUSION HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_F_250_SUPER_DUTY'] = [1 if x == 'F-250 SUPER DUTY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_IMPALA_LIMITED'] = [1 if x == 'IMPALA LIMITED' else 0 for x in valores_x['model']]
    valores_x['PRE_model_DART'] = [1 if x == 'DART' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SPARK'] = [1 if x == 'SPARK' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVEO'] = [1 if x == 'AVEO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CALIBER'] = [1 if x == 'CALIBER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SEBRING'] = [1 if x == 'SEBRING' else 0 for x in valores_x['model']]
    valores_x['PRE_model_4RUNNER'] = [1 if x == '4RUNNER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ALTIMA_HYBRID'] = [1 if x == 'ALTIMA HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SEQUOIA'] = [1 if x == 'SEQUOIA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVALANCHE'] = [1 if x == 'AVALANCHE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TITAN'] = [1 if x == 'TITAN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_M3'] = [1 if x == 'M3' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SPECTRA'] = [1 if x == 'SPECTRA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RONDO'] = [1 if x == 'RONDO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_BORREGO'] = [1 if x == 'BORREGO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TAHOE_HYBRID'] = [1 if x == 'TAHOE HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ECONOLINE_CARGO'] = [1 if x == 'ECONOLINE CARGO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ECONOLINE_WAGON'] = [1 if x == 'ECONOLINE WAGON' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PT_CRUISER'] = [1 if x == 'PT CRUISER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RIDGELINE'] = [1 if x == 'RIDGELINE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_F_450_SUPER_DUTY'] = [1 if x == 'F-450 SUPER DUTY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MAGNUM'] = [1 if x == 'MAGNUM' else 0 for x in valores_x['model']]
    valores_x['PRE_model_DURANGO'] = [1 if x == 'DURANGO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MALIBU_CLASSIC'] = [1 if x == 'MALIBU CLASSIC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TAURUS_X'] = [1 if x == 'TAURUS X' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPLORER_SPORT_TRAC'] = [1 if x == 'EXPLORER SPORT TRAC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RAM_PICKUP_1500'] = [1 if x == 'RAM PICKUP 1500' else 0 for x in valores_x['model']]
    valores_x['PRE_model_F_350_SUPER_DUTY'] = [1 if x == 'F-350 SUPER DUTY' else 0 for x in valores_x['model']]
    valores_x['PRE_model_COBALT'] = [1 if x == 'COBALT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_Z4'] = [1 if x == 'Z4' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PACIFICA'] = [1 if x == 'PACIFICA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_6_SERIES'] = [1 if x == '6 SERIES' else 0 for x in valores_x['model']]
    valores_x['PRE_model_350Z'] = [1 if x == '350Z' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MATRIX'] = [1 if x == 'MATRIX' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_1500_CLASSIC'] = [1 if x == 'SILVERADO 1500 CLASSIC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_UPLANDER'] = [1 if x == 'UPLANDER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MONTE_CARLO'] = [1 if x == 'MONTE CARLO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_M5'] = [1 if x == 'M5' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FIVE_HUNDRED'] = [1 if x == 'FIVE HUNDRED' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELEMENT'] = [1 if x == 'ELEMENT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_S2000'] = [1 if x == 'S2000' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CAMRY_SOLARA'] = [1 if x == 'CAMRY SOLARA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_C_MAX_HYBRID'] = [1 if x == 'C-MAX HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SANTA_FE_SPORT'] = [1 if x == 'SANTA FE SPORT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CADENZA'] = [1 if x == 'CADENZA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELANTRA_GT'] = [1 if x == 'ELANTRA GT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ROGUE_SELECT'] = [1 if x == 'ROGUE SELECT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CORVETTE'] = [1 if x == 'CORVETTE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PRIUS_V'] = [1 if x == 'PRIUS V' else 0 for x in valores_x['model']]
    valores_x['PRE_model_C_MAX_ENERGI'] = [1 if x == 'C-MAX ENERGI' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FOCUS_ST'] = [1 if x == 'FOCUS ST' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RAM_PICKUP_2500'] = [1 if x == 'RAM PICKUP 2500' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ASPEN'] = [1 if x == 'ASPEN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ENTOURAGE'] = [1 if x == 'ENTOURAGE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_RAM_PICKUP_3500'] = [1 if x == 'RAM PICKUP 3500' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CARAVAN'] = [1 if x == 'CARAVAN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_STRATUS'] = [1 if x == 'STRATUS' else 0 for x in valores_x['model']]
    valores_x['PRE_model_DAKOTA'] = [1 if x == 'DAKOTA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TRAILBLAZER'] = [1 if x == 'TRAILBLAZER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_PRIUS_C'] = [1 if x == 'PRIUS C' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_3500HD'] = [1 if x == 'SILVERADO 3500HD' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CROWN_VICTORIA'] = [1 if x == 'CROWN VICTORIA' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ELANTRA_TOURING'] = [1 if x == 'ELANTRA TOURING' else 0 for x in valores_x['model']]
    valores_x['PRE_model_X6'] = [1 if x == 'X6' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_1500_HYBRID'] = [1 if x == 'SILVERADO 1500 HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SPRINTER_CARGO'] = [1 if x == 'SPRINTER CARGO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_EXPEDITION_EL'] = [1 if x == 'EXPEDITION EL' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TIBURON'] = [1 if x == 'TIBURON' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AMANTI'] = [1 if x == 'AMANTI' else 0 for x in valores_x['model']]
    valores_x['PRE_model_LAND_CRUISER'] = [1 if x == 'LAND CRUISER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_M6'] = [1 if x == 'M6' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_2500HD_CLASSIC'] = [1 if x == 'SILVERADO 2500HD CLASSIC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FREESTYLE'] = [1 if x == 'FREESTYLE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FUSION_ENERGI'] = [1 if x == 'FUSION ENERGI' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_1500HD'] = [1 if x == 'SILVERADO 1500HD' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_3500'] = [1 if x == 'SILVERADO 3500' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TRAILBLAZER_EXT'] = [1 if x == 'TRAILBLAZER EXT' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MALIBU_MAXX'] = [1 if x == 'MALIBU MAXX' else 0 for x in valores_x['model']]
    valores_x['PRE_model_CROSSFIRE'] = [1 if x == 'CROSSFIRE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_FREESTAR'] = [1 if x == 'FREESTAR' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MURANO_CROSSCABRIOLET'] = [1 if x == 'MURANO CROSSCABRIOLET' else 0 for x in valores_x['model']]
    valores_x['PRE_model_NV_CARGO'] = [1 if x == 'NV CARGO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_2_SERIES'] = [1 if x == '2 SERIES' else 0 for x in valores_x['model']]
    valores_x['PRE_model_MALIBU_HYBRID'] = [1 if x == 'MALIBU HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACCORD_HYBRID'] = [1 if x == 'ACCORD HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_AVALON_HYBRID'] = [1 if x == 'AVALON HYBRID' else 0 for x in valores_x['model']]
    valores_x['PRE_model_Z4_M'] = [1 if x == 'Z4 M' else 0 for x in valores_x['model']]
    valores_x['PRE_model_NV_PASSENGER'] = [1 if x == 'NV PASSENGER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SHELBY_GT500'] = [1 if x == 'SHELBY GT500' else 0 for x in valores_x['model']]
    valores_x['PRE_model_BLACK_DIAMOND_AVALANCHE'] = [1 if x == 'BLACK DIAMOND AVALANCHE' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SILVERADO_3500_CLASSIC'] = [1 if x == 'SILVERADO 3500 CLASSIC' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACTIVEHYBRID_X6'] = [1 if x == 'ACTIVEHYBRID X6' else 0 for x in valores_x['model']]
    valores_x['PRE_model_3_SERIES_GRAN_TURISMO'] = [1 if x == '3 SERIES GRAN TURISMO' else 0 for x in valores_x['model']]
    valores_x['PRE_model_M'] = [1 if x == 'M' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACTIVEHYBRID_5'] = [1 if x == 'ACTIVEHYBRID 5' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SPRINTER'] = [1 if x == 'SPRINTER' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TRANSIT_VAN'] = [1 if x == 'TRANSIT VAN' else 0 for x in valores_x['model']]
    valores_x['PRE_model_SPARK_EV'] = [1 if x == 'SPARK EV' else 0 for x in valores_x['model']]
    valores_x['PRE_model_TRANSIT_WAGON'] = [1 if x == 'TRANSIT WAGON' else 0 for x in valores_x['model']]
    valores_x['PRE_model_ACTIVEHYBRID_7'] = [1 if x == 'ACTIVEHYBRID 7' else 0 for x in valores_x['model']]
        
    valores_x['PRE_trim_LX'] = [1 if x == 'LX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5_S'] = [1 if x == '2.5 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1LT'] = [1 if x == '1LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT'] = [1 if x == 'LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE'] = [1 if x == 'SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2LT'] = [1 if x == '2LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS'] = [1 if x == 'LS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LTZ'] = [1 if x == 'LTZ' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1.6_SL'] = [1 if x == '1.6 SL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1.6_SV'] = [1 if x == '1.6 SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SDRIVE28I'] = [1 if x == 'SDRIVE28I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED'] = [1 if x == 'LIMITED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_5.0_R-SPEC'] = [1 if x == '5.0 R-SPEC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GLS'] = [1 if x == 'GLS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPORT'] = [1 if x == 'SPORT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPORT_2.0T'] = [1 if x == 'SPORT 2.0T' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TURBO'] = [1 if x == 'TURBO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GS'] = [1 if x == 'GS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BASE'] = [1 if x == 'BASE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.8'] = [1 if x == '3.8' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.8_TRACK'] = [1 if x == '3.8 TRACK' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_HYBRID'] = [1 if x == 'EX HYBRID' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5'] = [1 if x == '2.5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SX'] = [1 if x == 'SX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_+'] = [1 if x == '+' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX'] = [1 if x == 'EX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE'] = [1 if x == 'LE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_7-PASSENGER_MOBILITY_AUTO_ACCESS'] = [1 if x == 'LE 7-PASSENGER MOBILITY AUTO ACCESS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S'] = [1 if x == 'S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_L'] = [1 if x == 'L' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SR'] = [1 if x == 'SR' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500_S'] = [1 if x == '1500 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SL'] = [1 if x == 'SL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE'] = [1 if x == 'XLE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PRERUNNER'] = [1 if x == 'PRERUNNER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5_SL'] = [1 if x == '3.5 SL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1.6_S_PLUS'] = [1 if x == '1.6 S PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TUNDRA'] = [1 if x == 'TUNDRA' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5_SV'] = [1 if x == '3.5 SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TWO'] = [1 if x == 'TWO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SV'] = [1 if x == 'SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1.8_SL'] = [1 if x == '1.8 SL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FE+_S'] = [1 if x == 'FE+ S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5_S'] = [1 if x == '3.5 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PRERUNNER_V6'] = [1 if x == 'PRERUNNER V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_SPECIAL_EDITION'] = [1 if x == 'S SPECIAL EDITION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_V6'] = [1 if x == 'V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FE+_SV'] = [1 if x == 'FE+ SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_528I'] = [1 if x == '528I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_328I'] = [1 if x == '328I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_135I'] = [1 if x == '135I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_128I'] = [1 if x == '128I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE28I'] = [1 if x == 'XDRIVE28I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E-350_SUPER_DUTY_XL'] = [1 if x == 'E-350 SUPER DUTY XL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEL'] = [1 if x == 'SEL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TITANIUM'] = [1 if x == 'TITANIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT_FLEET'] = [1 if x == 'LT FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_WORK_TRUCK'] = [1 if x == 'WORK TRUCK' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SES'] = [1 if x == 'SES' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLS'] = [1 if x == 'XLS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SXT'] = [1 if x == 'SXT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_V6'] = [1 if x == 'S V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLT'] = [1 if x == 'XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LTZ_FLEET'] = [1 if x == 'LTZ FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_AMERICAN_VALUE_PACKAGE'] = [1 if x == 'AMERICAN VALUE PACKAGE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FX2'] = [1 if x == 'FX2' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING'] = [1 if x == 'TOURING' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E-150'] = [1 if x == 'E-150' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HYBRID'] = [1 if x == 'HYBRID' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE35I'] = [1 if x == 'XDRIVE35I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500'] = [1 if x == '1500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ECO'] = [1 if x == 'ECO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2LS_FLEET'] = [1 if x == '2LS FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E-350_SUPER_DUTY'] = [1 if x == 'E-350 SUPER DUTY' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1LT_FLEET'] = [1 if x == '1LT FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LARIAT'] = [1 if x == 'LARIAT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS_3500'] = [1 if x == 'LS 3500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XL'] = [1 if x == 'XL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CREW'] = [1 if x == 'CREW' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS_FLEET'] = [1 if x == 'LS FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_V6'] = [1 if x == 'EX V-6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_4_6'] = [1 if x == '4.6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_L'] = [1 if x == 'EX-L' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GT'] = [1 if x == 'GT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CARGO_VAN_XLT'] = [1 if x == 'CARGO VAN XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HF'] = [1 if x == 'HF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_KOUP_EX'] = [1 if x == 'KOUP EX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2'] = [1 if x == '2' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1_8_S'] = [1 if x == '1.8 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3500_S'] = [1 if x == '3500 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_335I'] = [1 if x == '335I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_535I_XDRIVE'] = [1 if x == '535I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_THREE'] = [1 if x == 'THREE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_535I'] = [1 if x == '535I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_328I_XDRIVE'] = [1 if x == '328I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_740I'] = [1 if x == '740I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_550I'] = [1 if x == '550I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_335D'] = [1 if x == '335D' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BASE_7_PASSENGER'] = [1 if x == 'BASE 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_335I_XDRIVE'] = [1 if x == '335I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT1'] = [1 if x == 'LT1' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_C'] = [1 if x == 'C' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EXPRESS'] = [1 if x == 'EXPRESS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FX4'] = [1 if x == 'FX4' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LTZ_1500'] = [1 if x == 'LTZ 1500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_STX'] = [1 if x == 'STX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SIGNATURE'] = [1 if x == 'SIGNATURE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_FLEET'] = [1 if x == 'SE FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PANEL_LS'] = [1 if x == 'PANEL LS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GLS_PZEV'] = [1 if x == 'GLS PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LX_S'] = [1 if x == 'LX-S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT2'] = [1 if x == 'LT2' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE50I'] = [1 if x == 'XDRIVE50I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500'] = [1 if x == '2500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E_250'] = [1 if x == 'E-250' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE35D'] = [1 if x == 'XDRIVE35D' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HEAT'] = [1 if x == 'HEAT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SI'] = [1 if x == 'SI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING_L'] = [1 if x == 'TOURING-L' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RT'] = [1 if x == 'R/T' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_AERO'] = [1 if x == 'AERO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_!'] = [1 if x == '!' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2_0_SR'] = [1 if x == '2.0 SR' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2_0_S'] = [1 if x == '2.0 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_8_PASSENGER'] = [1 if x == 'XLE 8-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PLATINUM'] = [1 if x == 'PLATINUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SXT_FLEET'] = [1 if x == 'SXT FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2_0_SL'] = [1 if x == '2.0 SL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1SS'] = [1 if x == '1SS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_750LI'] = [1 if x == '750LI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500_LT'] = [1 if x == '1500 LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_5L'] = [1 if x == '3.5L' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_X'] = [1 if x == 'X' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EL_LIMITED'] = [1 if x == 'EL LIMITED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_5_SR'] = [1 if x == '3.5 SR' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TUNDRA_GRADE'] = [1 if x == 'TUNDRA GRADE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BLUE'] = [1 if x == 'BLUE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_III'] = [1 if x == 'III' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_DX-VP'] = [1 if x == 'DX-VP' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_528I_XDRIVE'] = [1 if x == '528I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE48I'] = [1 if x == 'XDRIVE48I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SS'] = [1 if x == 'SS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_7_PASSENGER'] = [1 if x == 'XLE 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE30I'] = [1 if x == 'XDRIVE30I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500_LTZ'] = [1 if x == '1500 LTZ' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_V6'] = [1 if x == 'SE V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RT'] = [1 if x == 'RT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_0SI'] = [1 if x == '3.0SI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_335XI'] = [1 if x == '335XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SLT'] = [1 if x == 'SLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ST'] = [1 if x == 'ST' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_0I'] = [1 if x == '3.0I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_4_8I'] = [1 if x == '4.8I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500_LS'] = [1 if x == '1500 LS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_328XI'] = [1 if x == '328XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_650I'] = [1 if x == '650I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_525I'] = [1 if x == '525I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XR'] = [1 if x == 'XR' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SR5'] = [1 if x == 'SR5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RTS'] = [1 if x == 'RTS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_530I'] = [1 if x == '530I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_7_PASSENGER'] = [1 if x == 'LE 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_SULEV'] = [1 if x == 'SE SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_KING_RANCH'] = [1 if x == 'KING RANCH' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX3_S'] = [1 if x == 'ZX3 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_DELUXE'] = [1 if x == 'DELUXE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX4_SE'] = [1 if x == 'ZX4 SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS2'] = [1 if x == 'LS2' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CARGO'] = [1 if x == 'CARGO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT3'] = [1 if x == 'LT3' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEL_FLEET'] = [1 if x == 'SEL FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_325I'] = [1 if x == '325I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_5_SE'] = [1 if x == '3.5 SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_325XI'] = [1 if x == '325XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XE'] = [1 if x == 'XE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CE'] = [1 if x == 'CE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_NISMO'] = [1 if x == 'NISMO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_330I'] = [1 if x == '330I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_530XI'] = [1 if x == '530XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX4_SES'] = [1 if x == 'ZX4 SES' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3500'] = [1 if x == '3500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EDDIE_BAUER'] = [1 if x == 'EDDIE BAUER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LARAMIE'] = [1 if x == 'LARAMIE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS_1500'] = [1 if x == 'LS 1500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_P'] = [1 if x == 'EX-P' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPECIAL_EDITION'] = [1 if x == 'SPECIAL EDITION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_STANDARD'] = [1 if x == 'STANDARD' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SRT-8'] = [1 if x == 'SRT-8' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_8_PASSENGER'] = [1 if x == 'LE 8-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_LIMITED_7_PASSENGER'] = [1 if x == 'XLE LIMITED 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_V6'] = [1 if x == 'XLE V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SLE_V6'] = [1 if x == 'SLE V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E-350_SUPER_DUTY_XLT'] = [1 if x == 'E-350 SUPER DUTY XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_8_ULTIMATE'] = [1 if x == '3.8 ULTIMATE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GT_PREMIUM'] = [1 if x == 'GT PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PREMIUM'] = [1 if x == 'PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FORTE5_EX'] = [1 if x == 'FORTE5 EX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_320I'] = [1 if x == '320I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_PLUS'] = [1 if x == 'LE PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_PLUS'] = [1 if x == 'S PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LX_PZEV'] = [1 if x == 'LX PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_L_W_REAR_ENTERTAINMENT'] = [1 if x == 'EX-L W/REAR ENTERTAINMENT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HYBRID_PZEV_W_LEATHER_AND_NAVIGATION'] = [1 if x == 'HYBRID PZEV W/LEATHER AND NAVIGATION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_7_PASSENGER'] = [1 if x == 'LIMITED 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_550I_XDRIVE'] = [1 if x == '550I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_C_HEMI'] = [1 if x == 'C HEMI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SEL_PLUS'] = [1 if x == 'SEL PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CE_7_PASSENGER'] = [1 if x == 'CE 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GL'] = [1 if x == 'GL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_8_R_SPEC'] = [1 if x == '3.8 R-SPEC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FLEET'] = [1 if x == 'FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_8_PASSENGER'] = [1 if x == 'SE 8-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_335IS'] = [1 if x == '335IS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_740LI'] = [1 if x == '740LI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2SS'] = [1 if x == '2SS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_AVEO5_1LT'] = [1 if x == 'AVEO5 1LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT_1500'] = [1 if x == 'LT 1500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_MAINSTREET'] = [1 if x == 'MAINSTREET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LUX'] = [1 if x == 'LUX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RUSH'] = [1 if x == 'RUSH' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_C_V'] = [1 if x == 'C/V' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CITADEL'] = [1 if x == 'CITADEL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EL_KING_RANCH'] = [1 if x == 'EL KING RANCH' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LX_FLEET'] = [1 if x == 'LX FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SHOCK'] = [1 if x == 'SHOCK' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LARIAT_LIMITED'] = [1 if x == 'LARIAT LIMITED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CARGO_VAN_XL'] = [1 if x == 'CARGO VAN XL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SHO'] = [1 if x == 'SHO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3_8_GRAND_TOURING'] = [1 if x == '3.8 GRAND TOURING' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ULTIMATE'] = [1 if x == 'ULTIMATE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_PZEV'] = [1 if x == 'LIMITED PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_TURBO'] = [1 if x == 'EX TURBO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PRO-4X'] = [1 if x == 'PRO-4X' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1_8_S_KROM_EDITION'] = [1 if x == '1.8 S KROM EDITION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_R'] = [1 if x == 'SE-R' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1_6'] = [1 if x == '1.6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_R_SPEC_V'] = [1 if x == 'SE-R SPEC V' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_FFV'] = [1 if x == 'LIMITED FFV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TUNDRA_FFV'] = [1 if x == 'TUNDRA FFV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_750I_XDRIVE'] = [1 if x == '750I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_750LI_XDRIVE'] = [1 if x == '750LI XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_750I'] = [1 if x == '750I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_AVEO5_LS'] = [1 if x == 'AVEO5 LS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HERO'] = [1 if x == 'HERO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RT_FLEET'] = [1 if x == 'RT FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_FLEET'] = [1 if x == 'LIMITED FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CLASSIC'] = [1 if x == 'CLASSIC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SRT8'] = [1 if x == 'SRT8' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING_PLUS'] = [1 if x == 'TOURING PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HARLEY_DAVIDSON'] = [1 if x == 'HARLEY-DAVIDSON' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EL_SSV_FLEET'] = [1 if x == 'EL SSV FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_WAGON_XLT'] = [1 if x == 'WAGON XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RTL'] = [1 if x == 'RTL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_V6'] = [1 if x == 'LIMITED V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_KOUP_SX'] = [1 if x == 'KOUP SX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E_150_XL'] = [1 if x == 'E-150 XL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1_8_BASE'] = [1 if x == '1.8 BASE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_KROM_EDITION'] = [1 if x == 'S KROM EDITION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500_LT1'] = [1 if x == '1500 LT1' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_AVEO5_2LT'] = [1 if x == 'AVEO5 2LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GLS_V6'] = [1 if x == 'GLS V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RIO5_LX'] = [1 if x == 'RIO5 LX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1_8_KROM'] = [1 if x == '1.8 KROM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_528XI'] = [1 if x == '528XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_535XI'] = [1 if x == '535XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_AVEO5_SPECIAL_VALUE'] = [1 if x == 'AVEO5 SPECIAL VALUE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_LT'] = [1 if x == '2500 LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PANEL_LT'] = [1 if x == 'PANEL LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3500_170_WB'] = [1 if x == '3500 170 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_144_WB'] = [1 if x == '2500 144 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_60TH_ANNIVERSARY'] = [1 if x == '60TH ANNIVERSARY' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GT_DELUXE'] = [1 if x == 'GT DELUXE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FX4_OFF-ROAD'] = [1 if x == 'FX4 OFF-ROAD' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_VALUE_PACKAGE'] = [1 if x == 'VALUE PACKAGE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_SULEV'] = [1 if x == 'S SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SL_SULEV'] = [1 if x == 'SL SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_V6'] = [1 if x == 'LE V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_525XI'] = [1 if x == '525XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_760LI'] = [1 if x == '760LI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SSV_FLEET'] = [1 if x == 'SSV FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX5_SES'] = [1 if x == 'ZX5 SES' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX4_ST'] = [1 if x == 'ZX4 ST' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SC'] = [1 if x == 'SC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RIO5_SX'] = [1 if x == 'RIO5 SX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ENTHUSIAST'] = [1 if x == 'ENTHUSIAST' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_OFF-ROAD'] = [1 if x == 'SE OFF-ROAD' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_330CI'] = [1 if x == '330CI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_330XI'] = [1 if x == '330XI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_325CI'] = [1 if x == '325CI' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_WAGON_TITANIUM_LWB'] = [1 if x == 'WAGON TITANIUM LWB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_4.4I'] = [1 if x == '4.4I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SRT-10'] = [1 if x == 'SRT-10' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_HIGH_ROOF_158_WB'] = [1 if x == '2500 HIGH ROOF 158 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_140_WB'] = [1 if x == '2500 140 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX5_SE'] = [1 if x == 'ZX5 SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_SULEV'] = [1 if x == 'LIMITED SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_WAGON_XLT_LWB'] = [1 if x == 'WAGON XLT LWB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPECTRA5'] = [1 if x == 'SPECTRA5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LX_HYBRID'] = [1 if x == 'LX HYBRID' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_S'] = [1 if x == '2500 S' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_ECO'] = [1 if x == 'LE ECO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_228I'] = [1 if x == '228I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RS'] = [1 if x == 'RS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EL_XLT'] = [1 if x == 'EL XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ELECTRIC'] = [1 if x == 'ELECTRIC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX-L_W_NAVIGATION'] = [1 if x == 'EX-L W/NAVIGATION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HYBRID_PZEV'] = [1 if x == 'HYBRID PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPORT_W_NAVIGATION'] = [1 if x == 'SPORT W/NAVIGATION' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING_W_NAVIGATION_AND_REAR_ENTERTAINMENT'] = [1 if x == 'TOURING W/NAVIGATION AND REAR ENTERTAINMENT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GS_PZEV'] = [1 if x == 'GS PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.0T'] = [1 if x == '2.0T' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_PLUS'] = [1 if x == 'PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_L_7-PASSENGER'] = [1 if x == 'L 7-PASSENGER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ONE'] = [1 if x == 'ONE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XDRIVE35I_PREMIUM'] = [1 if x == 'XDRIVE35I PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1LS_FLEET'] = [1 if x == '1LS FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BEV'] = [1 if x == 'BEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_5'] = [1 if x == '5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_IV'] = [1 if x == 'IV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT2_XFE'] = [1 if x == 'LT2 XFE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPECTRA5_SX'] = [1 if x == 'SPECTRA5 SX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SRT4'] = [1 if x == 'SRT4' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_320I_XDRIVE'] = [1 if x == '320I XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SRT8_SUPERBEE'] = [1 if x == 'SRT8 SUPERBEE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING_ELITE'] = [1 if x == 'TOURING ELITE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_II'] = [1 if x == 'II' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XRS'] = [1 if x == 'XRS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RTX'] = [1 if x == 'RTX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GTC'] = [1 if x == 'GTC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1.8'] = [1 if x == '1.8' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_LUXURY'] = [1 if x == 'SE LUXURY' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_128I_SULEV'] = [1 if x == '128I SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_C_JOHN_VARVATOS'] = [1 if x == 'C JOHN VARVATOS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_WAGON_XLT_PREMIUM'] = [1 if x == 'WAGON XLT PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_FIVE'] = [1 if x == 'FIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_V8'] = [1 if x == 'S V8' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_C_LUXURY_SERIES'] = [1 if x == 'C LUXURY SERIES' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SXT_PLUS'] = [1 if x == 'SXT PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_DIESEL'] = [1 if x == 'DIESEL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_SV'] = [1 if x == '2500 SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_X_RUNNER_V6'] = [1 if x == 'X-RUNNER V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.0T_R-SPEC'] = [1 if x == '2.0T R-SPEC' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5'] = [1 if x == '3.5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZXW_SES'] = [1 if x == 'ZXW SES' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3.5_SE-R'] = [1 if x == '3.5 SE-R' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_NATURAL_GAS'] = [1 if x == 'NATURAL GAS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_UPTOWN'] = [1 if x == 'UPTOWN' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPORT_V6'] = [1 if x == 'SPORT V6' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GX'] = [1 if x == 'GX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLT_SPORT'] = [1 if x == 'XLT SPORT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RTL_W/LEATHER'] = [1 if x == 'RTL W/LEATHER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TRAIL'] = [1 if x == 'TRAIL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XFE'] = [1 if x == 'XFE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LS_2500'] = [1 if x == 'LS 2500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_PREMIUM'] = [1 if x == 'XLE PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ZX3_SES'] = [1 if x == 'ZX3 SES' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ACTIVEHYBRID_3'] = [1 if x == 'ACTIVEHYBRID 3' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_BIGHORN'] = [1 if x == 'BIGHORN' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RALLYE'] = [1 if x == 'RALLYE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_V'] = [1 if x == 'V' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPECIAL_VALUE'] = [1 if x == 'SPECIAL VALUE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SXL'] = [1 if x == 'SXL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SVT_RAPTOR'] = [1 if x == 'SVT RAPTOR' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LE_V8'] = [1 if x == 'LE V8' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_50TH_ANNIVERSARY'] = [1 if x == '50TH ANNIVERSARY' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_170_WB'] = [1 if x == '2500 170 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_4.8IS'] = [1 if x == '4.8IS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SPORT_PZEV'] = [1 if x == 'SPORT PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3500_SV'] = [1 if x == '3500 SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_328I_SULEV'] = [1 if x == '328I SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1500_SV'] = [1 if x == '1500 SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_DX'] = [1 if x == 'DX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RE_MIX'] = [1 if x == 'RE:MIX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LIMITED_HEV'] = [1 if x == 'LIMITED HEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SDRIVE30I'] = [1 if x == 'SDRIVE30I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_1.6_BASE'] = [1 if x == '1.6 BASE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GT_LIMITED'] = [1 if x == 'GT LIMITED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_TOURING'] = [1 if x == 'XLE TOURING' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_GT_SULEV'] = [1 if x == 'GT SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3500_HIGH_ROOF_158_WB'] = [1 if x == '3500 HIGH ROOF 158 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SDRIVE35I'] = [1 if x == 'SDRIVE35I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_HYBRID_W_LEATHER'] = [1 if x == 'HYBRID W/LEATHER' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_S_PREMIUM'] = [1 if x == 'S PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_WAGON_XLT_SWB'] = [1 if x == 'WAGON XLT SWB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ACTIVEHYBRID_5'] = [1 if x == 'ACTIVEHYBRID 5' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CARGO_VAN_XLT_LWB'] = [1 if x == 'CARGO VAN XLT LWB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SR_FFV'] = [1 if x == 'SR FFV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT_2500'] = [1 if x == 'LT 2500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ADVANCED'] = [1 if x == 'ADVANCED' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_Z71_LT'] = [1 if x == 'Z71 LT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_3500_HIGH_ROOF_140_WB'] = [1 if x == '3500 HIGH ROOF 140 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_I'] = [1 if x == 'I' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SLE'] = [1 if x == 'SLE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_NISMO_RS'] = [1 if x == 'NISMO RS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EX_PZEV'] = [1 if x == 'EX PZEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SRT8_392'] = [1 if x == 'SRT8 392' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_TOURING_FLEET'] = [1 if x == 'TOURING FLEET' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_E_150_XLT'] = [1 if x == 'E-150 XLT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CROSSROAD'] = [1 if x == 'CROSSROAD' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2500_HIGH_ROOF_140_WB'] = [1 if x == '2500 HIGH ROOF 140 WB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_DETONATOR'] = [1 if x == 'DETONATOR' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_V6_PREMIUM'] = [1 if x == 'V6 PREMIUM' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_250_MEDIUM_ROOF'] = [1 if x == '250 MEDIUM ROOF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5_SL'] = [1 if x == '2.5 SL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_328I_XDRIVE_SULEV'] = [1 if x == '328I XDRIVE SULEV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_740LI_XDRIVE'] = [1 if x == '740LI XDRIVE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT_ECO'] = [1 if x == 'LT ECO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_LT_3500'] = [1 if x == 'LT 3500' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_2.5_SV'] = [1 if x == '2.5 SV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SX_TURBO'] = [1 if x == 'SX TURBO' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_PLUS'] = [1 if x == 'SE PLUS' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_250_LOW_ROOF'] = [1 if x == '250 LOW ROOF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_150_LOW_ROOF'] = [1 if x == '150 LOW ROOF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_350_XL_LOW_ROOF'] = [1 if x == '350 XL LOW ROOF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_EL_XL'] = [1 if x == 'EL XL' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_ECOBOOST'] = [1 if x == 'ECOBOOST' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SR5_FFV'] = [1 if x == 'SR5 FFV' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_250_HIGH_ROOF'] = [1 if x == '250 HIGH ROOF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_CARGO_VAN_XL_LWB'] = [1 if x == 'CARGO VAN XL LWB' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_328D'] = [1 if x == '328D' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XSE'] = [1 if x == 'XSE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_XLE_TOURING_SE'] = [1 if x == 'XLE TOURING SE' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_350_XL_HIGH_ROOF'] = [1 if x == '350 XL HIGH ROOF' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_SE_SPORT'] = [1 if x == 'SE SPORT' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_RE_FLEX'] = [1 if x == 'RE:FLEX' else 0 for x in valores_x['trim']]
    valores_x['PRE_trim_350_XL_MEDIUM_ROOF'] = [1 if x == '350 XL MEDIUM ROOF' else 0 for x in valores_x['trim']]

    return valores_x

def coletar_dados_usuario():
    
        # Inputs numéricos
    with st.sidebar.expander("Condição do Veículo"):
        idade_carro = st.number_input("Idade do Veículo", min_value=0, step=1, value=0, key="idade_carro_input")
        mmr = st.number_input("Preço da Tabela Fipe", min_value=0, step=1, value=0, key="mmr_input")
        condition = st.number_input("Estado do Veículo ( 0 - 50) ", min_value=0, step=1, value=0, key="condition_input")
        odometer = st.number_input("Kilometragem", min_value=0, step=1, value=0, key="odometer_input")  
    
    # Inputs categóricos
    with st.sidebar.expander("Especificação Técnica do Veículo"):
        make = st.selectbox("Fabricante", ['KIA', 'BMW', 'NISSAN', 'CHEVROLET', 'FORD', 'HYUNDAI', 'TOYOTA', 'DODGE', 'CHRYSLER', 'HONDA'], key="make_input")
        body = st.selectbox("Categoria", ['SUV', 'SEDAN', 'CONVERTIBLE', 'COUPE', 'HATCHBACK', 'CREW CAB', 'ELANTRA COUPE', 'GENESIS COUPE', 'WAGON', 'MINIVAN', 'VAN', 'DOUBLE CAB', 'CREWMAX CAB', 'ACCESS CAB', 'KING CAB', 'SUPERCREW', 'EXTENDED CAB', 'E-SERIES VAN', 'SUPERCAB', 'REGULAR CAB', 'KOUP', 'QUAD CAB', 'CLUB CAB', 'MEGA CAB', 'TRANSIT VAN', 'REGULAR-CAB'], key="body_input")
        state = st.selectbox("Estado", ['CA', 'TX', 'PA', 'MN', 'AZ', 'WI', 'TN', 'MD', 'FL', 'NE', 'NV', 'OH', 'MI', 'NJ', 'SC', 'NC', 'VA', 'IN', 'IL', 'CO', 'UT', 'GA', 'MO', 'NY', 'LA', 'WA', 'PR', 'MA', 'HI', 'OR', 'QC', 'AB', 'ON', 'OK', 'MS', 'NM', 'AL', 'NS'], key="state_input")
        color = st.selectbox("Cor", ['WHITE', 'GRAY', 'BLACK', 'RED', 'SILVER', 'BLUE', 'PURPLE', 'BURGUNDY', 'GOLD', 'BEIGE', 'YELLOW', 'GREEN', 'NÃO ESPECIFICADO', 'BROWN', 'CHARCOAL', 'ORANGE', 'TURQUOISE', 'PINK', 'OFF-WHITE', 'LIME'], key="color_input")
        interior = st.selectbox("Cor Interior", ['BLACK', 'BEIGE', 'TAN', 'GRAY', 'BROWN', 'BURGUNDY', 'WHITE', 'SILVER', 'OFF-WHITE', 'RED', 'YELLOW', 'BLUE', 'NÃO ESPECIFICADO', 'PURPLE', 'GREEN', 'ORANGE', 'GOLD'], key="interior_input")
        if make == 'KIA':
            model = st.selectbox("Modelo", ['SORENTO', 'OPTIMA', 'RIO', 'SOUL', 'FORTE', 'SPORTAGE', 'SEDONA', 'SPECTRA', 'RONDO', 'BORREGO', 'CADENZA', 'AMANTI'],
                                key="model_input")
            trim = st.selectbox("Tipo", ["LX", "EX HYBRID", "SX", "+", "BASE", "EX", "KOUP EX", "HYBRID", "!", "PREMIUM", "FORTE5 EX", "EX TURBO", "SPORT", "KOUP SX", "RIO5 LX", "RIO5 SX", "SPECTRA5", "LX HYBRID", "SPECTRA5 SX", "LIMITED", "SXL", "SX TURBO"],
                                key="trim_input")
        if make == 'BMW':
            model = st.selectbox("Modelo", ["X1","5 SERIES","3 SERIES","1 SERIES","X3","7 SERIES","5 SERIES GRAN TURISMO","X5","M3","Z4","6 SERIES","M5","X6","M6","2 SERIES","Z4 M","ACTIVEHYBRID X6","3 SERIES GRAN TURISMO","M","ACTIVEHYBRID 5","ACTIVEHYBRID 7"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["SDRIVE28I", "528I", "328I", "135I", "128I", "XDRIVE28I", "XDRIVE35I", "335I", "535I XDRIVE", "535I", "328I XDRIVE", "740I", "550I", "335D", "335I XDRIVE", "XDRIVE50I", "XDRIVE35D", "750LI", "528I XDRIVE", "XDRIVE48I", "XDRIVE30I", "BASE", "3.0SI", "335XI", "3.0I", "4.8I", "328XI", "650I", "525I", "530I", "325I", "325XI", "330I", "530XI", "320I", "550I XDRIVE", "335IS", "740LI", "750I XDRIVE", "750LI XDRIVE", "750I", "528XI", "535XI", "525XI", "760LI", "330CI", "330XI", "325CI", "4.4I", "228I", "XDRIVE35I PREMIUM", "320I XDRIVE", "128I SULEV", "ACTIVEHYBRID 3", "4.8IS", "328I SULEV", "SDRIVE30I", "SDRIVE35I", "ACTIVEHYBRID 5", "328I XDRIVE SULEV", "740LI XDRIVE", "328D"],
                                key="trim_input")
        if make == 'NISSAN':
            model = st.selectbox("Modelo", ["ALTIMA", "VERSA", "VERSA NOTE", "370Z", "JUKE", "SENTRA", "ROGUE", "NV", "LEAF", "NV200", "QUEST", "MAXIMA", "XTERRA", "FRONTIER", "CUBE", "ARMADA", "MURANO", "PATHFINDER", "ALTIMA HYBRID", "TITAN", "350Z", "ROGUE SELECT", "MURANO CROSSCABRIOLET", "NV CARGO", "NV PASSENGER"],
                                key="model_input")
            trim = st.selectbox("Tipo",  ["2.5 S", "1.6 SL", "1.6 SV", "2.5", "BASE", "S", "SR", "1500 S", "SL", "3.5 SL", "1.6 S PLUS", "3.5 SV", "SV", "1.8 SL", "FE+ S", "3.5 S", "FE+ SV", "2", "1.8 S", "3500 S", "1.6 S", "2.0 SR", "2.0 S", "PLATINUM", "LE", "2.0 SL", "X", "SE", "3.5 SR", "3.5 SE", "XE", "NISMO", "PRO-4X", "1.8 S KROM EDITION", "SE-R", "1.6", "SE-R SPEC V", "1.8 BASE", "TITANIUM", "TOURING", "S KROM EDITION", "1.8 KROM", "S SULEV", "SL SULEV", "ENTHUSIAST", "SE OFF-ROAD", "2500 S", "1.8", "2500 SV", "3.5", "3.5 SE-R", "LE V8", "3500 SV", "1500 SV", "1.6 BASE", "NISMO RS", "2.5 SL", "2.5 SV"],
                                key="trim_input") 
        if make == 'CHEVROLET':
            model = st.selectbox("Modelo", ["CRUZE", "CAMARO", "IMPALA", "MALIBU", "SILVERADO 1500", "TRAVERSE", "SILVERADO 2500HD", "EQUINOX", "CAPTIVA SPORT", "VOLT", "EXPRESS CARGO", "COLORADO", "EXPRESS", "SONIC", "SUBURBAN", "HHR", "TAHOE", "IMPALA LIMITED", "SPARK", "AVEO", "AVALANCHE", "TAHOE HYBRID", "MALIBU CLASSIC", "COBALT", "SILVERADO 1500 CLASSIC", "UPLANDER", "MONTE CARLO", "CORVETTE", "TRAILBLAZER", "SILVERADO 3500HD", "SILVERADO 1500 HYBRID", "SILVERADO 2500HD CLASSIC", "SILVERADO 1500HD", "SILVERADO 3500", "TRAILBLAZER EXT", "MALIBU MAXX", "MALIBU HYBRID", "BLACK DIAMOND AVALANCHE", "SILVERADO 3500 CLASSIC", "SPARK EV"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["1LT", "LT", "2LT", "LS", "LTZ", "LT FLEET", "WORK TRUCK", "LTZ FLEET", "BASE", "1500", "ECO", "2LS FLEET", "1LT FLEET", "LS 3500", "LS FLEET", "LT1", "LTZ 1500", "PANEL LS", "LT2", "2500", "1SS", "1500 LT", "SS", "1500 LTZ", "1500 LS", "LS2", "CARGO", "LT3", "3500", "LS 1500", "2SS", "AVEO5 1LT", "LT 1500", "AVEO5 LS", "1500 LT1", "AVEO5 2LT", "SPORT", "AVEO5 SPECIAL VALUE", "2500 LT", "PANEL LT", "FLEET", "RS", "1LS FLEET", "LT2 XFE", "DIESEL", "XFE", "LS 2500", "SPECIAL VALUE", "50TH ANNIVERSARY", "LT 2500", "Z71 LT", "LT ECO", "LT 3500", "GS"],
                                key="trim_input")
        if make == 'FORD':
            model = st.selectbox("Modelo", ["FUSION", "E-SERIES WAGON", "ESCAPE", "EDGE", "FOCUS", "FLEX", "FIESTA", "F-150", "EXPLORER", "E-SERIES VAN", "EXPEDITION", "MUSTANG", "TRANSIT CONNECT", "TAURUS", "ESCAPE HYBRID", "RANGER", "FUSION HYBRID", "F-250 SUPER DUTY", "ECONOLINE CARGO", "ECONOLINE WAGON", "F-450 SUPER DUTY", "TAURUS X", "EXPLORER SPORT TRAC", "F-350 SUPER DUTY", "FIVE HUNDRED", "C-MAX HYBRID", "C-MAX ENERGI", "FOCUS ST", "CROWN VICTORIA", "EXPEDITION EL", "FREESTYLE", "FUSION ENERGI", "FREESTAR", "SHELBY GT500", "TRANSIT VAN", "TRANSIT WAGON"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["SE", "E-350 SUPER DUTY XL", "LIMITED", "SEL", "TITANIUM", "SES", "XLS", "XLT", "BASE", "S", "FX2", "E-150", "HYBRID", "SPORT", "E-350 SUPER DUTY", "LARIAT", "XL", "V6", "GT", "CARGO VAN XLT", "FX4", "STX", "E-250", "EL LIMITED", "KING RANCH", "ZX3 S", "DELUXE", "ZX4 SE", "SEL FLEET", "ZX4 SES", "EDDIE BAUER", "STANDARD", "E-350 SUPER DUTY XLT", "ST", "GT PREMIUM", "SEL PLUS", "EL KING RANCH", "LX FLEET", "LARIAT LIMITED", "PLATINUM", "CARGO VAN XL", "SHO", "HARLEY-DAVIDSON", "EL SSV FLEET", "WAGON XLT", "E-150 XL", "PREMIUM", "60TH ANNIVERSARY", "GT DELUXE", "FX4 OFF-ROAD", "SSV FLEET", "SE FLEET", "ZX5 SES", "ZX4 ST", "WAGON TITANIUM LWB", "ZX5 SE", "WAGON XLT LWB", "EL XLT", "ELECTRIC", "BEV", "LX", "SE LUXURY", "WAGON XLT PREMIUM", "ZXW SES", "XLT SPORT", "ZX3 SES", "SVT RAPTOR", "CARGO", "WAGON XLT SWB", "CARGO VAN XLT LWB", "E-150 XLT", "V6 PREMIUM", "250 MEDIUM ROOF", "250 LOW ROOF", "150 LOW ROOF", "350 XL LOW ROOF", "EL XL", "ECOBOOST", "250 HIGH ROOF", "CARGO VAN XL LWB", "350 XL HIGH ROOF", "350 XL MEDIUM ROOF"],
                                key="trim_input")
        if make == 'HYUNDAI':
            model = st.selectbox("Modelo", ["SONATA", "ELANTRA", "SANTA FE", "GENESIS", "SONATA HYBRID", "ACCENT", "VELOSTER", "ELANTRA COUPE", "AZERA", "TUCSON", "GENESIS COUPE", "VERACRUZ", "EQUUS", "SANTA FE SPORT", "ELANTRA GT", "ENTOURAGE", "ELANTRA TOURING", "TIBURON"],                        
                                key="model_input")
            trim = st.selectbox("Tipo", ["SE", "LIMITED", "5.0 R-SPEC", "GLS", "SPORT", "SPORT 2.0T", "TURBO", "GS", "BASE", "3.8", "3.8 TRACK", "4.6", "SIGNATURE", "GLS PZEV", "BLUE", "SE V6", "SE SULEV", "LX", "3.8 ULTIMATE", "GL", "3.8 R-SPEC", "3.8 GRAND TOURING", "ULTIMATE", "LIMITED PZEV", "LIMITED V6", "GLS V6", "GT", "LIMITED SULEV", "GS PZEV", "2.0T", "5", "2.0T R-SPEC", "SPORT PZEV", "RE:MIX", "GT LIMITED", "GT SULEV", "ECO", "RE:FLEX"],
                                key="trim_input")
        if make == 'TOYOTA':
            model = st.selectbox("Modelo", ["COROLLA", "SIENNA", "YARIS", "CAMRY", "TACOMA", "FJ CRUISER", "AVALON", "RAV4", "TUNDRA", "PRIUS", "CAMRY HYBRID", "VENZA", "HIGHLANDER", "HIGHLANDER HYBRID", "PRIUS PLUG-IN", "4RUNNER", "SEQUOIA", "MATRIX", "CAMRY SOLARA", "PRIUS V", "PRIUS C", "LAND CRUISER", "AVALON HYBRID"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["LE", "LE 7-PASSENGER MOBILITY AUTO ACCESS", "L", "S", "XLE", "PRERUNNER", "BASE", "TUNDRA", "TWO", "PRERUNNER V6", "S SPECIAL EDITION", "LIMITED", "V6", "SE", "THREE", "BASE 7-PASSENGER", "SPORT", "XLE 8-PASSENGER", "PLATINUM", "TUNDRA GRADE", "III", "XLE 7-PASSENGER", "TOURING", "XR", "SR5", "LE 7-PASSENGER", "SE V6", "CE", "XLS", "LE 8-PASSENGER", "XLE LIMITED 7-PASSENGER", "XLE V6", "SLE V6", "LE PLUS", "S PLUS", "LIMITED 7-PASSENGER", "CE 7-PASSENGER", "FLEET", "SE 8-PASSENGER", "LIMITED FFV", "TUNDRA FFV", "XL", "LE V6", "LE ECO", "PLUS", "L 7-PASSENGER", "ONE", "IV", "II", "XRS", "FIVE", "X-RUNNER V6", "SPORT V6", "TRAIL", "XLE PREMIUM", "V", "SR", "XLE TOURING", "S PREMIUM", "SR FFV", "ADVANCED", "I", "SLE", "SR5 FFV", "XSE", "XLE TOURING SE", "SE SPORT"],
                                key="trim_input")
        if make == 'DODGE':
            model = st.selectbox("Modelo", ["AVENGER", "JOURNEY", "GRAND CARAVAN", "CHARGER", "NITRO", "CHALLENGER", "DART", "CALIBER", "MAGNUM", "DURANGO", "RAM PICKUP 1500", "RAM PICKUP 2500", "RAM PICKUP 3500", "CARAVAN", "STRATUS", "DAKOTA", "SPRINTER CARGO", "SPRINTER"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["SE", "SXT", "AMERICAN VALUE PACKAGE", "CREW", "BASE", "EXPRESS", "SE FLEET", "HEAT", "R/T", "AERO", "SXT FLEET", "3.5L", "SLT", "RT", "ST", "LARAMIE", "LIMITED", "SRT-8", "MAINSTREET", "LUX", "RUSH", "C/V", "CITADEL", "SHOCK", "HERO", "RT FLEET", "SRT8", "3500 170 WB", "2500 144 WB", "SRT-10", "2500 HIGH ROOF 158 WB", "2500 140 WB", "SRT4", "SRT8 SUPERBEE", "GT", "SXT PLUS", "UPTOWN", "BIGHORN", "RALLYE", "2500 170 WB", "3500 HIGH ROOF 158 WB", "3500 HIGH ROOF 140 WB", "SRT8 392", "CROSSROAD", "2500 HIGH ROOF 140 WB", "DETONATOR", "SE PLUS", "FLEET"],
                                key="trim_input")
        if make == 'CHRYSLER':
            model = st.selectbox("Modelo", ["200", "300", "TOWN AND COUNTRY", "SEBRING", "PT CRUISER", "PACIFICA", "ASPEN", "CROSSFIRE"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["LX", "S V6", "TOURING", "LIMITED", "C", "BASE", "TOURING-L", "SRT-8", "GT", "C HEMI", "S", "LIMITED FLEET", "CLASSIC", "TOURING PLUS", "GTC", "C JOHN VARVATOS", "S V8", "C LUXURY SERIES", "LIMITED HEV", "SRT8", "TOURING FLEET"],
                                key="trim_input")
        if make == 'HONDA':
            model = st.selectbox("Modelo", ["ACCORD", "CR-V", "CIVIC", "FIT", "PILOT", "ODYSSEY", "CROSSTOUR", "CR-Z", "ACCORD CROSSTOUR", "INSIGHT", "RIDGELINE", "ELEMENT", "S2000", "ACCORD HYBRID"],
                                key="model_input")
            trim = st.selectbox("Tipo", ["EX V-6", "EX", "LX", "SPORT", "EX-L", "TOURING", "HF", "BASE", "SE", "LX-S", "SI", "DX-VP", "RT", "HYBRID", "RTS", "EX-P", "SPECIAL EDITION", "LX PZEV", "EX-L W/REAR ENTERTAINMENT", "HYBRID PZEV W/LEATHER AND NAVIGATION", "RTL", "VALUE PACKAGE", "SC", "EX-L W/NAVIGATION", "HYBRID PZEV", "SPORT W/NAVIGATION", "TOURING W/NAVIGATION AND REAR ENTERTAINMENT", "TOURING ELITE", "RTX", "NATURAL GAS", "GX", "RTL W/LEATHER", "DX", "HYBRID W/LEATHER", "EX PZEV"],
                                key="trim_input")

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
    condition = st.sidebar.number_input("Estado do Veículo ( 0 - 50) ", min_value=0, step=1, value=0, key="condition_input")
    odometer = st.sidebar.number_input("Kilometragem", min_value=0, step=1, value=0, key="odometer_input")  

# Inputs categóricos
#with st.sidebar.expander("Especificação Técnica do Veículo"):
    make = st.sidebar.selectbox("Fabricante", ['KIA', 'BMW', 'NISSAN', 'CHEVROLET', 'FORD', 'HYUNDAI', 'TOYOTA', 'DODGE', 'CHRYSLER', 'HONDA'], key="make_input")
    body = st.sidebar.selectbox("Categoria", ['SUV', 'SEDAN', 'CONVERTIBLE', 'COUPE', 'HATCHBACK', 'CREW CAB', 'ELANTRA COUPE', 'GENESIS COUPE', 'WAGON', 'MINIVAN', 'VAN', 'DOUBLE CAB', 'CREWMAX CAB', 'ACCESS CAB', 'KING CAB', 'SUPERCREW', 'EXTENDED CAB', 'E-SERIES VAN', 'SUPERCAB', 'REGULAR CAB', 'KOUP', 'QUAD CAB', 'CLUB CAB', 'MEGA CAB', 'TRANSIT VAN', 'REGULAR-CAB'], key="body_input")
    state = st.sidebar.selectbox("Estado", ['CA', 'TX', 'PA', 'MN', 'AZ', 'WI', 'TN', 'MD', 'FL', 'NE', 'NV', 'OH', 'MI', 'NJ', 'SC', 'NC', 'VA', 'IN', 'IL', 'CO', 'UT', 'GA', 'MO', 'NY', 'LA', 'WA', 'PR', 'MA', 'HI', 'OR', 'QC', 'AB', 'ON', 'OK', 'MS', 'NM', 'AL', 'NS'], key="state_input")
    color = st.sidebar.selectbox("Cor", ['WHITE', 'GRAY', 'BLACK', 'RED', 'SILVER', 'BLUE', 'PURPLE', 'BURGUNDY', 'GOLD', 'BEIGE', 'YELLOW', 'GREEN', 'NÃO ESPECIFICADO', 'BROWN', 'CHARCOAL', 'ORANGE', 'TURQUOISE', 'PINK', 'OFF-WHITE', 'LIME'], key="color_input")
    interior = st.sidebar.selectbox("Cor Interior", ['BLACK', 'BEIGE', 'TAN', 'GRAY', 'BROWN', 'BURGUNDY', 'WHITE', 'SILVER', 'OFF-WHITE', 'RED', 'YELLOW', 'BLUE', 'NÃO ESPECIFICADO', 'PURPLE', 'GREEN', 'ORANGE', 'GOLD'], key="interior_input")
    if make == 'KIA':
        model = st.sidebar.selectbox("Modelo", ['SORENTO', 'OPTIMA', 'RIO', 'SOUL', 'FORTE', 'SPORTAGE', 'SEDONA', 'SPECTRA', 'RONDO', 'BORREGO', 'CADENZA', 'AMANTI'],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["LX", "EX HYBRID", "SX", "+", "BASE", "EX", "KOUP EX", "HYBRID", "!", "PREMIUM", "FORTE5 EX", "EX TURBO", "SPORT", "KOUP SX", "RIO5 LX", "RIO5 SX", "SPECTRA5", "LX HYBRID", "SPECTRA5 SX", "LIMITED", "SXL", "SX TURBO"],
                              key="trim_input")
    if make == 'BMW':
        model = st.sidebar.selectbox("Modelo", ["X1","5 SERIES","3 SERIES","1 SERIES","X3","7 SERIES","5 SERIES GRAN TURISMO","X5","M3","Z4","6 SERIES","M5","X6","M6","2 SERIES","Z4 M","ACTIVEHYBRID X6","3 SERIES GRAN TURISMO","M","ACTIVEHYBRID 5","ACTIVEHYBRID 7"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["SDRIVE28I", "528I", "328I", "135I", "128I", "XDRIVE28I", "XDRIVE35I", "335I", "535I XDRIVE", "535I", "328I XDRIVE", "740I", "550I", "335D", "335I XDRIVE", "XDRIVE50I", "XDRIVE35D", "750LI", "528I XDRIVE", "XDRIVE48I", "XDRIVE30I", "BASE", "3.0SI", "335XI", "3.0I", "4.8I", "328XI", "650I", "525I", "530I", "325I", "325XI", "330I", "530XI", "320I", "550I XDRIVE", "335IS", "740LI", "750I XDRIVE", "750LI XDRIVE", "750I", "528XI", "535XI", "525XI", "760LI", "330CI", "330XI", "325CI", "4.4I", "228I", "XDRIVE35I PREMIUM", "320I XDRIVE", "128I SULEV", "ACTIVEHYBRID 3", "4.8IS", "328I SULEV", "SDRIVE30I", "SDRIVE35I", "ACTIVEHYBRID 5", "328I XDRIVE SULEV", "740LI XDRIVE", "328D"],
                              key="trim_input")
    if make == 'NISSAN':
        model = st.sidebar.selectbox("Modelo", ["ALTIMA", "VERSA", "VERSA NOTE", "370Z", "JUKE", "SENTRA", "ROGUE", "NV", "LEAF", "NV200", "QUEST", "MAXIMA", "XTERRA", "FRONTIER", "CUBE", "ARMADA", "MURANO", "PATHFINDER", "ALTIMA HYBRID", "TITAN", "350Z", "ROGUE SELECT", "MURANO CROSSCABRIOLET", "NV CARGO", "NV PASSENGER"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo",  ["2.5 S", "1.6 SL", "1.6 SV", "2.5", "BASE", "S", "SR", "1500 S", "SL", "3.5 SL", "1.6 S PLUS", "3.5 SV", "SV", "1.8 SL", "FE+ S", "3.5 S", "FE+ SV", "2", "1.8 S", "3500 S", "1.6 S", "2.0 SR", "2.0 S", "PLATINUM", "LE", "2.0 SL", "X", "SE", "3.5 SR", "3.5 SE", "XE", "NISMO", "PRO-4X", "1.8 S KROM EDITION", "SE-R", "1.6", "SE-R SPEC V", "1.8 BASE", "TITANIUM", "TOURING", "S KROM EDITION", "1.8 KROM", "S SULEV", "SL SULEV", "ENTHUSIAST", "SE OFF-ROAD", "2500 S", "1.8", "2500 SV", "3.5", "3.5 SE-R", "LE V8", "3500 SV", "1500 SV", "1.6 BASE", "NISMO RS", "2.5 SL", "2.5 SV"],
                              key="trim_input") 
    if make == 'CHEVROLET':
        model = st.sidebar.selectbox("Modelo", ["CRUZE", "CAMARO", "IMPALA", "MALIBU", "SILVERADO 1500", "TRAVERSE", "SILVERADO 2500HD", "EQUINOX", "CAPTIVA SPORT", "VOLT", "EXPRESS CARGO", "COLORADO", "EXPRESS", "SONIC", "SUBURBAN", "HHR", "TAHOE", "IMPALA LIMITED", "SPARK", "AVEO", "AVALANCHE", "TAHOE HYBRID", "MALIBU CLASSIC", "COBALT", "SILVERADO 1500 CLASSIC", "UPLANDER", "MONTE CARLO", "CORVETTE", "TRAILBLAZER", "SILVERADO 3500HD", "SILVERADO 1500 HYBRID", "SILVERADO 2500HD CLASSIC", "SILVERADO 1500HD", "SILVERADO 3500", "TRAILBLAZER EXT", "MALIBU MAXX", "MALIBU HYBRID", "BLACK DIAMOND AVALANCHE", "SILVERADO 3500 CLASSIC", "SPARK EV"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["1LT", "LT", "2LT", "LS", "LTZ", "LT FLEET", "WORK TRUCK", "LTZ FLEET", "BASE", "1500", "ECO", "2LS FLEET", "1LT FLEET", "LS 3500", "LS FLEET", "LT1", "LTZ 1500", "PANEL LS", "LT2", "2500", "1SS", "1500 LT", "SS", "1500 LTZ", "1500 LS", "LS2", "CARGO", "LT3", "3500", "LS 1500", "2SS", "AVEO5 1LT", "LT 1500", "AVEO5 LS", "1500 LT1", "AVEO5 2LT", "SPORT", "AVEO5 SPECIAL VALUE", "2500 LT", "PANEL LT", "FLEET", "RS", "1LS FLEET", "LT2 XFE", "DIESEL", "XFE", "LS 2500", "SPECIAL VALUE", "50TH ANNIVERSARY", "LT 2500", "Z71 LT", "LT ECO", "LT 3500", "GS"],
                              key="trim_input")
    if make == 'FORD':
        model = st.sidebar.selectbox("Modelo", ["FUSION", "E-SERIES WAGON", "ESCAPE", "EDGE", "FOCUS", "FLEX", "FIESTA", "F-150", "EXPLORER", "E-SERIES VAN", "EXPEDITION", "MUSTANG", "TRANSIT CONNECT", "TAURUS", "ESCAPE HYBRID", "RANGER", "FUSION HYBRID", "F-250 SUPER DUTY", "ECONOLINE CARGO", "ECONOLINE WAGON", "F-450 SUPER DUTY", "TAURUS X", "EXPLORER SPORT TRAC", "F-350 SUPER DUTY", "FIVE HUNDRED", "C-MAX HYBRID", "C-MAX ENERGI", "FOCUS ST", "CROWN VICTORIA", "EXPEDITION EL", "FREESTYLE", "FUSION ENERGI", "FREESTAR", "SHELBY GT500", "TRANSIT VAN", "TRANSIT WAGON"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["SE", "E-350 SUPER DUTY XL", "LIMITED", "SEL", "TITANIUM", "SES", "XLS", "XLT", "BASE", "S", "FX2", "E-150", "HYBRID", "SPORT", "E-350 SUPER DUTY", "LARIAT", "XL", "V6", "GT", "CARGO VAN XLT", "FX4", "STX", "E-250", "EL LIMITED", "KING RANCH", "ZX3 S", "DELUXE", "ZX4 SE", "SEL FLEET", "ZX4 SES", "EDDIE BAUER", "STANDARD", "E-350 SUPER DUTY XLT", "ST", "GT PREMIUM", "SEL PLUS", "EL KING RANCH", "LX FLEET", "LARIAT LIMITED", "PLATINUM", "CARGO VAN XL", "SHO", "HARLEY-DAVIDSON", "EL SSV FLEET", "WAGON XLT", "E-150 XL", "PREMIUM", "60TH ANNIVERSARY", "GT DELUXE", "FX4 OFF-ROAD", "SSV FLEET", "SE FLEET", "ZX5 SES", "ZX4 ST", "WAGON TITANIUM LWB", "ZX5 SE", "WAGON XLT LWB", "EL XLT", "ELECTRIC", "BEV", "LX", "SE LUXURY", "WAGON XLT PREMIUM", "ZXW SES", "XLT SPORT", "ZX3 SES", "SVT RAPTOR", "CARGO", "WAGON XLT SWB", "CARGO VAN XLT LWB", "E-150 XLT", "V6 PREMIUM", "250 MEDIUM ROOF", "250 LOW ROOF", "150 LOW ROOF", "350 XL LOW ROOF", "EL XL", "ECOBOOST", "250 HIGH ROOF", "CARGO VAN XL LWB", "350 XL HIGH ROOF", "350 XL MEDIUM ROOF"],
                              key="trim_input")
    if make == 'HYUNDAI':
        model = st.sidebar.selectbox("Modelo", ["SONATA", "ELANTRA", "SANTA FE", "GENESIS", "SONATA HYBRID", "ACCENT", "VELOSTER", "ELANTRA COUPE", "AZERA", "TUCSON", "GENESIS COUPE", "VERACRUZ", "EQUUS", "SANTA FE SPORT", "ELANTRA GT", "ENTOURAGE", "ELANTRA TOURING", "TIBURON"],                        
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["SE", "LIMITED", "5.0 R-SPEC", "GLS", "SPORT", "SPORT 2.0T", "TURBO", "GS", "BASE", "3.8", "3.8 TRACK", "4.6", "SIGNATURE", "GLS PZEV", "BLUE", "SE V6", "SE SULEV", "LX", "3.8 ULTIMATE", "GL", "3.8 R-SPEC", "3.8 GRAND TOURING", "ULTIMATE", "LIMITED PZEV", "LIMITED V6", "GLS V6", "GT", "LIMITED SULEV", "GS PZEV", "2.0T", "5", "2.0T R-SPEC", "SPORT PZEV", "RE:MIX", "GT LIMITED", "GT SULEV", "ECO", "RE:FLEX"],
                              key="trim_input")
    if make == 'TOYOTA':
        model = st.sidebar.selectbox("Modelo", ["COROLLA", "SIENNA", "YARIS", "CAMRY", "TACOMA", "FJ CRUISER", "AVALON", "RAV4", "TUNDRA", "PRIUS", "CAMRY HYBRID", "VENZA", "HIGHLANDER", "HIGHLANDER HYBRID", "PRIUS PLUG-IN", "4RUNNER", "SEQUOIA", "MATRIX", "CAMRY SOLARA", "PRIUS V", "PRIUS C", "LAND CRUISER", "AVALON HYBRID"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["LE", "LE 7-PASSENGER MOBILITY AUTO ACCESS", "L", "S", "XLE", "PRERUNNER", "BASE", "TUNDRA", "TWO", "PRERUNNER V6", "S SPECIAL EDITION", "LIMITED", "V6", "SE", "THREE", "BASE 7-PASSENGER", "SPORT", "XLE 8-PASSENGER", "PLATINUM", "TUNDRA GRADE", "III", "XLE 7-PASSENGER", "TOURING", "XR", "SR5", "LE 7-PASSENGER", "SE V6", "CE", "XLS", "LE 8-PASSENGER", "XLE LIMITED 7-PASSENGER", "XLE V6", "SLE V6", "LE PLUS", "S PLUS", "LIMITED 7-PASSENGER", "CE 7-PASSENGER", "FLEET", "SE 8-PASSENGER", "LIMITED FFV", "TUNDRA FFV", "XL", "LE V6", "LE ECO", "PLUS", "L 7-PASSENGER", "ONE", "IV", "II", "XRS", "FIVE", "X-RUNNER V6", "SPORT V6", "TRAIL", "XLE PREMIUM", "V", "SR", "XLE TOURING", "S PREMIUM", "SR FFV", "ADVANCED", "I", "SLE", "SR5 FFV", "XSE", "XLE TOURING SE", "SE SPORT"],
                              key="trim_input")
    if make == 'DODGE':
        model = st.sidebar.selectbox("Modelo", ["AVENGER", "JOURNEY", "GRAND CARAVAN", "CHARGER", "NITRO", "CHALLENGER", "DART", "CALIBER", "MAGNUM", "DURANGO", "RAM PICKUP 1500", "RAM PICKUP 2500", "RAM PICKUP 3500", "CARAVAN", "STRATUS", "DAKOTA", "SPRINTER CARGO", "SPRINTER"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["SE", "SXT", "AMERICAN VALUE PACKAGE", "CREW", "BASE", "EXPRESS", "SE FLEET", "HEAT", "R/T", "AERO", "SXT FLEET", "3.5L", "SLT", "RT", "ST", "LARAMIE", "LIMITED", "SRT-8", "MAINSTREET", "LUX", "RUSH", "C/V", "CITADEL", "SHOCK", "HERO", "RT FLEET", "SRT8", "3500 170 WB", "2500 144 WB", "SRT-10", "2500 HIGH ROOF 158 WB", "2500 140 WB", "SRT4", "SRT8 SUPERBEE", "GT", "SXT PLUS", "UPTOWN", "BIGHORN", "RALLYE", "2500 170 WB", "3500 HIGH ROOF 158 WB", "3500 HIGH ROOF 140 WB", "SRT8 392", "CROSSROAD", "2500 HIGH ROOF 140 WB", "DETONATOR", "SE PLUS", "FLEET"],
                              key="trim_input")
    if make == 'CHRYSLER':
        model = st.sidebar.selectbox("Modelo", ["200", "300", "TOWN AND COUNTRY", "SEBRING", "PT CRUISER", "PACIFICA", "ASPEN", "CROSSFIRE"],
                              key="model_input")
        trim = st.sidebar.selectbox("Tipo", ["LX", "S V6", "TOURING", "LIMITED", "C", "BASE", "TOURING-L", "SRT-8", "GT", "C HEMI", "S", "LIMITED FLEET", "CLASSIC", "TOURING PLUS", "GTC", "C JOHN VARVATOS", "S V8", "C LUXURY SERIES", "LIMITED HEV", "SRT8", "TOURING FLEET"],
                              key="trim_input")
    if make == 'HONDA':
        model = st.sidebar.selectbox("Modelo", ["ACCORD", "CR-V", "CIVIC", "FIT", "PILOT", "ODYSSEY", "CROSSTOUR", "CR-Z", "ACCORD CROSSTOUR", "INSIGHT", "RIDGELINE", "ELEMENT", "S2000", "ACCORD HYBRID"],
                              key="model_input")
        trim = st.selectbox("Tipo", ["EX V-6", "EX", "LX", "SPORT", "EX-L", "TOURING", "HF", "BASE", "SE", "LX-S", "SI", "DX-VP", "RT", "HYBRID", "RTS", "EX-P", "SPECIAL EDITION", "LX PZEV", "EX-L W/REAR ENTERTAINMENT", "HYBRID PZEV W/LEATHER AND NAVIGATION", "RTL", "VALUE PACKAGE", "SC", "EX-L W/NAVIGATION", "HYBRID PZEV", "SPORT W/NAVIGATION", "TOURING W/NAVIGATION AND REAR ENTERTAINMENT", "TOURING ELITE", "RTX", "NATURAL GAS", "GX", "RTL W/LEATHER", "DX", "HYBRID W/LEATHER", "EX PZEV"],
                              key="trim_input")

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
    st.markdown(f'<p style="font-size: 25px; font-weight: bold;">Preço Previsto do Veículo: $ {preco_formatado}</p>', unsafe_allow_html=True)
       
def main(): 
    st.set_page_config(page_title="Motor Web", page_icon="🚗")
    
    st.sidebar.image('transferir.png', use_column_width=True)

    # Criação do navbar
    navbar = st.sidebar.selectbox('Navegação', ['Página Inicial', 'Previsão de Preço'])

    if navbar == "Página Inicial":
        st.markdown("<h2 style='text-left: center; color: yellow;'>MOTOR WEB</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-left: center; color: white;'>Bem-vindo ao Sistema de Previsão de Preço de Veículos!</h3>", unsafe_allow_html=True)
        st.write("""
            Este sistema foi desenvolvido para oferecer uma estimativa do valor de mercado de veículos com base em diversas variáveis do mercado automotivo. 
            Nossa tecnologia utiliza algoritmos avançados para analisar as tendências atuais do mercado e considerar fatores importantes, como:

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
        st.write("""
                 Nossa plataforma analisa cuidadosamente os dados do veículo para prever seu valor de mercado. 
                 Com base nas informações fornecidas, oferecemos uma estimativa precisa do preço do veículo. 
                 Nosso objetivo é ajudá-lo a entender o valor atual do veículo no mercado automotivo. 
                 Após fornecer todas as informações necessárias, clique no botão Enviar para gerar a estimativa de preço do veículo.
                 """)
        interface_previsao()

if __name__ == "__main__":
    main()