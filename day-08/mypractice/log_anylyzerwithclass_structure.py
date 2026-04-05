import json
import os

class LogAnalyzer:
    
    def __init__(self, filename):
        self.filename = filename
        self.project_dir = os.path.dirname(os.path.abspath(__file__))  #  project folder
        self.filepath = os.path.join(self.project_dir, filename)
        self.lines = []
        self.counts = {}

    def read_logs(self):
        try:
            with open(self.filepath, 'r') as file:
                self.lines = file.readlines()
            print(f"Successfully read: {self.filepath}")
        except FileNotFoundError:
            print(f"Error: '{self.filename}' not found in project folder ({self.project_dir})")
            print(f"Available files: {os.listdir(self.project_dir)}")  #  shows what files exist
            self.lines = []

    def analyze(self):
        if not self.lines:
            print("No lines to analyze.")
            return
        
        self.counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }
        for line in self.lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1

        print("Log counts are:", self.counts)

    def save_to_json(self):
        if not self.counts:
            print("No counts to save.")
            return
        
        output_filename = self.filename.replace('.log', '_counts.json')
        output_path = os.path.join(self.project_dir, output_filename)  #  saves in project folder
        
        with open(output_path, 'w') as json_file:
            json.dump(self.counts, json_file, indent=4)
        print(f"Log counts saved to: {output_path}")

    def run(self):
        self.read_logs()
        self.analyze()
        self.save_to_json()


#  Take user input
if __name__ == "__main__":
    filename = input("Enter the log filename (e.g. app.log): ")
    analyzer = LogAnalyzer(filename)
    analyzer.run()