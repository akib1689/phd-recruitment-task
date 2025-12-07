# Work Log

## Task 1: Account Setup and Registration

### Boa Platform Registration

I began my task by registering for an account on the Boa platform. Boa is a powerful tool for mining software repositories and analyzing source code at scale. From their website, I learned that users must register and be approved before they can access the platform.

#### Registration Process

1. **Initial Access**: I navigated to the Boa website at <https://boa.cs.iastate.edu/boa/>
2. **Account Creation**: Since the platform requires registration and approval before use, I completed the user registration form
3. **Confirmation**: Successfully submitted my registration request and received confirmation within one business day.

#### Screenshots of Registration Process

**Registration Page:**

![Boa Registration Page](../assets/screenshots/register.png)

**Login Page (Post-Registration):**

![Boa Login Page](../assets/screenshots/login.png)

#### What I have tried in the meantime

As I await for my account approval, I tried to install and set up Boa locally. There is not much documentation on how to do this, but I found this github repository:

- [Boa docker](https://github.com/boalang/boa-docker.git)
- [Boa compiler](https://github.com/boalang/compiler.git)

The boa docker image was not working for me, The documentation was outdated and only ran on Arm architecture. I tried to build the image on both my M2 macbook air (arm platform) and and Ubuntu 22.04 (x86_64 platform) but I was not able to make it work.

Main issues I faced:

- On the M2 macbook air, the docker build failed because some of the install command on the dockerfile, the PPA was renamed. I tried to fix it but then I faced other issues with the dependencies. Like It was trying to copy some files from my `/usr/lib` folder to the docker image but those files did not exist on my machine.

- On the Ubuntu machine, the docker build was not successful because I could not run arm images on an x86_64 machine. I tried to use `--platform=linux/arm64/v8` flag but then I faced other issues with the dependencies.

## Task 2: Reviewing Boa Documentation and Examples

After I got my access to the Boa platform, I started reviewing the exampls and documentation available at [https://boa.cs.iastate.edu/examples/index.php](https://boa.cs.iastate.edu/examples/index.php). and I tried to run those examples on my local machine. During this process, I discovered that there is a boa extension for VSCode that makes it easier to write and run boa scripts. I installed the extension and tried to run some of the examples provided in the documentation. I tried to run the most programming language example that is available in the documentation (first example available in the documentation). Using the vs code extension, I was able to run the example but when getting results using the extension, I faced problem the output was showing `undefined`. The output was okay but not showing in the extension output window. I had to check the output files generated in the platform to see the results.
See screenshot below:
![Boa VSCode Extension Output](../assets/screenshots/boa-vscode-extension-output.png)
![Boa Platform Output File](../assets/screenshots/boa-platform-output-file.png)

## Task 3: Creating Dataset of Control Flows with Known Vulnerabilities

### Subtask 3.1: Identifying Bug-Fix Commits

Written a Boa script to identify commits that indicate bug fixes using keywords such as "bug", "fix", "patch", "issue", "error", "vulnerability", "security", "CVE", "buffer", "injection", "npe", and "overflow". The script iterates over all commits in the Boa dataset and checks if the commit message contains any of the specified keywords. If a match is found, it outputs the project URL, commit URL, and commit message.
