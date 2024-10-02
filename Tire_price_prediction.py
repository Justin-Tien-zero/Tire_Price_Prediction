import streamlit as st
import joblib
import pandas as pd
import requests

# 載入模型與標準化轉換模型
model = joblib.load('Tire_Price_model.joblib')
scaler = joblib.load('Tire_Price_scaler.joblib')

list1 = [0 for _ in range(9)]
st.title('Maruti汽車輪胎市售價格預測')

def get_exchange_rates():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
    data = response.json()
    return data['rates']

# 如果 session_state 中不存在 price_ntd，則初始化
if 'price_inr' not in st.session_state:
    st.session_state.price_inr = 0.0

col1, col2 = st.columns(2)

# Model:
options0 = ('800', 'A-Star', 'Alto', 'Alto K10', 'Baleno', 'Celerio', 'Celerio X', 'Ciaz', 'Dzire', 'Eeco', 'Ertiga', 'Esteem', 'Fronx',
            'Grand Vitara', 'Grand Vitara 2003-2007 XI', 'Gypsy', 'Kizashi', 'New Swift (2018)', 'Omni', 'Ritz', 'SX4', 'Stingray',
            'Swift', 'Swift ', 'Swift Deca', 'Swift Dzire', 'Swift Dzire 2008', 'Vitara Brezza', 'Wagon R', 'Zen', 'Zen Estilo')

# Tyre Brand：
options1 = ('Apollo', 'BridgeStone', 'CEAT', 'Continental', 'Falken', 'Firestone', 'GoodYear', 'Hankook', 'JKTyre', 'Kumho', 'MRF', 'Maxxis', 'Michelin', 'Pirelli', 'UltraMile', 'Yokohama')

# Serial No.：
options2 = ('A348', 'AMAZER3G', 'Ainac 4G', 'Ainac 4GS', 'Altrust',
       'Amazer 3G Maxx', 'Amazer 4G', 'Amazer 4G Eco', 'Amazer 4G Life',
       'Amazer XL', 'Amazer4G', 'Apterra Cross', 'Apterra HP',
       'Aspire 4G', 'Assurance Armorgrip', 'Assurance Duraplus',
       'Assurance Duraplus 2', 'Assurance Triplemax',
       'Assurance Triplemax 2', 'AssuranceDuraplus', 'Azenis PT 722',
       'B-Series B250', 'B-Series B290', 'BluEarth AE50', 'BluEarth RV2',
       'BluEarth-GT AE51', 'Cinturato P1 Verde', 'Cinturato P4',
       'Cinturato P6', 'Cinturato P7', 'Comfort Contact CC6',
       'Conti 4X4 Contact', 'ContiComfortContact CC5',
       'ContiMax Contact MC5', 'Czar HP', 'Czar Sports', 'DB E70B',
       'Ducaro Hi-Miler', 'Duraplus', 'Duraplus DP-M1',
       'Dynapro HP (RA23)', 'Eagle F1 Directional 5', 'Eagle F1 GSD3',
       'Eagle NCT5', 'Earth-1 E400', 'EcoRun ZE914', 'Ecopia EP150',
       'Ecowing KH27', 'Efficient Grip SUV', 'Elanzo Nxt',
       'Elanzo Touring', 'Energy XM2', 'Excellence', 'FR500', 'FS100',
       'FuelSmart', 'GPS2', 'GT3', 'Geolandar A/T G015',
       'Geolandar A/T G016', 'Geolandar G92C', 'Geolandar SUV G055',
       'L607', 'Latitude Tour', 'Linam R 51', 'MAP3', 'MS300',
       'Manchester United', 'Milage X3', 'Milaze', 'Milaze HD',
       'Optimo K415', 'Optimo K715', 'Optimo ME02', 'Potenza G3',
       'Primacy 4ST', 'Primacy SUV', 'Ranger H/T', 'S-Series S248',
       'S-Series S322', 'S.Drive AS01', 'Scorpion Verde All Season',
       'SecuraDrive', 'Sincera835', 'Sincera845', 'Taximaxx', 'Tornado',
       'Turanza ER60', 'Turanza T001', 'Turanza T005', 'UM 551',
       'UM 787 LT', 'UX Royale', 'Ultima NXT', 'Ultima Neo',
       'Ultima Sport', 'Ultima XP', 'Ultima XPC', 'UltraContact UC6',
       'Victra I-Pro MA I-Pro', 'ZCC', 'ZCT', 'ZLO', 'ZLX', 'ZTX', 'ZV2K',
       'ZVTS', 'ZVTSM', 'ZVTV', 'Ziex ZE914 EcoRun')
# Type：
options3 = ('Tube', 'Tubeless')
# Aspect_Rstio：
options6 = ('0', '55', '60', '65', '70', '80')

# Aspect_Rstio：
options8 = ('1', '2', '3', '4', '5')

columns = ['Model(車型)',
           'Tyre Brand(輪胎品牌)',
           'Serial No.(輪胎系列)',
           'Type(輪胎類型)',
           'Load Index(載重指數)',
           'Tire_Width(輪胎寬度)',
           'Aspect_Rstio(扁平比)',
           'Wheel_diam(輪胎內徑)',
           'Rating(用戶評分)'
          ]

df_s = pd.read_csv('df_tires.csv')

with col1:
    
    list1[0] = options0.index(st.selectbox(f'{columns[0]}:', options0))
    selected_brand = st.selectbox(f'{columns[1]}:', options1)
    list1[1] = options1.index(selected_brand)
    filtered_Series = df_s[df_s['Tyre Brand'] == selected_brand]['Serial No.'].sort_values().unique()
    selected_Series = st.selectbox(f'{columns[2]}:', filtered_Series)       
    list1[2] = options2.index(selected_Series)   
    list1[3] = options3.index(st.radio(f'{columns[3]}:', options3))

with col2:
    list1[4] = st.slider(f'{columns[4]}:', value=85, min_value=60, max_value=110, step=1)
    st.write('Values:', list1[4])
    list1[5] = st.slider(f'{columns[5]}:', value=175, min_value=145, max_value=230, step=5)
    list1[6] = options6.index(st.selectbox(f'{columns[6]}:', options6))
    list1[7] = st.slider(f'{columns[7]}:', value=15, min_value=12, max_value=29, step=1)
    st.write(f'您選擇的輪胎規格為{list1[5]}/{options6[list1[6]]} R{list1[7]}')
    list1[8] = options8.index(st.radio(f'{columns[8]}:', options8)) + 1

if st.button('預測'):
    X_new = [list1]
    X_new = scaler.transform(X_new)
    price_inr_input = model.predict(X_new)[0]
    if price_inr_input != st.session_state.price_inr:
        st.session_state.price_inr = price_inr_input
    st.write(f'### 輪胎的預測售價為：{st.session_state.price_inr:.2f} INR')



# 獲取當前匯率
exchange_rates = get_exchange_rates()

# 讓用戶選擇輸出貨幣
currency_options = ["TWD", "USD"]
currency = st.selectbox("貨幣換算", currency_options)

# 根據選擇的貨幣顯示結果
if currency in exchange_rates:
    conversion_rate = exchange_rates[currency]
    converted_price = st.session_state.price_inr * conversion_rate
    st.write(f"換算價格: {converted_price:.2f} {currency} (匯率: {conversion_rate:.4f})")