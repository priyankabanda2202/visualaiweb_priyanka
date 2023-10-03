from visual_ai_react_ui import visual_ai_react_main
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import requests
from urllib.parse import quote

import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
page_css = """
    <style>
        [data-testid="stHeader"]{
            background: white;
            height: 0rem
        }
        [data-testid="stAppViewContainer"]{
            background: white;
        }
        [data-testid="stVerticalBlock"]{
            gap: 0rem
        }
        .main > div {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
"""

st.markdown(page_css, unsafe_allow_html=True)

if "prompt" not in st.session_state:
    st.session_state.prompt = None

if "api_response" not in st.session_state:
    st.session_state.api_response = None

def show_graph(promp):
    st.session_state.show_graph = True
    # qstr = quote(promp)
    # resp = requests.get("http://10.189.108.234:8084/visualai?query="+qstr)
    resp = requests.post("http://10.189.108.25:8084/visualai",json=promp,headers={"Content-Type": "application/json"})
    if resp:
        st.session_state.api_response = resp.json()
    with col3:
        # if st.session_state.api_response:
        if resp:
            visual_ai_react_main("myDashboardAIInsights",resp.json()['response_data']['insights'])


if st.session_state.prompt is None:
    propmt = visual_ai_react_main("welcome")
    st.session_state.prompt = propmt

else:
    visual_ai_react_main("myDashboardHeader")
    col1,col2,col3 = st.columns([1.25,5,1.5])
    with col1:
        visual_ai_react_main("myDashboardReports")
    # with col3:
        # if st.session_state.api_response:
        #     visual_ai_react_main("myDashboardAIInsights",st.session_state.api_response['response_data']['insights'])
    with col2:
        promp = visual_ai_react_main("myDashboardQuery")
        dataFrameDict = {}
        x_axis_data = []
        y_axis_data = []
        variables = []
        show_graph(promp)
        if "api_response" in st.session_state:
            response = st.session_state.api_response
            subCol1, subCol2 = col2.columns([1,1])

            # This if condition is for data coming with xvalue, yvalue and zvalue. zvalue expected to be None
            if(response and response['response_data'] and 'variables' not in response['response_data'] and response['response_data']['metrics'][0]['zvalue'] is None):
            # if('variables' not in response['response_data'] and response['response_data']['metrics'][0]['zvalue'] is None):
                for item in response['response_data']['metrics']:
                    x_axis_data.append(item.get('xvalue'))
                x_axis_data = list(dict.fromkeys(x_axis_data))
                x_axis_data.sort()
                dataFrameDict[" "] = x_axis_data
                for status in x_axis_data:
                    for metric in response['response_data']['metrics']:
                        if(metric.get('xvalue') == status):
                            if(metric.get('yvalue') is not None):
                                y_axis_data.append(int(metric.get('yvalue')))
                            else:
                                y_axis_data.append(0)
                dataFrameDict["value"] = y_axis_data
                df = pd.DataFrame(dataFrameDict)
                with subCol1:
                    chart_data = alt.Chart(df).encode(
                    x=alt.X(' :O', axis=alt.Axis(labelAngle=0)),
                    y=alt.Y('value:Q'),
                    text=alt.Y('value:Q'),
                    color=alt.value('#481BAE')
                    ).properties(width= 550, height = 400)
                    st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
                    # st.altair_chart(chart_data.mark_line() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
                with subCol2:
                    labels = dataFrameDict[' ']
                    sizes = dataFrameDict['value']
                    # explode = (0, x0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
                    # plt.figure(figsize=(2, 2))
                    # plt.pie(sizes, labels=labels, radius=1)
                    # plt.axis('equal')
                    # st.pyplot(plt)
                    colors = ["#481BAE", "#87C9F2", "#53B8B9"]
                    fig1, ax1 = plt.subplots(figsize=(15, 9))

                    patches, text = ax1.pie(sizes, shadow=False, startangle=90, radius=1)
                    labelsq = [f'{l}, {s}' for l, s in zip(labels, sizes)]
                    ax1.legend(patches, labelsq, loc="lower right")
                    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                    st.pyplot(fig1)


            # This condition is for trend analysis graphs that have variables defined
            elif(response and response['response_data'] and 'variables' in response['response_data']):
                for item in response['response_data']['metrics']:
                    x_axis_data.append(item.get('claim completion month adj'))
                dataFrameDict["Month"] = x_axis_data
                for variable in response['response_data']['variables']:
                    variables.append(variable)
                    dataFrameDict[variable] = []
                for variable in variables:
                    for item in response['response_data']['metrics']:
                        dataFrameDict[variable].append(item.get(variable))
                with subCol1:
                    data = pd.DataFrame(dataFrameDict)
                    prediction_table = pd.melt(data, id_vars=['Month'], value_vars=variables)
                    chart = alt.Chart(prediction_table).mark_line(
                            opacity=1,
                            ).encode(
                            x = alt.X('Month:O', axis=alt.Axis(labelAngle=0)),
                            y = alt.Y('value:Q'),
                            color = alt.Color('variable:N')
                        ).properties(width=550, height=450)
                    st.altair_chart(chart)
                with subCol2:
                    chart = alt.Chart(prediction_table).encode(
                    x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),
                    y = alt.Y('value:Q'),
                    color = alt.Color('variable:N'),
                    text= alt.Y('value:Q'),
                    column=alt.Column('Month:N', title="", spacing =0),
                    ).properties(width=80)
                    st.altair_chart(chart.mark_bar(strokeWidth=10))
            
            # with subCol1:
            #     chart_data = alt.Chart(df).encode(
            #         x=alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
            #         y=alt.Y('value:Q'),
            #         text=alt.Y('value:Q')
            #     ).properties(width= 400, height = 250)
            #     st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
            #     # st.altair_chart(chart_data.mark_line() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
            #     labels = dataFrameDict['Claim status']
            #     sizes = dataFrameDict['value']
            #     explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            #     fig1, ax1 = plt.subplots()
            #     ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            #             shadow=True, startangle=90)
            #     ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            #     st.pyplot(fig1)

            # with subCol2: 
            #     # chart_data = alt.Chart(df).encode(
            #     # x=alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
            #     # y=alt.Y('value:Q'),
            #     # text=alt.Y('value:Q')
            #     # ).properties(width= 400, height = 250)
            #     # st.altair_chart(chart_data.mark_line() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
            #     # st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))

            #     data = pd.DataFrame(dataFrameDict)
            #     prediction_table = pd.melt(data, id_vars=['Month'], value_vars=variables)
            #     chart = alt.Chart(prediction_table).mark_line(
            #             opacity=1,
            #             ).encode(
            #             x = alt.X('Month:O', axis=alt.Axis(labelAngle=0)),
            #             y = alt.Y('value:Q'),
            #             color = alt.Color('variable:N')
            #         ).properties(width=400, height=250)
            #     st.altair_chart(chart)

            #     chart = alt.Chart(prediction_table).encode(
            #     x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),
            #     y = alt.Y('value:Q'),
            #     color = alt.Color('variable:N'),
            #     text= alt.Y('value:Q'),
            #     column=alt.Column('Month:N', title="", spacing =0),
            #     ).properties(width=50)
            #     st.altair_chart(chart.mark_bar(strokeWidth=10))



