# -*- coding: utf-8 -*-
"""
Created on 20240902

@author: Zwj
"""


# 请确保model.sav的路径与实际路径相匹配
MODEL_PATH = 'model.sav'
# 载入预先训练好的模型
model = load(MODEL_PATH)

# 定义一个函数来处理输入并进行预测
def predict_properties(input_features):
    T = input_features['Temperature']
    RT = input_features['Residence_time']
    FR = input_features['Flow_rate']
    QR = input_features['Q_rate']
    Hg0 = input_features['Hg']
    CO2 = input_features['CO2_c']
    O2 = input_features['O2_c']
    SO2 = input_features['SO2_c']
    NO = input_features['NO_c']
    Cl2 = input_features['Cl2_c']
    Br2 = input_features['Br2_c']
    HCl = input_features['HCl_c']
    HBr = input_features['HBr_c']

    # 4. 合并输入特征并转换为 NumPy 数组
    x=np.array([[T,RT,FR,QR,Hg0,CO2,O2,SO2,NO,Cl2,Br2,HCl,HBr]])
    #x=np.array(x).reshape(-1,9)
    # 5. 使用模型进行预测
    prediction = model.predict(x)
    return prediction
#%%
# 使用 CSS 来自定义 Streamlit 应用的样式
st.markdown(f"""
    <style>
    html, body {{
        font-family: 'Times New Roman', Times, serif;
    }}
    [class*="st-"] {{
        font-family: 'Times New Roman', Times, serif;
    }}
    h1 {{
        font-size: 27px; /* 设置表头字体大小 */
    }}
    .reportview-container {{
        background-color: #ADD8E6; /* 修改为浅蓝色背景 */
    }}
    .sidebar .sidebar-content {{
        background-color: #456789; /* 侧边栏颜色 */
    }}
    </style>
    """, unsafe_allow_html=True)

#%%
st.markdown('<h1 class="big-font">Prediction of gaseous compositions producted from liquefaction of biomass</h1>', unsafe_allow_html=True)


# 输入字段布局
col1, col2= st.columns(2)
with col1:
    st.markdown(f'<div class="st-bc">', unsafe_allow_html=True)
    st.markdown('**Atmosphere compositions**')
    CO2 = st.number_input('CO2 (ppm)', min_value=0.0, value=10000, step=1, key='CO2_c')
    O2 = st.number_input('O2 (ppm)', min_value=0.0, value=50.0, step=0.1, key='O2_c')
    SO2 = st.number_input('SO2 (ppm)', min_value=0.0, value=50.0, step=0.1, key='SO2_c')
    NO = st.number_input('NO (ppm)', min_value=0.0, value=50.0, step=0.1, key='NO_c')
    Cl2 = st.number_input('Cl2 (ppm)', min_value=0.0, value=50.0, step=0.1, key='Cl2_c')
    Br2 = st.number_input('Br2 (ppm)', min_value=0.0, value=50.0, step=0.1, key='Br2_c')
    HCl = st.number_input('HCl (ppm)', min_value=0.0, value=5.0, step=0.1, key='HCl_c')
    HBr = st.number_input('HBr (ppm)', min_value=0.0, value=1.5, step=0.1, key='HBr_c')

    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="st-ba">', unsafe_allow_html=True)
    st.markdown('**Operating conditions**')
    T = st.number_input('Tempreature (°C)', min_value=0.0, value=400.0, step=0.1, key='Temperature')
    RT = st.number_input('Residence time (min)', min_value=0.0, value=100.0, step=0.1, key='Residence_time')
    FR= st.number_input('Flow rate ()', min_value=0.0, value=100.0, step=0.1, key='Flow_rate')
    QR = st.number_input('Quench rate (K/s)', min_value=0.0, value=50.0, step=0.1, key='Q_rate')
    Hg0 = st.number_input('Hg0 (μg/m3)', min_value=0.0, value=50.0, step=0.1, key='Hg')
    st.markdown('</div>', unsafe_allow_html=True)

# 收集所有输入数据
input_features = {'Temperature': T, 'Residence_time': RT, 'Flow_rate': FR, 'Q_rate': QR,
                  'Hg':Hg0, 'CO2_c': CO2, 'O2_c': O2,'SO2_c': SO2, 'NO_c': NO,'Cl2_c': Cl2,'Br2_c': Br2,
                  'HCl_c': HCl,'HBr_c': HBr}

# 当用户点击预测按钮时执行
# 在每列之上显示标题
st.write('Prediction of gaseous compositions:')
col1= st.columns(0)
if st.button('Predict'):
    prediction = predict_properties(input_features)
    # 显示预测结果
    col1.write(f'Hg oxidation percent (%): float(prediction[:,0])')

else:
    # 按钮未点击时也在三列中显示标签
    col1.write('Hg oxidation percent (%) =')



#%%
