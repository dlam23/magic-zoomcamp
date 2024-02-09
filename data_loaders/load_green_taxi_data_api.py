import io
import pandas as pd
import pyarrow as pa
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    taxi_schema = pa.schema([
        pa.field("VendorID", pa.int64()),
        pa.field("lpep_pickup_datetime", pa.timestamp('ns', tz='UTC')),
        pa.field("passenger_count", pa.int64()),
        pa.field("trip_distance", pa.float64()),
        pa.field("RatecodeID", pa.int64()),
        pa.field("store_and_fwd_flag", pa.string()),
        pa.field("PULocationID", pa.int64()),
        pa.field("DOLocationID", pa.int64()),
        pa.field("payment_type", pa.int64()),
        pa.field("fare_amount", pa.float64()),
        pa.field("extra", pa.float64()),
        pa.field("mta_tax", pa.float64()),
        pa.field("tip_amount", pa.float64()),
        pa.field("tolls_amount", pa.float64()),
        pa.field("improvement_surcharge", pa.float64()),
        pa.field("total_amount", pa.float64()),
        pa.field("congestion_surcharge", pa.float64()),
    ])

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    
    df = pd.read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet')

    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-'

    for month in range(2, 13):
        month_str = str(month)
        formatted_month = month_str.zfill(2)
        print(url + formatted_month + ".parquet")
        df = pd.concat([df, pd.read_parquet(url + formatted_month + ".parquet")])

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
