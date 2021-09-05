import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    
    fromf = input("Enter a path you want to back up: ")
    to = input("Enter a path you want to go to dropbox: ")
    
    access_token = "WyQ_y_o96IwAAAAAAAAAAaQV2CYX5_l3Sd249sh_Z0xH26xssqgxG9PKZ_UXjYuz"
    transferData = TransferData(access_token)

    file_from = fromf
    file_to = to  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File backed up.")

main()