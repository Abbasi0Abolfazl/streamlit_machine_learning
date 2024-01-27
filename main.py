import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Estimator - تخمینگر",
    page_icon=":bar_chart:",
    layout="wide"
)

st.markdown("""
    <style>
        body {
            direction: rtl;
            text-align: right;
            font-size: 30px;
        }

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
# Estimator - تخمینگر

## توضیحات

سایت "Estimator - تخمینگر" یک اپلیکیشن وب است که برای تخمین قیمت‌ها با استفاده از مدل‌های یادگیری ماشین ایجاد شده است. کاربران می‌توانند از این سایت برای تخمین قیمت لپ تاپ، خانه در ایالات متحده، خانه در ایران، و همچنین بازار سهام استفاده کنند.

## استفاده از فایل CSV

برای آموزش مدل‌های یادگیری ماشین، از یک فایل CSV به نام "training_data.csv" استفاده شده است. این فایل حاوی داده‌های آموزشی است که بر اساس آن مدل‌های یادگیری ماشین ساخته شده‌اند. کاربران می‌توانند مشاهده را کلیک کنند تا فایل را مشاهده کرده و در صورت نیاز، فایل خود را بارگیری کنند.

## تخمین‌های ممکن

سایت امکان تخمین قیمت برای چهار دسته اصلی را فراهم می‌کند:

1. **تخمین قیمت لپ تاپ**
2. **تخمین قیمت خانه در ایالات متحده**
3. **تخمین قیمت خانه در ایران**
4. **تخمین قیمت بازار سهام**

## نحوه استفاده

برای استفاده از سایت، کاربران مراحل زیر را انجام می‌دهند:

1. اگر تمایل دارند، فایل CSV آموزشی را مشاهده و یا فایل خود را بارگیری می‌کنند.
2. برای هر قسمت از تخمین (لپ تاپ، خانه در ایالات متحده، خانه در ایران یا بازار سهام)، ویژگی‌های مورد نظر را وارد می‌کنند.
3. سپس، سایت براساس ویژگی‌های وارد شده، قیمت تخمین زده شده توسط مدل یادگیری ماشین را اعلام می‌کند.

## اجزای پروژه

پروژه از Streamlit برای ساخت این اپلیکیشن وب استفاده کرده است. از مدل‌های یادگیری ماشین بر اساس داده‌های آموزشی بهینه‌سازی شده‌اند.

""")
    st.markdown("""
#### هدف این سایت ارائه یک ابزار کاربردی برای تخمین قیمت محصولات و دارایی‌ها با استفاده از یادگیری ماشین است.
#### این سایت برای کاربرانی طراحی شده است که می‌خواهند قیمت محصولات و دارایی‌ها را بدون نیاز به داشتن دانش تخصصی در زمینه یادگیری ماشین تخمین بزنند.
                """)
    

def do_laptop():    
    training_data = pd.read_csv("training_data.csv", encoding='latin1')

    st.markdown("<h3 style='color:red;'>نمونه داده ناسالم(نامناسب برای یادگیری ماشین)</h3>", unsafe_allow_html=True)
    st.write(training_data.head())
    
    st.markdown("<h3 style='color:red;'>نمونه داده ناسالم(نامناسب برای یادگیری ماشین)</h3>", unsafe_allow_html=True)
    
    




def do_estimation_us():
    st.markdown('### House Price Estimation (USA)')

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
