import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])
server = app.server

app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            [
            html.Title('Brooklyn House Price Prediction'),
                html.H1('Brooklyn House Prices'),
            html.Header('Use this app to predict House Prices in Brooklyn')
            ]
        ),
        dbc.Row([
            dbc.Col([
                dbc.Form([
                    html.Label("Neighborhood of the house ", className="text-primary"),
                    dcc.Dropdown(
                        id="neighborhood",
                        options=[
                            {"label": "BAY RIDGE", "value": "BAY RIDGE"},
                            {"label": "BEDFORD STUYVESANT", "value": "BEDFORD STUYVESANT"},
                            {"label": "BENSONHURST", "value": "BENSONHURST"},
                            {"label": "BOROUGH PARK", "value": "BOROUGH PARK"},
                            {"label": "BRIGHTON BEACH", "value": "BRIGHTON BEACH"},
                            {"label": "BROOKLYN HEIGHTS", "value": "BROOKLYN HEIGHTS"},
                            {"label": "BUSHWICK", "value": "BUSHWICK"},
                            {"label": "CANARSIE", "value": "CANARSIE"},
                            {"label": "CLINTON HILL", "value": "CLINTON HILL"},
                            {"label": "CROWN HEIGHTS", "value": "CROWN HEIGHTS"},
                            {"label": "CYPRESS HILLS", "value": "CYPRESS HILLS"},
                            {"label": "EAST NEW YORK", "value": "EAST NEW YORK"},
                            {"label": "FLATBUSH-CENTRAL", "value": "FLATBUSH-CENTRAL"},
                            {"label": "FLATBUSH-EAST", "value": "FLATBUSH-EAST"},
                            {"label": "FLATBUSH-NORTH", "value": "FLATBUSH-NORTH"},
                            {"label": "GRAVESEND", "value": "GRAVESEND"},
                            {"label": "GREENPOINT", "value": "GREENPOINT"},
                            {"label": "MADISON", "value": "MADISON"},
                            {"label": "MARINE PARK", "value": "MARINE PARK"},
                            {"label": "MIDWOOD", "value": "MIDWOOD"},
                            {"label": "OCEAN HILL", "value": "OCEAN HILL"},
                            {"label": "OCEAN PARKWAY-NORTH", "value": "OCEAN PARKWAY-NORTH"},
                            {"label": "OCEAN PARKWAY-SOUTH", "value": "OCEAN PARKWAY-SOUTH"},
                            {"label": "PARK SLOPE", "value": "PARK SLOPE"},
                            {"label": "SHEEPSHEAD BAY", "value": "SHEEPSHEAD BAY"},
                            {"label": "SUNSET PARK", "value": "SUNSET PARK"},
                            {"label": "WILLIAMSBURG-EAST", "value": "WILLIAMSBURG-EAST"},
                            {"label": "OTHER", "value": "OTHER"}
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("No of Residential Units on the tax lot", className="text-primary"),
                    dcc.Dropdown(
                        id="res-units",
                        options=[
                            {"label": "0", "value": 0},
                            {"label": "1", "value": 1},
                            {"label": "2", "value": 2},
                            {"label": "3", "value": 3},
                            {"label": "3.5", "value": 3.5},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("Land Area", className="text-primary"),
                    dbc.Input(id="land-sqft", placeholder="in Sq.ft min-0, max-6150", min=0, max=6150,
                              type="number", className="form-control"),
                ]),
                dbc.Form([
                    html.Label("Tax Class at Sale", className="text-primary"),
                    dcc.Dropdown(
                        id="tax-class",
                        options=[
                            {"label": "0", "value": 0},
                            {"label": "1", "value": 1},
                            {"label": "2", "value": 2},
                            {"label": "3.5", "value": 3.5},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("Building Class at Sale", className="text-primary"),
                    dcc.Dropdown(
                        id="building-class",
                        options=[
                            {"label": "A1", "value": "A1"},
                            {"label": "A5", "value": "A5"},
                            {"label": "A9", "value": "A9"},
                            {"label": "B1", "value": "B1"},
                            {"label": "B2", "value": "B2"},
                            {"label": "B3", "value": "B3"},
                            {"label": "B9", "value": "B9"},
                            {"label": "C0", "value": "C0"},
                            {"label": "C1", "value": "C1"},
                            {"label": "C2", "value": "C2"},
                            {"label": "C3", "value": "C3"},
                            {"label": "C6", "value": "C6"},
                            {"label": "D4", "value": "D4"},
                            {"label": "S2", "value": "S2"},
                            {"label": "OTHER", "value": "OTHER"},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("Split Zone", className="text-primary"),
                    dcc.Dropdown(
                        id="split-zone",
                        options=[
                            {"label": "Yes", "value": "Y"},
                            {"label": "No", "value": "N"},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
            ]),
            dbc.Col([
                dbc.Form([
                    html.Label("Lot Area", className="text-primary"),
                    dbc.Input(id="lot-area", placeholder="in Sq.ft min-0, max-7800", min=0, max=7800,
                              type="number", className="form-control"),
                ]),
                dbc.Form([
                    html.Label("Lot Depth", className="text-primary"),
                    dbc.Input(id="lot-depth", placeholder="min-99.7, max-100.42", min=0, max=7800,
                              type="number", className="form-control"),
                ]),
                dbc.Form([
                    html.Label("Proximity Code", className="text-primary"),
                    dcc.Dropdown(
                        id="prox-code",
                        options=[
                            {"label": "Not available", "value": 0},
                            {"label": "Detached", "value": 1},
                            {"label": "Semi-attached", "value": 2},
                            {"label": "Attached", "value": 3},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("Irregular Lot?", className="text-primary"),
                    dcc.Dropdown(
                        id="irr-lot-code",
                        options=[
                            {"label": "Yes", "value": "Y"},
                            {"label": "No", "value": "N"},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("Basement", className="text-primary"),
                    dcc.Dropdown(
                        id="basement-code",
                        options=[
                            {"label": "None/No Basement", "value": 0},
                            {"label": "Above grade full basement", "value": 1},
                            {"label": "Below grade full basement", "value": 2},
                            {"label": "Above grade partial basement", "value": 3},
                            {"label": "Below grade partial basement", "value": 4},
                            {"label": "Unknown", "value": 5},
                        ],
                        value="Select",
                        className="form-control"
                    ),
                ]),
                dbc.Form([
                    html.Label("Resid FAR", className="text-primary"),
                    dbc.Input(id="resid-far", placeholder="min-0, max-4.75", min=0, max=4.725,
                              type="number", className="form-control"),
                ]),
                dbc.Form([
                    html.Label("Age of the House", className="text-primary"),
                    dbc.Input(id="age", placeholder="min-17, max-136", min=17, max=136,
                              type="number", className="form-control"),
                ]),
            ])
                ]),
            dbc.Button("Predict Price of the House", id='submit-button', className="btn btn-secondary my-2 my-sm-0",
                       n_clicks=0, style={'text-align': 'center', 'margin': 'auto', 'display':'flex', 'padding': '10px'}),
            html.Div(id='outputs', className='alert alert-dismissible alert-light', style={'text-align': 'center'})
    ]
)

@app.callback(
    Output('outputs', 'children'),
    Input('submit-button', 'n_clicks'),
    State('neighborhood', 'value'),
    State('res-units', 'value'),
    State('land-sqft', 'value'),
    State('tax-class', 'value'),
    State('building-class', 'value'),
    State('split-zone', 'value'),
    State('lot-area', 'value'),
    State('lot-depth', 'value'),
    State('prox-code', 'value'),
    State('irr-lot-code', 'value'),
    State('basement-code', 'value'),
    State('resid-far', 'value'),
    State('age', 'value'),
)
def predict_house_price(n_clicks, neighborhood, residential_units, land_sqft, tax_class_at_sale,
                        building_class_at_sale, SplitZone, LotArea, LotDepth,
                        ProxCode, IrrLotCode, BsmtCode, ResidFAR, age):

    if n_clicks == 0:
        return html.Div()

    params_dict = {
        'neighborhood': neighborhood,
        'residential_units': residential_units,
        'land_sqft': land_sqft,
        'tax_class_at_sale': tax_class_at_sale,
        'building_class_at_sale': building_class_at_sale,
        'SplitZone': SplitZone,
        'LotArea': LotArea,
        'LotDepth': LotDepth,
        'ProxCode': ProxCode,
        'IrrLotCode': IrrLotCode,
        'BsmtCode': BsmtCode,
        'ResidFAR': ResidFAR,
        'age': age
    }
    # print(params_dict)
    df = pd.DataFrame(params_dict, index=[0])

    with open('xgboost.pkl', 'rb') as f:
        xgb = joblib.load(f)
    try:
        xgb_pred = np.exp(xgb.predict(df)).round(2)
    except ValueError as e:
        return "Please Enter all the fields"

    return f"The Predicted House Price is ${xgb_pred[0]}"

if __name__ == "__main__":
    app.run_server()