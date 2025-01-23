import os
import json
from dash import Dash, html, Input, Output, State
import dash_bootstrap_components as dbc

from ai import chat_session


app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Regex Wizard"),
            dbc.Card([
                dbc.CardBody([
                    dbc.Input(id="prompt", placeholder="Enter your prompt here"),
                    dbc.Button("Generate", id="generate"),
                ]),

                dbc.CardBody(id="output")
            ])
        ])
    ])
])


@app.callback(
    Output("output", "children"),
    Input("generate", "n_clicks"),
    State("prompt", "value"),
)
def generate_regex(n_clicks, prompt):
    """ Generate the regex based on the prompt """
    if n_clicks is None:
        return ""

    res = chat_session.send_message(prompt)

    res_data = json.loads(res.text)

    # Call the AI model to generate the regex
    return [
        dbc.Row([
            dbc.Col([
                html.H2("Generated Regex"),
                html.Pre(res_data["regex"]),
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H2("Valid Matches"),
            ] + [html.Pre(m) for m in res_data["valid_matches"]]),
        ]),
        dbc.Row([
            dbc.Col([
                html.H2("Invalid Matches"),
            ] + [html.Pre(m) for m in res_data["invalid_matches"]]),
        ])



    ]


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "localhost"),
        port=os.environ.get("PORT", "8000"),
        debug=os.environ.get("DEBUG", False)
    )
