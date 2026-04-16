import os

class FileScanner:
    def __init__(self, root_directory):
        self.root_directory = root_directory

    def scan(self):
        print(f"Scanning directory: {self.root_directory}")
        for dirpath, dirnames, filenames in os.walk(self.root_directory):
            print(f'Found directory: {dirpath}')
            for filename in filenames:
                self.process_file(os.path.join(dirpath, filename))

    def process_file(self, file_path):
        print(f'Processing file: {file_path}')
        # Add file processing logic here

if __name__ == '__main__':
    scanner = FileScanner('/')  # Change to the desired root directory
    scanner.scan()