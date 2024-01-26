import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Price Prediction",
    page_icon=":bar_chart:",
    layout="wide"
)


def main():
    st.title("اپلیکیشن شما")

    # ایجاد یک منو برای صفحه اصلی
    # page_options = ["خانه", "لپتاپ", "تخمین قیمت خانه (آمریکا)", "تخمین قیمت خانه (ایران)", "درباره ما"]
    # selected_page = st.sidebar.selectbox("انتخاب صفحه", page_options)
    
    selected_page = st.sidebar.radio("انتخاب صفحه", ["خانه", "لپتاپ", "تخمین قیمت خانه (آمریکا)", "تخمین قیمت خانه (ایران)", "درباره ما"])


    # نمایش محتوای مربوط به هر صفحه
    if selected_page == "خانه":
        show_home_page()
    elif selected_page == "لپتاپ":
        show_laptop_page()
    elif selected_page == "تخمین قیمت خانه (آمریکا)":
        show_us_home_price_page()
    elif selected_page == "تخمین قیمت خانه (ایران)":
        show_iran_home_price_page()
    elif selected_page == "درباره ما":
        show_about_us_page()

def show_home_page():
    st.header("خانه")
    # افزودن محتوای صفحه اصلی

def show_laptop_page():
    st.header("لپتاپ")
    # افزودن محتوای صفحه لپتاپ

def show_us_home_price_page():
    st.header("تخمین قیمت خانه (آمریکا)")
    # افزودن محتوای صفحه تخمین قیمت خانه در آمریکا

def show_iran_home_price_page():
    st.header("تخمین قیمت خانه (ایران)")
    
    # افزودن محتوای صفحه تخمین قیمت خانه در ایران

def show_about_us_page():
    st.header("درباره ما")
    # افزودن محتوای صفحه درباره ما

if __name__ == "__main__":
    main()

