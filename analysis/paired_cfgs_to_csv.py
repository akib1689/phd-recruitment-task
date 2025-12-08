
import csv
import os
import re

# take jobid as input
jobid = input("Enter the job ID: ").strip()
input_path = f'assets/data-samples/job-{jobid}-output.txt'
output_path = f'assets/data-samples/job-{jobid}.csv'

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
        # Split into all fields. The source text joins fields with '[|]'.
        parts = [p.strip() for p in line.split('[|]')]

        # Expected fields (based on how rows are printed elsewhere):
        # 0 project_name
        # 1 project_description
        # 2 project_url
        # 3 project_creation_date
        # 4 project_database
        # 5 project_interfaces
        # 6 project_oss
        # 7 project_languages
        # 8 project_topics
        # 9 (possibly empty)
        # 10 commit_url
        # 11 files_changed_count
        # 12 commit_message (msg_clean)
        # 13 file_path
        # 14 method_name
        # 15 cfg_dot_curr (may have appended ' , POST' or ' , PRE')

        # Pad parts with empty strings up to 16 fields to avoid index errors
        if len(parts) < 16:
            parts += [''] * (16 - len(parts))

        project_name = parts[0]
        project_description = parts[1]
        project_url = parts[2]
        project_creation_date = parts[3]
        project_database = parts[4]
        project_interfaces = parts[5]
        project_oss = parts[6]
        project_languages = parts[7]
        project_topics = parts[8]
        # If the input contains an extra empty field at index 9, we accept that.
        commit_url = parts[10]
        files_changed_count = parts[11]
        commit_message = parts[12]
        file_path = parts[13]
        method_name = parts[14]

        # The CFG field may have an appended ' , POST' or ' , PRE'. We'll extract that.
        cfg_field = parts[15]
        cfg_state = ''
        if cfg_field:
            # Look for a trailing comma followed by PRE or POST, case-insensitive
            m = re.search(r"\s*,\s*(PRE|POST)\s*$", cfg_field, re.IGNORECASE)
            if m:
                cfg_state = m.group(1).upper()
                cfg = re.sub(r"\s*,\s*(PRE|POST)\s*$", '', cfg_field, flags=re.IGNORECASE).strip()
            else:
                # If not found, check if there is a trailing word PRE/POST without comma
                m2 = re.search(r"\s+(PRE|POST)\s*$", cfg_field, re.IGNORECASE)
                if m2:
                    cfg_state = m2.group(1).upper()
                    cfg = re.sub(r"\s+(PRE|POST)\s*$", '', cfg_field, flags=re.IGNORECASE).strip()
                else:
                    cfg = cfg_field
        else:
            cfg = ''

        rows.append([
            project_name,
            project_description,
            project_url,
            project_creation_date,
            project_database,
            project_interfaces,
            project_oss,
            project_languages,
            project_topics,
            commit_url,
            files_changed_count,
            commit_message,
            file_path,
            method_name,
            cfg,
            cfg_state,
        ])

# Write with '|' as separator
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    headers = [
        'project_name',
        'project_description',
        'project_url',
        'project_creation_date',
        'project_database',
        'project_interfaces',
        'project_oss',
        'project_languages',
        'project_topics',
        'commit_url',
        'files_changed_count',
        'commit_message',
        'file_path',
        'method_name',
        'cfg_dot',
        'CFG State',
    ]
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
print(f"Comma-separated file created at {output_path}")
    