# import requests
# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.express as px

# # 🔗 Change URL to your MVC API endpoint
# API_URL = "http://localhost:5279/  Employees/GetEmployeesJson"

# # create dash app
# app = Dash(__name__)

# def load_data(): 
#     data = requests.get(API_URL).json()
#     df = pd.DataFrame(data)  
                           
#     # convert join date to year
#     df["join_year"] = pd.to_datetime(df["join_date"]).dt.year   
 
#     # group salary by year (sum or avg)
#     grouped = df.groupby("join_year")["salary"].sum().reset_index()     
#     grouped["salary"] = grouped["salary"] / 100
#     return grouped
                                                                                      
# df = load_data()                                                                                                                               
                              
# fig = px.line(                 
#     df,                    
#     x="join_year",                      
#     y="salary",       
#     title="Employee Salary Trend by Year",  
#     markers=True    
# )                

# fig.update_layout(
#     yaxis=dict(
#         title="Salary (in thousandS)", tickformat=",", tickprefix="₹" 
#     )
# ) 
            
# app.layout = html.Div(children=[
#     html.H1("Employee Salary Line Graph"),
#     dcc.Graph(id="salary-graph", figure=fig)  
# ])             

# if __name__ == "__main__":             
#     app.run(host="localhost", port=8050, debug=True)





# import requests
# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.express as px

# # 🔗 MVC API URL (MAKE SURE MVC APP IS RUNNING)
# API_URL = "http://localhost:5279/Employees/GetEmployeesJson"

# # create Dash app
# app = Dash(__name__)

# def load_data():
#     # call MVC API
#     response = requests.get(API_URL)

#     if response.status_code != 200:
#         raise Exception(f"API Error: {response.status_code}")

#     data = response.json()
#     df = pd.DataFrame(data)

#     # 🔧 FIX column names from MVC (camelCase → PascalCase)
#     df.rename(columns={
#         "prev_Year_sal": "Prev_Year_sal",
#         "current_Year_sal": "Current_Year_sal"
#     }, inplace=True)

#     # convert join_date to year
#     df["join_year"] = pd.to_datetime(df["join_date"]).dt.year

#     # calculate salary difference
#     df["salary_diff"] = df["Current_Year_sal"] - df["Prev_Year_sal"]

#     # group by join year
#     grouped = df.groupby("join_year").agg(
#         Prev_Year_sal=("Prev_Year_sal", "mean"),
#         Current_Year_sal=("Current_Year_sal", "mean"),
#         Avg_Diff=("salary_diff", "mean")
#     ).reset_index()

#     return grouped

# # load data                                  
# df = load_data()                         
                        
# # 📊 BAR GRAPH → Previous Year Salary
# bar_fig = px.bar(
#     df,
#     x="join_year",
#     y="Prev_Year_sal",
#     title="Previous Year Salary (Bar Graph)",
#     color="join_year"
# )

# # 📈 LINE GRAPH → Current Year Salary
# line_fig = px.line(
#     df,
#     x="join_year",           
#     y="Current_Year_sal",                          
#     title="Current Year Salary (Line Graph)",               
#     markers=True
# )

# # 📉 Average Salary Difference
# avg_diff = round(df["Avg_Diff"].mean(), 2)

# # layout
# app.layout = html.Div([
#     html.H1("Employee Salary Analysis Dashboard"),

#     dcc.Graph(figure=bar_fig),
#     dcc.Graph(figure=line_fig),

#     html.H3(f"Average Salary Difference: ₹ {avg_diff}")
# ])

# # run app
# if __name__ == "__main__":
#     app.run(host="localhost", port=8050, debug=True)



# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.graph_objects as go

# # Your full employee data example (adjust with real data)
# data = {
#     "ID": [901, 902, 903, 904, 905, 906],
#     "Name": ["RAJ", "ANU", "RAHUL", "rakul", "RAMAN", "RAM"],
#     "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
#     "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
#     "Previous Date": [
#         "01-12-2025 00:00:00",
#         "05-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "02-12-2025 00:00:00",
#         "04-12-2025 00:00:00",
#     ],
#     "Current Date": [
#         "02-01-2025 00:00:00",
#         "10-10-2024 00:00:00",
#         "12-01-2024 00:00:00",
#         "24-05-2025 00:00:00",
#         "01-02-2025 00:00:00",
#         "02-01-2024 00:00:00",
#     ],
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Convert dates to datetime
# df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
# df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")

# # Initialize Dash app
# app = Dash(__name__)

# # Bar chart for previous salaries
# bar_prev = go.Bar(
#     x=df["Name"],
#     y=df["Previous Salary"],
#     name="Previous Salary",
#     marker_color="lightblue",
# )

# # Bar chart for current salaries
# bar_curr = go.Bar(
#     x=df["Name"],
#     y=df["Current Salary"],
#     name="Current Salary",
#     marker_color="orange",
# )

# # Line chart showing salary change for each employee as line segments connecting previous and current salary
# lines = []
# for i, row in df.iterrows():
#     lines.append(
#         go.Scatter(
#             x=[row["Name"], row["Name"]],
#             y=[row["Previous Salary"], row["Current Salary"]],
#             mode="lines+markers",
#             line=dict(color="green", width=3),
#             marker=dict(size=8),
#             showlegend=False,
#         )
#     )

# # Annotations to show the Previous Date and Current Date above respective bars
# annotations = []
# for i, row in df.iterrows():
#     annotations.append(
#         dict(
#             x=row["Name"],
#             y=row["Previous Salary"],
#             text=row["Previous Date"].strftime("%d-%m-%Y"),
#             showarrow=False,
#             yshift=15,
#             font=dict(color="blue", size=10),
#         )
#     )
#     annotations.append(
#         dict(
#             x=row["Name"],
#             y=row["Current Salary"],
#             text=row["Current Date"].strftime("%d-%m-%Y"),
#             showarrow=False,
#             yshift=15,
#             font=dict(color="darkorange", size=10),
#         )
#     )

# # Layout setup
# layout = go.Layout(
#     title="Previous and Current Salaries with Salary Change per Employee",
#     barmode="group",
#     yaxis=dict(title="Salary", rangemode="tozero"),
#     annotations=annotations,
#     xaxis=dict(title="Employee Name"),
# )

# # Compose figure with bars and line segments
# fig = go.Figure(data=[bar_prev, bar_curr] + lines, layout=layout)

# # Dash app layout
# app.layout = html.Div(
#     [
#         html.H1("Employee Salary Analysis"),
#         dcc.Graph(figure=fig),
#     ]
# )

# if __name__ == "__main__":
#     app.run(host="localhost", port=8050, debug=True)




# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.graph_objects as go

# # Employee data
# data = {
#     "ID": [901, 902, 903, 904, 905, 906],
#     "Name": ["RAJ", "ANU", "RAHUL", "rakul", "RAMAN", "RAM"],
#     "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
#     "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
#     "Previous Date": [
#         "01-12-2025 00:00:00",
#         "05-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "02-12-2025 00:00:00",
#         "04-12-2025 00:00:00",
#     ],
#     "Current Date": [
#         "02-01-2025 00:00:00",
#         "10-10-2024 00:00:00",
#         "12-01-2024 00:00:00",
#         "24-05-2025 00:00:00",
#         "01-02-2025 00:00:00",
#         "02-01-2024 00:00:00",
#     ],
# }

# df = pd.DataFrame(data)
# df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
# df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")

# # Dash app
# app = Dash(__name__)

# # Histogram bars
# bar_prev = go.Bar(
#     x=df["Name"],
#     y=df["Previous Salary"],
#     name="Previous Salary",
#     marker_color="blue",
# )
# bar_curr = go.Bar(
#     x=df["Name"],
#     y=df["Current Salary"],
#     name="Current Salary",
#     marker_color="pink",
# )

# # Line points showing ups/down above histogram
# # We'll place them slightly above the maximum salary for visibility
# max_salary = df[["Previous Salary", "Current Salary"]].max().max()
# line_y = df["Current Salary"] - df["Previous Salary"]  # Salary change
# # Shift line above bars for visualization
# line_y_shifted = max_salary + 5000 + line_y  # Add offset

# line = go.Scatter(
#     x=df["Name"],
#     y=line_y_shifted,
#     mode="lines+markers+text",
#     name="Salary Change",
#     line=dict(color="green", width=3),
#     marker=dict(size=10),
#     text=[f"{val:+}" for val in line_y],  # Show + or - values
#     textposition="top center",
# )

# # Annotations for Previous/Current Dates above bars
# annotations = []
# for i, row in df.iterrows():
#     annotations.append(dict(
#         x=row["Name"],
#         y=row["Previous Salary"],
#         text=row["Previous Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="blue", size=10)
#     ))
#     annotations.append(dict(
#         x=row["Name"],
#         y=row["Current Salary"],
#         text=row["Current Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="darkorange", size=10)
#     ))

# # Layout
# layout = go.Layout(
#     title="Employee Salaries with Salary Change Line Above Histogram",
#     barmode="group",
#     yaxis=dict(title="Salary", rangemode="tozero"),
#     annotations=annotations,
# )

# # Combine figure
# fig = go.Figure(data=[bar_prev, bar_curr, line], layout=layout)

# # Dash layout
# app.layout = html.Div([
#     html.H1("Employee Salary Analysis"),
#     dcc.Graph(figure=fig)
# ])

# if __name__ == "__main__":
#     app.run(host="localhost", port=8050, debug=True)



# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.graph_objects as go

# # Employee data
# data = {
#     "ID": [901, 902, 903, 904, 905, 906],
#     "Name": ["RAJ", "ANU", "RAHUL", "rakul", "RAMAN", "RAM"],
#     "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
#     "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
#     "Previous Date": [
#         "01-12-2025 00:00:00",
#         "05-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "02-12-2025 00:00:00",
#         "04-12-2025 00:00:00",
#     ],
#     "Current Date": [
#         "02-01-2025 00:00:00",
#         "10-10-2024 00:00:00",
#         "12-01-2024 00:00:00",
#         "24-05-2025 00:00:00",
#         "01-02-2025 00:00:00",
#         "02-01-2024 00:00:00",
#     ],
# }

# df = pd.DataFrame(data)
# df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
# df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")

# # Dash app
# app = Dash(__name__)

# # Histogram bars
# bar_prev = go.Bar(
#     x=df["Name"],
#     y=df["Previous Salary"],
#     name="Previous Salary",
#     marker_color="blue",
# )
# bar_curr = go.Bar(
#     x=df["Name"],
#     y=df["Current Salary"],
#     name="Current Salary",
#     marker_color="pink",

# # Calculate max salary for offset
# max_salary = df[["Previous Salary", "Current Salary"]].max().max()

# # Salary difference (for text and color)
# line_y_diff = df["Current Salary"] - df["Previous Salary"]

# # Shift line points visually above bars
# line_y_shifted = max_salary + 5000 + line_y_diff

# # Create custom hover text to show actual salary, not shifted y
# hover_texts = [
#     f"{name}<br>Salary Change: {diff:+}<br>Actual Current Salary: {curr}"
#     for name, diff, curr in zip(df["Name"], line_y_diff, df["Current Salary"])
# ]

# # Line trace with shifted y but hover showing actual salary
# line = go.Scatter(
#     x=df["Name"],
#     y=line_y_shifted,
#     mode="lines+markers+text",
#     name="Salary Change",
#     line=dict(color="green", width=3),
#     marker=dict(size=10),
#     text=[f"{val:+}" for val in line_y_diff],  # Show + or - values above points
#     textposition="top center",
#     hoverinfo="text",
#     hovertext=hover_texts,
# )

# # Annotations for Previous/Current Dates above bars
# annotations = []
# for i, row in df.iterrows():
#     annotations.append(dict(
#         x=row["Name"],
#         y=row["Previous Salary"],
#         text=row["Previous Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="blue", size=10)
#     ))
#     annotations.append(dict(
#         x=row["Name"],
#         y=row["Current Salary"],
#         text=row["Current Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="darkorange", size=10)
#     ))

# # Layout
# layout = go.Layout(
#     title="Employee Salaries with Salary Change Line Above Histogram",
#     barmode="group",
#     yaxis=dict(title="Salary", rangemode="tozero"),
#     annotations=annotations,
# )

# # Combine figure
# fig = go.Figure(data=[bar_prev, bar_curr, line], layout=layout)

# # Dash layout
# app.layout = html.Div([
#     html.H1("Employee Salary Analysis"),
#     dcc.Graph(figure=fig)
# ])

# if __name__ == "__main__":
#     app.run(host="localhost", port=8050, debug=True)




# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.graph_objects as go

# # Employee data
# data = {
#     "ID": [901, 902, 903, 904, 905, 906],
#     "Name": ["RAJ", "ANU", "RAHUL", "rakul", "RAMAN", "RAM"],
#     "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
#     "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
#     "Previous Date": [
#         "01-12-2025 00:00:00",
#         "05-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "02-12-2025 00:00:00",
#         "04-12-2025 00:00:00",
#     ],
#     "Current Date": [
#         "02-01-2025 00:00:00",
#         "10-10-2024 00:00:00",
#         "12-01-2024 00:00:00",
#         "24-05-2025 00:00:00",
#         "01-02-2025 00:00:00",
#         "02-01-2024 00:00:00",
#     ],
# }

# df = pd.DataFrame(data)
# df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
# df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")

# app = Dash(__name__)

# bar_prev = go.Bar(
#     x=df["Name"],
#     y=df["Previous Salary"],
#     name="Previous Salary",
#     marker_color="blue",
# )
# bar_curr = go.Bar(
#     x=df["Name"],
#     y=df["Current Salary"],
#     name="Current Salary",
#     marker_color="pink",
# )

# max_salary = df[["Previous Salary", "Current Salary"]].max().max()
# line_y_diff = df["Current Salary"] - df["Previous Salary"]
# line_y_shifted = max_salary + 5000 + line_y_diff

# hover_texts = [
#     f"{name}<br>Salary Change: {diff:+}<br>Actual Current Salary: {curr}"
#     for name, diff, curr in zip(df["Name"], line_y_diff, df["Current Salary"])
# ]

# line = go.Scatter(
#     x=df["Name"],
#     y=line_y_shifted,
#     mode="lines+markers+text",
#     name="Salary Change",
#     line=dict(color="green", width=3),
#     marker=dict(size=10),
#     text=[f"{curr}" for curr in df["Current Salary"]],  # Show actual salary as label
#     textposition="top center",
#     hoverinfo="text",
#     hovertext=hover_texts,
# )

# annotations = []
# for i, row in df.iterrows():
#     annotations.append(dict(
#         x=row["Name"],
#         y=row["Previous Salary"],
#         text=row["Previous Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="blue", size=10)
#     ))
#     annotations.append(dict(
#         x=row["Name"],
#         y=row["Current Salary"],
#         text=row["Current Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="darkorange", size=10)
#     ))

# layout = go.Layout(
#     title="Employee Salaries with Salary Change Line Above Histogram",
#     barmode="group",
#     yaxis=dict(title="Salary", rangemode="tozero"),
#     annotations=annotations,
# )

# fig = go.Figure(data=[bar_prev, bar_curr, line], layout=layout)

# app.layout = html.Div([
#     html.H1("Employee Salary Analysis"),
#     dcc.Graph(figure=fig)
# ])

# if __name__ == "__main__":
#     app.run(host="localhost", port=8050, debug=True)




# import pandas as pd
# from dash import Dash, dcc, html
# import plotly.graph_objects as go

# # Employee data
# data = {
#     "ID": [901, 902, 903, 904, 905, 906],
#     "Name": ["RAJ", "ANU", "RAHUL", "RAKUL", "RAMAN", "RAM"],
#     "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
#     "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
#     "Previous Date": [
#         "01-12-2025 00:00:00",
#         "05-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "01-12-2025 00:00:00",
#         "02-12-2025 00:00:00",
#         "04-12-2025 00:00:00",
#     ],
#     "Current Date": [
#         "02-01-2025 00:00:00",
#         "10-10-2024 00:00:00",
#         "12-01-2024 00:00:00",
#         "24-05-2025 00:00:00",
#         "01-02-2025 00:00:00",
#         "02-01-2024 00:00:00",
#     ],
# }

# df = pd.DataFrame(data)
# df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
# df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")

# app = Dash(__name__)

# # Bars for Previous and Current Salary
# bar_prev = go.Bar(
#     x=df["Name"],
#     y=df["Previous Salary"],
#     name="Previous Salary",
#     marker_color="blue",
# )
# bar_curr = go.Bar(
#     x=df["Name"],
#     y=df["Current Salary"],
#     name="Current Salary",
#     marker_color="pink",
# )

# max_salary = df[["Previous Salary", "Current Salary"]].max().max()
# line_y_diff = df["Current Salary"] - df["Previous Salary"]
# line_y_shifted = max_salary + 5000 + line_y_diff

# hover_texts = [
#     f"{name}<br>Salary Change: {diff:+}<br>Actual Current Salary: {curr}"
#     for name, diff, curr in zip(df["Name"], line_y_diff, df["Current Salary"])
# ]

# line = go.Scatter(
#     x=df["Name"],
#     y=line_y_shifted,
#     mode="lines+markers+text",
#     name="Salary Change",
#     line=dict(color="green", width=3),
#     marker=dict(size=10),
#     text=[f"{curr}" for curr in df["Current Salary"]],  # Show actual salary as label
#     textposition="top center",
#     hoverinfo="text",
#     hovertext=hover_texts,
# )

# # Calculate numeric x positions for employees (categorical x-axis mapped to numbers)
# name_to_num = {name: i for i, name in enumerate(df["Name"])}

# # Group bar width fraction (approximate)
# group_bar_width = 0.4  # You can adjust this if bars are too wide/narrow

# annotations = []
# for i, row in df.iterrows():
#     base_x = name_to_num[row["Name"]]
    
#     # Previous Salary bar is left bar in group: shift left by half bar width
#     annotations.append(dict(
#         x=base_x - group_bar_width/2,
#         y=row["Previous Salary"],
#         text=row["Previous Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="blue", size=10),
#         xref='x',
#         yref='y',
#         xanchor='center',
#         align='center',
#     ))
    
#     # Current Salary bar is right bar in group: shift right by half bar width
#     annotations.append(dict(
#         x=base_x + group_bar_width/2,
#         y=row["Current Salary"],
#         text=row["Current Date"].strftime("%d-%m-%Y"),
#         showarrow=False,
#         yshift=15,
#         font=dict(color="darkorange", size=10),
#         xref='x',
#         yref='y',
#         xanchor='center',
#         align='center',
#     ))

# layout = go.Layout(
#     title="Employee Salaries with Salary Change Line Above Histogram",
#     barmode="group",
#     yaxis=dict(title="Salary", rangemode="tozero"),
#     xaxis=dict(
#         tickvals=list(name_to_num.values()),
#         ticktext=list(name_to_num.keys())
#     ),
#     annotations=annotations,
# )

# fig = go.Figure(data=[bar_prev, bar_curr, line], layout=layout)

# app.layout = html.Div([
#     html.H1("Employee Salary Analysis"),
#     dcc.Graph(figure=fig)
# ])

# if __name__ == "__main__":
#     app.run(host="localhost", port=8050, debug=True)




import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go

# Employee data
data = {
    "ID": [901, 902, 903, 904, 905, 906],
    "Name": ["RAJ", "ANU", "RAHUL", "RAKUL", "RAMAN", "RAM"],
    "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
    "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
    "Previous Date": [  
        "01-12-2025 00:00:00",
        "05-12-2025 00:00:00",  
        "01-12-2025 00:00:00",
        "01-12-2025 00:00:00",
        "02-12-2025 00:00:00",
        "04-12-2025 00:00:00", 
    ], 
    "Current Date": [ 
        "02-01-2025 00:00:00",  
        "10-10-2024 00:00:00",  
        "12-01-2024 00:00:00",  
        "24-05-2025 00:00:00",
        "01-02-2025 00:00:00",
        "02-01-2024 00:00:00",
    ],
}

df = pd.DataFrame(data)
df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")  
df["Previous Date"]= pd.to_datetime(df["Current Date"],format="%d-%m-%Y %H:%M:%S") 
app = Dash(__name__)
      
# Bars
bar_prev = go.Bar( 
    x=df["Name"],        
    y=df["Previous Salary"],        
    name="Previous Salary",      
    marker_color="lightblue",    
)              
bar_curr = go.Bar(
    x=df["Name"],                                     
    y=df["Current Salary"],                               
    name="Current Salary",   
    marker_color="pink",     
)                                         

# ✅ Salary Difference (ACTUAL values)                
df["Salary Difference"] = df["Current Salary"] - df["Previous Salary"]                  

line = go.Scatter(    
    x=df["Name"],   
    y=df["Salary Difference"],   # 👈 NO shifting                                                                
    mode="lines+markers+text",
    name="Salary Difference",               
    line=dict(color="green", width=3),                  
    marker=dict(size=10),                                                         
    text=df["Salary Difference"],            
    textposition="top center",          
)                          
           
# Numeric x positions for precise annotations     
name_to_num = {name: i for i, name in enumerate(df["Name"])}         
group_bar_width = 0.4 
                                

annotations = []     
for _, row in df.iterrows():                 
    base_x = name_to_num[row["Name"]]      
     
    # Previous Date 
    annotations.append(dict(
        x=base_x + group_bar_width / 2,                                                                                  
        y=row["Previous Salary"],                    
        text=row["Previous Date"].strftime("%d-%m-%Y"),                                    
        showarrow=False,                                       
        yshift=15,                                                         
        font=dict(color="blue", size=10),
        xref="x",
        yref="y",      
    ))    
   

    yaxis=dict(title="Salary / Difference", rangemode="tozero"),
    xaxis=dict(     
        tickvals=list(name_to_num.values()),  
        ticktext=list(name_to_num.keys()) 
     ),           
                                                        
layout = go.layout(
    title ="employees salaries with salary difference line",   
    barmode="group",
 
)
  
fig = go.Figure(data=[bar_prev, bar_curr, line], layout=layout)  

app.layout = html.Div([    
    html.H1("Employee salary Analysis"),
    dcc.Graph(figure=fig)    
])                                                                        

if __name__ == "__main__":
    app.run(host="localhost", port=8050, debug=True)



import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go

# Employee data
data = {
    "ID": [901, 902, 903, 904, 905, 906],
    "Name": ["RAJ", "ANU", "RAHUL", "RAKUL", "RAMAN", "RAM"],
    "Previous Salary": [40000, 10000, 25000, 35000, 15000, 20000],
    "Current Salary": [45000, 35000, 30000, 40000, 35000, 25000],
    "Previous Date": [  
        "01-12-2025 00:00:00",
        "05-12-2025 00:00:00",  
        "01-12-2025 00:00:00",
        "01-12-2025 00:00:00",
        "02-12-2025 00:00:00",
        "04-12-2025 00:00:00", 
    ],   
    "Current Date": [ 
        "02-01-2025 00:00:00",
        "10-10-2024 00:00:00",
        "12-01-2024 00:00:00",    
        "24-05-2025 00:00:00",
        "01-02-2025 00:00:00",
        "02-01-2024 00:00:00",
    ],
}

df = pd.DataFrame(data)
df["Previous Date"] = pd.to_datetime(df["Previous Date"], format="%d-%m-%Y %H:%M:%S")
df["Current Date"] = pd.to_datetime(df["Current Date"], format="%d-%m-%Y %H:%M:%S")

app = Dash(__name__)

# Bars 
bar_prev = go.Bar( 
    x=df["Name"],
    y=df["Previous Salary"],
    name="Previous Salary", 
    marker_color="lightblue",     
)              
bar_curr = go.Bar(
    x=df["Name"],                                     
    y=df["Current Salary"],                              
    name="Current Salary",        
    marker_color="pink",     
)                                  

# ✅ Salary Difference (ACTUAL values)
df["Salary Difference"] = df["Current Salary"] - df["Previous Salary"]   

line = go.Scatter( 
    x=df["Name"], 
    y=df["Salary Difference"],   # 👈 NO shifting                                                                
    mode="lines+markers+text",  
    name="Salary Difference", 
    line=dict(color="green", width=3),              
    marker=dict(size=10),                                                         
    text=df["Salary Difference"],         
    textposition="top center",                        
)              
          
# Numeric x positions for precise annotations     
name_to_num = {name: i for i, name in enumerate(df["Name"])}    
group_bar_width = 0.4        
                                
annotations = []    
for _, row in df.iterrows():                 
    base_x = name_to_num[row["Name"]]     
     
    # Previous Date 
    annotations.append(dict(             
        x=base_x + group_bar_width / 2,                                                                              
        y=row["Previous Salary"],                    
        text=row["Previous Date"].strftime("%d-%m-%Y"),                                    
        showarrow=False,                                         
        yshift=15,                                                          
        font=dict(color="blue", size=10),
        xref="x",      
        yref="y",                          
    ))                       
    annotations.append(dict(
        x=base_x + group_bar_width / 2,
        y=row["Current Salary"],  
        text=row["Current Date"].strftime("%d-%m-%Y"),
        showarrow=False,
        yshift=15,                                                           
        font=dict(color="orange", size=10),
        xref="x", 
        yref="y",   
    ))
layout = go.Layout(       
    title="Employees Salaries with Salary Difference Line",
    barmode="group",
    yaxis=dict(title="Salary / Difference", rangemode="tozero"),
    xaxis=dict( 
        tickvals=list(name_to_num.values()), 
        ticktext=list(name_to_num.keys())
        ),     
          annotations=annotations         
)            
         
fig = go.Figure(data=[bar_prev, bar_curr, line], layout=layout) 
app.layout = html.Div([       
    html.H1("Employee salary Analysis"),  
    dcc.Graph(figure=fig)      
])        
                     
if __name__ == "__main__":
    app.run(host="localhost", port=8050, debug=True)    

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    data = response.json() 
    print("Title:", data['title']) 
    print("Completed:", data['completed']) 
else: 
    print("Failed to get data") 


    import pandas as pd  
 
data = {
    'Name': ['Payal', 'Rahul', 'Sneha'],
    'Age': [24, 27, 22],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)  
print(df)  
LookupError("\nAverage DataFrame:", df['group_bar_width'].mean())
print("\nAverage Age:", df['Age'].mean())

    


