# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update


# Create a dash application
app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the spaceX into pandas dataframe
spacex_df =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


# Application layout
app.layout = html.Div(children=[ 
                                html.H1('Space X Launch Information', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': '24px'}),
                                html.Div([
                                    html.Div([
                                        html.Div(
                                            [
                                            html.H2('Launch Site:', style={'margin-right': '2em'}),
                                            ]
                                        ),
                                          dcc.Dropdown(id='LaunchSite', 
                                                     options=[{'label': i, 'value': i} for i in sapcex_df["LaunchSite"]],
                                                     placeholder="Select a launch site",
                                                     style={'width':'80%', 'padding':'3px', 'font-size': '20px', 'text-align-last' : 'center'}),
                                            ], style={'display': 'flex'}),  
                                          ]),

                        ])