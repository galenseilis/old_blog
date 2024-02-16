---
title: Plotting Ciw's Café Example As A Sankey Diagram Using Plotly
date: 2024-02-10 02:09:34
categories: [simulation,discrete-event-simulation,python,ciw]
tags: [discrete-event-simulation,python,ciw,plotly,sankey-diagram,statistics,queueing-theory,arrival-distributions,exponential-distribution,routing,service-network,modelling,simulation,visualization,service-distributions]
math: true
mermaid: true
---

In this post we'll run the [café example](https://ciw.readthedocs.io/en/latest/Tutorial-II/tutorial_v.html) from the Ciw documentation, collect the results, and display them as a [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram).

First, we can run the example:

```python
import ciw
import pandas as pd

ciw.seed(2018)

N = ciw.create_network(
    arrival_distributions=[
        ciw.dists.Exponential(rate=0.3),
        ciw.dists.Exponential(rate=0.2),
        None,
    ],
    service_distributions=[
        ciw.dists.Exponential(rate=1.0),
        ciw.dists.Exponential(rate=0.4),
        ciw.dists.Exponential(rate=0.5),
    ],
    routing=[[0.0, 0.3, 0.7], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]],
    number_of_servers=[1, 2, 2],
)

Q = ciw.Simulation(N)

Q.simulate_until_max_time(200)

recs = pd.DataFrame(Q.get_all_records())
```

In order to prepare the results from Ciw for the Plotly Sankey diagramming class, we need to do some additional processing. I also just want to include the arrival node and the exit node just because I can. So we'll need to extract how many times an arrival came into the system from the arrival node:

```python
first_nodes = (
    recs.sort_values(by="arrival_date")
    .groupby("id_number")["node"]
    .apply(lambda x: x.iloc[0])
    .value_counts()
    .reset_index(name="flow")
    .rename(columns={"index": "destination"})
    .assign(node=0)
)
```

We'll also need to compute the amount of flow to/from the other nodes. The reason why the arrival node is separate is because it isn't included in the records table anyway.


```python
recs = (
        recs
        .groupby(by=["node", "destination"])
        .size()
        .reset_index(name="flow")
        .replace({-1:4})
        )
```

Now we can combine these two information sources and get rid of the `-1` for the exit node since we will want a proper index.

```python
recs = pd.concat((first_nodes, recs))
```

Finally, let's sort the values just for fun (as far as I know this doesn't change anyway of substance).

```python
recs = recs.sort_values(by=['destination', 'node', 'flow'])
```

Now we can prepare the Plotly figure as follows:

```python
from plotly.graph_objects import go

fig = go.Figure(
            go.Sankey(
                    arrangement='snap',
                    node=dict(
                        label=['ArrivalNode', 'ColdFood', 'HotFood', 'Till', 'Exit'],
                        pad=10
                        ),
                    link=dict(
                        arrowlen=15,
                        source=recs.node,
                        target=recs.destination,
                        value=recs.flow
                        )
                )
        )
```

Then we can finall change some background stuff and print the HTML which I have promptly pasted below into this post:

```python
fig.layout.paper_bgcolor = 'rgba(0.5,0.5,0.5,0.5)'
fig.layout.plot_bgcolor = 'rgba(0.5,0.5,0.5,0.5)'

print(fig.to_html(full_html=False, include_plotlyjs='cdn'))
```

And there we have it. A Sankey diagram from Ciw's results output. 

<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.29.1.min.js"></script>                <div id="40390c2a-a3de-43d6-9a52-a4416cb9bdd9" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("40390c2a-a3de-43d6-9a52-a4416cb9bdd9")) {                    Plotly.newPlot(                        "40390c2a-a3de-43d6-9a52-a4416cb9bdd9",                        [{"arrangement":"snap","link":{"arrowlen":15,"source":[1,1,2,3,0,0],"target":[2.0,3.0,3.0,4.0,null,null],"value":[13,37,46,83,33,50]},"node":{"label":["ArrivalNode","ColdFood","HotFood","Till","Exit"],"pad":10},"type":"sankey"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"paper_bgcolor":"rgba(0.5,0.5,0.5,0.5)","plot_bgcolor":"rgba(0.5,0.5,0.5,0.5)"},                        {"responsive": true}                    )                };                            </script>        </div>


I'll be the first to admit that this diagram could use some work, but I am please at how this gives a prototype with little code. Primarily it is how jumbled up the arcs are going out of cold food. It may be possible to use different drawing layouts for `x` and `y` to obtain a nicer arrangement. The [Networkx](https://networkx.org/documentation/stable/reference/drawing.html) package has some `layout` functions that might supply such arrangments even if the core Networkx drawing utilities are not used. 

Now, to me, the point of such a diagram isn't to show a *plan* for a model, but rather to show what actually happened. it shows us how much of the customers went through which of the routing paths.

The above code needs some minor changes to be reusable, but it is definitely a process that can be generalized to work on othe simulation records from Ciw. The details of the model were not particularly important beyond what could be extracted from the results. The structure of the model was implicit in the results. Some parts of the structure could be missing when the simulation is either small or heavily constrained, but then again that might be desirable if you are interested in seeing actually flow rather than what you think you put into the model.
