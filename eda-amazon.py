import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./amazon.csv', sep =',', parse_dates = ['date'], encoding = 'latin1')

df.head()


# List to categorize the variable "month"
month_cat = ['Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro']

df = df.astype(
    {'year' : 'int' ,
    'state' : 'string'}
)

# Categorize "month"
df['month'] = df['month'].astype('category').cat.set_categories(month_cat)

# Analysis will use data after year 2000
# I'm assuming the first two years of measurement are not robust enough
df = df.query('year >= 2000')


# Quick statistics of column "number" (number of fires reported)
df.number.describe().round(2)

# dataframe grouped by year
df_year = df.groupby('year').sum('number').reset_index().round(2)


# dataframe grouped by State
df_state = (
    df
    .groupby('state')
    .agg(
        fires_reported = ('number', 'sum'),
        mean           = ('number', 'mean'),
        std            = ('number', 'std')
    )
    .sort_values('fires_reported', ascending = False)
    .round(2)
    .reset_index()
)

# Create our statistical dataframe for analysis and plotting
df_stats = (
    df
    .groupby(['year','month','state'])
    .agg(fires_reported = ('number', 'sum'))
    .round(2)
    .reset_index()
)


# I've created a dict to add another variable which is the brazilian region (Portuguese)
regions = {
    'Acre': 'Norte',
    'Alagoas': 'Nordeste',
    'Amapa': 'Norte',
    'Amazonas': 'Norte',
    'Bahia': 'Nordeste',
    'Ceara': 'Nordeste',
    'Distrito Federal': 'Centro-Oeste',
    'Espirito Santo': 'Sudeste',
    'Goias': 'Centro-Oeste',
    'Maranhao': 'Nordeste',
    'Mato Grosso': 'Centro-Oeste',
    'Minas Gerais': 'Sudeste',
    'Paraiba': 'Nordeste',
    'Pará': 'Norte',
    'Pernambuco': 'Nordeste',
    'Piau': 'Nordeste',
    'Rio': 'Sudeste',
    'Rondonia': 'Norte',
    'Roraima': 'Norte',
    'Santa Catarina': 'Sul',
    'Sao Paulo': 'Sudeste',
    'Sergipe': 'Nordeste',
    'Tocantins': 'Norte'
}

# Apply map to create column with the regions of each State
df['region'] = df.state.map(regions).astype('string')


# Dataframe grouped by regions
df_regions = (
    df
    .groupby('region')
    .agg(
        num_states       = ('state', 'nunique'),
        num_reports      = ('region', 'count'),
        fires_reported   = ('number', 'sum'),
        avg_per_report   = ('number', 'mean')
    )
    .assign(avg_per_state = lambda df: df.fires_reported.div(df.num_states))
    .sort_values('avg_per_state', ascending = False)
    .round(2)
    .reset_index()
)



# Plot 1: Quantity of Forest fires reported each year
plt.figure(figsize=(15,10))

sns.lineplot(
    data = df_stats,
    x = 'year',
    y = 'fires_reported',
    estimator = 'sum',
    color = 'red',
    label='N. of Wildifires',
    ci= None
).set_xticks(df_year.year.values)


# Trendline in Black
z = np.polyfit(np.unique(df_year.year),df_year.number, 1)
p = np.poly1d(z)

plt.plot(df_year.year,p(df_year.year),"k--", alpha = 0.5)


plt.title('Total Forest Fires in Brazil (2000 - 2017)', fontsize = 25)
plt.xlabel(None)
plt.ylabel(None)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.xlim(2000, 2017)
plt.show()


# Plot 2 : Boxplot grouped by Month
plt.figure(figsize=(15,10))

sns.boxplot(
    data = df_stats,
    x = 'month',
    y = 'fires_reported',
    palette = 'flare'
)

plt.title('BoxPlot - Total Wildfires by State ', fontsize = 25)
plt.ylabel(None)
plt.xlabel(None)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.show()


# Plot 3 : Distribution of the number of reports (You can adjust the binwidth as you wish)
plt.figure(figsize=(15,5))

sns.histplot(
    x = df.number,
    color = 'red',
    binwidth = 50, # arbitrary number
    kde = True
)

plt.title('Data distribution of Forest Fires reported', fontsize = 25)
plt.ylabel(None)
plt.xlabel(None)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlim(0, 1100)
plt.show()



# Plot 4 : Top 10 States with the highest number of Fires reported
plt.figure(figsize=(15,7))

sns.barplot(
    data = df_state.nlargest(10, 'fires_reported'),
    x = 'fires_reported',
    y = 'state',
    palette = 'rocket',
    orient='h'
)

plt.title('Top 10 - Total Wildfires by State ', fontsize = 25)
plt.ylabel(None)
plt.xlabel(None)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.show()



# Plot 5 : Brazilian Regions in number of Fires reported
plt.figure(figsize=(15,7))

sns.barplot(
    data = df_regions.sort_values('fires_reported', ascending = False),
    x = 'fires_reported',
    y = 'region',
    palette = 'rocket',
    orient='h'
)

plt.title('Total Wildfires by Brazilian Region', fontsize = 25)
plt.ylabel(None)
plt.xlabel(None)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.show()



# Plot 6 : Time-Series of Forest fires by State
plt.figure(figsize=(15,7))

sns.lineplot(
    data = df,
    x = 'date',
    y = 'number',
    hue = 'region',
    estimator = 'sum',
    palette = 'coolwarm',
    ci = None
)

plt.title('Time Series - Total of Wildfires by Region', fontsize = 25)
plt.ylabel(None)
plt.xlabel(None)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.show()
