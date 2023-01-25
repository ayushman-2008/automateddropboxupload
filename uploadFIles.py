import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)
    
    def upload_file(self, file_from, file_to):
        with open(file_from, "rb") as source:
            data = source.read()
        try:
            self.dbx.files_upload(data, file_to, mode=dropbox.files.WriteMode("overwrite"))
            print("File uploaded successfully.")
        except Exception as e:
            print("Error uploading file: " + str(e))
            

def main():
    access_token = "sl.BXd50fKjWjYs42GJPUiyv1X8d_mFfTcV2D17lULuvW7SxqWzD5Y-VA_U_-r0dUTewTp1QCYRc9f8SVvFQmuGT3s1bZ_t1oojnHpuKE9CbpW4uEL6az58y19E08kEebnRcXoA3mA"
    file_from = input("Enter the file to be uploaded: ")
    file_to = input("Enter the full path to upload the file to, including the name: ")
    transferData = TransferData(access_token)
    transferData.upload_file(file_from, file_to)

if __name__ == "__main__":
    main()