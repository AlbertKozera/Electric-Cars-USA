import plotly.graph_objects as go
import statistics
import numpy
import pandas_log
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
import plotly.io as pio
from jupyter_dash import JupyterDash
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


df = pd.read_csv('https://gist.githubusercontent.com/AlbertKozera/6396b4333d1a9222193e11401069ed9a/raw/dca34e16091ba533a53bc447edad12ddb041af2d/Pojazdy%2520elektryczne%2520w%2520USA.csv')

for col in df.columns:
    df[col] = df[col].astype(str)
df['range'] = pd.to_numeric(df['range'])
df['year of production'] = pd.to_numeric(df['year of production'])

df_range = df.drop(columns = ['state', 'brand', 'model', 'year of production', 'type']).groupby('code', as_index=False)
df_year = df.drop(columns = ['state', 'brand', 'model', 'range', 'type']).groupby('code', as_index=False)
df_brand = df.drop(columns = ['state', 'model', 'range', 'year of production', 'type'])
df_model = df.drop(columns = ['state', 'brand', 'range', 'year of production', 'type'])

df_brand_most_common = df_brand.groupby('code')['brand'].apply(lambda x: x.value_counts().index[0]).reset_index()
df_model_most_common = df_model.groupby('code')['model'].apply(lambda x: x.value_counts().index[0]).reset_index()
df_range_mean = df_range.agg({'range':'mean'})
df_range_std = df_range.agg({'range':'std'})
df_range_var = df_range.agg({'range':'var'})
df_year_mean = df_year.agg({'year of production':'mean'})
df_year_std = df_year.agg({'year of production':'std'})
df_year_var = df_year.agg({'year of production':'var'})
df_percentage_by_type = pd.crosstab(df['code'],df['type'],normalize='index').apply(lambda x: x*100).reset_index()
dict_percentage_by_brand = pd.crosstab(df['code'],df['brand'],normalize='index').reset_index(drop=True).apply(lambda x: round(x*100, 2)).apply(lambda x: pd.Series(x).nlargest(3).to_dict(), axis=1)
dict_percentage_by_model = pd.crosstab(df['code'],df['model'],normalize='index').reset_index(drop=True).apply(lambda x: round(x*100, 2)).apply(lambda x: pd.Series(x).nlargest(3).to_dict(), axis=1)

#-------------------------------# Chernoff car
def parameter1(img, brand):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/fonts/PottaOne-Regular.ttf", 16)
    draw.text((100, 60),brand,(151,151,151),font=font)
    #img.show()
    return img
    
def parameter2(img, model):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/fonts/PottaOne-Regular.ttf", 16)
    draw.text((160, 60),model,(151,151,151),font=font)
    #img.show()
    return img

def parameter3(img, multiplier):
    multiplier = int((round((multiplier/100) % 1, 4) * 10000) - 1600)
    background = img
    foreground = Image.open('assets/parts/part3.png')
    foreground = foreground.resize((foreground.size[0] + multiplier, foreground.size[1]))
    img = Image.new('RGBA',(background.size[0] + foreground.size[0], background.size[1]))
    img.paste(background, (0,0))
    img.paste(foreground, (background.size[0],0), foreground)
    #img.show()
    return img

def parameter4(img, multiplier):
    multiplier = multiplier - 130
    background = img
    foreground = Image.open('assets/parts/part2.png')
    foreground = foreground.resize((foreground.size[0] + int(multiplier / 2), foreground.size[1] + int(multiplier / 2)))
    background.paste(foreground, (42 - int(multiplier / 4),95 - int(multiplier / 4)), foreground)
    background.paste(foreground, (342 - int(multiplier / 4),95 - int(multiplier / 4)), foreground)
    img = background
    #img.show()
    return img

def parameter5(img, bev, phev):
    background = img
    foreground1 = Image.open('assets/parts/part4.png')
    original_size_x = foreground1.size[0]
    original_size_y = foreground1.size[1]
    size_x = int(foreground1.size[0] * bev/100)
    size_y = int(foreground1.size[1] * bev/100)
    if size_x == 0 or size_y == 0:
        size_x = 1
        size_y = 1
    foreground1 = foreground1.resize((size_x, size_y))
    background.paste(foreground1, (int(250 + (original_size_x - size_x)),int(90 + (original_size_y - size_y))), foreground1)
    foreground2 = Image.open('assets/parts/part5.png')
    original_size_x = foreground2.size[0]
    original_size_y = foreground2.size[1]
    size_x = int(foreground2.size[0] * phev/100)
    size_y = int(foreground2.size[1] * phev/100)
    if size_x == 0 or size_y == 0:
        size_x = 1
        size_y = 1
    foreground2 = foreground2.resize((size_x, size_y))
    background.paste(foreground2, (int(145 + (original_size_x - size_x)),int(90 + (original_size_y - size_y))), foreground2)
    img = background
    #img.show()
    return img
#-------------------------------# Chernoff car
#-------------------------------# Chernoff car generator
for index, row in df_brand_most_common.iterrows():
    parameter1(Image.open('assets/parts/part1.png'), row['brand']).save('assets/'+ row['code'] +'.png')

for index, row in df_model_most_common.iterrows():
    parameter2(Image.open('assets/'+ row['code'] +'.png'), row['model']).save('assets/'+ row['code'] +'.png')

for index, row in df_year_mean.iterrows():
    parameter3(Image.open('assets/'+ row['code'] +'.png'), round(row['year of production'], 2)).save('assets/'+ row['code'] +'.png')

for index, row in df_range_mean.iterrows():
    parameter4(Image.open('assets/'+ row['code'] +'.png'), round(row['range'], 2)).save('assets/'+ row['code'] +'.png')
    
for index, row in df_percentage_by_type.iterrows():
    parameter5(Image.open('assets/'+ row['code'] +'.png'), int(row['Battery Electric Vehicle (BEV)']), int(row['Plug-in Hybrid Electric Vehicle (PHEV)'])).save('assets/'+ row['code'] +'.png')   
#-------------------------------# Chernoff car generator

fig = go.Figure(data=go.Choropleth(
    locations=df['code'].drop_duplicates(keep='first').reset_index(drop=True),
    z = round(df_range_mean['range'], 2),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    hovertemplate='Zasięg --- mean:[%{z}] - std:[' + round(df_range_std['range'], 2).astype(str) + '] - var:[' + round(df_range_var['range'], 2).astype(str) + ']' 
        + '<br>Rocznik --- mean:[' + round(df_year_mean['year of production'], 2).astype(str) + '] - std:[' + round(df_year_std['year of production'], 2).astype(str) + '] - var:[' + round(df_year_var['year of production'], 2).astype(str) + ']'   
        + '<br>Rodzaj napędu --- {\'BEV\': ' +  round(df_percentage_by_type['Battery Electric Vehicle (BEV)'], 2).astype(str) + ' , \'PHEV\': ' + round(df_percentage_by_type['Plug-in Hybrid Electric Vehicle (PHEV)'], 2).astype(str) + '}'
        + '<br>Marka --- ' +  dict_percentage_by_brand.values.astype(str) 
        + '<br>Model --- ' +  dict_percentage_by_model.values.astype(str) 
        + '<extra>' + df['state'].drop_duplicates(keep='first').reset_index(drop=True) + '<br>' + df['code'].drop_duplicates(keep='first').reset_index(drop=True) + '</extra>',
    marker_line_color='black',
    colorbar_title="Średni zasięg pojazdu [km]",
))


fig.update_layout(
    title_text='Popularność samochodów elektrycznych w USA',   
    height=750,
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
)

#-------------------------------#

app = dash.Dash(__name__, suppress_callback_exceptions = False)

app.layout = html.Div([    
    dcc.Graph(
        id='choropleth',
        figure=fig
    ),
    html.Div([ 
        html.Img(id='chernoff-car')
        ],
        style={
            'position': 'absolute',
            'top': '700px',
            'left': '1080px'
        }
    )
])

#-------------------------------# callback
@app.callback(
    Output(component_id='chernoff-car', component_property='src'),
    Input(component_id='choropleth', component_property='hoverData')
)
def update_output_div(hoverData):
    if hoverData is not None:     
        src = hoverData['points'][0]['location']
        return app.get_asset_url(src + '.png')
    else:
        return hoverData
#-------------------------------# callback  

if __name__ == '__main__':
    app.run_server(debug=False)
