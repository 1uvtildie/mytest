import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="广西职业师范学院",layout="wide")

#标题
st.title("广西职业师范学院")
tab1,tab2,tab3,tab4,tab5,tab6= st.tabs(["瓦煲粉数字档案", "南宁美食数据仪表", "相册","音乐播放器","视频网站","个人简历生成器"])

with tab1:
    # 章节1
    st.header(":blue[*瓦煲粉菜品*]")
    
    # 子章节1
    st.subheader("瓦煲鲜肉粉")
    # 描述1
    st.markdown(":green[瓦煲滚汤，鲜肉秒涮，薄嫩锁汁，骨汤鲜甜，粉滑吸味，端上桌咕嘟冒泡，一口下去，暖到胃里。]")
    
    # 子章节2
    st.subheader("瓦煲猪杂粉")
    # 描述2
    st.markdown(":green[猪肝、粉肠、猪红齐聚瓦煲，番茄炒红油，骨汤兜底，咕嘟间脆变嫩，酸胡椒点睛，汤浓肉香，双筷捞光。]")
    
    # 子章节3
    st.subheader("瓦煲老友粉")
    # 描述3
    st.markdown(":green[先爆豆豉酸笋，再冲老火骨汤，酸辣鲜“嘭”地炸开，指天椒提劲，番茄回甘，猪杂脆嫩，嗦粉冒汗，南宁灵魂醒神。]")
    
    # 分割线
    st.markdown('***')
    
    # 章节2
    st.header(":blue[*菜品选择占比*]")
    c1, c2, c3 = st.columns(3)
    c1.metric(label="瓦煲鲜肉粉", value="40%", delta="-5%")
    c2.metric(label="瓦煲猪杂粉", value="30%", delta="6%")
    c3.metric(label="瓦煲老友粉", value="30%", delta="-2%")
    
    # 分割线
    st.markdown('***')
    
    # 章节3
    st.header(':blue[*今日客流量情况*]')
    st.metric(label="今日到访人数", value="228", delta="10", label_visibility='hidden')
    
    # 分割线
    st.markdown('***')
    
    # 章节4
    st.header(":blue[*瓦煲粉菜单*]")
    data = {
        '今日已售': [89, 67, 72],
        '可加配料': ['葱花，香菜，酸菜，小米辣', '葱花，香菜，酸菜，小米辣', '葱花，香菜，酸菜，小米辣'],
        '价格': [10, 10, 12],
    }
    
    index = pd.Series(['瓦煲鲜肉粉', '瓦煲猪杂粉', '瓦煲老友粉'], name='名称')
    df = pd.DataFrame(data, index=index)
    st.dataframe(df)
    
    # 分割线
    st.markdown('***')
    
    # 章节5
    st.header(':blue[*Python代码块*]')
    
    python_code = '''def hello():
    print("你好，欢迎品尝瓦煲粉！")

st.header(":blue[*菜品选择占比*]")
c1,c2,c3=st.columns(3)
c1.metric(label="瓦煲鲜肉粉", value="40%", delta="-5%")
c2.metric(label="瓦煲猪杂粉", value="30%", delta="6%")
c3.metric(label="瓦煲老友粉", value="30%", delta="-2%")
'''
    
    # 斜体说明文字样式
    st.caption('<i>显示的是菜品占比的Python代码块内容</i>', unsafe_allow_html=True)
    st.code(python_code)
    
    # 底部文字
    st.text('''欢迎大家来品尝！
2025-12-11''')

    
with tab2:
    st.subheader("📍餐厅定位")
    
    # 创建地图数据
    map_data = {
        "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
        "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
    }
    
    mp_df = pd.DataFrame(map_data)
    st.map(mp_df)
    
    # 定义数据,以便创建数据框 - 餐厅评分
    data_1 = {
        '名称': ['星艺荟尝不忘', '高峰柠檬鸭', '复记老友粉', '好友缘', '西冷牛排店'],
        "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    }
    
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data_1)
    
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3, 4, 5], name='序号')
    
    # 将新索引应用到数据框上
    df.index = index
    
    # 修改df，用名称列作为df的索引，替换原有的索引
    df.set_index('名称', inplace=True)
    
    st.subheader("⭐️餐厅评分")
    # 通过x指定名称所在这一列为条形图的x轴
    st.bar_chart(df)
    
    # 定义数据,以便创建数据框 - 每月价格
    data = {
        '月份': ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
        '星艺会尝不忘': [134, 165, 157, 182, 112, 220, 155, 167, 200, 152, 105, 175],
        '高峰柠檬鸭': [184, 211, 108, 177, 149, 196, 119, 166, 203, 155, 123, 189],
        '复记老友粉': [142, 105, 213, 184, 131, 100, 116, 162, 207, 157, 128, 178],
        '好友缘': [139, 209, 111, 172, 146, 194, 121, 168, 204, 100, 125, 186],
        '西冷牛排店': [145, 107, 216, 180, 135, 198, 114, 165, 210, 150, 130, 182],
    }
    
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    
    # 修改df，用月份列作为df的索引，替换原有的索引
    df.set_index('月份', inplace=True)
    
    st.subheader("💰不同餐厅不同月份价格折线图")
    # 显示折线图
    st.line_chart(df, width=800, height=300, use_container_width=False)
    
    st.subheader("🕗不同餐厅不同月份价格面积图")
    # 显示面积图
    st.area_chart(df, width=800, height=300, use_container_width=False)

with tab3:
    st.title("我的相册")
    
    # 初始化相册索引
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    
    # 定义图片数组
    images = [
        {
            'url': "https://www.quazero.com/uploads/allimg/140228/1-14022QA426.jpg",
            'text': '猫'
        },
        {
            'url': "https://img2.jiemian.com/101/original/20160424/14614792893239600_a700x398.jpg",
            'text': '狗'
        },
        {
            'url': "http://k.sinaimg.cn/n/front/320/w640h480/20181025/bbXl-hmxrkzw6725472.jpg/w700d1q75cms.jpg",
            'text': '兔'
        }
    ]
    
    # 显示当前图片
    st.image(
        images[st.session_state['ind']]['url'],
        caption=images[st.session_state['ind']]['text']
    )
    
    # 图片导航函数
    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
    
    def lastImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
    
    # 创建两列布局
    c1, c2 = st.columns(2)
    
    # 按钮"上一张"
    with c1:
        st.button("上一张", on_click=lastImg, use_container_width=True)
    
    # 按钮"下一张"
    with c2:
        st.button("下一张", on_click=nextImg, use_container_width=True)


with tab4:
    st.title("🎶 音频播放器")
    
    # 初始化音频索引
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    
    # 定义音频列表
    audio_list = [
        {
            'url': "https://p2.music.126.net/lUSMfAPtr1o-BMuosKfVQw==/109951172254331834.jpg",
            'text': '专辑封面',
            'textname': '歌名：跟悲伤结了帐',
            'musician': '歌手：Gareth.T/揽佬SKAI ISYOURGOD',
            'time': '时长：3:03',
            'music': 'https://music.163.com/song/media/outer/url?id=2759426653.mp3'
        },
        {
            'url': "http://p2.music.126.net/BQAY8w9XzOj_j1wZgIsczQ==/109951168247366566.jpg",
            'text': '专辑封面',
            'textname': '歌名：浆果',
            'musician': '歌手：TINY7',
            'time': '时长：4:28',
            'music': 'https://music.163.com/song/media/outer/url?id=2015896805.mp3'
        },
        {
            'url': "http://exp-picture.cdn.bcebos.com/e177fc9147e833e0f9b7c0b430ea3e863148591d.jpg?x-bce-process=image%2Fcrop%2Cx_0%2Cy_0%2Cw_628%2Ch_361%2Fformat%2Cf_auto%2Fquality%2Cq_80",
            'text': '专辑封面',
            'textname': '歌名：罗生门（Follow）',
            'musician': '歌手：梨冻紧/Wiz_H张子豪',
            'time': '时长：4:03',
            'music': 'https://music.163.com/song/media/outer/url?id=1456890009.mp3'
        }
    ]
    
    # 歌曲导航函数
    def nextMusic():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(audio_list)
    
    def lastMusic():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(audio_list)
    
    # 获取当前音乐
    current_audio = audio_list[st.session_state['ind']]
    audio_file = current_audio['music']
    
    # 分左右两列布局 (1:2比例)
    left_col, right_col = st.columns([1, 2])
    
    # 左边：专辑封面
    with left_col:
        st.image(
            current_audio['url'],
            caption=current_audio['text']
        )
    
    # 右边：歌曲信息和控制按钮
    with right_col:
        st.subheader(current_audio['textname'])
        st.text(current_audio['musician'])
        st.text(current_audio['time'])
        
        # 上一首和下一首按钮分列
        prev_col, next_col = st.columns(2)
        
        with prev_col:
            st.button("上一首", on_click=lastMusic, use_container_width=True)
        
        with next_col:
            st.button("下一首", on_click=nextMusic, use_container_width=True)
    
    # 显示音频播放器
    st.audio(audio_file)


with tab5:
    # 定义视频列表，含每集的url、标题和集数信息
    video_arr = [
        {
            'url': 'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第一集.mp4',
            'title': '喜羊羊与灰太狼-第1集',
            'episode': 1
        },
        {
            'url': 'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第二集.mp4',
            'title': '喜羊羊与灰太狼-第2集',
            'episode': 2
        },
        {
            'url': 'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第三集.mp4',
            'title': '喜羊羊与灰太狼-第3集',
            'episode': 3
        },
        {
            'url': 'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第四集.mp4',
            'title': '喜羊羊与灰太狼-第4集',
            'episode': 4
        },
        {
            'url': 'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第五集.mp4',
            'title': '喜羊羊与灰太狼-第5集',
            'episode': 5
        },
        {
            'url': 'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第六集.mp4',
            'title': '喜羊羊与灰太狼-第6集',
            'episode': 6
        }
    ]
    
    # 初始化视频索引
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    
    # 设置动态标题
    current_title = video_arr[st.session_state['ind']]['title']
    st.title(current_title)
    
    # 播放当前选中视频
    st.video(video_arr[st.session_state['ind']]['url'], autoplay=True)
    
    # 切换集数函数
    def play(i):
        st.session_state['ind'] = int(i)
    
    # 分排显示集数按钮
    row1 = st.columns(3)
    for i in range(3):
        with row1[i]:
            st.button(f'第{i+1}集', use_container_width=True, on_click=play, args=([i]))
    
    row2 = st.columns(3)
    for i in range(3, 6):
        with row2[i-3]:
            st.button(f'第{i+1}集', use_container_width=True, on_click=play, args=([i]))
    
    # 分割线
    st.markdown('***')
    
    # 显示喜羊羊与灰太狼作品简介
    st.caption("""
《喜羊羊与灰太狼》是由**广东原创动力文化传播有限公司**制作的原创动画作品系列，以**友情、搞笑、童话**为主题。该动画系列以羊族和狼族之间妙趣横生的故事为主线，讲述了羊狼从斗争到和平的故事。截至2025年7月，《喜羊羊与灰太狼》共播出作品43季3081集（主线31季2402集、网络短剧12季679集）、电影12部（动画电影10部、真人电影2部）、舞台剧5部。
""")


with tab6:
    # 标题
    st.header("✅ 个人简历生成器")
    st.markdown("*使用Streamlit创建您的个性化简历*")
    
    # 分列布局
    left_col, right_col = st.columns([1, 2])
    
    # 左边：个人信息表单
    with left_col:
        st.subheader("个人信息表单")
        # 分隔线
        st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', 
                   unsafe_allow_html=True)
        
        user_name = st.text_input('姓名')
        user_image = st.file_uploader(
            "上传照片", 
            type=["jpg", "png", "jpeg"], 
            help="支持 JPG, PNG 格式，最大 5MB"
        )
        user_position = st.text_input('职位')
        user_phone = st.text_input('电话')
        user_address = st.text_input('邮箱')
        user_DOB = st.date_input("选择您的出生日期")
        user_sex = st.radio('性别', ['男', '女', '其他'], horizontal=True)
        
        start_salary, end_salary = st.select_slider(
            '选择期望的薪资范围(K)',
            options=[5, 7, 10, 12, 15, 17, 20, 25, 30],
            value=(10, 20)
        )
        
        my_range = range(0, 31)
        numbers = st.select_slider('工作经验（年）', options=my_range, value=None)
        user_education = st.selectbox(
            '学历', 
            ['小学', '初中', '高中', '专科', '专升本', '本科', '研究生', '博士', '硕士']
        )
        
        user_language = st.multiselect(
            '语言能力', 
            ['汉语', '英语', '日语', '韩语', '法语', '德语', '西班牙语']
        )
        
        user_personal = st.text_area(
            label='个人简介:', 
            placeholder='请简要介绍您的专业背景、职业目标和个人特点...'
        )
        
        user_skills = st.multiselect(
            '技能（可多选）',
            ['Java', 'HTML/CSS', '机器学习', 'Python', 'C语言', '软件测试', '数据结构', '管理信息系统'],
            max_selections=8
        )
        
        best_time = st.time_input("每日最佳联系时间段:")
    
    # 右边：简历实时预览
    with right_col:
        st.subheader("简历实时预览")
        # 分隔线
        st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', 
                   unsafe_allow_html=True)
        
        # 右边内部分为两列
        preview_left, preview_right = st.columns([2, 1], gap="large")
        
        # 右边的左边：基本信息
        with preview_left:
            st.header(f'姓名: {user_name}')
            if user_image is not None:
                st.image(user_image, width=200)
            st.text(f'职位: {user_position}')
            st.text(f'电话: {user_phone}')
        
        # 右边的右边：联系信息
        with preview_right:
            st.text(f'邮箱: {user_address}')
            st.text(f'出生日期: {user_DOB}')
            st.text(f'性别: {user_sex}')
            st.text(f'学历: {user_education}')
            st.text(f'工作经验: {numbers}年')
            st.text(f'期望薪资: {start_salary}k-{end_salary}k')
            if best_time:
                st.text(f'最佳联系时间: {best_time.strftime("%H:%M")}')
            else:
                st.text('最佳联系时间: 未选择')
            st.text(f'语言能力: {"、".join(user_language)}')
        
        # 分隔线
        st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', 
                   unsafe_allow_html=True)
        
        # 个人简介部分
        st.subheader('个人简介')
        st.text(user_personal)
        
        # 专业技能部分
        st.subheader('专业技能')
        if user_skills:
            for skill in user_skills:
                st.write(f"• {skill}")
        
        # 分隔线
        st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', 
                   unsafe_allow_html=True)
