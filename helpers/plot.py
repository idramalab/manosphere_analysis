from matplotlib.image import imread
from tempfile import NamedTemporaryFile
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime


def get_size(fig, dpi=100):
    with NamedTemporaryFile(suffix='.png') as f:
        fig.savefig(f.name, bbox_inches='tight', dpi=dpi)
        height, width, _channels = imread(f.name).shape
        return width / dpi, height / dpi


def set_size(fig, size, dpi=100, eps=1e-2, give_up=2, min_size_px=10):
    target_width, target_height = size
    set_width, set_height = target_width, target_height  # reasonable starting point
    deltas = []  # how far we have
    while True:
        fig.set_size_inches([set_width, set_height])
        actual_width, actual_height = get_size(fig, dpi=dpi)
        set_width *= target_width / actual_width
        set_height *= target_height / actual_height
        deltas.append(abs(actual_width - target_width) + abs(actual_height - target_height))
        if deltas[-1] < eps:
            return True
        if len(deltas) > give_up and sorted(deltas[-give_up:]) == deltas[-give_up:]:
            return False
        if set_width * dpi < min_size_px or set_height * dpi < min_size_px:
            return False


def plot_days_counts(days_and_counts_list, colors, lines, path=None,
                     leg=False, ylabel='', xlabel="", ncols=4,
                     ylim_norm=[0, 9.6], yticks_norm=[0, 3.2, 6.4, 9.6],
                     ax=None, legend=False, figsize=(6.5, 2.75), forums=False, total=False,
                     helper=None):
    percs_all = []
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    k = 0
    for days_and_counts in days_and_counts_list:

        if k == 0 and forums:
            k += 1
            continue
        if total:
            counts = [x[0] for x in days_and_counts]
        else:
            counts = [x[0] / helper[x[1]] * 100 for x in days_and_counts]

        days = [datetime.strptime(x[1], '%d-%m-%Y') for x in days_and_counts]
        days2 = mdates.date2num(days)
        percs = counts

        percs_all.append(percs)
        ax.plot_date(days2, percs, colors[k], linestyle=lines[k])
        k += 1

    months = mdates.MonthLocator(7)
    year = mdates.YearLocator()
    year_fmt = mdates.DateFormatter("%y")

    ax.xaxis.set_major_locator(year)
    ax.xaxis.set_minor_locator(months)
    ax.xaxis.set_major_formatter(year_fmt)
    ax.set_ylabel(ylabel)
    ax.xaxis.grid(color='#DCDCDC', linestyle='dashed')
    ax.xaxis.grid(color='#EEEEEE', linestyle='dashed', which="minor")
    ax.yaxis.grid(color='#DCDCDC', linestyle='dashed')
    ax.set_xlabel(xlabel)

    if forums:
        ax.set_xlim([datetime.strptime('2005-11-21', '%Y-%m-%d'), datetime.strptime('2019-02-10', '%Y-%m-%d')])
    else:
        ax.set_xlim([datetime.strptime('2007-11-21', '%Y-%m-%d'), datetime.strptime('2019-02-10', '%Y-%m-%d')])

    if total:
        ax.set_yscale("linear")
    else:
        ax.set_ylim(ylim_norm)
        ax.set_yticks(yticks_norm)

    for tick in ax.get_xmajorticklabels():
        tick.set_horizontalalignment('center')

    if legend:
        ax.legend(leg, bbox_to_anchor=(0., 1.15, 1., .102), loc=3,
                  ncol=ncols, mode="expand", borderaxespad=0., fontsize=11.5,
                  fancybox=False,
                  shadow=False,
                  frameon=False,
                  edgecolor=None)
    if ax is None:
        set_size(fig, figsize)
        fig.savefig(path, bbox_inches='tight')
        plt.show()


def plot_toxicity(days_and_counts_list, colors, lines, path=None,
                  leg=False, ylabel='', xlabel="", ncols=4,
                  ax=None, legend=False, inner_legend=False,
                  figsize=(6.5, 2.75), forums=False):
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    k = 0
    for x in days_and_counts_list:
        ax.fill_between(x.index, x.low, x.high, alpha=0.15, color=colors[k])
        line = ax.plot(x.index, x["pe"], colors[k], linestyle=lines[k])
        k += 1

    months = mdates.MonthLocator(7)
    year = mdates.YearLocator()
    year_fmt = mdates.DateFormatter("%y")

    ax.xaxis.set_major_locator(year)
    ax.xaxis.set_minor_locator(months)
    ax.xaxis.set_major_formatter(year_fmt)
    ax.set_ylabel(ylabel)
    ax.xaxis.grid(color='#DCDCDC', linestyle='dashed')
    ax.xaxis.grid(color='#EEEEEE', linestyle='dashed', which="minor")
    ax.yaxis.grid(color='#DCDCDC', linestyle='dashed')
    ax.set_xlabel(xlabel)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

    if forums:
        ax.set_xlim([datetime.strptime('2005-11-21', '%Y-%m-%d'), datetime.strptime('2019-02-10', '%Y-%m-%d')])
    else:
        ax.set_xlim([datetime.strptime('2007-11-21', '%Y-%m-%d'), datetime.strptime('2019-02-10', '%Y-%m-%d')])

    for tick in ax.get_xmajorticklabels():
        tick.set_horizontalalignment('center')

    if legend:
        ax.legend(leg, bbox_to_anchor=(0., 1.15, 1., .102), loc=3,
                  ncol=ncols, mode="expand", borderaxespad=0., fontsize=11.5,
                  fancybox=False,
                  shadow=False,
                  frameon=False,
                  edgecolor=None)

    if inner_legend:
        from matplotlib.lines import Line2D

        line = [Line2D([0], [0], color=colors[0], lw=1.5, ls=lines[0])]


        ax.legend(
            handles=line,
            labels=leg,
            ncol=1, fancybox=False, shadow=False,
            frameon=False, edgecolor=None, fontsize=11.5
        )

    if ax is None:
        set_size(fig, figsize)
        fig.savefig(path, bbox_inches='tight')
        plt.show()

