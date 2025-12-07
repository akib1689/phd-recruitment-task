# PhD recruitment task

This repository contains the materials and instructions for the PhD recruitment task.
Please follow the guidelines below to complete the task.

## Task Description

1. Create a Boa account at [https://boa.cs.iastate.edu/boa/](https://boa.cs.iastate.edu/boa/).
1. Review Boa's documentation and program examples available at [https://boa.cs.iastate.edu/examples/index.php](https://boa.cs.iastate.edu/examples/index.php).
1. Use Boa to create a dataset containing the control flows of projects (i.e., CFG) that have known vulnerabilities, issues, and bugs. This dataset must contain commit messages of fixes.

    1. These are a few examples of keywords that show the existence of bugs, vulnerabilities, or issues in the commit: bug, patch, issue, fix, lint, error, vulnerability, security, CVE, buffer, injection, npe, overflow, etc.

    1. The dataset must be formatted to contain project url, commit url, commit message, and serialized CFG (nodes + edges as strings).

1. With the dataset at hand, answer the following questions:

    1. From the selected projects, what are the top 10 that have the most commits on fixing bugs, issues, and vulnerabilities?

        1. What are their common characteristics? For example, are they all related to machine learning, to mobile development, etc?
        1. Is there anything that all the top projects don't have in common?
        1. Do any of those projects have incivil commits? By incivil comments, we mean commit messages containing offensive, rude, or hostile language (e.g., as detected by a toxicity classifier or manual review).
        1. Regarding the CFGs of those projects, is the depth of the CFG correlated in any way to the existence of bugs, vulnerabilities, and issues?
    1. Analyze the commits from all projects and identify the most common types of issues, vulnerabilities, and bugs.
1. Create a presentation to showcase findings and conclusions.

### Deliverables

A presentation slide deck summarizing: Methodology, Key findings and observations, Figures/tables/graphs where appropriate, conclusions & limitations.

## Project Structure

```sh
├── analysis
├── assets
│   ├── data-samples
│   ├── diagrams
│   └── screenshots
│       ├── login.png
│       └── register.png
├── docs
├── presentation
└── README.md
```

- `analysis/`: Contains scripts and notebooks used for data analysis.
- `assets/`: Contains data samples, diagrams, and screenshots used in the presentation.
- `docs/`: Contains additional documentation related to the project.
- `presentation/`: Contains the slide deck summarizing the findings and conclusions.

## Progress Tracking

### Completed

- [x] Boa account registration
- [x] Initial documentation setup
- [x] Repository structure creation
- [x] Account approval (awaiting administrator approval)
- [x] Boa example programs review
- [x] Run a program to find all the commit messages containing keywords indicating bug-fix commits.

### In Progress

- [ ] Query development planning

### Planned

- [ ] Boa query development for bug-fix commit detection
- [ ] CFG extraction implementation
- [ ] Dataset generation and analysis
- [ ] Presentation creation with reveal.js

## Journey Documentation

For detailed step-by-step documentation of my progress, please see:  
📖 [Journey Documentation](docs/README.md)
