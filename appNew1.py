from newUserDasboard import newUserDashboard
import streamlit as st

from visual_ai_react_ui import visual_ai_react_main
from mockedData import mockDataNewWireframe2, data1
import pandas as pd
import numpy as np
import altair as alt
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
        .main > div {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
"""

st.markdown(page_css, unsafe_allow_html=True)

visual_ai_react_main("myDashboardHeader")
col1,col2,col3 = st.columns([1.25,5,1.5])
with col1:
    visual_ai_react_main("myDashboardReports")
with col2:
    visual_ai_react_main("myDashboardQuery")
    dataFrameDict = {}
    x_axis_data = []
    y_axis_data = []
    if(data1['response_data']['metrics'][0]['zvalue'] is None):
        for item in data1['response_data']['metrics']:
            x_axis_data.append(item.get('xvalue'))
        x_axis_data = list(dict.fromkeys(x_axis_data))
        x_axis_data.sort()
        dataFrameDict["Claim status"] = x_axis_data
        for status in x_axis_data:
            for metric in data1['response_data']['metrics']:
                if(metric.get('xvalue') == status):
                    if(metric.get('yvalue') is not None):
                        y_axis_data.append(int(metric.get('yvalue')))
                    else:
                        y_axis_data.append(0)
        dataFrameDict["value"] = y_axis_data
        df = pd.DataFrame(dataFrameDict)
    subCol1, subCol2 = col2.columns([1,1])
    with subCol1:
        chart_data = alt.Chart(df).encode(
            x=alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
            y=alt.Y('value:Q'),
            text=alt.Y('value:Q')
        ).properties(width= 400, height = 250)
        st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
        # st.altair_chart(chart_data.mark_line() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
        labels = dataFrameDict['Claim status']
        sizes = dataFrameDict['value']
        explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    with subCol2: 
        # chart_data = alt.Chart(df).encode(
        # x=alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
        # y=alt.Y('value:Q'),
        # text=alt.Y('value:Q')
        # ).properties(width= 400, height = 250)
        # st.altair_chart(chart_data.mark_line() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))
        # st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15))

        dataFrameDict = {}
        x_axis_data = []
        variables = []
        for item in mockDataNewWireframe2['response_data']['metrics']:
            x_axis_data.append(item.get('datevalue'))
        dataFrameDict["Month"] = x_axis_data
        for variable in mockDataNewWireframe2['response_data']['variables']:
            variables.append(variable)
            dataFrameDict[variable] = []
        for variable in variables:
            for item in mockDataNewWireframe2['response_data']['metrics']:
                dataFrameDict[variable].append(item.get(variable))

        data = pd.DataFrame(dataFrameDict)
        prediction_table = pd.melt(data, id_vars=['Month'], value_vars=variables)
        chart = alt.Chart(prediction_table).mark_line(
                opacity=1,
                ).encode(
                x = alt.X('Month:O', axis=alt.Axis(labelAngle=0)),
                y = alt.Y('value:Q'),
                color = alt.Color('variable:N')
            ).properties(width=400, height=250)
        st.altair_chart(chart)

        chart = alt.Chart(prediction_table).encode(
        x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),
        y = alt.Y('value:Q'),
        color = alt.Color('variable:N'),
        text= alt.Y('value:Q'),
        column=alt.Column('Month:N', title="", spacing =0),
        ).properties(width=50)
        st.altair_chart(chart.mark_bar(strokeWidth=10))

with col3:
    visual_ai_react_main("myDashboardAIInsights")
    