import streamlit as st
import pandas as pd
import plotly.express as px

def get_dataframe_from_excel():
    df = pd.read_excel('C:\\Users\\712\\Desktop\\supermarket_sales.xlsx',
                       sheet_name='销售数据',
                       skiprows=1,
                       index_col='订单号')
    df['小时数'] = pd.to_datetime(df['时间'], format="%H:%M:%S").dt.hour
    return df

# 关键：add_sidebar_func 函数要完整包裹筛选逻辑和 return 语句
def add_sidebar_func(df):
    # 创建侧边栏
    with st.sidebar:
        st.header("请筛选数据：")
        # 筛选城市
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "请选择城市：",
            options=city_unique,
            default=city_unique,
        )
        # 筛选顾客类型
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,
            default=customer_type_unique,
        )
        # 筛选性别
        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            "请选择性别.",
            options=gender_unique,
            default=gender_unique,
        )
    
    # 筛选数据（注意：这部分要在函数内，且缩进和函数内的代码对齐）
    df_selection = df.query(
        "城市 == @city & 顾客类型 ==@customer_type & 性别 == @gender"
    )
    
    # ✅ 关键：return 在 add_sidebar_func 函数内，缩进正确
    return df_selection

# 其他函数（hour_chart / product_line_chart / main_page_demo）...
def hour_chart(df):
    sales_by_hour = df.groupby(by=["小时数"])["总价"].sum()
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
    )
    return fig_hour_sales

def product_line_chart(df):
    sales_by_product_line = df.groupby(by=["产品类型"])["总价"].sum().sort_values(ascending=False)
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
    )
    return fig_product_sales

def main_page_demo(df):
    st.title('📊销售仪表板')
    left_key_col, middle_key_col, right_key_col = st.columns(3)

    total_sales = int(df["总价"].sum())
    average_rating = round(df["评分"].mean(), 1)
    star_rating_string = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df["总价"].mean(), 2)

    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f"RMB ¥ {total_sales:,}")
    
    with middle_key_col:
        st.subheader("顾客评分的平均值: ")
        st.subheader(f"({average_rating}) {star_rating_string}")
    
    with right_key_col:
        st.subheader("每单的平均销售额:")
        st.subheader(f"RMB ¥ {average_sale_by_transaction}")

    st.divider()
    left_chart_col, right_chart_col = st.columns(2)
    with left_chart_col:
        hour_fig = hour_chart(df)
        st.plotly_chart(hour_fig, use_container_width=True)
    
    with right_chart_col:
        product_fig = product_line_chart(df)
        st.plotly_chart(product_fig, use_container_width=True)

def run_app():
    st.set_page_config(
        page_title="📊销售仪表板",
        layout="wide"
    )
    sale_df = get_dataframe_from_excel()
    df_selection = add_sidebar_func(sale_df)
    main_page_demo(df_selection)

# 启动应用
if __name__ == "__main__":
    run_app()
