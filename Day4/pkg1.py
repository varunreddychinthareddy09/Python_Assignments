import os.path
import datetime

class File():
    def __init__ (self, directory): 
        self.directory = directory

    def getMaxsizeFile(self, n):
        files = [(file, os.path.getsize(os.path.join(self.directory, file))) 
            for file in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, file))]
        files.sort(key=lambda x: x[1], reverse=True) 
        return [file[0] for file in files[:n]] 

    def getLatestFiles(self, date):
        files = [(f, os.path.getmtime(os.path.join(self.path, f))) 
                for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        date_timestamp = datetime.datetime(date.year, date.month, date.day).timestamp()
        latest_files = [f[0] for f in files if f[1] > date_timestamp]
        return latest_files
        for root,dir ,files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.basename(file_path)
                file_size = os.path.getsize(file_path)
                file_sizes[file_name] = file_size