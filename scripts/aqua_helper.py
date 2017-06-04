import pandas as pd
import folium
from matplotlib import pyplot as plt
import numpy as np

def time_slice(df, time_period):
    # Only take data for time period of interest
    df = df[df.time_period == time_period]

    # Pivot table
    df = df.pivot(index='country', columns='variable', values='value')

    df.columns.name = time_period

    return df

def country_slice(df, country):
    # Only take data for country of interest
    df = df[df.country == country]

    # Pivot table
    df = df.pivot(index='variable', columns='time_period', values='value')

    df.index.name = country
    return df

def time_series(df, country, variable):
    # Only take data for country/variable combo
    series = df[(df.country == country) & (df.variable == variable)]

    # Drop years with no data
    series = series.dropna()[['year_measured', 'value']]

    # Change years to int and set as index
    series.year_measured = series.year_measured.astype(int)
    series.set_index('year_measured', inplace=True)
    series.columns = [variable]
    return series

simple_regions = {
    'World | Asia': 'Asia',
    'Americas | Central America and Caribbean | Central America': 'North America',
    'Americas | Central America and Caribbean | Greater Antilles': 'North America',
    'Americas | Central America and Caribbean | Lesser Antilles and Bahamas': 'North America',
    'Americas | Northern America | Northern America': 'North America',
    'Americas | Northern America | Mexico': 'North America',
    'Americas | Southern America | Guyana': 'South America',
    'Americas | Southern America | Andean': 'South America',
    'Americas | Southern America | Brazil': 'South America',
    'Americas | Southern America | Southern America': 'South America',
    'World | Africa': 'Africa',
    'World | Europe': 'Europe',
    'World | Oceania': 'Oceania'
}

def subregion(data, region):
    return data[data.region == region]

def variable_slice(df, variable):
    df = df[df.variable==variable]
    df = df.pivot(index='country', columns='time_period', values='value')
    return df


def plot_map(df, variable, time_period=None, log=False,
             legend_name=None, threshold_scale=None,
             geo=r'../../data/aquastat/world.json'):

    if time_period:
        df = time_slice(df, time_period).reset_index()
    else:
        df = df.reset_index()

    if log:
        df[variable] = df[variable].apply(np.log)

    map = folium.Map(location=[34, -45], zoom_start=2,
                     width=1200, height=600)
    map.choropleth(geo_path=geo,
                   data=df,
                   columns=['country', variable],
                   key_on='feature.properties.name', reset=True,
                   fill_color='PuBuGn', fill_opacity=0.7, line_opacity=0.2,
                   legend_name=legend_name if legend_name else variable,
                   threshold_scale=threshold_scale)
    return map


def map_over_time(df, variable, time_periods, log=False,
                  threshold_scale=None, legend_name=None,
                  geo=r'../../data/aquastat/world.json'):

    time_slider = widgets.SelectionSlider(options=time_periods.tolist(),
                                          value=time_periods[0],
                                          description='Time period:',
                                          disabled=False,
                                          button_style='')
    widgets.interact(plot_map, df=widgets.fixed(df),
                     variable=widgets.fixed(variable),
                     time_period=time_slider, log=widgets.fixed(log),
                     legend_name=widgets.fixed(legend_name),
                     threshold_scale=widgets.fixed(threshold_scale),
                     geo=widgets.fixed(geo));


def plot_hist(df, variable, bins=None, xlabel=None, by=None,
              ylabel=None, title=None, logx=False, ax=None):
    if not bins:
        bins = 20

    if not ax:
        fig, ax = plt.subplots(figsize=(12, 8))
    if logx:
        if df[variable].min() <=0:
            df[variable] = df[variable] - df[variable].min() + 1
            print('Warning: data <=0 exists, data transformed by %0.2g before plotting' % (- df[variable].min() + 1))
        bins = np.logspace(np.log10(df[variable].min()),
                           np.log10(df[variable].max()), bins)
        ax.set_xscale("log")

    if by:
        if type(df[by].unique()) == pd.core.categorical.Categorical:
            cats = df[by].unique().categories.tolist()
        else:
            cats = df[by].unique().tolist()

        for cat in cats:
            to_plot = df[df[by] == cat][variable].dropna()
            ax.hist(to_plot, bins=bins);
    else:
        ax.hist(df[variable].dropna().values, bins=bins);

    if xlabel:
        ax.set_xlabel(xlabel);
    if ylabel:
        ax.set_ylabel(ylabel);
    if title:
        ax.set_title(title);

    return ax

def conditional_bar(series, bar_colors=None, color_labels=None, figsize=(13,24),
                   xlabel=None, by=None, ylabel=None, title=None):
    fig, ax  = plt.subplots(figsize=figsize)
    if not bar_colors:
        bar_colors = mpl.rcParams['axes.prop_cycle'].by_key()['color'][0]
    plt.barh(range(len(series)),series.values, color=bar_colors)
    plt.xlabel('' if not xlabel else xlabel);
    plt.ylabel('' if not ylabel else ylabel)
    plt.yticks(range(len(series)), series.index.tolist())
    plt.title('' if not title else title);
    plt.ylim([-1,len(series)]);
    if color_labels:
        for col, lab in color_labels.items():
            plt.plot([], linestyle='',marker='s',c=col, label= lab);
        lines, labels = ax.get_legend_handles_labels();
        ax.legend(lines[-len(color_labels.keys()):], labels[-len(color_labels.keys()):], loc='upper right');
    plt.close()
    return fig


def plot_scatter(df, x, y, xlabel=None, ylabel=None, title=None,
                 logx=False, logy=False, by=None, ax=None):
    if not ax:
        fig, ax = plt.subplots(figsize=(12, 10))

    colors = mpl.rcParams['axes.prop_cycle'].by_key()['color']
    if by:
        groups = df.groupby(by)
        for j, (name, group) in enumerate(groups):
            ax.scatter(group[x], group[y], color=colors[j], label=name)
        ax.legend()
    else:
        ax.scatter(df[x], df[y], color=colors[0])
    if logx:
        ax.set_xscale('log')
    if logy:
        ax.set_yscale('log')

    ax.set_xlabel(xlabel if xlabel else x);
    ax.set_ylabel(ylabel if ylabel else y);
    if title:
        ax.set_title(title);

def two_hist(df, variable, bins=50,
              ylabel='Number of countries', title=None):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18,8))
    ax1 = plot_hist(df, variable, bins=bins,
                    xlabel=variable, ylabel=ylabel,
                    ax=ax1, title=variable if not title else title)
    ax2 = plot_hist(df, variable, bins=bins,
                    xlabel='Log of '+ variable, ylabel=ylabel,
                    logx=True, ax=ax2,
                    title='Log of '+ variable if not title else title)
    plt.close()
    return fig

def hist_over_var(df, variables, bins=50, first_choice=None,
                  ylabel='Number of countries', title=None):
    if not first_choice:
        first_choice = variables[0]
    variable_slider = widgets.Dropdown(options=variables.tolist(),
                                       value=first_choice,
                                       description='Variable:',
                                       disabled=False,
                                       button_style='')
    widgets.interact(two_hist, df=widgets.fixed(df),
                     variable=variable_slider, ylabel=widgets.fixed(ylabel),
                     title=widgets.fixed(title), bins=widgets.fixed(bins));
