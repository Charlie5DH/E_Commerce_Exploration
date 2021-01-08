import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# define colors
colors = {'GRAY1':'#231F20', 'GRAY2':'#414040', 'GRAY3':'#555655',
         'GRAY4':'#646369', 'GRAY5':'#76787B', 'GRAY6':'#828282',
         'GRAY7':'#929497', 'GRAY8':'#A6A6A5', 'GRAY9':'#BFBEBE',
         'BLUE1':'#174A7E', 'BLUE2':'#4A81BF', 'BLUE3':'#94B2D7',
         'BLUE4':'#94AFC5', 'RED1':'#C3514E', 'RED2':'#E6BAB7',
         'GREEN1':'#0C8040', 'GREEN2':'#9ABB59', 'ORANGE1':'#F79747',}


def load_data(data_dir):
    '''
    Load all datasets from data folder
    '''
    customer = pd.read_csv(data_dir + 'olist_customers_dataset.csv')
    geolocation = pd.read_csv(data_dir + 'olist_geolocation_dataset.csv')
    orders = pd.read_csv(data_dir + 'olist_orders_dataset.csv')
    order_items = pd.read_csv(data_dir + 'olist_order_items_dataset.csv')
    order_payments = pd.read_csv(data_dir + 'olist_order_payments_dataset.csv')
    order_reviews = pd.read_csv(data_dir + 'olist_order_reviews_dataset.csv')
    products = pd.read_csv(data_dir + 'olist_products_dataset.csv')
    sellers = pd.read_csv(data_dir + 'olist_sellers_dataset.csv')
    return customer, geolocation, orders, order_items, order_payments, order_reviews, products, sellers

def countplot(data, column, figsize=(12,6)):
    '''
    Plot a countpot with the percentage on top of the bar 
    using seaborn library.
    column: name of the column (str)
    data: dataframe
    '''
    fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=figsize)

    ax1 = sns.countplot(data=data, x='order_status')
    total = float(len(data[column]))
    for p in ax1.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/total)
        x = p.get_x() + p.get_width()
        y = p.get_height()
        ax1.annotate(percentage, (x, y),ha='center')
    plt.tight_layout()
    
def extract_from_date(data, timestamp_column, suffix):
    '''
    Add time fratures to dataset
    '''
    data[timestamp_column] = pd.to_datetime(data[timestamp_column])
    
    data[str(suffix + '_year')] = data[timestamp_column].dt.year
    data[str(suffix + '_month')] = data[timestamp_column].dt.month
    data[str(suffix + '_month_name')] = data[timestamp_column].dt.month_name()
    data[str(suffix + '_year_month')] = data[timestamp_column].dt.strftime('%Y%m')
    data[str(suffix + '_date')] = data[timestamp_column].dt.strftime('%Y%m%d')
    data[str(suffix + '_week')] = data[timestamp_column].dt.isocalendar().week
    data[str(suffix + '_day')] = data[timestamp_column].dt.day
    data[str(suffix + '_dayofweek')] = data[timestamp_column].dt.dayofweek
    data[str(suffix + '_day_name')] = data[timestamp_column].dt.day_name()
    data[str(suffix + '_hour')] = data[timestamp_column].dt.hour
    data[str(suffix + 'day_time')] = pd.cut(data[str(suffix + '_hour')], bins=[0, 12, 18, 23], labels=['morning', 'afternoon', 'night'])
    
    return data

def annotate_percentage(ax, data=None, total = None,title=None,
                        horizontal=False, size=14, fontsize=18, yy=1.02, offset=20):
    '''
    Annotates a percentage and the amounth at the top of the bar plot.
    Sets the title of the plot
    yy: height of the title
    fontsize: fontsize of the title
    size: is the size of the annotation
    '''
    if horizontal:
        if total is None:
            total = float(len(data))
        xmax=ax.get_xlim()[1] 
        offset = xmax*0.005
        for p in ax.patches:
            text = '{:.1f}'.format(p.get_width())
            x = p.get_x() + p.get_width() + offset
            y = p.get_height()/2 + p.get_y()
            ax.annotate(text, (x, y), size=size)
        ax.set_title(title, fontsize=fontsize, y=yy)
    else:
        if total is None:
            total = float(len(data))
        xmax=ax.get_xlim()[1] 
        offset = xmax*0.005
        for p in ax.patches:
            percentage = '{:.1f}%\n{:.1f}'.format(100 * p.get_height()/total, p.get_height())
            x = p.get_x() + p.get_width()/2
            y = p.get_height() + offset
            ax.annotate(percentage, (x, y), ha='center', size=size)
        ax.set_title(title, fontsize=fontsize, y=yy)
    
def get_iqr(df, feature, k_factor = 1.5, remove=True):
    '''
    Return the interquartile range and defines an outlier range
    based in a k factor.
    if remove==True: returns a dataframe with the removed outliers
    and a dataframe with the outliers
    '''
    q25, q75 = np.percentile(df[feature], 25), np.percentile(df[feature], 75)
    IQR = q75 - q25
    cut_off = IQR * k_factor
    lower, upper = q25 - cut_off, q75 + cut_off
    if remove:
        data = df.loc[(df[feature] > lower) & (df[feature] < upper)]
        outliers = df.loc[(df[feature] < lower) & (df[feature] > upper)]
        return data, outliers
    return IQR, lower, upper

def annotate_total(ax, data=None, horizontal=False, total = None,
                   title=None, size=14, fontsize=18, yy=1.02, offset=20):
    '''
    Annotates a percentage and the amounth at the top of the bar plot.
    Sets the title of the plot
    yy: height of the title
    fontsize: fontsize of the title
    size: is the size of the annotation
    horizontal: defines if the bars are horizontal or not
    '''

    if horizontal:
        if total is None:
            total = float(len(data))
        xmax=ax.get_xlim()[1] 
        offset = xmax*0.005
        for p in ax.patches:
            text = '{:.1f}'.format(p.get_width())
            x = p.get_x() + p.get_width() + offset
            y = p.get_height()/2 + p.get_y()
            ax.annotate(text, (x, y), size=size)
        ax.set_title(title, fontsize=fontsize, y=yy)
    else:
        if total is None:
            total = float(len(data))
        xmax=ax.get_xlim()[1] 
        offset = xmax*0.005
        for p in ax.patches:
            text = '{:.1f}'.format(p.get_height())
            x = p.get_x() + p.get_width()/2
            y = p.get_height() + offset
            ax.annotate(text, (x, y), ha='center', size=size)
        ax.set_title(title, fontsize=fontsize, y=yy)
    
def remove_chart_borders():
    # remove chart border
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    
def annotate(ax, text, x=0.5, y=0.5, line=False,stacked=False, color='#94AFC5', fontsize=16, linespacing=1.45):
    '''
    Add text annotation in plot using x and y in percents.
    final y value is 100, must specify if the graph is stacked,
    this is to allow insert text at the end of the figure.
    '''
    if stacked:
        X_end = (len(ax.patches)/2)
    else:
        X_end = (len(ax.patches))
    if line:
        X_end = ax.axes.get_xlim()[1]
    y_end = ax.axes.get_ylim()[1]
    
    plt.text(X_end*x, y_end*y, text, 
             fontsize=fontsize, linespacing=linespacing, 
             color=color)
    
def line_plot_annotate(ax, values, x, y, fontsize=14):
    '''
    values is the array of number we want to annotate
    x is the values in the x axis, can be an index value
    from a pandas dataframe.
    y is the values in the y axis, may be the same as values
    if the annotations are the values
    
    Example:
    values = df.loc[state].sort_index()[:'201803']['order_id'].values
    x = df.loc[state].sort_index()[:'201803']['order_id'].index
    y = df.loc[state].sort_index()[:'201803']['order_id'].values
    '''
    for i, txt in enumerate(values):
        ax.annotate(txt, (x[i], y[i]),fontsize=fontsize)

def plot_circle(ax, labels, sizes, color_list, text, startangle=30, text_loc=(-0.2,-0.1), text_color='#4A81BF'):
    '''
    Make circle plot.
    Example:
    labels = df_orders_pay.groupby('payment_type').count().sort_values(by='order_id', ascending=False).index
    sizes = df_orders_pay.groupby('payment_type').count().sort_values(by='order_id', ascending=False).order_id.values
    color_list = [colors['BLUE2'], colors['ORANGE1'],colors['GRAY3'],colors['RED1']]
    '''
    ax.pie(sizes, colors = color_list, labels=labels, autopct='%1.1f%%', startangle=startangle)
    #draw circle
    centre_circle = ax.Circle((0,0), 0.8, fc='white')
    ax.annotate(text , text_loc, fontsize=24, color=text_color)

    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle

    ax.axis('equal')  
    plt.tight_layout()
    plt.show()
    
    
def date_plot_categorical(data, categorical, dated_feature, ax, key, top_values=True,
                          size=5, markersize=10, title='', count=True, markers=None):
    '''
    Makes a dated line plot (define the date in dataset)
    of the counting or sum of a categorical variable in 
    your dataset. Example:
    A dataset can have the year and month for a categorical
    feature, this method creates a line plot of the categorie
    by counting or summing every item in a date. The dated column
    can be derived from a timestamp.
    
    data: the original dataset
    categorical: the categorical feature to count
    dated_feature: name of column with dates
    top_values: True-> Takes the categories most common categories
    size: How many categories, if top_values=False takes all. 
    ax: the axis to plot
    key: key value to count or sum (non categorical if Sum)
    count: if True counts the categories.
           False -> Sums the values (the key value must be the value to sum)
    '''
    
    if markers is None:
        # create valid markers from mpl.markers
        valid_markers = ([item[0] for item in mpl.markers.MarkerStyle.markers.items() if
        item[1] is not 'nothing' and not item[1].startswith('tick') and not item[1].startswith('caret')])
        markers = np.random.choice(valid_markers, orders_customer.shape[1], replace=False)
    
    # Count
    if top_values:
        # take the most common categories
        categories = data[categorical].value_counts()[:size].index
    else:
        # take all categories
        categories = data[categorical].unique()
    
    if count:
        df = data.groupby([categorical, dated_feature]).count().sort_index()
        
        for i, category in enumerate(categories):
        # locate the categories
            sns.lineplot(data = df.loc[category][key], label=category, ax=ax,
                         marker=markers[i], markersize=markersize)
    # Sum
    else:
        df = data.groupby([categorical, dated_feature]).sum().sort_index()
        
        for i, category in enumerate(categories):
        # locate the categories
            sns.lineplot(data = df.loc[category][key], label=category, ax=ax,
                         marker=markers[i], markersize=markersize)
    ax.legend()    
    ax.set_title(title, fontsize=18)
    remove_chart_borders()