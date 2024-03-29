# DS4B 101-P: PYTHON FOR DATA SCIENCE AUTOMATION ----
# SQL DATABASES (Module 2): Working with SQLAlchemy ----

# IMPORTS ----
import sqlalchemy as sql
import pandas as pd
# FUNCTION DEFINITION ----
# %%

def collect_data(conn_string = 'sqlite:///00_database/bike_orders_database.sqlite'):
    """
    Collects and combines the bike orders data.

    Args:
        conn_string (str, optional): A SQLAlchemy connectio string to find the database. 
        Defaults to 'sqlite:///00_database/bike_orders_database.sqlite'.

    Returns:
        DataFrame: A pandas data frame that combines data from tables:
        - orderlines: Transactions data
        - bikes: Products data
        - bikeshops: customers data
    """
    # 1.0 Connect to database 
    engine = sql.create_engine(conn_string)
    
    conn = engine.connect()
    
    table_names = ['bikes', 'bikeshops', 'orderlines']
    
    data_dict = {}
    for table in table_names:
        data_dict[table] = pd.read_sql(f'select * from {table}', con=conn) \
            .drop('index', axis=1)
        
    conn.close()
    # 2.0 Combining and Cleanin Data
    
    joined_df = pd.DataFrame(data_dict['orderlines']).merge(
        right = data_dict['bikes'],
        how = 'left',
        left_on = 'product.id',
        right_on='bike.id'
    ).merge(
        right = data_dict['bikeshops'],
        how = 'left',
        left_on = 'customer.id',
        right_on = 'bikeshop.id'
    )
    
    # 3.0 Cleaning Data
    df = joined_df
    df['order.date'] = pd.to_datetime(df['order.date'])
    
    temp_df = df['description'].str.split(' - ', expand = True)
    df['category.1'] = temp_df[0]
    df['category.2'] = temp_df[1]
    df['frame.material'] = temp_df[2]
    
    temp_df = df['location'].str.split(', ', n=1, expand = True)
    df['city'] = temp_df[0]
    df['state'] = temp_df[1]
    
    df['total.price'] = df['quantity'] * df['price']
    
    cols_to_keep_list = [
    'order.id', 
    'order.line', 
    'order.date',  
    'model', 
    'quantity',
    'price', 
    'total.price',
    'bikeshop.name', 
    'category.1', 
    'category.2',
    'frame.material', 
    'city', 
    'state' 
    ]
    df = df[cols_to_keep_list]
    
    df.columns = df.columns.str.replace('.', '_')
    
    return df

collect_data()

# %%
