import pyarrow as pa
import pyarrow.parquet as pq
import os

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/galvanic-crow-412709-aa795a6e6c06.json"

bucket_name = 'mage-zoomcamp-dylan'
project_id = 'galvanic-crow-412709'

table_name = "nyc_green_taxi_data"

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data_to_google_cloud_storage(data: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=["lpep_pickup_date"],
        filesystem=gcs
    )