import dropbox

class PyDropbox:
    """Simple Wrapper for Dropbox Python API"""
    def __init__(self, token):
        """
        Args:
            token (string): authentication token to log-in
        Generate token at https://www.dropbox.com/developers/apps
        """
        self.dbx = dropbox.Dropbox(token)

    def encode(self, data):
        """Encode given data to UTF-8"""
        return str(data).encode('utf-8')

    def upload(self, data, to_path):
        binary_data = self.encode(data)
        self.dbx.files_upload(binary_data, to_path)

    def download(self, from_path, to_path):
        self.dbx.files_download_to_file(to_path, from_path)
