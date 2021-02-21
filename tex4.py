import plotly.express as px
df = px.data.tips()

df = px.data.gapminder().query("year==2007 and continent=='Americas'")


fig = px.scatter(df, x="gdpPercap", y="lifeExp", text="country", log_x=True, size_max=100, color="lifeExp")
fig.update_traces(textposition='top center')
fig.update_layout(title_text='Life Expectency', title_x=0.5)
fig.show()