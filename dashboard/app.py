from allplants_test_ import *
from assets import *
from style import *
import dash
from dash import  dcc
from dash import  html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.html.Div import Div
from dash.dependencies import Input, Output
import dash_table


app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
#load_figure_template("lux")
card_1 = dbc.Card(
    [dbc.CardHeader(" Total Revenues", 
    style={
        'color':'#38786D',
        'font-weight': '700',
        'text-align':'center',
        "font-size": "25px",
        'height':'80px',
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
    'margin':'20px 50px 100px 50px',
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
    ]), 
        style={"height": 210, 'width':650,
        'font-size':"20px",
        'color':'#6AA3F2',
        'margin':'20px 50px 30px 50px',
    })],
    #'padding':'45px 20px 20px 20px'
    className="h-100",
)


# write a for loop
graph_card_1= dbc.Card([
        dbc.CardHeader("1. How much revenue came from 1st time orders only each month?",
                        style={'colour':'#273A37',
                                "font-size": "25px",
                                'height':'80px',
                                'font-weight': '500'}), 
        dbc.CardBody([
            dcc.Graph(figure = question_fig_1)
            ,html.Div(children=[
                    html.H4('Analysis'),
                    html.P(
                            "Each month, we had approximately £45K from the first time order from 3rd Aug to 4th Oct. However, we had the highest number of first time orders in Sep 2020, in which we generated £75.67K, accounting for 14.84% of the total revenue given the dataset. We can investigate reasons why there was an increase. I reckoned maybe Allplants implemented new advertising strategies that brought more new customers.\n",
                            className="card-text",
                            style=analysis_text_style),
                        html.P(
                            "For the following activities, we should focus on which platforms brought the most customers and what campaigns we used to motivate customers to sign up and make the purchase decision.\n"
                            "Secondly, we need to look at supply and delivery. We can look at the areas if we have problems with the supply and delivery, the number of products done by the food development each day, week.\n"
                            "Thirdly, We can also look at the customer experience by getting data about the conversation rate from 3rd Aug to 4th Oct, the number of the second order from the first order, etc.\n",
                            className="card-text",
                            style=analysis_text_style),
                        html.P(
                            "Secondly, we need to look at supply and delivery. We can look at the areas if we have problems with the supply and delivery, the number of products done by the food development each day, week.\n"
                            "Thirdly, We can also look at the customer experience by getting data about the conversation rate from 3rd Aug to 4th Oct, the number of the second order from the first order, etc.\n",
                            className="card-text",
                            style=analysis_text_style),
                        html.P(
                            "Thirdly, We can also look at the customer experience by getting data about the conversation rate from 3rd Aug to 4th Oct, the number of the second order from the first order, etc.\n",
                            className="card-text",
                            style=analysis_text_style)

            ])
            ])])

graph_card_2= dbc.Card([dbc.CardHeader("2. Which customer (or customer id!) placed the most orders in this time period, and how many orders did they place? (3rd Aug 20 to 4th Oct 20)",
        style={'colour':'#273A37',
                "font-size": "25px",
                'height':'100px',
                'font-weight': '500'}), 

        dbc.CardBody([dcc.Graph(
            figure = question_fig_2),
            html.Div(
                children=[
                        html.H4('Analysis'),
                        html.P(
                            "To answer the question, the customer id (55873) ordered the most given the time."
                            "Given the sample dataset, the total number of customers placed was 11 orders. Presumably, the customer is a regular customer. The customer had purchased products at Allplants for the 30th time, from the 3rd of August to the 4th of October.",
                            className="card-text",
                            style=analysis_text_style
                        ),
                        html.P('For the next action, we may need to investigate the types of orders the customer id(55873) ordered the most, and maybe we should send discounts or some forms of coupon or referrals. The customer is likely to enjoy the service provided by Allplants.',
                            className="card-text",
                             style=analysis_text_style
                        ),
                        html.P("I\'d like to ask questions about the behaviours of the customer. Could we create more customers like the customer id (55873)? Why did top 5 customers order so many products from Allplants, apart from the quality and brands? Did they order similar products? If we can get more data about these groups of people, could we retarget similar customer prospects online when doing digital marketing?",
                            className="card-text",
                            style=analysis_text_style
                        )

                        ])
          
                        ]
                        
                        )])

graph_card_3= dbc.Card([
                dbc.CardHeader("3. Making use of both datasets, what was the dish that this same customer ordered the most? And how many times did they order it?",
                                style={'colour':'#273A37',
                                        "font-size": "25px",
                                        'height':'100px',
                                        'font-weight': '500'}), 
                dbc.CardBody([
                                dcc.Graph(figure = question_fig_3),
                                            html.Div(children=[
                                                    html.H4('Analysis'),
                                                    html.P(
                                                            "The customer(55873) ordered serveral products the most such as CARBONARA_2, SHEPHERD_2, BANOFFEE_1,CRUMBLE_1,ORZO_2. The number of theses products is all 9. "
                                                            "make up the bulk of the card's content.",
                                                            className="card-text",
                                                            style=analysis_text_style
                                                            ),
                                                    html.P('Having done some basic google, this was what I found at the website and made a slide together',
                                                            className="card-text",
                                                            style=analysis_text_style
                                                            )
                                                    
                                                    
                                                    
                                                    ])
                                            
                                                    
])])



graph_card_4= dbc.Card([
                dbc.CardHeader("4. The food development team have asked for your help in deciding what new dish(es) they should create next.",
                        style={'colour':'#273A37',
                            "font-size": "25px",
                            'height':'100px',
                            'font-weight': '500'}), 
                dbc.CardBody([
                    dcc.Graph(figure = question_fig_4_a),dcc.Graph(figure=question_fig_4_b),
                    html.Div(
                        children=[  
                            html.H4('Analysis'),                  
                            html.P(
                                    "We know the MEAL is our key product line many customers purchased from the chart above. It is also not surprising to see BREAKFAST come after."
                                    "It's fascinating to see PIZZA wasn't on the top 3, and I wondered if customers prefer to buy pizza from supermarkets because the pizza price is cheaper or more convenient ",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P(
                                    "Another possible reason could be many customers are working professionals, so they're likely to use kitchens at work to cook these pre-made meals. Meals are more manageable comparing to pizza, in my opinion.",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P(
                                    "We would like to look into details about specific products within these categories (MEAL, BREAKFAST, TREAT etc.)",
                                    className="card-text",
                                    style=analysis_text_style)
                            

                        ]
                    )

                                    
                                    ])])


graph_card_5= dbc.Card([
                dbc.CardHeader("4. The food development team have asked for your help in deciding what new dish(es) they should create next.",
                        style={'colour':'#273A37',
                            "font-size": "25px",
                            'height':'100px',
                            'font-weight': '500'}), 
                dbc.CardBody([
                    html.Div(
                        
                        children=[
                            html.H4('Analysis'),              
                            html.P(
                                    "My first thought would be to frame this question in a slightly different way:"
                                    "What's the weekly average sales did we have for one unit of sku_code ?"
                                   ,
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P(
                                    "**The average is the sample mean rather than the population mean",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P(
                                    "We would like to look into details about specific products within these categories (MEAL, BREAKFAST, TREAT etc.)",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.Img(
                                        src='data:image/png;base64,{}'.format(formular_base64),
                                        style={
                                                'display': 'block',
                                                'margin': 'auto',
                                                'width': '50%'
                                        }
                                            ),
                            html.Br(),
                            html.P(
                                    "We know we have the average sales of 6,9K units of sku_code. That's our benchmark without considering any other factors such as product types, tastes, nutritions etc.",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P(
                                    "Since Allplants is doing food business, we would need to consider the similarities of tastes of products we're going to launch, if we would like to make a good prediction for the potential sales on a weekly basis and also recommending the price range for the new products.",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P(
                                    "Let's have a look at products we're launching. They are croissant, pain au chocolat & pain aux raisins.",
                                    className="card-text",
                                    style=analysis_text_style),  
                            html.Img(src='data:image/png;base64,{}'.format(lan_products_base64)
                                    ,
                                    style=style_image
                            ),
                            html.Br(),
                            html.Br(),
                            html.P("Personally, I'd think I should compare the products to `BREAKFAST` or `TREAT`",
                                    className="card-text",
                                    style=analysis_text_style
                            
                            ),

                            html.P("Let's look at products under these 2 product types",
                                    className="card-text",
                                    style=analysis_text_style    ),
                            html.Img(src='data:image/png;base64,{}'.format(breakfast_base64)
                                    ,
                                    style=style_image
                            ),
                            html.Br(),
                            html.Img(src='data:image/png;base64,{}'.format(treats_base64)
                                    ,
                                    style=style_image
                            ),
                            html.Br(),
                            html.P("Having looked at these products, I would select BANOFFEE_1, FONDANT_1, TR_TIRAMISU_1 regarding my personal tastes."
                                    "They're approximately close to the new products we're going to launch."
                                    "However, the breakfast are more smoothie-base food.",
                                    className="card-text",
                                    style=analysis_text_style),
                            html.P("In terms of the number of sales, we can see the weekly average sales of these prdocuts (BANOFFEE_1, FONDANT_1, TR_TIRAMISU_1)",
                                    className="card-text",
                                    style=analysis_text_style)]),
                            dcc.Graph(figure = question_fig_5),

                            html.Div(children=[

                                html.P("From this chart, we can see FONDANT_1 has the highest weekly average sales of 82 units, comparing with other two products."
                                "The TR_TIRAMISU_1 has been sold at 1.9 units. So I'd say the products we're going launch could be sold from 1.9 units to 82 units per week."
                                "In terms of pricing, we can have a look at the revenue and the price per item.",
                                className="card-text",
                                style=analysis_text_style
                                ),
                            html.Img(src='data:image/png;base64,{}'.format(formular_b_base64)
                                    ,
                                    style= {'display': 'block',
                                        'margin': 'auto',
                                        'width': '50%'}
                                        ),
                            html.Br(),
                            dash_table.DataTable(
                                    id='rev_table',
                                    columns=[{"name": i, "id": i} 
                                            for i in revenue_tb.columns],
                                    data=revenue_tb.to_dict('records'),
                                    style_cell=dict(textAlign='left',backgroundColor="#8AC6BD"),
                                    style_header=dict(backgroundColor="#38786D",color="#EAF2F1",textAlign='center'),
                                    style_data=dict(color="#323A39")
                                ),
                            html.Br(),
                            html.Div(children=[
                                html.P("Since we only have data about revenue, we can get a figure by subtracting gross revenue from the product of the total sales multiplying the total items. However, I couldn't tell what the figure was, but my guess would be profit. I could be wrong because prices and costs are two unknown variables. So I would need more information and data about price and cost to give a better conclusion.",
                                    className="card-text",
                                    style=analysis_text_style),
                                html.P("Yet, I was confused by seeing BANOFFEE_1 and FONDANT_1 have really low numbers of 0.10 and 0.08, respectively. Are they really that cheap, and the profit margins are so low for each item sold at Allplants.",
                                        className="card-text",
                                        style=analysis_text_style
                                    ),
                                html.P("In Sainsbury, Croissant, Pain Au Chocolat, Pain Au Raisins are sold at 80P",
                                        className="card-text",  
                                        style=analysis_text_style),
                                html.P("At Allplants, the product option is usually selling in buddle. For prices, I would recommend we can price new products from the maximum of £4 to the minimum of £0.8 if a customer decide to add these treats to the product buddle.",
                                        className="card-text",
                                        style=analysis_text_style),
                                html.H1('Thank You!',
                                        style={
                                            'text-align':"center",
                                            'font-size':'144px'})
                                    ])






                            ])

                                    
                                    ])])

app.layout = html.Div(
    children =[
        html.Img(src='data:image/png;base64,{}'.format(logo_base64),
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
                                        'padding':'50px 10px 50px 10px',
                                        'color':'#273A37'}),
                                dbc.CardDeck([graph_card_1]),
                                html.Br(),
                                html.Br(),
                                dbc.CardDeck([graph_card_2]),
                                html.Br(),
                                html.Br(),
                                dbc.CardDeck([graph_card_3]),
                                html.Br(),
                                html.Br(),
                                dbc.CardDeck([graph_card_4]),
                                html.Br(),
                                html.Br(),
                                dbc.CardDeck([graph_card_5])
                                            ],
                                                width=10
                                            )
                                        ]
                                    ),
                                    fluid=True,
                                    className='m-3'
                                ),
            style = {'margin':'0px 10px 10px 190px'}
        ),
        html.Section(children=[
            'Created:08/10/2021',
            " by ", html.B('David Zhong',style={'text-align':'center'}),
            html.Br(),
            html.Div(children=[html.A("Twitter  ",href='https://twitter.com/ShenghongZhong',style={'white-space':'pre'}),
                        html.A("LinkedIn  ",href='https://www.linkedin.com/in/shenghongzhong',style={'white-space':'pre'}),
                        html.A('Medium  ',href='https://davidshenghongzhong.medium.com',style={'white-space':'pre'}),
                        html.A('Github  ',href='https://github.com/Shenghongzhong',style={'white-space':'pre'})],
                        style={
                            'margin':'5px 5 px 5px'
                        })
        
            

        ],
        style={
            'text-align':'center'
        })
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
