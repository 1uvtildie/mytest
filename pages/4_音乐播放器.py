import streamlit as st

st.set_page_config(page_title="音频",page_icon="🎸")
st.title("🎶 音频播放器")

if'ind' not in st.session_state:
    st.session_state['ind']=0

List=[
    {
        'url':"https://p2.music.126.net/lUSMfAPtr1o-BMuosKfVQw==/109951172254331834.jpg",
        'text':'专辑封面',
        'textname':'歌名：跟悲伤结了帐',
        'musicsian':'歌手：Gareth.T/揽佬SKAI ISYOURGOD',
        'time':'时长：3:03',
        'music':'https://music.163.com/song/media/outer/url?id=2759426653.mp3'
    },{
        'url':"http://p2.music.126.net/BQAY8w9XzOj_j1wZgIsczQ==/109951168247366566.jpg",
        'text':'专辑封面',
        'textname':'歌名：浆果',
        'musicsian':'歌手：TINY7',
        'time':'时长：4:28',
        'music':'https://music.163.com/song/media/outer/url?id=2015896805.mp3'
    },
        {
        'url':"http://exp-picture.cdn.bcebos.com/e177fc9147e833e0f9b7c0b430ea3e863148591d.jpg?x-bce-process=image%2Fcrop%2Cx_0%2Cy_0%2Cw_628%2Ch_361%2Fformat%2Cf_auto%2Fquality%2Cq_80",
        'text':'专辑封面',
        'textname':'歌名：罗生门（Follow）',
        'musicsian':'歌手：梨冻紧/Wiz_H张子豪',
        'time':'时长：4:03',
        'music':'https://music.163.com/song/media/outer/url?id=1456890009.mp3'
    }]

#下一首歌曲
def nextMusic():
    st.session_state['ind']=(st.session_state['ind']+1)%len(List)
#上一首歌曲  
def lastMusic():
    st.session_state['ind']=(st.session_state['ind']-1)%len(List)
#获取音乐
audio_file = List[st.session_state['ind']]['music']

#分左右列表
c3,c4=st.columns([1,2])


#按钮“左边图片”
with c3:
    st.image(List[st.session_state['ind']]['url'],caption=List[st.session_state['ind']]['text'])

#按钮“右边列表”
with c4:
    st.subheader(List[st.session_state['ind']]['textname'])
    st.text(List[st.session_state['ind']]['musicsian'])
    st.text(List[st.session_state['ind']]['time'])
#上一首和下一首分列
    c1,c2=st.columns(2)
    with c1:
        st.button("上一首",on_click=lastMusic,use_container_width=True)
    with c2:
        st.button("下一首",on_click=nextMusic,use_container_width=True)

#显示播放器
st.audio(audio_file)
