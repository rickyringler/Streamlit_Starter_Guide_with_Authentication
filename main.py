import pandas as pd
import streamlit as st
import time

'''
ENTER APPLICATION NAME HERE
'''

st.set_page_config(page_title="My App",layout="wide")

def check_password():
    def password_entered():

        progress_text = "Loading. Please wait :)"
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.015)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(5)
        my_bar.empty()

        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("Password is incorrect.")
        return False
    else:
        return True

if check_password():
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:

        '''
        ENTER APPLICATION LOGO HERE
        '''

        st.image("temporary_logo.png")
    with col3:
        st.write("")
    st.markdown("""
                    <html>
                        <head>
                        <style>
                            ::-webkit-scrollbar {
                                width: 15px;
                                }

                                /* Track */
                                ::-webkit-scrollbar-track {
                                background: #f1f1f1;
                                }

                                /* Handle */
                                ::-webkit-scrollbar-thumb {
                                background: #888;
                                }

                                /* Handle on hover */
                                ::-webkit-scrollbar-thumb:hover {
                                background: #555;
                                }
                        </style>
                        </head>
                        <body>
                        </body>
                    </html>
                """, unsafe_allow_html=True)

    '''
    ENTER APPLICATION NAME HERE
    '''
    st.markdown("<h1 style='text-align: center; color: darkslategray;'>ENTER APPLICATION NAME HERE</h1>", unsafe_allow_html=True)

    '''
    ENTER REPORT NAME HERE
    '''

    st.markdown("<h2 style='text-align: center; color: darkslategray;'>ENTER REPORT NAME HERE</h2>", unsafe_allow_html=True)

    '''
    ENTER REPORT FILE HERE
    '''

    report = pd.read_csv("my_data.csv",index_col=0)

    report_options = report["FIELD_NAME"].drop_duplicates()
    report_all_data = report.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Export All Report Data",
        report_all_data,
        "Report All Data.csv",
        "text/csv",
        key="download-tools-report_all_data",
    )
    report_choices = st.selectbox("Select a Value to Filter", report_options)

    if report == "":
        report_export = report_all_data
    else:
        report_export = report.loc[(report["FIELD_NAME"] == report_choices)]

    st.dataframe(report_export)
    report_export = report_export.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Export Selection",
        report_export,
        "Report Data.csv",
        "text/csv",
        key="download-tools-reportdata",
    )
