import time
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns

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

        .stHeadingContainer {text-align: center !important}
        
        [data-testid="InputInstructions"] { display: None; } 
        
    </style>

""", unsafe_allow_html=True)
        # .st-emotion-cache-zt5igj{color: red;}




    
    
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

        
def load_data():
    bad_data = pd.read_csv(r"CSV_data\bad_data.csv", encoding='latin1')
    clean_data = pd.read_csv(r"CSV_data\clean_data.csv", encoding='latin1')
    return bad_data, clean_data

def do_laptop():
    bad_data, clean_data = load_data()

    st.markdown("<h3 style='color:red;direction: rtl;'>نمونه داده ناسالم(نامناسب برای یادگیری ماشین)</h3>", unsafe_allow_html=True)
    st.write(bad_data.head())

    show_chart = st.checkbox("نمایش نمودار")

    if show_chart:
            st.header("نمودار داده ناسالم")
            column_name_bad = st.selectbox("ستون را مشخص کنید", list(bad_data.columns))
            
            st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable deprecation warning
            fig_bad, ax_bad = plt.subplots(figsize=(9, 7))
            
            sns.countplot(x=column_name_bad, data=bad_data, ax=ax_bad)

            ax_bad.tick_params(axis='x', rotation=80)
            st.markdown(f'<img src="data:image/png;base64,{chart_to_base64(fig_bad)}" style="width: auto;">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:green;direction: rtl;'>فایل مورد استفاده صحیح برای Train (تمرین دادن)  ماشین که این فایل پردازش و اصلاح شده</h3>",
                unsafe_allow_html=True)

    st.markdown("<h3 style='color:green;direction: rtl;'>فایل مورد استفاده صحیح برای Train (تمرین دادن)  ماشین که این فایل پردازش و اصلاح شده</h3>", unsafe_allow_html=True)
    st.write(clean_data.head())

    show_chart = st.checkbox("نمایش نمودار داده صحیح")

    if show_chart:
            st.header("نمودار داده صحیح")
            column_name_clean = st.selectbox("ستون را مشخص کنید", list(clean_data.columns))
            
            st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable deprecation warning
            fig_bad, ax_bad = plt.subplots(figsize=(9, 7))
            
            sns.countplot(x=column_name_clean, data=clean_data, ax=ax_bad)

            ax_bad.tick_params(axis='x', rotation=80)
            st.markdown(f'<img src="data:image/png;base64,{chart_to_base64(fig_bad)}" style="width: auto;">', unsafe_allow_html=True)
            


# def uppppp():

#     uploaded_file = st.file_uploader("Choose a file")
#     print(uploaded_file)
#     if uploaded_file is not None:
#         st.write("You selected the file:", uploaded_file.name)
#         df = pd.read_csv(uploaded_file)
#         return df

# def do_estimation_us():
#     st.markdown('### House Price Estimation (USA)')
#     if 'clicked' not in st.session_state:
#         st.session_state.clicked = False
#     st.button('Upload File', on_click=set_clicked)
#     if st.session_state.clicked:
#         df = uppppp()
#         if df is not None:
#             st.write(df)



def upload_file():
    uploaded_file = st.file_uploader("Choose a file")
    return uploaded_file

def do_estimation_us():
    st.markdown('### House Price Estimation (USA)')
    
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    # Use st.button with on_click callback to handle the file upload
    if st.button('Upload File'):
        st.session_state.clicked = True

    # Check if the button is clicked and perform the file upload
    if st.session_state.clicked:
        uploaded_file = upload_file()

        # Process the uploaded file
        if uploaded_file is not None:
            st.write("You selected the file:", uploaded_file.name)
            try:
                df = pd.read_csv(uploaded_file)
                st.write(df)
            except Exception as  e:
                
                st.error(f"این فایل قابل نمایش نیست به دلیل : {e}")



            
            

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
