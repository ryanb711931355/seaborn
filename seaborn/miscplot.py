import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

__all__ = ["palplot", "dogplot"]


def palplot(pal, size=1):
    """Plot the values in a color palette as a horizontal array.

    Parameters
    ----------
    pal : sequence of matplotlib colors
        colors, i.e. as returned by seaborn.color_palette()
    size :
        scaling factor for size of plot

    """
    n = len(pal)
    _, ax = plt.subplots(1, 1, figsize=(n * size, size))
    ax.imshow(np.arange(n).reshape(1, n),
              cmap=mpl.colors.ListedColormap(list(pal)),
              interpolation="nearest", aspect="auto")
    ax.set_xticks(np.arange(n) - .5)
    ax.set_yticks([-.5, .5])
    # Ensure nice border between colors
    ax.set_xticklabels(["" for _ in range(n)])
    # The proper way to set no ticks
    ax.yaxis.set_major_locator(ticker.NullLocator())


def dogplot(*_, **__):
    """Who's a good boy?"""
    from urllib.request import urlopen
    from urllib.error import URLError
    from io import BytesIO

    urls = [
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/png/img{}.png",
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/main/png/img{}.png",
        "https://github.com/mwaskom/seaborn-data/raw/master/png/img{}.png",
    ]
    pic = np.random.randint(2, 7)
    img = None
    for url in urls:
        try:
            data = BytesIO(urlopen(url.format(pic)).read())
            img = plt.imread(data)
            break
        except (URLError, OSError, ValueError):
            continue
    if img is None:
        # Remote image unavailable; show a placeholder so the function still works
        img = np.ones((100, 100, 3))
    f, ax = plt.subplots(figsize=(5, 5), dpi=100)
    f.subplots_adjust(0, 0, 1, 1)
    ax.imshow(img)
    ax.set_axis_off()
