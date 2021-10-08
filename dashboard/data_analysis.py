import pandas as pd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

file = '/Users/shenghongzhong/Documents/pinich/dashboard/data/countries_vaccination_df.csv'


# Setting the smaller datatype to makke pandas job fatser and easier
selected_dtypes = {
    'total_vaccinations': 'float32',
    'people_vaccinated': 'float32',
    'people_fully_vaccinated': 'float32',
    'daily_vaccinations_raw': 'float32',
    'daily_vaccinations': 'float32',
    'Distance(mi)': 'float32'   
}
# Selecting columns for out analysis purpose
selected_cols = ['country', 'iso_code', 'date', 'total_vaccinations',
       'people_vaccinated', 'people_fully_vaccinated',
       'daily_vaccinations_raw', 'daily_vaccinations','vaccines', 'source_name']

vaccination_df = pd.read_csv('/Users/shenghongzhong/Documents/pinich/dashboard/data/vaccination_df.csv', 
                            usecols=selected_cols, 
                            dtype=selected_dtypes, 
                            parse_dates=['date'])




countries_vaccination_df = pd.read_csv(file)




top_fig = px.bar(countries_vaccination_df.head(20), x='country', y='total_vaccinations',
            hover_data=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'], color='country')
#fig.update_layout(template='plotly_dark')
top_fig.update_layout(title='Top 20 Countries in view of Total Vaccinations',
                 xaxis_title= "Country Name",
                 yaxis_title= "Population")

vaccinated_fig = go.Figure()
# I will skip the country China from this graph as China has not displayed their data regarding these two coulmns.
vaccinated_fig.add_trace(go.Bar(x=countries_vaccination_df[1:20].country, y=countries_vaccination_df[1:20].people_fully_vaccinated,
                    marker_color='crimson',
                    name='people_fully_vaccinated'))
vaccinated_fig.add_trace(go.Bar(x=countries_vaccination_df[1:20].country, y=countries_vaccination_df[1:20].people_vaccinated,
                    marker_color='yellow',
                    name='people_vaccinated'))
#vaccinated_fig.update_layout(template='plotly_dark')
vaccinated_fig.update_layout(title="Comparision between people_fully_vaccinated and people_vaccinated",
                 xaxis_title = "Country Name", yaxis_title= "Population")



top_fiv = list(countries_vaccination_df.country.head(5))
top_fiv_country_df = vaccination_df[vaccination_df['country'].isin(top_fiv)]

line_fig = px.line(top_fiv_country_df, x='date', y='total_vaccinations', 
              color='country', line_group='country', hover_name='country')
#line_fig.update_layout(template='plotly_dark')
line_fig.update_layout(title="Line plot for Total Vaccinations",
                 xaxis_title="Date",
                 yaxis_title="Total Vaccinations")


# population

population_df = pd.read_csv('/Users/shenghongzhong/Documents/pinich/dashboard/data/population_by_country_2020.csv', usecols=['Country (or dependency)', 'Population (2020)'])
population_df= population_df.rename(columns={'Country (or dependency)':'country',
                               'Population (2020)':'population'})
merged_df = countries_vaccination_df.merge(population_df,left_on='country', right_on='country', how='left')

pop_fig = go.Figure(data=[
    go.Bar(x=merged_df[1:11].country, y=merged_df[1:11].people_fully_vaccinated, marker_color='#bcbd22', name='people_fully_vaccinated'),
    go.Bar(x=merged_df[1:11].country, y=merged_df[1:11].people_vaccinated, marker_color='#9467bd', name='people_vaccinated'),
    go.Bar(x=merged_df[1:11].country, y=merged_df[1:11].population, marker_color='#1f77b4', name='population')
])
pop_fig.update_layout(barmode='group')
#pop_fig.update_layout(template='plotly_dark')
pop_fig.update_layout(title="A comparitive Bar Chart between 'people_vaccinated', 'people_full_vaccinated' and 'Population'",
                 xaxis_title= "Country Name",
                 yaxis_title= "Population")



#coutry


country_name = 'China' # You can type any country name here and run this cell you will get the data for the country
country_vaccination_df = vaccination_df[vaccination_df['country']== country_name]
top_10 = list(merged_df.sort_values('population', ascending=False)['country'].head(10))

top_ten_fig = go.Figure()

top_ten_fig.add_trace(go.Scatter(x=country_vaccination_df.date,
                        y=country_vaccination_df.daily_vaccinations, visible=True))
buttons = []
for x in top_10:
    buttons.append(dict(method='restyle',
                        label=x,
                        visible=True,
                        args=[{'x':[vaccination_df[vaccination_df['country']== x].date],
                               'y':[vaccination_df[vaccination_df['country']== x].daily_vaccinations],
                               'type':'scatter'}, [0]],
                       )
                  )
updatemenu = []
your_menu = dict()
updatemenu.append(your_menu)

updatemenu[0]['buttons'] = buttons
updatemenu[0]['direction'] = 'down'
updatemenu[0]['showactive'] = True

# add dropdown menus to the figure
top_ten_fig.update_layout(showlegend=False, updatemenus=updatemenu)
#top_ten_fig.update_layout(template="plotly_dark")
top_ten_fig.update_layout(title="Daily vaccination graph for top 10 most populous countries")







# Customer summary tables