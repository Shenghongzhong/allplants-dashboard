from data_analysis import *
from assets import *
import dash
from dash import  dcc
from dash import  html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
#load_figure_template("lux")
card_1 = dbc.Card(
    [dbc.CardHeader("Total Number of Countries", style={'color':'#38786D'}),
     dbc.CardBody("222", 
    style={"height": 150,
    'font-size':'80px', 'margin':'10px 50px 50px 50px',
    'color':'#6AA3F2'})],
    className="h-100",
)

card_2 = dbc.Card(
    [dbc.CardHeader("Full Vaccinated Rate", style={'color':'#38786D'}), 
    dbc.CardBody("23.0%", 
    style={"height": 140,
    'font-size':'60px',
    'margin':'20px 50px 50px 50px',
    'color':'#6AA3F2'})],
    className="h-100",
)

card_3 = dbc.Card(
    [dbc.CardHeader("Top 3 Vaccine Manufacturers",style={'color':'#38786D'}), 
    dbc.CardBody(html.Ol(children=[
        html.Li('Pfizer/BioNTech '),
        html.Li('Moderna '),
        html.Li('Oxford/AstraZeneca ')
    ]), style={"height": 210, 'width':650,
    'font-size':"25px",
    'color':'#6AA3F2',
    'padding':'45px 20px 20px 20px'})],
    className="h-100",
)


# write a for loop
graph_card_1= dbc.Card([dbc.CardHeader("Here's a graph",style={'colour':'#273A37'}), dbc.CardBody([dcc.Graph(figure = line_fig)])])
graph_card_2= dbc.Card([dbc.CardHeader("Here's a graph",style={'colour':'#273A37'}), dbc.CardBody([dcc.Graph(figure = top_fig)])])
graph_card_3= dbc.Card([dbc.CardHeader("Here's a graph",style={'colour':'#273A37'}), dbc.CardBody([dcc.Graph(figure = pop_fig)])])
graph_card_4= dbc.Card([dbc.CardHeader("Here's a graph",style={'colour':'#273A37'}), dbc.CardBody([dcc.Graph(figure = top_ten_fig)])])
graph_card_5= dbc.Card([dbc.CardHeader("Here's a graph",style={'colour':'#273A37'}), dbc.CardBody([dcc.Graph(figure = vaccinated_fig)])])

app.layout = html.Div(
    children =[
        html.Img(src='data:image/png;base64,{}'.format(test_base64),
        style = {'width':'15%','height':'15%','margin':'10px 10px 10px 585px'}),
        html.Br(),
        html.H1('MVP Demo Dashboard - COVID-19 Vaccine Tracking',
        style ={'margin':'10px 10px 10px 250px',
        'color':'#273A37'
        }),
        html.Div(
            dbc.Container(
                dbc.Alert( 'Hello there, this is a demo!', color='success'),
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
                                dbc.CardDeck([graph_card_4]),
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
            html.I('Founder/Data Scientist')
        ])
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
