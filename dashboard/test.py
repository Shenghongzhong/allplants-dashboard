import dash
from dash import  dcc
from dash import  html
import dash_bootstrap_components as dbc
from data_analysis import *
from dash_bootstrap_templates import load_figure_template
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
#load_figure_template("lux")
card = dbc.Card(
    [dbc.CardHeader("Header"), dbc.CardBody("Body", style={
        "height": 250,})],
    className="h-100",
)


# write a for loop
graph_card_1= dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody([dcc.Graph(figure = line_fig)])])
graph_card_2= dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody([dcc.Graph(figure = top_fig)])])
graph_card_3= dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody([dcc.Graph(figure = pop_fig)])])
graph_card_4= dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody([dcc.Graph(figure = top_ten_fig)])])
graph_card_5= dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody([dcc.Graph(figure = vaccinated_fig)])])

app.layout = html.Div(
    children =[
        html.Img(src='data:image/png;base64,{}'.format(test_base64),
        style = {'width':'10%','height':'50%'}),
        html.H1('MVP Demo Dashboard - COVID-19 Vaccine Tracking'),
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
                                dbc.CardDeck([card]*4),
                                html.H2('Here is some important information to height....'),
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
            )
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
