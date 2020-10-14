
"""Corona_visualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16c9Q9QdbgyuXVs2k2-ov7oGcrNUZdW6b

# Covid-19 Data Visualization using Plotly Express (50 graphs)

### For Fast Processing :Go to runtime(headbar)> Change runtime type > GPU

## Task 1: Importing Necessary Libraries

Importing Pandas and Matplotlib
"""

import pandas as pd       #Data analysis and Manipulation
import matplotlib.pyplot as plt   #Data Visualization

"""Importing Plotly"""

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go                # Importing Plotly
import plotly.express as px

"""Initializing Plotly (#Plotly Consumes a lot of computing power, so its default mode is off in Google Colab, Hence we need to initialize it)"""

import plotly.io as pio
#pio.renderers.default = 'colab'     # To initialize plotly

"""### Task 2: Importing the Datasets"""

df1= pd.read_csv("covid.csv")
df1.head()

df2= pd.read_csv("covid_grouped.csv")
df2.head()

df2.tail()

"""Dataset 1 and Dataset 2 Columns"""

df1.columns

df1.drop(['NewCases','NewDeaths', 'NewRecovered'], axis=1, inplace=True)

df1.head()

"""Creating Tables"""

from plotly.figure_factory import create_table
table=create_table(df1.head(10), colorscale="blues")
py.iplot(table)

"""### Task 3: Quick Visualizations with Custom Bar Charts"""

#dataset 1, x,y,color,height,hover_data
df1.columns

"""Total Cases vs Countries

Total Death vs Countries
"""

px.bar(df1.head(10), x='Country/Region', y='TotalDeaths', color='Country/Region', height=500, hover_data=['Country/Region', 'Continent'])

"""Total Recovered vs Countries"""

px.bar(df1.head(10), x='Country/Region', y='TotalRecovered', color='TotalRecovered', height=500, hover_data=['Country/Region', 'Continent'])

"""Total Tests vs Countries (Orientation)"""

px.bar(df1.head(10), x='TotalTests', y='Country/Region', color='TotalTests', orientation="h",height=500, hover_data=['Country/Region', 'Continent'])

px.bar(df1.head(10), x='TotalTests', y='Continent', color='TotalTests', orientation="h",height=500, hover_data=['Country/Region', 'Continent'])

"""## Task 4: Data Visualization using Bubble Chart"""

# px.scatter, x,y, size, color, hover_data, size_max, log_x,log_y
df1.columns

"""Total Cases vs Continent (50 countries)"""

px.scatter(df1, x='Continent',y='TotalCases', hover_data=['Country/Region', 'Continent'], 
           color='TotalCases', size='TotalCases', size_max=80)

px.scatter(df1.head(57), x='Continent',y='TotalCases', hover_data=['Country/Region', 'Continent'], 
           color='TotalCases', size='TotalCases', size_max=80, log_y=True)

"""Total Tests vs Continent (50 countries)"""

px.scatter(df1.head(54), x='Continent',y='TotalTests', hover_data=['Country/Region', 'Continent'], 
           color='TotalTests', size='TotalTests', size_max=80)

px.scatter(df1.head(50), x='Continent',y='TotalTests', hover_data=['Country/Region', 'Continent'], 
           color='TotalTests', size='TotalTests', size_max=80, log_y=True)

"""Total Deaths vs Continent (20 countries)"""

px.scatter(df1.head(50), x='Continent',y='TotalDeaths', hover_data=['Country/Region', 'Continent'], 
           color='TotalDeaths', size='TotalDeaths', size_max=80, log_y=True)

"""Total Cases vs Countries (All Countries)"""



px.scatter(df1.head(100), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'],
           color='TotalCases', size='TotalCases', size_max=80)

"""Total Cases vs Countries (Top 30)"""

px.scatter(df1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size='TotalCases', size_max=80, log_y=True)

df1.columns

"""Total death vs Countries (Top 10)"""

px.scatter(df1.head(10), x='Country/Region', y= 'TotalDeaths', hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size= 'TotalDeaths', size_max=80)

"""Total Tests/1M vs Countries (Top 50)"""

px.scatter(df1.head(30), x='Country/Region', y= 'Tests/1M pop', hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size= 'Tests/1M pop', size_max=80)

px.scatter(df1.head(30), x='Country/Region', y= 'Tests/1M pop', hover_data=['Country/Region', 'Continent'],
           color='Tests/1M pop', size= 'Tests/1M pop', size_max=80)

df1.columns

"""Total case vs Total death"""

px.scatter(df1.head(30), x='TotalCases', y= 'TotalDeaths', hover_data=['Country/Region', 'Continent'],
           color='TotalDeaths', size= 'TotalDeaths', size_max=80)

px.scatter(df1.head(30), x='TotalCases', y= 'TotalDeaths', hover_data=['Country/Region', 'Continent'],
           color='TotalDeaths', size= 'TotalDeaths', size_max=80, log_x=True, log_y=True)

"""Total test vs Total cases"""

px.scatter(df1.head(30), x='TotalTests', y= 'TotalCases', hover_data=['Country/Region', 'Continent'],
           color='TotalTests', size= 'TotalTests', size_max=80, log_x=True, log_y=True)

"""## Advanced Data Visualization using Line graph & Bar graph (Dataset 2)"""

# This Dataset contains DATE column which makes it more appropriate for more advanced Data Visualization

df2.columns

df2.head()

df2.tail()

"""Date Vs Confirmed (All Countries)"""

px.bar(df2, x="Date", y="Confirmed", color="Confirmed", hover_data=["Confirmed", "Date", "Country/Region"], height=400)

px.bar(df2, x="Date", y="Confirmed", color="Confirmed", hover_data=["Confirmed", "Date", "Country/Region"],log_y=True, height=400)

"""Date vs Death (All countries)[Line Graph]"""

px.bar(df2, x="Date", y="Deaths", color="Deaths", hover_data=["Confirmed", "Date", "Country/Region"],log_y=False, height=400)

df_US= df2.loc[df2["Country/Region"]=="US"]

"""Date Vs Confirmed (US)"""

px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400)

"""Date vs Recovered (US)"""

px.bar(df_US,x="Date", y="Recovered", color="Recovered", height=400)

"""Date vs Death (US)"""

px.line(df_US,x="Date", y="Recovered", height=400)

px.line(df_US,x="Date", y="Deaths", height=400)

px.line(df_US,x="Date", y="Confirmed", height=400)

"""Date vs New Cases (US)[Line graph]"""

px.line(df_US,x="Date", y="New cases", height=400)

px.bar(df_US,x="Date", y="New cases", height=400)

"""Date Vs New cases (India) [Line graph]"""

df_india= df2.loc[df2["Country/Region"]== "India"]

px.bar(df_india, x="Date", y="New cases", height=400)

px.line(df_india, x="Date", y="New cases", height=400)

"""Date Vs Confirmed (India)"""

px.bar(df_india, x="Date", y="Confirmed", height=400)

"""Date Vs New Death (India)"""

px.bar(df_india, x="Date", y="Deaths", height=400)

px.bar(df_india, x="Date", y="New deaths", height=400)

px.bar(df_india, x="Date", y="Recovered", height=400)

px.bar(df_india, x="Date", y="New recovered", height=400)

px.scatter(df_US, x="Confirmed", y="Deaths", height=400)

px.scatter(df_india, x="Confirmed", y="New cases", height=400)

"""# Task 6: Represent Geographic Data as Choropleth Maps"""

# A choropleth map displays divided geographical areas or regions that are coloured, shaded or patterned in relation to a data variable.
#Dataset 2
#parameters= dataset, locations= ISOALPHA, color, hover_name, color_continuous_scale= [RdYlGn, Blues, Viridis...], animation_frame= Date

#Amazing Representation of data in a map . Choropleth maps provide an easy way to visualize how a measurement varies across a geographic area.

#Equi-rectangular Projection: Total cases
px.choropleth(df2,
              locations="iso_alpha",
              color="Confirmed",
              hover_name="Country/Region", 
              color_continuous_scale="Blues",
              animation_frame="Date")



px.choropleth(df2,
              locations='iso_alpha',
              color="Deaths",
              hover_name="Country/Region",
              color_continuous_scale="Viridis",
              animation_frame="Date" )

"""Orthographic Projection : Total Death"""

px.choropleth(df2,
              locations='iso_alpha',
              color="Deaths",
              hover_name="Country/Region",
              color_continuous_scale="Viridis",
              projection="orthographic",
              animation_frame="Date" )

"""Equirectangular Projection : Total Recovered"""

px.choropleth(df2,
              locations='iso_alpha',
              color="Recovered",
              hover_name="Country/Region",
              color_continuous_scale="RdYlGn",
              projection="natural earth",
              animation_frame="Date" )



"""## Task 7: Animations"""

#px.bar (data, x,y, color, hover_name, animation_frame)
#px.scatter (data, x,y, color, hover_name, animation_frame, size, size_max)

"""Bar Animation : Total Cases"""

px.bar(df2, x="WHO Region", y="Confirmed", color="WHO Region", animation_frame="Date", hover_name="Country/Region")

"""Bar Animation : New cases"""

px.bar(df2, x="WHO Region", y="New cases", color="WHO Region", animation_frame="Date", hover_name="Country/Region")



"""## Bonus Lecture : WordCloud (Reasons of Death) (New dataset-3)"""

#Step 1. Importing WordCloud and datasets
#Step 2. Exploring data  using pandas                       #NEW DATASET 3
#Step 3. Creating WordCloud

#Step3a= Convert the column with diseases count into list using tolist() function
#Step3b= Convert the list to one single string
#Step3x= Convert the string into WordCloud

from wordcloud import WordCloud


df3= pd.read_csv("covid death.csv")
df3.head()

df3.tail()

df3.groupby(["Condition"]).count()

df3.groupby(["Condition Group"]).count()

#Step 3 : WordCloud 1

#Step3a= Convert the column with diseases count into list using tolist() function

sentences= df3["Condition"].tolist()

#Step3b= Convert the list to one single string

sentences_as_a_string= ' '.join(sentences)

#Step3c= Convert the string into WordCloud

plt.figure(figsize=(14,14))
plt.imshow(WordCloud().generate(sentences_as_a_string))

#Step 3 : WordCloud 2- "Condition Group" column

#Step3a= Convert the column with diseases count into list using tolist() function

column2_tolist= df3["Condition Group"].tolist()

#Step3b= Convert the list to one single string

column_to_string= " ".join(column2_tolist)

#Step3c= Convert the string into WordCloud

plt.figure(figsize=(20,20))
plt.imshow(WordCloud().generate(column_to_string))

