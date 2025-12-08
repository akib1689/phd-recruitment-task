import getpass
import os

import requests
from boaapi.boa_client import BOA_API_ENDPOINT, BoaClient
from boaapi.status import CompilerStatus, ExecutionStatus
from tqdm import tqdm

client = BoaClient(endpoint=BOA_API_ENDPOINT)
user = input("Username [%s]: " % getpass.getuser())
if not user:
    user = getpass.getuser()
client.login(user, getpass.getpass())
print('successfully logged in to Boa API')

# get the last job
job = client.last_job();

print('Last job details:')
print(job)

if job.is_running() is False and job.exec_status == ExecutionStatus.FINISHED:
    print('Job is not running and finished successfully. Downloading output...')
    outputSize, outputHash = job.output_hash()
    output_file = f'assets/data-samples/job-{job.id}-output.txt'
    if os.path.exists(output_file):
        print(f'Output file {output_file} already exists. Skipping download.')
        exit(0)
    
    print(f'Output size: {outputSize} bytes')
    print(f'Output hash: {outputHash}')
    job_url = job.get_url() + '/download'
    # make the job public if not already (this is a hack to avoid authentication issues)
    job.set_public(True)
    print(f'Downloading from {job_url} ...')
    response = requests.get(job_url, stream=True)
    response.raise_for_status()
    total = int(response.headers.get('content-length', 0))
    chunk_size = 8192
    with open(f'job-{job.id}-output.txt', 'wb') as f, tqdm(
        desc=f'Downloading job-{job.id}-output.txt',
        total=total,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))
    print(f'Output downloaded to job-{job.id}-output.txt')
    # make the job private again
    job.set_public(False)
else:
    print('Job is still running. Please wait until it finishes.')
    