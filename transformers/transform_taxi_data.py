if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Rows with zero passengers:", data[data['passenger_count'] == 0]['passenger_count'].count())
    # Specify your transformation logic here

    return data[data['passenger_count'] > 0]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output[output['passenger_count'] == 0]['passenger_count'].count() == 0, 'There are rides with zero passengers.'
