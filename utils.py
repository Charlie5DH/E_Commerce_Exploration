import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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

def annotate_percentage(ax, data=None, total = None,title=None, size=14, fontsize=18, yy=1.02, offset=20):
    '''
    Annotates a percentage and the amounth at the top of the bar plot.
    Sets the title of the plot
    yy: height of the title
    fontsize: fontsize of the title
    size: is the size of the annotation
    '''
    if total is None:
        total = float(len(data))
    for p in ax.patches:
        percentage = '{:.1f}%\n{:.1f}'.format(100 * p.get_height()/total, p.get_height())
        x = p.get_x() + p.get_width()/2
        y = p.get_height() + offset
        ax.annotate(percentage, (x, y), ha='center', size=size)
    ax.set_title(title, fontsize=fontsize, y=yy)