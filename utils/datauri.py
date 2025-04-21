from datauri import DataURI
import base64

def get_data_uri(file):
    return DataURI.make('image/jpeg', charset='utf-8', base64=True, data=file.read())

