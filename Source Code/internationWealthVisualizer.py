import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# collecting data from GDP.csv
df = pd.read_csv('../Data_Sets/GDP.csv')

# creating app variable for our dashboard
app = dash.Dash()

# creating interactive map visual
fig = go.Figure(data = go.Choropleth(
    locations = df['Country Code'],
    z = df['2019 [YR2019]'],
    text = df['Country Name'],
    colorscale= 'Blues',
    autocolorscale= False,
    reversescale= True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix= '$',
    colorbar_title='GDP<br>US$',
))

# creating layout of the graph
fig.update_layout(
    title_text='2019 Global GDP',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source= <a href="https://databank.worldbank.org/source/world-development-indicators#"> World Bank</a>',
        showarrow=False
    )
                   ]
)

# global GDP interactive map
data_GDP = [
    go.Choropleth(
        locations=df['Country Code'],
        z=df['2019 [YR2019]'],
        text=df['Country Name'],
        colorscale= 'Blues',
        autocolorscale= False,
        reversescale= True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix= '$',
        colorbar_title='GDP<br>US$',
    )
]

# creating layout of website
app.layout= html.Div(children=[
    html.H1(children= 'International Wealth Visualizer',
            style={
                'textAlign' : 'center',
                'color' : '#ADA5A3'
            }
            ),
    html.Div('A tool that allows you to be able to view the wealth of the world and provides', style={'textAlign' : 'center'}),
    html.Div('you with info regarding GDP, GNI, Cost of Living, and Currency', style={'textAlign' : 'center'}),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='Interactive Map', children=[
                html.H3('Interactive Map', style={'color' : '#9CB4C6'}),
                dcc.Graph(
                    id='Graph1',
                    figure={
                        'data' : data_GDP,
                        'layout' : go.Layout(
                            title= 'Global GDP in 2019'
                        )

                    }
                )

            ]),
            dcc.Tab(label='Currency Converter', children=[

            ]),
            dcc.Tab(label='My Page', children=[

            ])
        ]

        )
    ]

    )

]
)
#fig.write_html('world.html', auto_open = True)
if __name__ == '__main__':
    app.run_server()