import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case_string)
    return snake_case_string.lower()

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    data = data[(data["passenger_count"] != 0) & (data["trip_distance"] != 0)]

    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date

    data.columns = data.columns.to_series().apply(camel_to_snake)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert any(output["vendor_id"].isin([1, 2])), 'vendor_id is neither one of the existing values.'
    assert output[output["passenger_count"] == 0]["passenger_count"].count() == 0, 'There are rides with zero passengers.'
    assert output[output["trip_distance"] == 0]["passenger_count"].count() == 0, 'There are rides with zero trip distance.'
 
