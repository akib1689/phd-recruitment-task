
import os

input_path = './assets/data-samples/job-113733-output.txt'
output_path = './assets/data-samples/paired_cfgs.csv'

# Check if input file exists
if not os.path.exists(input_path):
    print(f"Input file {input_path} does not exist.")
    exit(1)

rows = []
with open(input_path, 'r') as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        # Remove the prefix
        if line.startswith('paired_cfgs[] = '):
            line = line[len('paired_cfgs[] = '):]
        # Split into 6 fields using ' , ' as separator, but only for the first 5 splits
        parts = line.split(' , ', 5)
        if len(parts) < 6:
            continue
        repo_url = parts[0].strip()
        commit_url = parts[1].strip()
        commit_message = parts[2].strip()
        # The method name is the 4th field, but clean up if needed
        method_name = parts[3].strip()
        cfg = parts[4].strip()
        action = parts[5].strip()
        rows.append([repo_url, commit_url, commit_message, method_name, cfg, action])

# Write with '|' as separator
with open(output_path, 'w', newline='') as csvfile:
    csvfile.write('repo_url,commit_url,commit_message,method_name,cfg,action\n')
    for row in rows:
        csvfile.write(','.join(row) + '\n')
print(f"Comma-separated file created at {output_path}")
    