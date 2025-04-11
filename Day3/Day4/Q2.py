import os
from datetime import datetime, date
from pkg.file import File

class MaxFile(File):
    def __init__(self, path):
        super().__init__(path)
        self.path = path

    def getMaxSizeFile(self, n):
        files_with_sizes = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path)
                    files_with_sizes.append((file_path, size))
        files_with_sizes.sort(key=lambda x: x[1], reverse=True)
        return [file[0] for file in files_with_sizes[:n]]

    def getLatestFiles(self, start_date):
        start_timestamp = datetime.combine(start_date, datetime.min.time()).timestamp()
        recent_files = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if os.path.isfile(file_path):
                    mod_time = os.path.getmtime(file_path)
                    if mod_time > start_timestamp:
                        recent_files.append(file_path)
        return recent_files



if __name__ == "__main__":
    import datetime

    folder_path = r"C:\Users\N. Sai Swagath\Desktop\Assesments"  
    fs = MaxFile(folder_path)

    print("Top 2 largest files:")
    print(fs.getMaxSizeFile(2))

    print("\nFiles modified after 1st Feb 2018:")
    print(fs.getLatestFiles(datetime.date(2018, 2, 1)))
