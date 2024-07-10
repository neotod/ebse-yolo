import nextcloud_client

def download_dataset():
    nc = nextcloud_client.Client("https://storage.cse-sbu.ir/")
    nc.login(
        user_id="itsneotod@gmail.com",
        password="bKGvk/GYZ/cwSeYqppQzOEzGTfJSQ+7iEvLnKKsKHQw=",
    )

    nc.get_file("dataset_r_full.zip", local_file='./artifacts/dataset_r_full.zip')

def extract_zip(zip_file_base_path, extract_path):
    import zipfile

    with zipfile.ZipFile(zip_file_base_path, 'r') as f:
        f.extractall(extract_path)