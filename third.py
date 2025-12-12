import streamlit as st

st.set_page_config(page_title="相册",page_icon="🐈")
st.title("我的相册")

if'ind' not in st.session_state:
    st.session_state['ind']=0

images=[
    {
        'url':"https://www.quazero.com/uploads/allimg/140228/1-14022QA426.jpg",
        'text':'猫'
    },{
        'url':"https://img2.jiemian.com/101/original/20160424/14614792893239600_a700x398.jpg",
        'text':'狗'
    },
        {
        'url':"http://k.sinaimg.cn/n/front/320/w640h480/20181025/bbXl-hmxrkzw6725472.jpg/w700d1q75cms.jpg",
        'text':'兔'
    }]


#图片数组
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)

def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)

c1,c2=st.columns(2)

#按钮“上一张”
with c1:
    st.button("上一张",on_click　=lastImg,use_container_width=True)


#按钮“下一张”
with c2:
    st.button("下一张",on_click　=nextImg,use_container_width=True)
