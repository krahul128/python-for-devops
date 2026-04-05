 #This function will help to read the logs from the 'app.log' file and print its contents to the console. It uses a context manager (the 'with' statement) to ensure that the file is properly closed after its suite finishes, even if an error occurs. The 'r' mode is used to open the file for reading.  

def read_logs():
    lines = []
    with open('app.log', 'r') as file:
        lines = file.readlines()
    return  lines


def analyze(lines):
   log_counts = {
       "INFO": 0,
       "WARNING": 0,
       "ERROR": 0           
   }
   for line in lines:
     if "INFO" in line:
        log_counts.update({"INFO": log_counts["INFO"] + 1})
     elif "WARNING" in line: 
        log_counts.update({"WARNING": log_counts["WARNING"] + 1})   
     elif "ERROR" in line:
        log_counts.update({"ERROR": log_counts["ERROR"] + 1})       
     else:
        pass

   return log_counts
lines = read_logs()  
counts = analyze(lines)


print("log counts are: ", counts)


import json

with open('log_counts.json', 'w') as json_file:
    json.dump(counts, json_file, indent=4)

print("log counts saved to log_counts.json")