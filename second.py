import streamlit as st
import pandas as pd
import numpy as np





st.subheader("📍餐厅定位")
map_data={

   "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],

   "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]

}

mp_df=pd.DataFrame(map_data)
st.map(mp_df)





# 定义数据,以便创建数据框
data_1 = {

    '名称':['星艺荟尝不忘', '高峰柠檬鸭', '复记老友粉','好友缘', '西冷牛排店'],

    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],

}

# 根据上面创建的data，创建数据框

df = pd.DataFrame(data_1)



# 定义数据框所用的新索引

index = pd.Series([1, 2, 3,4,5], name='序号')



# 将新索引应用到数据框上

df.index = index

# 修改df，用名称列作为df的索引，替换原有的索引

df.set_index('名称',inplace=True)



st.subheader("⭐️餐厅评分")

# 通过x指定名称所在这一列为条形图的x轴

st.bar_chart(df)





# 定义数据,以便创建数据框

data = {

    '月份':['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','12月','12月'],

    '星艺会尝不忘':[134, 165, 157, 182, 112, 220, 155, 167, 200, 152, 105, 175],

    '高峰柠檬鸭':[184, 211, 108, 177, 149, 196, 119, 166, 203, 155, 123, 189],

    '复记老友粉':[142, 105, 213, 184, 131, 100, 116, 162, 207, 157, 128, 178],

    '好友缘':[139, 209, 111, 172, 146, 194, 121, 168, 204, 100, 125, 186],

    '西冷牛排店':[145, 107, 216, 180, 135, 198, 114, 165, 210, 150, 130, 182],

}

# 根据上面创建的data，创建数据框

df = pd.DataFrame(data)



# 修改df，用月份列作为df的索引，替换原有的索引

df.set_index('月份',inplace=True)



st.subheader("💰不同餐厅不同月份价格折线图")



#显示折线图

st.line_chart(df, width=800, height=300, use_container_width=False)





st.subheader("🕗不同餐厅不同月份价格面积图")

#显示折线图

st.area_chart(df, width=800, height=300, use_container_width=False)

