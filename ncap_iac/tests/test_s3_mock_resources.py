from unittest.mock import MagicMock

## Make a mock s3 bucket with two dummy path variables.
def make_mock_bucket():
    mock_stored_obj_attrs = {"key":"key/key/key"}
    mock_stored_obj = MagicMock(**mock_stored_obj_attrs) 
    mock_bucket_attrs = {'objects.filter.return_value':[mock_stored_obj,mock_stored_obj]}
    mock_bucket = MagicMock(**mock_bucket_attrs)
    return mock_bucket
