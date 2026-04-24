#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().system('pip install dash plotly pandas numpy')


# In[15]:


import pandas as pd
import numpy as np

np.random.seed(42)

# - 1. Monthly Time Series -
months = pd.date_range(start="2023-01-01", periods=12, freq="MS")

channel_trends = pd.DataFrame({
    "month": months,
    "Programmatic": [6.2,5.8,7.1,8.4,9.8,11.2,12.5,10.8,9.2,8.1,7.4,7.0],
    "Paid Search":  [7.5,8.1,6.9,5.2,4.8,4.1,3.9,4.5,5.8,6.9,7.8,8.5],
    "Paid Social":  [1.2,1.8,2.4,3.1,3.8,4.2,5.1,4.8,3.9,3.2,2.8,2.4],
    "Organic":      [0.8,1.1,1.4,1.8,2.1,2.4,2.8,2.5,2.2,1.9,1.6,1.3],
})

# - 2. Main KPIs -
kpis = {
    "Spend":           {"value": "$36.00M", "delta": "+$491.79K", "positive": True},
    "CPM":             {"value": "$405K",   "delta": "+$1.28K",   "positive": False},
    "CTR":             {"value": "10.5%",   "delta": "+0.08%",    "positive": True},
    "CPC":             {"value": "$4K",     "delta": "-$18.34",   "positive": False},
    "Video Views":     {"value": "93K",     "delta": "+993.0",    "positive": True},
    "Impressions":     {"value": "89.0K",   "delta": "+937.0",    "positive": True},
    "Conversions":     {"value": "791",     "delta": "+36.0",     "positive": True},
    "Conversion Rate": {"value": "9.8%",    "delta": "+0.27%",    "positive": True},
}

# - 3. Channel Performance -
channel_perf = pd.DataFrame({
    "Channel":     ["Programmatic", "Paid Search", "Paid Social", "Organic"],
    "Impressions": ["34.7K", "31.4K", "11.4K", "11.5K"],
    "Imp_%":       ["-4.2%", "+30.7%", "-25.6%", "-8.0%"],
    "Imp_pos":     [False, True, False, False],
    "CTR":         ["10.44%", "10.57%", "10.28%", "10.6%"],
    "CTR_%":       ["+1.5%", "+3.1%", "-4.1%", "-0.4%"],
    "CTR_pos":     [True, True, False, False],
})

# - 4. Data Source Performance -
datasource_perf = pd.DataFrame({
    "Source":      ["Amazon Ad Server", "StackAdapt", "LinkedIn Ads",
                    "Facebook", "Google Display & Video 360",
                    "Bing Ads", "Google Search Ads 360"],
    "Impressions": ["5.8K", "4.8K", "5.8K", "5.7K", "4.7K", "4.8K", "5.8K"],
    "Imp_%":       ["+201.0%", "+68.7%", "-", "+99.0%", "+65.2%", "+3.7%", "-23.6%"],
    "Imp_pos":     [True, True, None, True, True, True, False],
    "CTR":         ["10.17%", "10%", "10.05%", "10.82%", "10.28%", "10.7%", "10.97%"],
    "CTR_%":       ["-10.0%", "-7.3%", "-", "+14.3%", "-5.8%", "-1.8%", "+11.0%"],
    "CTR_pos":     [False, False, None, True, False, False, True],
})

# - 5. Campaign Performance -
campaign_perf = pd.DataFrame({
    "Campaign": [
        "Business-focused zero tolerance arch...",
        "Persistent 24/7 attitude",
        "Integrated dedicated contingency",
        "Profound intangible policy",
        "Centralized modular throughput",
        "Automated uniform software",
        "Cross-platform static hierarchy",
        "Networked value-added time-frame",
    ],
    "Impressions": [931, 1000, 950, 978, 955, 952, 946, 953],
    "Imp_%":       ["-", "-", "-", "-", "-", "-", "-", "-"],
    "CTR":         ["10.42%", "9.71%", "9.58%", "8.69%", "9.42%", "10.19%", "9.3%", "11.54%"],
    "CTR_%":       ["-", "-", "-", "-", "-", "-", "-", "-"],
})


# In[17]:


from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

app = Dash(__name__)

# ── Colors -
BG        = "#1e1f2e"
CARD_BG   = "#ffffff"
PURPLE    = "#7c3aed"
PINK      = "#ec4899"
CYAN      = "#06b6d4"
ORANGE    = "#f97316"
GREEN     = "#22c55e"
RED       = "#ef4444"
TEXT_DARK = "#1e1f2e"
TEXT_GRAY = "#6b7280"

# - Data -
months = pd.date_range(start="2023-01-01", periods=12, freq="MS")
channel_trends = pd.DataFrame({
    "month":        months,
    "Programmatic": [6.2,5.8,7.1,8.4,9.8,11.2,12.5,10.8,9.2,8.1,7.4,7.0],
    "Paid Search":  [7.5,8.1,6.9,5.2,4.8,4.1,3.9,4.5,5.8,6.9,7.8,8.5],
    "Paid Social":  [1.2,1.8,2.4,3.1,3.8,4.2,5.1,4.8,3.9,3.2,2.8,2.4],
    "Organic":      [0.8,1.1,1.4,1.8,2.1,2.4,2.8,2.5,2.2,1.9,1.6,1.3],
})

channel_perf = pd.DataFrame({
    "Channel":     ["Programmatic", "Paid Search", "Paid Social", "Organic"],
    "Impressions": ["34.7K", "31.4K", "11.4K", "11.5K"],
    "Imp_%":       ["-4.2%", "+30.7%", "-25.6%", "-8.0%"],
    "Imp_pos":     [False, True, False, False],
    "CTR":         ["10.44%", "10.57%", "10.28%", "10.6%"],
    "CTR_%":       ["+1.5%", "+3.1%", "-4.1%", "-0.4%"],
    "CTR_pos":     [True, True, False, False],
})

datasource_perf = pd.DataFrame({
    "Source":      ["Amazon Ad Server", "StackAdapt", "LinkedIn Ads",
                    "Facebook", "Google Display & Video 360",
                    "Bing Ads", "Google Search Ads 360"],
    "Impressions": ["5.8K", "4.8K", "5.8K", "5.7K", "4.7K", "4.8K", "5.8K"],
    "Imp_%":       ["+201.0%", "+68.7%", "-", "+99.0%", "+65.2%", "+3.7%", "-23.6%"],
    "Imp_pos":     [True, True, None, True, True, True, False],
    "CTR":         ["10.17%", "10%", "10.05%", "10.82%", "10.28%", "10.7%", "10.97%"],
    "CTR_%":       ["-10.0%", "-7.3%", "-", "+14.3%", "-5.8%", "-1.8%", "+11.0%"],
    "CTR_pos":     [False, False, None, True, False, False, True],
})

campaign_perf = pd.DataFrame({
    "Campaign": [
        "Business-focused zero tolerance arch...",
        "Persistent 24/7 attitude",
        "Integrated dedicated contingency",
        "Profound intangible policy",
        "Centralized modular throughput",
        "Automated uniform software",
        "Cross-platform static hierarchy",
        "Networked value-added time-frame",
    ],
    "Impressions": [931, 1000, 950, 978, 955, 952, 946, 953],
    "Imp_%":       ["-", "-", "-", "-", "-", "-", "-", "-"],
    "CTR":         ["10.42%", "9.71%", "9.58%", "8.69%", "9.42%", "10.19%", "9.3%", "11.54%"],
    "CTR_%":       ["-", "-", "-", "-", "-", "-", "-", "-"],
})

# - Sparkline helper -
def sparkline(color):
    np.random.seed(abs(hash(color)) % 100)
    y = np.cumsum(np.random.randn(20)) + 10
    fig = go.Figure(go.Scatter(
        y=y, mode="lines",
        line=dict(color=color, width=1.5)
    ))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=50, width=150
    )
    return fig

# - KPI Card helper -
def kpi_card(title, value, delta, positive):
    color = GREEN if positive else RED
    arrow = "▲" if positive else "▼"
    return html.Div([
        html.P(title, style={"color": TEXT_GRAY, "fontSize": "12px", "margin": "0"}),
        html.H3(value, style={"color": TEXT_DARK, "margin": "4px 0", "fontSize": "24px"}),
        html.Span(f"{arrow} {delta}", style={"color": color, "fontSize": "11px"}),
        dcc.Graph(figure=sparkline(PURPLE), config={"displayModeBar": False},
                  style={"marginTop": "6px"})
    ], style={
        "background": CARD_BG, "borderRadius": "12px",
        "padding": "16px", "flex": "1", "minWidth": "160px",
        "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"
    })

# - Time series chart -
colors_ts = [PURPLE, PINK, CYAN, ORANGE]
fig_ts = go.Figure()
for i, ch in enumerate(["Programmatic", "Paid Search", "Paid Social", "Organic"]):
    fig_ts.add_trace(go.Scatter(
        x=channel_trends["month"], y=channel_trends[ch],
        name=ch, mode="lines",
        line=dict(color=colors_ts[i], width=2)
    ))
fig_ts.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=10, b=10),
    legend=dict(orientation="h", y=1.1, x=0),
    xaxis=dict(showgrid=False, color=TEXT_GRAY),
    yaxis=dict(showgrid=True, gridcolor="#f0f0f0",
               tickformat=".1f", ticksuffix="M", color=TEXT_GRAY),
    height=280
)

# - Table helpers -
def delta_span(val, positive):
    if val == "-" or positive is None:
        return html.Span(val, style={"color": TEXT_GRAY})
    color = GREEN if positive else RED
    arrow = "▲" if positive else "▼"
    return html.Span(f"{arrow} {val}", style={"color": color, "fontSize": "11px"})

def get_purple_bg(value_str, all_values):
    """Convert a numeric value to a purple background intensity"""
    try:
        val = float(value_str.replace("K","").replace("%","").replace("$","").replace(",",""))
        nums = []
        for v in all_values:
            try:
                nums.append(float(v.replace("K","").replace("%","").replace("$","").replace(",","")))
            except:
                pass
        if not nums or max(nums) == min(nums):
            return "transparent"
        intensity = (val - min(nums)) / (max(nums) - min(nums))
        alpha = 0.15 + intensity * 0.55
        return f"rgba(124, 58, 237, {alpha:.2f})"
    except:
        return "transparent"

def build_table(headers, rows, shade_cols=None):
    """Build an HTML table with optional purple heatmap shading on specified columns"""
    col_values = {}
    if shade_cols:
        for col_idx in shade_cols:
            col_values[col_idx] = [
                str(row[col_idx].children) if hasattr(row[col_idx], 'children') else str(row[col_idx])
                for row in rows
            ]

    tbody_rows = []
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            bg = "transparent"
            if shade_cols and i in shade_cols:
                raw = str(cell.children) if hasattr(cell, 'children') else str(cell)
                bg = get_purple_bg(raw, col_values[i])
            cells.append(html.Td(cell, style={
                "padding": "6px 8px",
                "fontSize": "12px",
                "backgroundColor": bg,
                "borderRadius": "4px"
            }))
        tbody_rows.append(html.Tr(cells))

    return html.Table([
        html.Thead(html.Tr([
            html.Th(h, style={
                "color": TEXT_GRAY, "fontSize": "11px",
                "padding": "6px 8px", "textAlign": "left",
                "borderBottom": "1px solid #f0f0f0"
            }) for h in headers
        ])),
        html.Tbody(tbody_rows)
    ], style={"width": "100%", "borderCollapse": "collapse"})

# - Build table rows -
ch_rows = []
for _, r in channel_perf.iterrows():
    ch_rows.append([
        html.Span(r["Channel"], style={"fontWeight": "500", "fontSize": "12px"}),
        r["Impressions"],
        delta_span(r["Imp_%"], r["Imp_pos"]),
        html.Span(r["CTR"], style={"color": PURPLE, "fontWeight": "600"}),
        delta_span(r["CTR_%"], r["CTR_pos"]),
    ])

ds_rows = []
for _, r in datasource_perf.iterrows():
    ds_rows.append([
        html.Span(r["Source"], style={"fontSize": "12px"}),
        r["Impressions"],
        delta_span(r["Imp_%"], r["Imp_pos"]),
        html.Span(r["CTR"], style={"color": PURPLE, "fontWeight": "600"}),
        delta_span(r["CTR_%"], r["CTR_pos"]),
    ])

camp_rows = []
for _, r in campaign_perf.iterrows():
    camp_rows.append([
        html.Span(r["Campaign"], style={"fontSize": "11px"}),
        str(r["Impressions"]),
        r["Imp_%"],
        html.Span(r["CTR"], style={"color": PURPLE, "fontWeight": "600"}),
        r["CTR_%"],
    ])

# - Section card wrapper -
def section_card(title, content):
    return html.Div([
        html.H4(title, style={"margin": "0 0 12px 0", "fontSize": "14px",
                               "color": TEXT_DARK, "fontWeight": "600"}),
        content
    ], style={
        "background": CARD_BG, "borderRadius": "12px",
        "padding": "16px", "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"
    })

# - Layout -
app.layout = html.Div([

    # Header
    html.Div([
        html.H2("📊 Executive Summary", style={"color": "#ffffff", "margin": "0", "fontSize": "18px"}),
        html.Span("Jan 1, 2023 – Mar 31, 2023", style={"color": "#a0a0b0", "fontSize": "12px"})
    ], style={"background": BG, "padding": "16px 24px",
              "display": "flex", "justifyContent": "space-between", "alignItems": "center"}),

    # Body
    html.Div([

        # Row 1: KPI Cards
        html.Div([
            kpi_card("Spend",       "$36.00M", "$491.79K", True),
            kpi_card("CPM",         "$405K",   "$1.28K",   False),
            kpi_card("CTR",         "10.5%",   "0.08%",    True),
            kpi_card("CPC",         "$4K",     "$18.34",   False),
        ], style={"display": "flex", "gap": "12px", "marginBottom": "12px"}),

        html.Div([
            kpi_card("Video Views",     "93K",   "993.0",  True),
            kpi_card("Impressions",     "89.0K", "937.0",  True),
            kpi_card("Conversions",     "791",   "36.0",   True),
            kpi_card("Conversion Rate", "9.8%",  "0.27%",  True),
        ], style={"display": "flex", "gap": "12px", "marginBottom": "12px"}),

        # Row 2: Chart + Tables
        html.Div([

            # Time series
            html.Div([
                section_card("Channel Trends Over Time",
                             dcc.Graph(figure=fig_ts, config={"displayModeBar": False}))
            ], style={"flex": "2"}),

            # Right tables
            html.Div([
                section_card("Channel Performance",
                             build_table(
                                 ["Channel", "Impressions", "% Δ", "CTR", "% Δ"],
                                 ch_rows, shade_cols=[1, 3])),
                html.Div(style={"height": "12px"}),
                section_card("Data Source Performance",
                             build_table(
                                 ["Source", "Impressions", "% Δ", "CTR", "% Δ"],
                                 ds_rows, shade_cols=[1, 3])),
                html.Div(style={"height": "12px"}),
                section_card("Campaign Performance",
                             build_table(
                                 ["Campaign", "Impressions", "% Δ", "CTR", "% Δ"],
                                 camp_rows, shade_cols=[1, 3])),
            ], style={"flex": "1", "display": "flex", "flexDirection": "column"})

        ], style={"display": "flex", "gap": "12px"}),

    ], style={"padding": "16px", "background": "#f4f5f7", "minHeight": "100vh"})

], style={"fontFamily": "Inter, sans-serif"})

# - Run -
if __name__ == "__main__":
    app.run(debug=True, port=8050)

print("✅ Dashboard ready! Open http://127.0.0.1:8050 in your browser")



# In[ ]:




