from dash import html

layout = html.Div([
    html.H2("🏠 国际房价与收入可视化平台", style={"marginTop": "30px"}),
    html.P("本平台基于公开数据，展示各国及美国各州的房价与收入变化趋势，支持多维度对比与预测分析。"),
    html.Hr(),
    html.H4("数据来源"),
    html.Ul([
        html.Li("国际房价与收入数据：世界银行、OECD等公开数据集"),
        html.Li("美国州级数据：美国房地产协会、美国劳工统计局"),
    ]),
    html.H4("导航说明"),
    html.Ul([
        html.Li("主页：项目简介与数据说明"),
        html.Li("国际房价：各国房价与收入对比分析"),
        html.Li("（其他页面可在导航栏访问）"),
    ]),
    html.P("请选择上方导航栏进入各功能页面。", style={"marginTop": "20px", "color": "#888"}),
])