import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""# Problem""")
    return


@app.cell
def _(mo):
    mo.md("""We compute the radius and center of the smallest enclosing ball for $N$ points in $d$ dimensions.""")
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Generate a cloud of points""")
    return


@app.cell
def _():
    import numpy as np
    import plotly.graph_objects as go

    return go, np


@app.cell
def _(np):
    pos = np.random.randn(10000, 3)
    return (pos,)


@app.cell
def _(go, pos):
    # Create the scatter plot
    fig = go.Figure(data=go.Scatter(x=pos[:, 0], y=pos[:, 1], mode="markers", marker=dict(symbol="x", size=10)))

    # Update layout for equal aspect ratio and axis labels
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
        ),
    )

    # Show the plot
    fig.show()

    # plot makes really only sense when using d=2
    return (fig,)


if __name__ == "__main__":
    app.run()
