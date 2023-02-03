import plotly.graph_objects as go


from data.data import raw_data

__data = raw_data.copy()

__mapping = {
    'amount': 'sum',
    'id': 'count'
}

__rename = {
    'amount': 'total_amount',
    'id': 'total_transactions'
}

__data = __data.groupby([__data.type]).agg(__mapping).rename(__rename, axis=1).reset_index()

figure = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=list(__data.columns),
                fill_color='blue',
                align='center',
                font={'color': 'white', 'size': 12},
                height = 40,
            ),
            cells=dict(
                values=[__data.type, __data.total_amount, __data.total_transactions],
                fill=dict(color=['paleturquoise', 'white', 'white']),
                align='center',
                height=25
            )
        ),
    ],
)

figure.update_layout(
    width=525,
    height=100,
    paper_bgcolor='black',
    margin={
        'l': 5,
        't': 5,
        'r': 5,
        'b': 5,
        'pad': 0
    }
)

