### Mining Software Repositories for Bug-Fix Patterns
**Analysis of Bug-Fix Commits and Vulnerability Patterns**

Note:
Hello all, today we'll explore patterns in software bugs and vulnerabilities across thousands of commits



Presented by: *Akibur Rahman*

Note: 
As you know by now, I'm Akibur Rahman, a software engineer at..
I completed my BSc in CSE from Bangladesh University of Engineering and Technology.



### Overview

This study analyzes bug-fix commits across GitHub repositories

Note:
The study aims to understand the patterns of bug-fix commits and their relationship with the project characteristics.
- To achieve this, we use Boa's GitHub dataset to mine commits at scale
- We extract the control flow graph (CFG) of each commit
- Then we try to find patterns in those commits.


### Research Questions

1. **Top Projects**: What are the top 10 projects with the most bug-fix commits and their characteristics?

Note:
- What characteristics do they share?
- What makes them different?
- Do any of the projects have incivil commits?
- Is there any correlation between the depth of the CFG and the number of bug-fix commits?


### Research Questions (cont.)

2. **Issue Types**: What are the most common types of bugs and vulnerabilities?

Note:
- Can we identify patterns in the bug-fix commits?
- Do they share any common characteristics?



### Methodology

**Data Collection Pipeline**
1. Boa Query: Keyword-based commit detection <!-- .element: class="fragment" -->
   - Keywords: `bug`, `fix`, `patch`, `issue`, `vulnerability`, `CVE`, etc.
1. CFG Extraction: Serialized control flow graphs <!-- .element: class="fragment" -->
1. Dataset Definition: Boa query output to dataset <!-- .element: class="fragment" -->
1. Scale: ~1.1 GB dataset <!-- .element: class="fragment" -->

Note:
- Keyword based commit detection of fix commits. I first defined the keywords that might be used in bug-fix commits.
- Then I used Boa to query the GitHub dataset and extract the commits.
- Then I iterated over the changed files and extracted the methods that were present in those file.
- Then I checked if the method was present in the previous commit or is this a new method?
- If it was an present in the previous commit of the repository then I kept both of their CFGs and if it was a new method then I kept the CFG of the new method.
- Then I defined the dataset schema with the mandatory fields and all other fields that I might need to analyze the data.


### Methodology (cont.)

**Data Preprocessing**
1. Parse the Boa platform output <!-- .element: class="fragment" -->
<li class="fragment">Write a <a href="https://github.com/akib1689/phd-recruitment-task/blob/main/notebooks/data_validation.ipynb">notebook</a> for exploratory data analysis</li>
1. Proceed with data analysis to answer the research questions <!-- .element: class="fragment" -->

Note:
- First I downloaded the output from the Boa platform and stored it in a text file.
- Then wrote a python script to parse that text file and populate the dataset.
- Then wrote an EDA notebook to explore the data.
- After that I started to analyze the data to answer the research questions.


**Data columns (total 16 columns):**
| # | Column                | Dtype |
|---|-----------------------| ----- |
| 0  | project_name           | string |
| 1  | project_description    | string |
| 2  | project_url            | string |
| 3  | project_creation_date  | string |
| 4  | project_database       | string |
| 5  | project_interfaces     | float64 |

Note:
- `project_name`: The name of the project
- `project_description`: The description of the project
- `project_url`: The URL of the project
- `project_creation_date`: The creation date of the project
- `project_database`: The databases That is used in the project Later I found out that this column was empty on the Github small dataset. That was present in the Boa Platform dataset.
- `project_interfaces`: The interfaces of the project Like mobile desktop etc.


**Data columns (total 16 columns):**
| # | Column                | Dtype |
|---|-----------------------| ----- |
| 6  | project_oss            | string |
| 7  | project_languages      | string |
| 8  | project_topics         | string |
| 9  | commit_url             | string |
| 10 | files_changed_count    | int64  |

Note:
- `project_oss`: The OS that this project was built for
- `project_languages`: The languages that are used in the project
- `project_topics`: The topics that are related to the project
- `commit_url`: The URL of the commit
- `files_changed_count`: The number of files that were changed in the commit


**Data columns (total 16 columns):**
| # | Column                | Dtype |
|---|-----------------------| ----- |
| 11 | commit_message         | string |
| 12 | file_path              | string |
| 13 | method_name            | string |
| 14 | cfg_dot                | string |
| 15 | cfg_state              | string |

Note:
- `commit_message`: The message of the commit
- `file_path`: The path of the file that was changed in the commit
- `method_name`: The name of the method that was changed in the commit
- `cfg_dot`: The control flow graph of the method in DOT format
- `cfg_state`: The state of the control flow graph (this has 2 values. `PRE` and `POST`) `PRE` means the method was present in the previous commit and the cfg dot that is present is the CFG of the method in the previous commit. `POST` means the method was present in the current commit and the cfg dot that is present is the CFG of the method in the current commit.



### Top 10 Projects

- Consider current commit and count the number of commits for each project <!-- .element: class="fragment" -->
- Higher the number of commits, higher the project is ranked <!-- .element: class="fragment" -->

Note:
To answer this question, 
- I first removed the rows with `PRE` in the `cfg_state` column, as they do not represent actual code changes.
- Then I grouped the DataFrame by `project_name` and count the number of commits for each project.
- Then I sorted the projects by the number of commits in descending order and selected the top 10.


| Rank | Project | Commits | Domain |
|------|---------|---------|--------|
| 1 | Ceylon compiler | 2,126 | Language Engineering |
| 2 | Calendar | 1,040 | Android Mobile |
| 3 | OpenNaaS Routing | 679 | Networking/NFV |

Note:
The top projects with most bug-fix related commits are:
- Ceylon compiler
- Calendar Appls platform packages
- OpenNaaS Routing 
With **2 thousand**, **1 thousand** and **679** commits respectively. 


### Top 10 Projects (cont.)

| Rank | Project | Commits | Domain |
|------|---------|---------|--------|
| 4 | Red5 Server | 630 | Media Streaming |
| 5 | Eclipse Web Tools | 595 | Eclipse IDE |
| 6 | Turmeric Runtime | 66 | Enterprise SOA |

Note:
The next projects are red 5 server and web tools which are form media and eclipse IDE domain


### Top 10 Projects (cont.)

| Rank | Project | Commits | Domain |
|------|---------|---------|--------|
| 7 | Mez | 58 | Time Tracking |
| 8 | petulant-batman | 49 | Student Project |
| 9 | Bartsy Venue Android | 47 | Android App |
| 10 | Compass2 | 30 | Sesam Integration |

Note:
- If you notice the steep decline from 2,126 to 30 commits indicates extreme skew in the dataset



### Similarities across 10 projects

1. Infrastructure Focus <!-- .element: class="fragment" --> 
1. Most are frameworks, compilers, or developer tools <!-- .element: class="fragment" -->

Note:
All of these projects are infrastructure focused. i.e. they are frameworks, compilers, or developer tools none of them are applications that end users use.



### Key Differences

1. **Scale (Power Law Distribution)**
   - Top: 2,126 commits <!-- .element: class="fragment" -->
   - Median: ~66 commits  <!-- .element: class="fragment" -->
   - Bottom: 30 commits <!-- .element: class="fragment" -->

Note:
Speaking of scale, the distribution of commits follows a power law distribution. 
That is, the top projects have many more commits than the median and the bottom projects.
As you can see, the top project has 2,126 commits, the median has 66 commits and the bottom has 30 commits.


### Key Differences (cont.)

2. **Governance Models**
   - Corporate/Foundation (Eclipse, eBay) <!-- .element: class="fragment" -->
   - Community (Red5) <!-- .element: class="fragment" -->
   - Academic (petulant-batman) <!-- .element: class="fragment" -->

Note:
Speaking of governance, the projects are distributed across different governance models. Like There are presence of both corporate and foundation projects, community projects and academic projects.

- From corporate domain we can see the presence of projects owned by companies like `eBay` and from the foundation domain we can see the presence of projects owned by organizations like `Eclipse`.
- There is also a representation of academic projects like `petulant-batman`. Also community maintained projects like `Red5` are also present.


### Key Differences (cont.)

3. **Application Domains**
   - Language Engineering (Ceylon) <!-- .element: class="fragment" -->
   - Mobile/Android (Calendar, Bartsy) <!-- .element: class="fragment" -->
   - Media Streaming (Red5) <!-- .element: class="fragment" -->
   - Networking (OpenNaaS) <!-- .element: class="fragment" -->
   - Enterprise SOA (Turmeric) <!-- .element: class="fragment" -->

Insight: High bug-fix counts span multiple industries <!-- .element: class="fragment" -->

Note:
This diversity suggests that bug-fixing intensity is not domain-specific but rather depends on project maturity and team practices



### Incivil Commits in Top Projects

**Question**: Do the most active projects have toxic communication?

<li class="fragment"> <b>Result</b>: Almost Zero </li>
<li class="fragment"> Only <b>1</b> toxic commit found across all top 10 projects </li>

Note:
- We answered the research question regarding incivil commits.
- We used a pre-trained toxicity classifier (`unitary/toxic-bert`) to analyze commit messages.
- The result was overwhelmingly positive: we found almost zero toxicity.
- Only a single commit in the `ceylon-compiler` project was flagged, and upon inspection, it was a false positive or minor issue ("fixed stupid typos").
- This indicates a high level of professionalism in these top infrastructure projects.



### CFG Depth & Bug Correlation

**Hypothesis**: Complex methods are more bug-prone.

<li class="fragment"> <b>Crash Fixes</b>: Mean depth <b>10.74</b> (Highest complexity) </li>
<li class="fragment"> <b>Security Fixes</b>: Mean depth <b>8.62</b> </li>
<li class="fragment"> <b>Maintenance</b>: Mean depth <b>4.46</b> (Lowest complexity) </li>

Note:
- We then looked at the correlation between Control Flow Graph (CFG) depth and bugs.
- We calculated the depth of the CFG for every method involved in a fix.
- The data confirms our hypothesis: methods requiring fixes for **Crashes** and **Security Vulnerabilities** have significantly deeper CFGs (higher cyclomatic complexity) than those involved in routine maintenance.
- Complexity breeds bugs.


### Do Fixes Reduce Complexity?

<li class="fragment"> <b>General Trend</b>: Most fixes do <b>not</b> significantly change </li>
<li class="fragment"> <b>Exception</b>: <b>Security Fixes</b> </li>
<li class="fragment"> Only category with <b>negative</b> mean delta (-0.01) </li>
<li class="fragment"> Suggests intentional simplification </li>

Note:
- We also asked: does fixing a bug reduce the code's complexity?
- Generally, the answer is no. Most bug fixes are small patches that don't fundamentally refactor the code, so the depth change is near zero.
- However, **Security Fixes** are an interesting exception. They are the only category showing a trend towards simplification.
- This suggests that when fixing security issues, developers potentially simplify logic to remove attack surfaces.



### Issue Type Clustering

**Goal**: Identify recurring bug patterns without manual labeling

Note:
To answer the second research question about identifying common issue types, I have used the semantic clustering pipeline. The main goal behind this is to make a pipeline that can identify recurring bug patterns without manual labeling. (Because of manual work that would need to be done, it is not a feasible option to label the issues manually).



### Pipeline
<li class="fragment"> <b>Text Representation</b>: <code>Message + Files + Methods</code></li>
<li class="fragment"> <b>Embedding</b>: <code>all-MiniLM-L6-v2</code> (384D vectors)</li>
<li class="fragment"> <b>Dimensionality Reduction</b>: UMAP (50D)</li>
<li class="fragment"> <b>Clustering</b>: HDBSCAN (density-based)</li>
<li class="fragment"> <b>Interpretation</b>: TF-IDF keyword extraction</li>

Note:
To answer the second research question about identifying common issue types, we employed a semantic clustering pipeline.
- First, we constructed a rich text representation for each commit by combining the commit message, the changed filenames, and the changed method names. This gives us more context than the message alone.
- We then used the `all-MiniLM-L6-v2` model from Sentence Transformers to convert this text into 384-dimensional vectors. We chose this model for its balance of speed and semantic capture quality.
- For dimensionality reduction, we used UMAP to reduce the vectors to 50 dimensions. This step is crucial to reduce noise and computational complexity while preserving the semantic manifold of the data.
- Then we applied HDBSCAN for clustering. We specifically chose HDBSCAN because it's a density-based algorithm that doesn't require pre-specifying the number of clusters (unlike K-Means) and, importantly, it can identify and exclude "noise" points that don't fit well into any cluster.
- finally, to interpret these clusters, we used TF-IDF analysis to extract the most representative keywords for each group.



### Clustering Results

| Cluster | Size | Top Keywords | Theme |
|---------|------|--------------|-------|
|11| 434 | jsf, jst, eclipse, org, plugins | IDE/Tooling |
|42| 322 | ceylon, redhat, ceylondoc, tools, compiler, getresourceurl | Code Generation |

Note:
Here are some of the most significant clusters we identified.
- **Cluster 11** (434 commits) is dominated by terms like "jsf", "eclipse", and "plugins", pointing to IDE tooling work, specifically related to the Eclipse Web Tools project.
- **Cluster 42** (322 commits) focuses on "ceylon", "compiler", and "tools", aligning with the Ceylon Compiler project.


### Clustering Results (cont.)

| Cluster | Size | Top Keywords | Theme |
|---------|------|--------------|-------|
|5| 231 | i2cat, net, mantychore, manticore, bundles, svn | Networking |
|29| 220 | opennaas, router, extensions, org, core, bundles | Networking |

Note:
- **Cluster 5** (231 commits) and **Cluster 29** (220 commits) are both related to Networking. Cluster 29 specifically involves "opennaas" and "router", which matches the OpenNaaS Routing project.
- This result is quite validating: the semantic clusters we found without supervision align very well with the dominant projects we identified in the first part of the analysis.



### Cluster Visualization


![UMAP Projection of semantic clusters](/assets/cluster-projection.png)


### Cluster Visualization (cont.)

- Dense regions: Well-defined issue types <!-- .element: class="fragment" -->
- Noise points: Unique or rare bugs <!-- .element: class="fragment" -->
- Separation: Distinct problem domains <!-- .element: class="fragment" -->

Note:
When we visualize these clusters using a 2D UMAP projection, we can see the semantic landscape of the bugs.
- There are clear, dense regions representing the well-defined issue types we just discussed.
- The scattered points are the "noise" identified by HDBSCAN. These represent unique, rare, or poorly described bugs that don't fit into the main categories.
- The separation between clusters confirms that there are distinct problem domains within the dataset—fixing a router bug is semantically very different from fixing a calendar UI bug.



### Key Findings

<li class="fragment"> <b>Java-Centric Dataset</b>: Strong bias toward Java infrastructure</li>
<li class="fragment"> <b>Power Law Distribution</b>: Few projects dominate fix activity</li>
<li class="fragment"> <b>Diverse Domains</b>: High bug counts across industries</li>
<li class="fragment"> <b>Semantic Patterns</b>: Clustering reveals 4+ distinct issue types</li>
<li class="fragment"> <b>Infrastructure Bias</b>: Tooling projects have higher fix rates</li>

Note:
Summarizing our key findings from both RQ1 and RQ2:
- First, the dataset is heavily Java-centric. Most of the top projects and clusters relate to Java ecosystem tools (Eclipse, Red5, Ceylon).
- We observed a power-law distribution in bug fixes: a handful of projects account for the vast majority of the activity, while the long tail has very few.
- Despite the Java bias, the domains are diverse: from Language Engineering to Mobile Apps to Networking.
- Our semantic clustering successfully revealed distinct issue types without manual intervention.
- And broadly, infrastructure and tooling projects seem to have higher rates of reported bug fixes compared to smaller end-user applications in this dataset.



### Limitations

**Dataset Constraints**
- **Language Bias**: Heavy Java representation
- **Keyword Reliance**: May miss unconventional commit messages
- **Time Period**: Snapshot of historical data

Note:
It is important to acknowledge the limitations of this study.
- The heavy Java representation in the Boa dataset limits the generalizability of our findings to other ecosystems like Python or JavaScript.
- Our reliance on specific keywords (like "bug", "fix") might miss commit messages that use non-standard terminology or just issue IDs.
- This is a historical snapshot, so it may not reflect current trends in software development.


### Future Directions

1. **Cross-Language Study**: Expand beyond Java
1. **Temporal Analysis**: Track bug patterns over time
1. **Automated Classification**: ML models for issue type prediction

Note:
Moving forward, there are several exciting directions for this research:
- We can correlate the Control Flow Graph (CFG) depth with bug density to see if more complex code is indeed more bug-prone.
- We should implement the toxicity analysis to understand the human aspect of these bug-fix interactions.
- Expanding the study to include more languages would improve generalizability.
- A temporal analysis could show us if the types of bugs change as a project matures.
- Finally, we could use our labeled clusters to train a supervised ML model to automatically classify new bug reports.



### Conclusions

**Impact & Significance**
- **Pattern Recognition**: Semantic clustering effectively identifies issue types
- **Scale Insights**: Dataset dominated by infrastructure projects
- **Methodology**: Reproducible pipeline for repository mining

**Next Steps**: Expand analysis and create automated classification systems

Note:
In conclusion, this work demonstrates the power of combining large-scale repository mining with modern NLP techniques.
- We showed that semantic clustering is an effective way to identify issue types without manual labeling.
- We gained insights into the scale and nature of bug fixes in the open-source ecosystem, particularly for infrastructure projects.
- And we have established a reproducible pipeline using Boa and Python that can be extended for future research.
- We are ready to take the next steps to expand this analysis and build more robust tools for developers.



### Thank You

**Questions?**

**Repository**: [phd-recruitment-task](https://github.com/akib1689/phd-recruitment-task)

**Analysis Notebooks**:
- `data_validation.ipynb` - Data validation and EDA
- `top_10_project_with_fix.ipynb` - Top 10 projects
- `issue_clustering_analysis.ipynb` - Semantic clustering

Note:
Thank you very much for your time. I have uploaded all the code, notebooks, and documentation to the GitHub repository listed here.
I am now happy to take any questions you might have.