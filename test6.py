import streamlit as st


#定义视频列表，含每集的url、标题和集数信息
video_arr=[
    {
        'url':'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第一集.mp4',
        'title':'喜羊羊与灰太狼-第1集',
        'episode':1
    },{
        'url':'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第二集.mp4',
        'title':'喜羊羊与灰太狼-第2集',
        'episode':2
    },{
        'url':'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第三集.mp4',
        'title':'喜羊羊与灰太狼-第3集',
        'episode':3
    },{
        'url':'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第四集.mp4',
        'title':'喜羊羊与灰太狼-第4集',
        'episode':4
    },{
        'url':'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第五集.mp4',
        'title':'喜羊羊与灰太狼-第5集',
        'episode':5
    },{
        'url':'https://mp-44fa5fcb-6636-49e6-94dd-bbde82a4ce6d.cdn.bspapp.com/第六集.mp4',
        'title':'喜羊羊与灰太狼-第6集',
        'episode':6
        }]

#判断内存中有没有ind
if 'ind' not in st.session_state:
    st.session_state['ind']=0

#设置动态标题
current_title=video_arr[st.session_state['ind']]['title']
st.title(current_title)

#播放当前选中视频
st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

#切换集数
def play(i):
    st.session_state['ind']=int(i)

#分排显示集数按钮
row1=st.columns(3)
for i in range(3):
    with row1[i]:
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))
row2=st.columns(3)
for i in range(3,6):
    with row2[i-3]:
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))

st.markdown('***')
#显示喜羊羊与灰太狼作品简介
st.caption("""
《喜羊羊与灰太狼》是由**广东原创动力文化传播有限公司**制作的原创动画作品系列，以**友情、搞笑、童话**为主题。该动画系列以羊族和狼族之间妙趣横生的故事为主线，讲述了羊狼从斗争到和平的故事。截至2025年7月，《喜羊羊与灰太狼》共播出作品43季3081集（主线31季2402集、网络短剧12季679集）、电影12部（动画电影10部、真人电影2部）、舞台剧5部。
""")
