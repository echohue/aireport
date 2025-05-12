import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout = 'wide', initial_sidebar_state='expanded')



df = pd.read_excel('RI_FinancialYearWise (2).xlsx',header = [0,1],skiprows = [2])

financial_year = ['All','FY-2021-22','FY-2022-23','FY-2023-24','FY-2024-25']

selected_year = st.sidebar.selectbox('Select the Year',financial_year)
total_roads = 0
total_ri_done = 0 
total_ri_missed = 0 
total_eligible = 0

for i in financial_year[1:]:
    total_roads+=df[(i,'Total No. of Roads')].sum()
    total_ri_done+=df[(i,'No. of Roads RI(M) Conducted')].sum()
    total_ri_missed+=df[(i,'No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float).sum()
    total_eligible+=df[(i,'No. of Eligible Roads for RI(M)')].sum()

if selected_year == 'All':
    st.sidebar.markdown(f'''
    <div data-testid ="stMetric" style = "background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        margin: 10px 10px 10px 10px;              
        border-radius: 5px;
        border-left: 0.5rem solid #3B1F2B;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                        <span>Total No. of Roads</span>
                        <h2 style = "font-size:32px;">{total_roads}</h2>
                        </div>

''',unsafe_allow_html = True)
    st.sidebar.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        margin: 10px 10px 10px 10px;              
        border-radius: 5px;
        border-left: 0.5rem solid #2E86AB;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                        <span>No of Roads Eligible for RI</span>
                        <h2 style = "font-size:32px;">{ total_eligible}</h2>
                        </div>

''',unsafe_allow_html = True)
    st.sidebar.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        margin: 10px 10px 10px 10px;              
        border-radius: 5px;
        border-left: 0.5rem solid #A23B72;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                        <span>No. of RIs Conducted</span>
                        <h2 style = "font-size:32px;">{total_ri_done}</h2>
                        </div>
''',unsafe_allow_html = True )
    st.sidebar.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        margin: 10px 10px 10px 10px;              
        border-radius: 5px;
        border-left: 0.5rem solid #F18F01;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                        <span>No. of RIs Missed</span>
                        <h2 style = "font-size:32px;">{total_ri_missed}</h2>
                        </div>
''',unsafe_allow_html=True)
    

else:
    st.sidebar.markdown(f'''
    <div data-testid="stMetric" style = "
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 5%;
        margin: 10px 10px 10px 10px;              
        border-radius: 5px;
        border-left: 0.5rem solid #3B1F2B;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;
    "
                        >
                        <span>Total No. of Roads</span>
                        <h1 style = "font-size:32px;">{df[(selected_year,'Total No. of Roads')].sum()}</h1>
                        </div>

    '''

    ,unsafe_allow_html=True)

    st.sidebar.markdown(f'''
    <div data-testid = "stMetric" style="
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 5%;
        margin: 10px 10px 10px 10px;              
        border-radius: 5px;
        border-left: 0.5rem solid #2E86AB;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                        <span>No of Roads Eligible for RI</span>
                        <h2 style = "font-size:32px;">{df[(selected_year,'No. of Eligible Roads for RI(M)')].sum()}</h2>
                        </div>
    ''',unsafe_allow_html = True)


    st.sidebar.markdown(f'''
    <div data-testid = "stMetric" style = "
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 5%;
        margin: 10px 10px 10px 10px; 
        border-radius: 5px;
        border-left: 0.5rem solid #A23B72;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;
                        ">
                        <span>No. of RIs Conducted</span>
                        <h2 style = "font-size:32px;">{df[(selected_year,'No. of Roads RI(M) Conducted')].sum()}</h2></div>

    ''',unsafe_allow_html=True)

    extracted_val = df[(selected_year,'No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float)
    sumofvals= extracted_val.sum()

    st.sidebar.markdown(f'''
    <div data-testid = "stMetric" style = "
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 5% 5% 5% 5%;
        margin: 10px 10px 10px 10px; 
        border-radius: 5px;
        border-left: 0.5rem solid #F18F01;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;
                        ">
                        <span>No. of RIs Missed</span>
                        <h2 style = "font-size:32px">{sumofvals}</h2>
                        </div>
    ''',unsafe_allow_html=True)
df1 = df[[('FY-2021-22','State'),('FY-2021-22',    'No. of Roads RI(M) Conducted'),('FY-2022-23',    'No. of Roads RI(M) Conducted'),('FY-2023-24',    'No. of Roads RI(M) Conducted'),('FY-2024-25',    'No. of Roads RI(M) Conducted')]]
df1.columns = ['State', 'FY-2021-22', 'FY-2022-23', 'FY-2023-24', 'FY-2024-25']
df_melted = df1.melt(id_vars=['State'], 
                    value_vars=['FY-2021-22', 'FY-2022-23', 'FY-2023-24', 'FY-2024-25'],
                    var_name='Financial Year', 
                    value_name='No. of Roads RI(M) Conducted')

df_not_done = df.copy()
df_not_done[('FY-2021-22','No. of Roads RI(M) Missed(%)')] = df_not_done[('FY-2021-22','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float)
df_not_done[('FY-2022-23','No. of Roads RI(M) Missed(%)')] = df_not_done[('FY-2022-23','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float)
df_not_done[('FY-2023-24','No. of Roads RI(M) Missed(%)')] = df_not_done[('FY-2023-24','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float)
df_not_done[('FY-2024-25','No. of Roads RI(M) Missed(%)')] = df_not_done[('FY-2024-25','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float)
df3 = df_not_done[[('FY-2021-22','State'),('FY-2021-22','No. of Roads RI(M) Missed(%)'),('FY-2022-23','No. of Roads RI(M) Missed(%)'),('FY-2023-24','No. of Roads RI(M) Missed(%)'),('FY-2024-25','No. of Roads RI(M) Missed(%)')]]
df3.columns = ['State','FY-2021-22','FY-2022-23','FY-2023-24','FY-2024-25']
df3_melted = df3.melt(id_vars=['State'],
                      value_vars=['FY-2021-22','FY-2022-23','FY-2023-24','FY-2024-25'],
                      var_name='Financial Year',
                      value_name='No. of Roads RI(M) Missed(%)'


)


st.header('Statewise Routine Inspection Analysis')
col1,col2 = st.columns(2)

with col1:
    
    selected_state = st.selectbox('Select the state',df[('FY-2021-22','State')].to_list())
    selected_graph = st.selectbox('Select the Graph',['Line Graph','Bar Graph'])
    years = ['FY-2021-22','FY-2022-23','FY-2023-24','FY-2024-25']
    ri_conducted = []
    ri_missed = []


    for i in years:
        ri_conducted.append(df.loc[df[('FY-2021-22','State')] == selected_state,(i,'No. of Roads RI(M) Conducted')].values[0])
        ri_missed.append(df.loc[df[('FY-2021-22','State')]== selected_state,(i,'No. of Roads RI(M) Missed(%)')].str.split('(').str[0].values[0])

    data = {
        'Year': years * 2,
        'Number of Roads': ri_conducted + ri_missed,
        'Type': ['RI Conducted'] * len(years) + ['RI Missed'] * len(years)
    }

    df_state = pd.DataFrame(data)

    data1 = {
        
        'Year': years * 2,
        'Value': ri_conducted + ri_missed,
        'Type': ['RI Conducted'] * len(years) + ['RI Missed'] * len(years)
    }
    df_state1 = pd.DataFrame(data1)

    df_long = df_state1.melt(id_vars=['Year', 'Type'], value_vars='Value',
                            var_name='Measurement', value_name='Number of Roads')


    if selected_graph == 'Line Graph':
        fig_line = px.line(df_state,x = 'Year', y = 'Number of Roads',color ='Type',title=f'RI(M) Conducted and Missed over Financial Years for {selected_state}')
        st.plotly_chart(fig_line)
    
    else:
        fig_bar = px.bar(df_long, x='Year', y='Number of Roads', color='Type', barmode='group',
                title=f'RI(M) Conducted and Missed over Financial Years for {selected_state}')
        st.plotly_chart(fig_bar)
    


with col2:
  col3,col4 = st.columns(2)
  with col3:
    st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Conducted(2021-2022)</span>
                <h2 style = "color:#04015e">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2021-22','No. of Roads RI(M) Conducted')].values[0]}</h2></div>
''',unsafe_allow_html=True)
    st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Conducted(2022-2023)</span>
                <h2 style = "color:#04015e">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2022-23','No. of Roads RI(M) Conducted')].values[0]}</h2></div>
''',unsafe_allow_html=True)
    st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Conducted(2023-2024)</span>
                <h2 style = "color:#04015e">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2023-24','No. of Roads RI(M) Conducted')].values[0]}</h2></div>
''',unsafe_allow_html=True)
    st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Conducted(2024-2025)</span>
                <h2 style = "color:#04015e">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2024-25','No. of Roads RI(M) Conducted')].values[0]}</h2></div>
''',unsafe_allow_html=True)

  with col4:
      st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Missed(2021-22)</span>
                <h2 style = "color:#726ef3">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2021-22','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float).values[0]}</h2></div>
''',unsafe_allow_html=True)
      st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Missed(2022-23)</span>
                <h2 style = "color:#726ef3">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2022-23','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float).values[0]}</h2></div>
''',unsafe_allow_html=True)
      st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Missed(2023-24)</span>
                <h2 style = "color:#726ef3">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2023-24','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float).values[0]}</h2></div>
''',unsafe_allow_html=True)
      st.markdown(f'''
    <div data-testid = "stMetric" style = "background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 5%;
    margin: 10px 10px 10px 10px; 
    border-radius: 5px;
    border-left: 0.5rem solid black;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.5) !important;">
                <span>RIs Missed(2024-25)</span>
                <h2 style = "color:#726ef3;">{df.loc[df[('FY-2021-22','State')] == selected_state,('FY-2024-25','No. of Roads RI(M) Missed(%)')].str.split('(').str[0].astype(float).values[0]}</h2></div>
''',unsafe_allow_html=True)
     
fig = px.line(df_melted, x='State', y='No. of Roads RI(M) Conducted', color='Financial Year',
              title='Number of Roads RI(M) Conducted Over Financial Years')


st.plotly_chart(fig,use_container_width = True)





fig2 = px.line(df3_melted,x='State',y='No. of Roads RI(M) Missed(%)',color = 'Financial Year',title = 'Number of Roads RI(M) Missed Over Financial Years')
st.plotly_chart(fig2)
