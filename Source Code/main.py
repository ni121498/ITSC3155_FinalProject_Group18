import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import json
import plotly.express as px


# collecting data from files
df = pd.read_csv('../Data_Sets/GDP.csv', skiprows=[218, 219, 220, 221, 222, 223])
df2 = pd.read_csv('../Data_Sets/GDP_Per_Capita.csv')
df3 = pd.read_csv('../Data_Sets/GNI.csv')
df4 = pd.read_csv('../Data_Sets/GNI_Per_Capita.csv')
df5 = pd.read_csv('../Data_Sets/gdpContAvg.csv')
df6 = pd.read_csv('../Data_Sets/gpdPerCap_ContAvg.csv')
df7 = pd.read_csv('../Data_Sets/gniContAvg.csv')
df8 = pd.read_csv('../Data_Sets/gniPerCap_ContAvg.csv')
df9 = pd.read_csv('../Data_Sets/countryCurrencies.csv')



# creating app variable for our dashboard
app = dash.Dash()

# method that pulls gdp data based on year passed in and returns data
def gdp_data(year):
    data = [
        go.Choropleth(
        locations=df['Country_Code'],
        z=df[year],
        text=df['Country_Name'],
        colorscale='Blues',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix='$',
        colorbar_title='GDP<br>US$',
        )
    ]
    return data

# method that pulls gdp per capita data based on year passed in and returns data
def gdp_per_cap_data(year):
    data = [
        go.Choropleth(
            locations=df2['Country_Code'],
            z=df2[year],
            text=df2['Country_Name'],
            colorscale='Sunsetdark',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix='$',
            colorbar_title='GDP Per Capita<br>US$'
        )
    ]
    return data

# method that pulls gni data based on year passed in and returns data
def gni_data(year):
    data = [
        go.Choropleth(
            locations=df3['Country_Code'],
            z=df3[year],
            text=df3['Country_Name'],
            colorscale='Viridis',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix='$',
            colorbar_title='GNI<br>US$'
        )
    ]
    return data

# method that pulls gni per capita based on year passed in and returns data
def gni_per_cap_data(year):
    data = [
        go.Choropleth(
            locations=df4['Country_Code'],
            z=df4[year],
            text=df4['Country_Name'],
            colorscale='Viridis',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix='$',
            colorbar_title='GNI Per Capita<br>US$'
        )
    ]
    return data

def currency_data(year):
    data=px.choropleth(
        df9,
        locations='Country_Code',
        color='Currency',
        hover_data=['Country_Name', year],
        title='Currencies of the World and Value in US$ in ' + year

    )
    fig = go.Figure(data)
    return fig

# loading continents json file
continents = json.load(open('../Data_Sets/continents.json'))
cont_id_map = {}
for feature in continents['features']:
    feature['id'] = feature['properties']['continent']

def gdp_cont_data(year):
    data=px.choropleth(
        df5,
        locations='Code',
        geojson=continents,
        color=year,
        title='Global GDP of Continent in ' + year
    )
    fig = go.Figure(data)
    return fig

def gdp_per_cap_cont_data(year):
    data=px.choropleth(
        df6,
        locations='Code',
        geojson=continents,
        color=year,
        color_continuous_scale='Reds',
        title='Global GDP per Capita of Continent in ' + year
    )
    fig = go.Figure(data)
    return fig

def gni_cont_data(year):
    data=px.choropleth(
        df7,
        locations='Code',
        geojson=continents,
        color=year,
        color_continuous_scale='Oranges',
        title='Global GNI of Continent in ' + year
    )
    fig = go.Figure(data)
    return fig

def gni_per_cap_cont_data(year):
    data = px.choropleth(
        df8,
        locations='Code',
        geojson=continents,
        color=year,
        color_continuous_scale='Greens',
        title='Global GNI of Continent in ' + year
    )
    fig = go.Figure(data)
    return fig

regions = json.load(open('../Data_Sets/custom.geo.json'))

def gdp_region_data(year):
    data = [
        go.Choropleth(
            locations=df7['sub_region_code'],
            # locationmode="continent names",
            z=df7[year],
            text=df7['sub_region'],
            colorscale='Reds',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix='$',
            colorbar_title='GDP<br>US$'
        )
    ]
    return data


# creating layout of website
app.layout = html.Div(children=[
    html.H1(children='International Wealth Visualizer',
            style={
                'textAlign': 'center',
                'color': '#ADA5A3'
            }),
    html.Div('A tool that allows you to be able to view the wealth of the world and provides',
             style={'textAlign': 'center'}),
    html.Div('you with info regarding GDP, GNI, Cost of Living, and Currency', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='Home', children=[

            ]),
            dcc.Tab(label='Income', children=[
                html.Br(),
                html.Br(),
                # Choose what year
                html.Div('Please Select Year'),
                html.Div(
                    dcc.Dropdown(
                        id='year_dropdown',
                        options=[
                            {'label': '2016', 'value': '2016'},
                            {'label': '2017', 'value': '2017'},
                            {'label': '2018', 'value': '2018'},
                            {'label': '2019', 'value': '2019'},
                            {'label': '2020', 'value': '2020'}
                        ])),
                html.Br(),

                # Choose graph to display
                html.Div('Please Select View Type'),
                html.Div(
                    dcc.Dropdown(
                        id='fig_dropdown',
                        options=[
                            {'label': 'Global GDP', 'value': 'gdp'},
                            {'label': 'Global GDP Per Capita', 'value': 'gdp_cap'},
                            {'label': 'Global GNI', 'value': 'gni'},
                            {'label': 'Global GNI Per Capita', 'value': 'gni_cap'}
                        ])),
                html.Br(),

                # Choose what to view
                html.Div('Please Select World View Type'),
                html.Div(
                    dcc.Dropdown(
                        id='view_dropdown',
                        options=[
                            {'label': 'Continent', 'value': 'continent'},
                            {'label': 'Region', 'value': 'region'},
                            {'label': 'Country', 'value': 'country'}
                        ])),

                html.Div(id='view_opt'),

                # Displays graph from dropdown
                html.Div(id='fig_plot')

            ]),
            dcc.Tab(label='Currency', children=[
                html.Br(),
                html.Br(),
                html.Div('This is a view of the world currencies showing how much each currency is in US dollars'),
                html.Br(),
                html.Br(),
                html.Div('Please Select Year'),
                html.Div(
                    dcc.Dropdown(
                        id='curr_drop',
                        options=[
                            {'label': '2016', 'value': '2016'},
                            {'label': '2017', 'value': '2017'},
                            {'label': '2018', 'value': '2018'},
                            {'label': '2019', 'value': '2019'}
                        ]
                    )
                ),
                html.Br(),
                html.Br(),
                html.Div(id='curr_plot')

            ]),
            dcc.Tab(label='My Page', children=[

            ]),
            dcc.Tab(label='Sign Up', children=[

            ]),
            dcc.Tab(label='Login', children=[

            ])
        ])
    ])
])


# App callback for Fig selection dropdown and year selection dropdown
@app.callback(
    dash.dependencies.Output('fig_plot', 'children'),
    dash.dependencies.Input('fig_dropdown', 'value'),
    dash.dependencies.Input('year_dropdown', 'value'),
    dash.dependencies.Input('view_dropdown', 'value'))
def update_graph(fig_name, selected_year, view):
    # returns the data based on country
    if view == 'country':
        if fig_name == 'gdp':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019':
                data_type = 'gdp'
                return dcc.Graph(
                    id='GDP_Graph',
                    figure={
                        'data': gdp_data(selected_year),
                        'layout': go.Layout(
                            title='Global GDP in ' + selected_year
                        )})

        if fig_name == 'gdp_cap':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019':
                data_type = 'gdp'
                return dcc.Graph(
                    id='GDP_Per_Capita_Graph',
                    figure={
                        'data': gdp_per_cap_data(selected_year),
                        'layout': go.Layout(
                            title='Global GDP Per Capita in' + selected_year
                        )})

        if fig_name == 'gni':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019':
                return dcc.Graph(
                    id='GNI_Graph',
                    figure={
                        'data': gni_data(selected_year),
                        'layout': go.Layout(
                            title='Global GNI in ' + selected_year
                        )})

        if fig_name == 'gni_cap':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019':
                return dcc.Graph(
                    id='GNI_Per_Capita_Graph',
                    figure={
                        'data': gni_per_cap_data(selected_year),
                        'layout': go.Layout(
                            title='Global GNI Per Capita in ' + selected_year
                        )})

    if view == 'continent':
        if fig_name == 'gdp':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019' :
                return dcc.Graph(
                    id='Continent_GDP',
                    figure=gdp_cont_data(selected_year)
                )
        if fig_name == 'gdp_cap':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019' :
                return dcc.Graph(
                    id='Continent_GDP_Cap',
                    figure=gdp_per_cap_cont_data(selected_year)
                )
        if fig_name == 'gni':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019' :
                return dcc.Graph(
                    id='Continent_GNI',
                    figure=gni_cont_data(selected_year)
                )
        if fig_name == 'gni_cap':
            if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019' :
                return dcc.Graph(
                    id='Continent_GNI_Cap',
                    figure=gni_per_cap_cont_data(selected_year)
                )
    if view == 'region':
        if fig_name == 'gdp':
            if selected_year == '2016':
                return dcc.Graph(
                    id='Region_GDP16',
                    figure={
                        'data' : currency_data(selected_year),
                        'layout' : go.Layout(
                            title= 'Global Average GDP of Sub Region in ' + selected_year
                        )
                    }
                )

@app.callback(
    dash.dependencies.Output('curr_plot', 'children'),
    dash.dependencies.Input('curr_drop', 'value')
)
def update_currency_fig(selected_year):
    if selected_year == '2016' or selected_year == '2017' or selected_year == '2018' or selected_year == '2019' :
        return dcc.Graph(
            id='Currency_Graph',
            figure=currency_data(selected_year)

        )

if __name__ == '__main__':
    app.run_server()
    #app.run_server(host='0.0.0.0', port=8124)
    #print(continents['features'][0]['properties'])
    #gdp_cont_data('2019').show()
    #fig.show()
