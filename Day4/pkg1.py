from Day4_Q1 import File
import datetime

if __name__ == "__main__":
    fs = File(".")

    max_files = fs.getMaxsizeFile(2)
    print("Max Size Files:", max_files)

    latest_files = fs.getLatestFiles(datetime.datetime(2018, 2, 1))
    print("Latest Files:", latest_files)
