import time
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

st.set_page_config(
    page_title="Estimator - تخمینگر",
    page_icon=":bar_chart:",
    layout="wide"
)

st.markdown("""
    <style>
        body {

            text-align: right;
            font-size: 30px;
        }
        [data-testid="stNotificationContentError"]{direction: rtl;}
        [data-testid="stButton"]{direction: rtl;text-align: right;}
        [data-testid="stCheckbox"]{direction: rtl;text-align: right;}

        .downloadBTN { 
            text-decoration: none; 
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            display: inline-block;
            cursor: pointer;
        }

        .stSpinner > div {
            width: 100px !important;
            height: 100px !important;
            margin: auto !important;
            transform: scale(2) !important;
        }

        .css-pxxe24 {
            visibility: hidden;
        }
        
        .custom-button {
        margin-top: 100px;
        margin-bottom: 100px;
        margin-right: 1000px;
        margin-left: 1000px;
        }

        .stHeadingContainer {text-align: center !important}
        
        [data-testid="InputInstructions"] { display: None; } 
        
    </style>

""", unsafe_allow_html=True)

    
def do_home():
    st.title("به سایت `تخمینگر` خوش آمدید ")

    st.markdown("""
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estimator - تخمینگر</title>
    <style>
        body {
            text-align: right;
            font-size: 30px;
            direction: rtl;
        }
    </style>
</head>
<body>
<h1>Estimator - تخمینگر</h1>

<h2>توضیحات</h2>
<p>سایت "Estimator - تخمینگر" یک اپلیکیشن وب است که برای تخمین قیمت‌ها با استفاده از مدل‌های یادگیری ماشین ایجاد شده است. کاربران می‌توانند از این سایت برای تخمین قیمت لپ تاپ، خانه در ایالات متحده، خانه در ایران، و همچنین بازار سهام استفاده کنند.</p>

<h2>استفاده از فایل CSV</h2>
<p>برای آموزش مدل‌های یادگیری ماشین، از یک فایل CSV به نام "training_data.csv" استفاده شده است. این فایل حاوی داده‌های آموزشی است که بر اساس آن مدل‌های یادگیری ماشین ساخته شده‌اند. کاربران می‌توانند مشاهده را کلیک کنند تا فایل را مشاهده کرده و در صورت نیاز، فایل خود را بارگیری کنند.</p>

<h2>تخمین‌های ممکن</h2>
<p>سایت امکان تخمین قیمت برای چهار دسته اصلی را فراهم می‌کند:</p>
<ol>
    <li><strong>تخمین قیمت لپ تاپ</strong></li>
    <li><strong>تخمین قیمت خانه در ایالات متحده</strong></li>
    <li><strong>تخمین قیمت خانه در ایران</strong></li>
    <li><strong>تخمین قیمت بازار سهام</strong></li>
</ol>

<h2>نحوه استفاده</h2>
<p>برای استفاده از سایت، کاربران مراحل زیر را انجام می‌دهند:</p>
<ol>
    <li>اگر تمایل دارند، فایل CSV آموزشی را و یا فایل خود را بارگیری می‌کنند.</li>
    <li>برای هر قسمت از تخمین (لپ تاپ، خانه در ایالات متحده، خانه در ایران یا بازار سهام)، ویژگی‌های مورد نظر را وارد می‌کنند.</li>
    <li>سپس، سایت براساس ویژگی‌های وارد شده، قیمت تخمین زده شده توسط مدل یادگیری ماشین را اعلام می‌کند.</li>
</ol>

<h2>اجزای پروژه</h2>
<p>پروژه از Streamlit برای ساخت این اپلیکیشن وب استفاده کرده است. از مدل‌های یادگیری ماشین بر اساس داده‌های آموزشی بهینه‌سازی شده‌اند.</p>
<p><strong>هدف این سایت ارائه یک ابزار کاربردی برای تخمین قیمت محصولات و دارایی‌ها با استفاده از یادگیری ماشین است.</strong></p>
<p><strong>این سایت برای کاربرانی طراحی شده است که می‌خواهند قیمت محصولات و دارایی‌ها را بدون نیاز به داشتن دانش تخصصی در زمینه یادگیری ماشین تخمین بزنند.</strong></p>

</body>
</html>
""", unsafe_allow_html=True)

def chart_to_base64(plt_chart):
    """
    Convert Matplotlib chart to base64 for Streamlit
    """
    import base64
    import io

    buffer = io.BytesIO()
    plt_chart.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt_chart.clear()

    return image_base64


def upload_file():
    uploaded_file = st.file_uploader("", type=["csv", 'xlsx'])
    return uploaded_file


def load_data():
    bad_data = pd.read_csv(r"CSV_data\bad_data.csv", encoding='latin1')
    clean_data = pd.read_csv(r"CSV_data\clean_data.csv", encoding='latin1')
    return bad_data, clean_data
def initialize_session_state():
    if 'remove' not in st.session_state:
        st.session_state.remove = False
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
        
def count_empty_values(df):
    empty_values = df.isnull().sum()
    return empty_values

def count_text_values(df):
    text_columns = df.select_dtypes(include=['object']).columns
    text_empty_values = df[text_columns].isna()
    text_empty_counts = text_empty_values.sum()
    return text_empty_counts

def plot_bad_data_chart(df):
    text_empty_counts = count_text_values(df)
    plt.bar(text_empty_counts.index, text_empty_counts.values)
    plt.xlabel(get_display(arabic_reshaper.reshape('ستون‌ها')))  # استفاده از arabic_reshaper
    plt.ylabel(get_display(arabic_reshaper.reshape('تعداد داده‌های خالی')))
    plt.title(get_display(arabic_reshaper.reshape('نمودار داده خراب')))
    plt.xticks(rotation=45) 
    st.pyplot()

def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=[np.number])

    if numeric_df.empty:
        st.warning("هیچ ستون عددی برای تحلیل همبستگی یافت نشد.")
        return

    correlation_matrix = numeric_df.corr()

    try:
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.show()
        st.pyplot()
    except Exception as e:
        st.warning("نمایش نمودار به دلیل مشکلات فنی امکانپذیر نیست. دلیل: ", e)
    
    
def do_laptop():
    initialize_session_state()
    
    if st.button('آپلود فایل'):
        st.session_state.clicked = True

    if st.session_state.clicked:
        uploaded_file = upload_file()
        if uploaded_file is not None:
            st.session_state.remove = True
            try:
                user_df = pd.read_csv(uploaded_file)
            except Exception as  e:
                st.error(f"این فایل قابل نمایش نیست به دلیل : {e}")
                st.session_state.remove = False
                

    bad_data, clean_data = load_data()
    if not st.session_state.remove:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3 style='color:red;direction: rtl;'>نمونه داده ناسالم(نامناسب برای یادگیری ماشین)</h3>", unsafe_allow_html=True)
            
            st.write(bad_data.head())

            show_chart_bad = st.checkbox("نمایش نمودار")
            
            if show_chart_bad:
                st.header("نمودار داده ناسالم")
                column_name_bad = st.selectbox("ستون را مشخص کنید", list(bad_data.columns))
                
                st.set_option('deprecation.showPyplotGlobalUse', False)  
                fig_bad, ax_bad = plt.subplots(figsize=(9, 7))
                
                sns.countplot(x=column_name_bad, data=bad_data)

                ax_bad.tick_params(axis='x', rotation=80)
                st.pyplot(fig_bad)

        with col2:
            st.markdown("<h3 style='color:green;direction: rtl;'>نمونه داده سالم(پردازش شده)</h3>", unsafe_allow_html=True)        
            st.write(clean_data.head())

            show_chart_clean = st.checkbox("نمایش نمودار داده صحیح")
            
            if show_chart_clean:
                st.header("نمودار داده صحیح")
                column_name_clean = st.selectbox("ستون را مشخص کنید", list(clean_data.columns))
                
                st.set_option('deprecation.showPyplotGlobalUse', False)  
                fig_clean, ax_clean = plt.subplots(figsize=(9, 7))
                
                sns.countplot(x=column_name_clean, data=clean_data)

                ax_clean.tick_params(axis='x', rotation=80)
                st.pyplot(fig_clean)
                
    else: 
        col1_U, col2_U = st.columns(2)

        with col2_U:
            
            st.markdown("<div class='custom-button'>", unsafe_allow_html=True)
            if st.button("پردازش"):
                st.write('sssssssssss')
            else:
                st.write("برای پردازش فایل بارگزاری شده خود لطفا بر روری دکمه 'پردازش' کلیک کنید")
            st.markdown("</div>", unsafe_allow_html=True)


        with col1_U:
            st.markdown("<h3 style='color:blue;direction: rtl;'>داده بارگزاری شده توسط کاربر</h3>", unsafe_allow_html=True)

            st.write(user_df.head())
        # check_box_1, check_box_2, check_box_3, check_box_4= st.columns(4)
        
        # with check_box_1:
        #     show_chart_U = st.checkbox("نمایش نمودار")
        #     if show_chart_U:
        #         column_name_U = st.selectbox("", list(user_df.columns))

        #         st.set_option('deprecation.showPyplotGlobalUse', False)  
        #         fig_u, ax_u = plt.subplots(figsize=(9, 7))

        #         sns.countplot(x=column_name_U, data=user_df)

        #         ax_u.tick_params(axis='x', rotation=90)
        #         st.pyplot(fig_u)
        # with check_box_2:
        #     show_empty_values = st.checkbox("نمایش تعداد داده‌های خالی")

        #     if show_empty_values:
        #         empty_values = count_empty_values(user_df)
        #         st.write(empty_values)
                
        # with check_box_3:    
        #     show_heatmap = st.checkbox("نمایش نمودار هیت‌مپ ماتریس همبستگی")
                
        #     if show_heatmap:
        #         plot_correlation_heatmap(user_df)
            
        # with check_box_4:    
        #             show_bad_data = st.checkbox("نمودار داده خراب")
        #             if show_bad_data:
        #                 plot_bad_data_chart(user_df)






def do_estimation_us():
    st.markdown('### House Price Estimation (USA)')
    input = st.text_input("text", key="text")

    def clear_text():
        st.session_state["text"] = ""
        
    st.button("clear text input", on_click=clear_text)
    st.write(input)

def do_estimation_iran():
    st.markdown('### House Price Estimation (Iran)')

def do_about_us():
    st.markdown('### About Us')

menu = {
    'items': { 
        'خانه': {'action': do_home, 'item_icon': 'house-door-fill', 'submenu': None},
        'تخمین قیمت لپ تاپ': {'action': do_laptop, 'item_icon': 'laptop-fill', 'submenu': None},
        'تخمین قیمت خانهUS': {'action': do_estimation_us, 'item_icon': 'house-fill', 'submenu': None},
        'تخمین قیمت خانهIR': {'action': do_estimation_iran, 'item_icon': 'house-door-fill', 'submenu': None},
        'درباره ما': {'action': do_about_us, 'item_icon': 'info-circle-fill', 'submenu': None},
    },  
    'menu_icon': 'bi bi-cash-coin',
    'default_index': 0,
    'with_view_panel': 'main',
    'orientation': 'horizontal',
    'styles': {
        "container": {"margin": "0px !important", "padding": "0!important", "align-items": "stretch", "background-color": "#fafafa", "text-align": "right", "direction": "rtl",},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "right", "direction": "rtl", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"font-size": "20px", "font-weight": "normal", "color": "black" , "text-align": "right", "direction": "rtl",},
    }
}

def show_menu(menu):
    def _get_options(menu):
        options = list(menu['items'].keys())
        return options

    def _get_icons(menu):
        icons = [v['item_icon'] for _k, v in menu['items'].items()]
        return icons


    kwargs = {
        'menu_title': None,  
        'options': _get_options(menu),
        'icons': _get_icons(menu),
        'menu_icon': menu['menu_icon'],
        'default_index': menu['default_index'],
        'orientation': menu['orientation'],
        'styles': menu['styles']
    }

    with_view_panel = menu['with_view_panel']
    if with_view_panel == 'main':
        menu_selection = option_menu(**kwargs)
    else:
        raise ValueError(f"Unknown view panel value: {with_view_panel}. Must be 'main'.")

    if menu['items'][menu_selection]['action']:
        menu['items'][menu_selection]['action']()

show_menu(menu)
