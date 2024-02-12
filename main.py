import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pip install plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
import plotly.express as px
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import time
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
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
        [data-testid="stNotificationContentInfo"]{direction: rtl;text-align: right;font-weight: 900;}
        
        [data-testid="InputInstructions"] { display: None; } 
        
        div[data-testid="stSelectbox"]{
            width: 70% !important;
            margin: 0 auto !important;
        }
        
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
    plt.xlabel(get_display(arabic_reshaper.reshape('ستون‌ها')))  
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

def show_other_chart(user_df):
    
    show_chart_U = st.checkbox("نمایش نمودار")
    if show_chart_U:
        column_name_U = st.selectbox("", list(user_df.columns))

        st.set_option('deprecation.showPyplotGlobalUse', False)  
        fig_u, ax_u = plt.subplots(figsize=(9, 7))

        sns.countplot(x=column_name_U, data=user_df)

        ax_u.tick_params(axis='x', rotation=90)
        st.pyplot(fig_u)
        
        
    show_empty_values = st.checkbox("نمایش تعداد داده‌های خالی")

    if show_empty_values:
        empty_values = count_empty_values(user_df)
        st.bar_chart(empty_values)
        # st.write(empty_values)
            
    show_heatmap = st.checkbox("نمایش نمودار هیت‌مپ ماتریس همبستگی")
        
    if show_heatmap:
        plot_correlation_heatmap(user_df)
        
    show_bad_data = st.checkbox("نمودار داده خراب")
    if show_bad_data:
        plot_bad_data_chart(user_df)

def load_data(type_data):
    clean_data = pd.read_csv(f"CSV_data\\clean_data_{type_data}.csv", encoding='latin1')
    
    if type_data == 'home_IR':
        bad_data = pd.read_csv(f"CSV_data\\bad_data_{type_data}.csv")
    else:
        bad_data = pd.read_csv(f"CSV_data\\bad_data_{type_data}.csv", encoding='latin1')
        
    return bad_data, clean_data


def initialize_session_state():
    # TODO زمانی که کاربر tab جدید میشود همه session ها باید خالی باشد
    if 'remove' not in st.session_state:
        st.session_state.remove = False
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
    if 'show_chart' not in st.session_state:
        st.session_state.show_chart = False
    if 'prediction' not in st.session_state:
        st.session_state.prediction = False


def do_laptop():
        
        
    initialize_session_state() 
    bad_data, clean_data = load_data('laptop')

    if st.button("تخمین قیمت "):
        st.session_state.prediction = True
        
    if st.session_state.prediction:
        x = clean_data.drop('Price_euros', axis=1)
        y = clean_data['Price_euros']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)
        scaler = StandardScaler()
        x_train_scaled = scaler.fit_transform(x_train)
        x_test_scaled = scaler.transform(x_test)

        forest = RandomForestRegressor()
        forest.fit(x_train_scaled, y_train)
        
        os_category = st.selectbox('نوع سیستم عامل', ['Windows', 'Linux', 'No OS'])
        company_category = st.selectbox('شرکت سازنده لپ تاپ', ['Acer', 'Razer', 'MSI'])
        windows_selected = 1 if os_category == 'Windows' else 0
        linux_selected = 1 if os_category == 'Linux' else 0
        no_os_selected = 1 if os_category == 'No OS' else 0
        
        
        cpu_category = st.selectbox('شرکت سازنده پردازنده', ['ADM', 'Intel'])
        gpu_category = st.selectbox('شرکت سازنده کارت گرافیک', ['NVIDIA', 'Intel', 'ADM'])
        laptop_type = st.selectbox('نوع لپ تاپ', ['Workstation','Ultrabook','Gaming','Notebook'])
        
        acer_selected = razer_selected = msi_selected = 0
        amd_selected = intel_selected = 0
        nvidia_selected = intel_gpu_selected = amd_gpu_selected = 0
        workstation_selected = ultrabook_selected = gaming_selected = notebook_selected = 0

        if company_category == 'Acer':
            acer_selected = 1
        elif company_category == 'Razer':
            razer_selected = 1
        elif company_category == 'MSI':
            msi_selected = 1

        if cpu_category == 'AMD':
            amd_selected = 1
        elif cpu_category == 'Intel':
            intel_selected = 1

        if gpu_category == 'NVIDIA':
            nvidia_selected = 1
        elif gpu_category == 'Intel':
            intel_gpu_selected = 1
        elif gpu_category == 'AMD':
            amd_gpu_selected = 1

        if laptop_type == 'Workstation':
            workstation_selected = 1
        elif laptop_type == 'Ultrabook':
            ultrabook_selected = 1
        elif laptop_type == 'Gaming':
            gaming_selected = 1
        elif laptop_type == 'Notebook':
            notebook_selected = 1
        
        
        weight = st.selectbox('وزن', [1.37, 1.83, 1.37])
        screen_height = st.selectbox('ارتفاع صفحه نمایش (پیکسل)', sorted(clean_data['Screen Height'].unique()))
        screen_width = st.selectbox('عرض صفحه (پیکسل)', sorted(clean_data['Screen Width'].unique()))
        ram = st.selectbox('رم (GB)', sorted(clean_data['Ram'].unique()))
        cpu_frequency = st.selectbox('CPU فرکانس (GHz)', [1.8, 3.1, 2.3])
        
        
        user_input = pd.DataFrame({
            'Windows': [windows_selected],
            'Linux': [linux_selected],
            'No OS': [no_os_selected],
            'MSI': [msi_selected],
            'AMD CPU': [amd_selected],
            'Intel CPU': [intel_selected],
            'Intel GPU': [intel_gpu_selected],
            'AMD GPU': [amd_gpu_selected],
            'Acer': [acer_selected],
            'Weight': [weight],
            'Razer': [razer_selected],
            'Workstation': [workstation_selected],
            'Ultrabook': [ultrabook_selected],
            'Nvidia GPU': [nvidia_selected],
            'Gaming': [gaming_selected],
            'CPU Frequency': [cpu_frequency],
            'Notebook': [notebook_selected],
            'Screen Height (Pixels)': [screen_height],
            'Screen Width (Pixels)': [screen_width],
            'Ram (GB)': [ram]
        })
        
        user_input.columns = x.columns

        user_input_scaled = scaler.transform(user_input)

        predicted_price = forest.predict(user_input_scaled)
        st.write(f'قیمت تخمینی لپ تاپ: {predicted_price[0]:,.2f} یورو')
        
        y_pred = forest.predict(x_test_scaled)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # نمایش معیارهای دقت
        st.write(f'خطای میانگین مطلق: {mae:,.2f} یورو')
        st.write(f'خطای میانگین مربعات: {mse:,.2f} یورو')
        st.write(f'{r2:.4f} : R-squared (R2) امتیاز ')

        # محاسبه درصد دقت
        دقت_درصدی = forest.score(x_test_scaled, y_test) * 100
        st.write(f'{دقت_درصدی:.2f}% : دقت مدل ')


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
                
                
    if st.session_state.remove:
        col1_U, col2_U = st.columns(2)

        with col2_U:
            
            
            
            st.markdown("<div class='custom-button'>", unsafe_allow_html=True)

            if "show_other_chart" not in st.session_state:
                st.session_state.show_other_chart = False

            if st.button("پردازش"):
                st.session_state.show_other_chart = True

            if st.session_state.show_other_chart:
                st.info("این بخش به دلیل اینکه فایل بارگزاری شده آموزش مدل ها یادگیری ماشین ارتباط مستقیمی با داده های آموزش دیده دارد باید توسط ادمین مورد ارزیابی قرار بگیرد ")
                st.info("شما می‌توانید برای دیدن نمودارهای بیشتر از فایل خود کلیک کنید")
                with st.expander("نمایش نمودار"):
                    show_other_chart(user_df)
                    
            else:
                st.write("برای پردازش فایل بارگزاری شده خود لطفا بر روی دکمه 'پردازش' کلیک کنید")

            st.markdown("</div>", unsafe_allow_html=True)



        with col1_U:
            st.markdown("<h3 style='color:blue;direction: rtl;'>داده بارگزاری شده توسط کاربر</h3>", unsafe_allow_html=True)

            st.write(user_df.head())
            

def check(df):
    l=[]
    columns=df.columns
    for col in columns:
        dtypes=df[col].dtypes
        nunique=df[col].nunique()
        sum_null=df[col].isnull().sum()
        l.append([col,dtypes,nunique,sum_null])
    df_check=pd.DataFrame(l)
    df_check.columns=['column','dtypes','nunique','sum_null']
    return df_check 


def do_estimation_iran():
    initialize_session_state() 
    bad_data, clean_data = load_data('home_IR')
    

    if st.button("تخمین قیمت "):
        st.session_state.prediction = True
        
    if st.session_state.prediction:
        X = clean_data.drop(['rent','deposit'],axis=1)
        Y = clean_data.pop('all_to_deposit')

        
        regression_tree_houses = DecisionTreeRegressor()

        X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=0)
        regression_tree_houses.fit(X_train, y_train)
        def format_func(value):
            return int(value)
        

        
        region_user = st.selectbox('طبقه ساختمانی که خانه در آن قرار دارد',
                             sorted(region.unique()))
        region_user_index = df1[region == region_user].index[0]
        region_user_address = df1.at[region_user_index, 'address']
        
        floor = st.selectbox('طبقه ساختمانی که خانه در آن قرار دارد',
                             sorted(clean_data['floor'].unique()),
                             format_func=format_func,
                             help='عدد 0 نشان دهنده طبقه همکف است')
        
        area = st.selectbox('مساحت خانه براساس متر مربع',
                            sorted(clean_data['area'].unique()),
                            format_func=format_func)
        
        age = st.selectbox('سن خانه(چند سال از ساخت خانه میگذرد )',
                           sorted(clean_data['age'].unique()),
                           format_func=format_func,
                           help='عدد 0 نشان دهنده این است که سن این خانه هنوز به یکسال هم نرسیده است')
        
        rooms = st.selectbox('تعداد اتاق های خانه',
                            sorted(clean_data['rooms'].unique()),
                            format_func=format_func)
        
        elavator = st.selectbox('وجود آسانسور در خانه', ['وجود دارد ', 'وجود ندارد'])
        elavator = 1 if elavator == 'وجود دارد ' else 0

        parking = st.selectbox('وجود پارکینگ در خانه', ['وجود دارد ', 'وجود ندارد'])
        parking = 1 if parking == 'وجود دارد ' else 0
        
        Warehouse = st.selectbox('وجود انبار در خانه', ['وجود دارد ', 'وجود ندارد'], )
        Warehouse = 1 if Warehouse == 'وجود دارد ' else 0
        st.write(X_test)
        y_pred_tree = regression_tree_houses.predict(X_test)
        st.write(f'r2_score: {metrics.r2_score(y_test,y_pred_tree)}')
        st.write(f'explained_variance_score: {metrics.explained_variance_score(y_test,y_pred_tree)}')
        st.write(f'mean_squared_error: {metrics.mean_squared_error(y_test,y_pred_tree)}')
        st.write(f'mean_absolute_error: {metrics.mean_absolute_error(y_test,y_pred_tree)}')
        
        
        user_input = pd.DataFrame({
            'address': [region_user_address],
            'floor': [floor],
            'area': [area],
            'age': [age],
            'rooms': [rooms],
        })
        
        # user_input.columns = X.columns

        # user_input_scaled = regression_tree_houses.transform(user_input)

        # predicted_price = regression_tree_houses.predict(user_input_scaled)
        # st.write(f'قیمت تخمینی لپ تاپ: {predicted_price[0]:,.2f} یورو')
        
        # y_pred = regression_tree_houses.predict(X_test)

        # mae = mean_absolute_error(y_test, y_pred)
        # mse = mean_squared_error(y_test, y_pred)
        # r2 = r2_score(y_test, y_pred)

        # نمایش معیارهای دقت
        # st.write(f'خطای میانگین مطلق: {mae:,.2f} یورو')
        # st.write(f'خطای میانگین مربعات: {mse:,.2f} یورو')
        # st.write(f'{r2:.4f} : R-squared (R2) امتیاز ')

        # # محاسبه درصد دقت
        # دقت_درصدی = regression_tree_houses.score(X_test, y_test) * 100
        # st.write(f'{دقت_درصدی:.2f}% : دقت مدل ')






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
                
                
    if st.session_state.remove:
        col1_U, col2_U = st.columns(2)

        with col2_U:
            
            
            
            st.markdown("<div class='custom-button'>", unsafe_allow_html=True)

            if "show_other_chart" not in st.session_state:
                st.session_state.show_other_chart = False

            if st.button("پردازش"):
                st.session_state.show_other_chart = True

            if st.session_state.show_other_chart:
                st.info("این بخش به دلیل اینکه فایل بارگزاری شده آموزش مدل ها یادگیری ماشین ارتباط مستقیمی با داده های آموزش دیده دارد باید توسط ادمین مورد ارزیابی قرار بگیرد ")
                st.info("شما می‌توانید برای دیدن نمودارهای بیشتر از فایل خود کلیک کنید")
                with st.expander("نمایش نمودار"):
                    show_other_chart(user_df)
                    
            else:
                st.write("برای پردازش فایل بارگزاری شده خود لطفا بر روی دکمه 'پردازش' کلیک کنید")

            st.markdown("</div>", unsafe_allow_html=True)



        with col1_U:
            st.markdown("<h3 style='color:blue;direction: rtl;'>داده بارگزاری شده توسط کاربر</h3>", unsafe_allow_html=True)

            st.write(user_df.head())
            
            

def do_estimation_us():
    initialize_session_state() 
    bad_data, clean_data = load_data('home_US')
    
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
                
                
    if st.session_state.remove:
        col1_U, col2_U = st.columns(2)

        with col2_U:
            
            
            
            st.markdown("<div class='custom-button'>", unsafe_allow_html=True)

            if "show_other_chart" not in st.session_state:
                st.session_state.show_other_chart = False

            if st.button("پردازش"):
                st.session_state.show_other_chart = True

            if st.session_state.show_other_chart:
                st.info("این بخش به دلیل اینکه فایل بارگزاری شده آموزش مدل ها یادگیری ماشین ارتباط مستقیمی با داده های آموزش دیده دارد باید توسط ادمین مورد ارزیابی قرار بگیرد ")
                st.info("شما می‌توانید برای دیدن نمودارهای بیشتر از فایل خود کلیک کنید")
                with st.expander("نمایش نمودار"):
                    show_other_chart(user_df)
                    
            else:
                st.write("برای پردازش فایل بارگزاری شده خود لطفا بر روی دکمه 'پردازش' کلیک کنید")

            st.markdown("</div>", unsafe_allow_html=True)



        with col1_U:
            st.markdown("<h3 style='color:blue;direction: rtl;'>داده بارگزاری شده توسط کاربر</h3>", unsafe_allow_html=True)

            st.write(user_df.head())


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
