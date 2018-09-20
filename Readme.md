# PyDropbox

Simple Wrapper for Dropbox Python API

## Requirements
- Python 3
- [Dropbox SDK](https://github.com/dropbox/dropbox-sdk-python)

## Install

```
pip install pydropbox
```

## Example Usage
```
# Import
from pydropbox import PyDropbox

# Login
# Generate token at https://www.dropbox.com/developers/apps
token = 'asdfk6lwenmc2x5vds012fnkl23d'
dbx = PyDropbox(token)

# Upload
dict_to_uploaded = {'content': 'this is content to be uploaded'}
path_at_dropbox = '/folder_name/file_name'
dbx.upload(dict_to_be_uploaded, path_at_dropbox)


# Download
local_path = './downloaded.json'
path_at_dropbox = '/folder_name/file_name'
dbx.download(local_path, path_at_dropbox)
```
