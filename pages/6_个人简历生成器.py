import streamlit as st
from datetime import datetime, timedelta


st.set_page_config(page_title="个人简历生成器", page_icon="✅", layout="wide")

#标题
st.header("✅个人简历生成器")
st.markdown('*使用Streamlit创建您的个性化简历*')

#分列
c1,c2=st.columns([1,2])

#左边
with c1:
    st.subheader("个人信息表单")
#分隔线
    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)
    user_name=st.text_input('姓名')
    user_image=st.file_uploader("上传照片",type=["jpg", "png", "jpeg"], help="支持 JPG, PNG 格式，最大 5MB")
    user_position=st.text_input('职位')
    user_phone=st.text_input('电话')
    user_address=st.text_input('邮箱')
    user_DOB=st.date_input("选择您的出生日期")
    user_sex=st.radio('性别',['男', '女', '其他'],horizontal=True)
    start_salary,end_salary=st.select_slider(
        '选择期望的薪资范围(K)',
        options=[5,7,10,12,15,17,20,25,30],
        value=(10,20)
        )
    my_range=range(0,31)
    numbers=st.select_slider('工作经验（年）',options=my_range,value=None)
    user_edcation=st.selectbox('学历',['小学', '初中', '高中','专科', '专升本', '本科','研究生', '博士', '硕士'])
    user_language=st.multiselect('语言能力',['汉语', '英语', '日语', '韩语', '法语', '德语', '西班牙语'])
    user_personal=st.text_area(label='个人简介:',placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
    user_skills=st.multiselect('技能（可多选）',
                               ['Java', 'HTML/CSS', '机器学习', 'Python', 'C语言', '软件测试', '数据结构','管理信息系统'],
                               max_selections=8)
    best_time=st.time_input("每日最佳联系时间段:")


#右边
with c2:
    st.subheader("简历实时预览")
#分隔线
    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)
    c3,c4=st.columns([2,1],gap="large")
#右边的左边
    with c3:
        st.header('姓名:'+str(user_name))
        if user_image is not None:
            st.image(user_image,width=200)  
        st.text('职位:'+str(user_position))
        st.text('电话:'+str(user_phone))
       
#右边的右边
    with c4:
        st.text('邮箱:'+str(user_address))
        st.text('出生日期:'+str(user_DOB))
        st.text('性别:'+str(user_sex))
        st.text('学历:'+str(user_edcation))
        st.text(f'工作经验: {numbers}年')
        st.text(f'期望薪资: {start_salary}k-{end_salary}k')
        st.text(f'最佳联系时间: {best_time.strftime("%H:%M")}')
        st.text('语言能力:'+('、'.join(user_language)))
#分隔线   
    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)

    st.subheader('个人简介')
    st.text(user_personal)
    st.subheader('专业技能')
    if user_skills:
        for skill in user_skills:
            st.write(f"• {skill}") 
#分隔线
    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)
