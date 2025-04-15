import os8
import datetime

class File:
    def __init__ (self, directory): 
        self.directory = directory

    def getMaxsizeFile(self, n):
        files = [(file, os.path.getsize(os.path.join(self.directory, file))) 
            for file in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, file))]
        files.sort(key=lambda x: x[1], reverse=True) 
        return [file[0] for file in files[:n]] 

    def getLatestFiles(self, date):
        files = [file for file in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, file))]
        latest_files = []
        for file in files:
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(self.directory, file)))
            if modification_time > date:
                latest_files.append(file)
        return latest_files

if __name__ =="__main__":
    fs = File(".") 

    max_files = fs.getMaxsizeFile(2)
    print("Max Size Files:", max_files)

    latest_files = fs.getLatestFiles(datetime.datetime(2018, 2, 1))
    print("Latest Files:", latest_files)