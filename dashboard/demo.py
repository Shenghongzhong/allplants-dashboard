from allplants_test_ import *
from assets import *
import dash
from dash import  dcc
from dash import  html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
#load_figure_template("lux")
card_1 = dbc.Card(
    [dbc.CardHeader(" Total Revenues", 
    style={
        'color':'#38786D',
        'font-weight': '700',
        'text-align':'center',
        "font-size": "25px",
        'white-space': 'pre',
        'line-break':'auto'}),
     dbc.CardBody("£135K", 
    style={"height": 150,
    'font-size':'54px', 'margin':'10px 50px 100px 50px',
    'color':'#6AA3F2'})],
    className="h-100",
)

card_2 = dbc.Card(
    [dbc.CardHeader("Top 5 Customers (id)", 
    style={
        'color':'#38786D',
        'font-weight': '700',
        'text-align':'center',
        "font-size": "25px",
        'font-weight': '700',
        'height':'80px'}), 
    dbc.CardBody(
        html.Ol(children=[
        html.Li('55873 '),
        html.Li('66581 '),
        html.Li('6805 '), 
        html.Li('64559 '),
        html.Li('54089 ')]),
    style={"height": 140,
    'font-size':'20px',
    'margin':'20px 50px 80px 50px',
    'color':'#6AA3F2'})],
    className="h-100",
)

card_3 = dbc.Card(
    [dbc.CardHeader("Top 5 Products",
    style={'color':'#38786D',
    'font-weight': '700',
    'text-align':'center',
    'font-weight': '700',
    "font-size": "25px",
    'height':'80px'}), 
    dbc.CardBody(html.Ol(children=[
        html.Li('BOLOGNESE_1 '),
        html.Li('PADTHAI_2 '),
        html.Li('PROTEIN_1 '),
        html.Li('PROTEIN_2 '),
        html.Li('BOLOGNESE_2 ')
    ]), style={"height": 210, 'width':650,
    'font-size':"20px",
    'color':'#6AA3F2',
    'margin':'20px 50px 10px 50px',
    })],
    #'padding':'45px 20px 20px 20px'
    className="h-100",
)


# write a for loop
graph_card_1= dbc.Card([dbc.CardHeader("1. How much revenue came from 1st time orders only each month?",
style={'colour':'#273A37',
        "font-size": "25px",
        'height':'80px',
        'font-weight': '500'}), dbc.CardBody([dcc.Graph(figure = question_fig_1)])])

graph_card_2= dbc.Card([dbc.CardHeader("2. Which customer (or customer id!) placed the most orders in this time period, and how many orders did they place? (3rd Aug 20 to 4th Oct 20)",
style={'colour':'#273A37',
        "font-size": "25px",
        'height':'100px',
        'font-weight': '500'}), 
dbc.CardBody([dcc.Graph(figure = question_fig_2)])])

graph_card_3= dbc.Card([dbc.CardHeader("3. Making use of both datasets, what was the dish that this same customer ordered the most? And how many times did they order it?",
style={'colour':'#273A37',
        "font-size": "25px",
        'height':'100px',
        'font-weight': '500'}), 
        dbc.CardBody(
            [dcc.Graph(figure = question_fig_3_a),dcc.Graph(figure=question_fig_3_b),
                            html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                )])])



graph_card_5= dbc.Card([
    dbc.CardHeader("4. The food development team have asked for your help in deciding what new dish(es) they should create next.",
    style={'colour':'#273A37',
        "font-size": "25px",
        'height':'100px',
        'font-weight': '500'}), 
dbc.CardBody([dcc.Graph(figure = question_fig_4)])])

app.layout = html.Div(
    children =[
        html.Img(src='data:image/png;base64,{}'.format(test_base64),
        style = {'width':'15%','height':'15%','margin':'10px 10px 10px 585px'}),
        html.Br(),
        html.H1('Order Performance Tracking Dashboard',
        style ={'margin':'10px 10px 10px 365px',
        'color':'#273A37'
        }),
        html.Div(
            dbc.Container(
                dbc.Alert( 'The dataset contains two tables, Order Information & Order Items, from 3rd August to 4th October 2020.', color='success'),
                className='p-5')
        ),
        html.Div(
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.CardDeck([card_1, card_2, card_3]),
                                html.H2('Here is some important information to highlight....', 
                                style = {
                                    'margin':'50px 10px 50px 10px',
                                    'color':'#273A37'
                                }),
                                dbc.CardDeck([graph_card_1]),
                                dbc.CardDeck([graph_card_2]),
                                dbc.CardDeck([graph_card_3]),
                                 dbc.CardDeck([graph_card_5])
                            ],
                            width=10
                        )
                    ]
                ),
                fluid=True,
                className='m-3'
            ),style = {'margin':'0px 10px 10px 190px'}
        ),
        html.Span(children=[
            f'Prepared:{datetime.now().date()}',
            " by ", html.B('David Zhong,  '),
            html.P('Data Scientist')
        ])
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
