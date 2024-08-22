import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Create a Dash application
app = dash.Dash(__name__)

# Data
years = ['2018', '2019', '2020', '2021', '2022']
gdp_recession = [2.5, 2.0, -3.0, 1.5, 2.0]  # GDP growth during recession
gdp_non_recession = [3.0, 3.2, 3.5, 2.8, 3.0]  # GDP growth during non-recession

# Set up the layout of the application
app.layout = html.Div([
    html.H1("GDP Growth Comparison: Recession vs Non-Recession"),  # Application title

    dcc.Graph(
        id='gdp-comparison-graph',
        figure={
            'data': [
                go.Scatter(x=years, y=gdp_recession, mode='lines+markers', name='GDP Growth During Recession', line=dict(color='red')),
                go.Scatter(x=years, y=gdp_non_recession, mode='lines+markers', name='GDP Growth During Non-Recession', line=dict(color='green'))
            ],
            'layout': go.Layout(
                title='GDP Growth Comparison: Recession vs Non-Recession',  # Graph title
                xaxis={'title': 'Year'},  # X-axis title
                yaxis={'title': 'GDP Growth (%)'},  # Y-axis title
                legend={'x': 0, 'y': 1.1, 'orientation': 'h'},  # Legend settings
                margin={'l': 40, 'r': 40, 't': 40, 'b': 40}  # Graph margins
            )
        }
    )
])

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
