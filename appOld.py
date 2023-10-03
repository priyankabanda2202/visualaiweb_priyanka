from visual_ai_react_ui import visual_ai_react_main
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from mockedData import mockData
import requests
from urllib.parse import quote
from datetime import datetime, timedelta

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

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

if "access_token" not in st.session_state:
    st.session_state.access_token = None

if "api_response" not in st.session_state:
    st.session_state.api_response = None

if "population_graph" not in st.session_state:
    st.session_state.population_graph = '.'

if "show_graph" not in st.session_state:
    st.session_state.show_graph = False

if "question" not in st.session_state:
    st.session_state.question = ''

if "slider_change" not in st.session_state:
    st.session_state.slider_change = False

if st.session_state.population_graph == '.' and not st.session_state.slider_change: 
    st.session_state.show_graph = False

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

params = st.experimental_get_query_params()
if params:
    print(params)
    st.session_state.access_token = params['accessToken']

def slid_change():
    st.session_state.slider_change = True

def show_graph():
    st.session_state.show_graph = True
    st.session_state.population_graph = str(None)
    qstr = quote(st.session_state.question_input)
    resp = requests.get("http://10.189.108.234:8084/visualai?query="+qstr)
    st.session_state.api_response = resp.json()

start_date = datetime(2023, 1, 1)
end_date = start_date + timedelta(days=364)

if st.session_state.access_token:
    with st.container():
        col1,col2 = st.columns([1,2])
    with col1:
        left_nav = visual_ai_react_main("leftNav")
        if(str(left_nav) == '.'):
            st.session_state.population_graph = str(left_nav)
            st.session_state.slider_change = False
        st.write(left_nav)
        # if st.session_state.show_graph: 
        #     st.write(visual_ai_react_main("insights", st.session_state.api_response['response_data']['insights']))

    with col2:
        st.subheader("Welcome to Claims Metrics Dashboard!")

        question = st.text_input(
            "input",
            label_visibility="hidden",
            disabled=st.session_state.disabled,
            placeholder="How can i help you?",
            on_change=show_graph,
            key="question_input"
        )
        st.session_state.question=question
        st.session_state.population_graph = '.'

        if (st.session_state.population_graph == '.' and not st.session_state.show_graph):
            # st.header("Sample of DTP deep dive metrics")
            st.write('')
            col3,col4 = col2.columns(2)
            
            # with col3:
                
                # st.subheader("Population Volume")
                # df = pd.DataFrame({'population':['Commercial', 'HOST', 'HOME'], 'val':[916305, 787229, 598168]})
                # chart_data = alt.Chart(df).encode(
                #     x=alt.X('val:Q', axis=alt.Axis(labelAngle=0)).axis(None),
                #     y=alt.Y('population:O', axis=alt.Axis(labelAngle=0), stack='center'),
                #     text=alt.Y('val:Q'),
                #     color = alt.Color('population:O', scale=alt.Scale(range=['#1F77B4','#beaed4','#fdc086']), title='', legend=None),
                # ).properties(width= 450, height = 300, )
                # st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=12, xOffset=20))
                
            # with col4:
                # st.subheader("Provider Status")
                # df = pd.DataFrame({'status':['In Network', 'Out of Network'], 'val':[2978336, 323366]})
                # chart_data = alt.Chart(df).encode(
                #     x=alt.X('val:Q', axis=alt.Axis(labelAngle=0)).axis(None),
                #     y=alt.Y('status:O', axis=alt.Axis(labelAngle=0)),
                #     text=alt.Y('val:Q', ),
                #     color = alt.Color('status:O', scale=alt.Scale(range=['#1F77B4','#fdc086']), title='', legend=None),
                # ).properties(width= 450, height = 300, )
                # st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=12, xOffset=20, strokeWidth=500 ))

        if st.session_state.show_graph:
            st.subheader("Claims Summary Metrics")
            chart_data = pd.DataFrame(
            np.random.randn(20, 1),
            columns=['time'])

            response = st.session_state.api_response
            x_axis_data = []
            y_axis_data = []
            dataFrameDict = {}
            states = []

            # def handleSliderChange():
            #     global x_axis_data
            #     global dataFrameDict
            #     global states
            #     sliderStartTime = st.session_state.myslider[0]
            #     sliderEndTime = st.session_state.myslider[1]
            #     if(response['response_data']['metrics'][0]['zvalue'] == None):
            #         dataToaccess = mockData[states[0]]
            #         dataFrameDict["value"] = []
            #         for status in x_axis_data:
            #             count = 0
            #             for date in dataToaccess.get(status): 
            #                 if(datetime.strptime(date, "%d/%m/%y") >= sliderStartTime and datetime.strptime(date, "%d/%m/%y") <= sliderEndTime):
            #                     count = count + 1
            #             dataFrameDict["value"].append(count)
            #         dataFrameDict['Claim status'] = x_axis_data
            #     else:
            #         dataToaccess = mockData
            #         for state in states:
            #             dataFrameDict[state] = []
            #             for status in x_axis_data:
            #                 count = 0
            #                 for date in dataToaccess[state][status]: 
            #                     if(datetime.strptime(date, "%d/%m/%y") >= sliderStartTime and datetime.strptime(date, "%d/%m/%y") <= sliderEndTime):
            #                         count = count + 1
            #                 dataFrameDict[state].append(count)
            #         dataFrameDict['Claim status'] = x_axis_data
            #     return dataFrameDict
                    
            ## Here goes the slider

            # startTime, endTime = st.slider(
            #     "slider",
            #     key="myslider",
            #     min_value=datetime(2022, 1 ,1),
            #     max_value=datetime(2023, 6, 1),
            #     value=(datetime(2022, 1 ,1), datetime(2023, 6, 1)),
            #     label_visibility="hidden",
            #     on_change=slid_change
            # )

            def fetchStateValues(state):
                Y_value = []
                for status in x_axis_data:
                    for metric in response['response_data']['metrics']:
                        if(state == metric.get('zvalue') and status == metric.get('xvalue')):
                            if(metric.get('yvalue') is not None):
                                Y_value.append(int(metric.get('yvalue')))
                            else:
                                Y_value.append(0)
                            break
                return Y_value

            ## This is for details coming from either NY or CA
            if(response['response_data']['metrics'][0]['zvalue'] is None):
                for item in response['response_data']['metrics']:
                    x_axis_data.append(item.get('xvalue'))
                x_axis_data = list(dict.fromkeys(x_axis_data))
                x_axis_data.sort()
                dataFrameDict["Claim status"] = x_axis_data
                if(response['response_desc'].find('NY')):
                    states.append("NY")
                else:
                    states.append("CA")
                for status in x_axis_data:
                    for metric in response['response_data']['metrics']:
                        if(metric.get('xvalue') == status):
                            if(metric.get('yvalue') is not None):
                                y_axis_data.append(int(metric.get('yvalue')))
                            else:
                                y_axis_data.append(0)
                dataFrameDict["value"] = y_axis_data

            ## This is for details coming from both NY and CA
            elif(response['response_data']['metrics'][0]['zvalue'] is not None):
                for item in response['response_data']['metrics']:
                    x_axis_data.append(item.get('xvalue'))
                x_axis_data = list(dict.fromkeys(x_axis_data))
                x_axis_data.sort()
                dataFrameDict["Claim status"] = x_axis_data
                for metric in response['response_data']['metrics']:
                    states.append(metric.get('zvalue'))
                states = list(dict.fromkeys(states))
                for state in states:
                    dataFrameDict[state] = fetchStateValues(state)

            # if(startTime > datetime(2022, 1 ,1) or endTime < datetime(2023, 6, 1)):   
            #     dataFrameDict = handleSliderChange()

            ## Here goes the graph
            if 'value' in dataFrameDict:
                df = pd.DataFrame(dataFrameDict)
                chart_data = alt.Chart(df).encode(
                    x=alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
                    y=alt.Y('value:Q'),
                    text=alt.Y('value:Q')
                ).properties(width= 800, height = 500)
                st.altair_chart(chart_data.mark_bar() + chart_data.mark_text(align='center', fontSize=16, yOffset=-15), use_container_width=True)
                if(len(dataFrameDict['Claim status']) > 1):
                    chart_data = alt.Chart(df).mark_line().encode(
                        x= alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
                        y= alt.Y('value:Q'),
                    ).properties(width= 800, height = 500)
                    st.altair_chart(chart_data, use_container_width=True)
                else:
                    chart_data = alt.Chart(df).mark_circle().encode(
                        x= alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
                        y= alt.Y('value:Q')
                    ).properties(width= 800, height = 500)
                    st.altair_chart(chart_data, use_container_width=True)
            else:
                col3,col4 = col2.columns(2)
                with col3:
                    data = pd.DataFrame(dataFrameDict)
                    prediction_table = pd.melt(data, id_vars=['Claim status'], value_vars=states)
                    chart = alt.Chart(prediction_table).mark_bar().encode(
                        x = alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
                        y = alt.Y('value:Q').stack('zero'),
                        color = alt.Color('variable:N'),
                        order=alt.Order('color_Category_sort_index:Q'),
                        tooltip= ['Claim status', 'value', 'variable']
                    ).properties(height=450)
                    text = alt.Chart(prediction_table).mark_text(dy=10,color='black').encode(
                        x=alt.X('Claim status:O'),
                        y=alt.Y('value:Q').stack('zero'),
                        detail='variable:N',
                        text=alt.Text('value:Q'),
                        order=alt.Order('color_Category_sort_index:Q'),
                        tooltip= ['Claim status', 'value', 'variable']
                    ).properties(height=450)
                    st.altair_chart(chart + text, use_container_width=True)
                    chart = alt.Chart(prediction_table).mark_line(
                        opacity=1,
                        ).encode(
                        x = alt.X('Claim status:O', axis=alt.Axis(labelAngle=0)),
                        y = alt.Y('value:Q'),
                        color = alt.Color('variable:N')
                    ).properties(width=1120)
                    st.altair_chart(chart)
                with col4:
                    chart = alt.Chart(prediction_table).encode(
                        x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),
                        y = alt.Y('value:Q'),
                        color = alt.Color('variable:N'),
                        text= alt.Y('value:Q'),
                        column=alt.Column('Claim status:N', title="", spacing =0),
                    ).properties(width=135)
                    st.altair_chart(chart.mark_bar(strokeWidth=10))
else:
    nav_to('http://10.189.108.234:8083/usermanagement/api/v1/authApi/customLogin?tenantId=visualAiWeb')


# dataFrameDict = {
#     "Date Value": ["Date1", "Date2", "Date3"],
#     "s1Value": [3,4,5],
#     "s2Value": [1,8,10],
#     "s3Value": [20,8,10]
# }