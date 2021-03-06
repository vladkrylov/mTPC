import os
import sys

timepix_files_path = sys.argv[1]
number_of_events = int(sys.argv[2])

timepix_files = [os.path.join(os.path.abspath(timepix_files_path), f) for f in os.listdir(timepix_files_path) if f.startswith("run_") and f.endswith(".txt")]
timepix_files.sort()
timepix_files = timepix_files[:number_of_events]

with open("TimePixData.txt", 'w') as fout:
    for i in xrange(len(timepix_files)):
        fout.write(timepix_files[i] + "\n")

