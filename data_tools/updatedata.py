from gdocs import GoogleDoc

doc_1 = {
    "key": "12HjCiVKUTo_IbrXjvV0MCwKaoI5wd4206Hc0XOccXTo",
    "file_name": "data",
    "file_format": "xlsx"
}

def get_data():
    g = GoogleDoc(**doc_1)
    g.get_auth()
    g.get_document()
    
if __name__ == "__main__":
    get_data()
