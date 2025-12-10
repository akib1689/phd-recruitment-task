# Mining Software Repositories for Bug-Fix Patterns

**Analysis of Bug-Fix Commits and Vulnerability Patterns**


## Overview

This study analyzes bug-fix commits across GitHub repositories using:
- **Boa Infrastructure** for large-scale repository mining
- **Control Flow Graph (CFG)** extraction
- **Semantic clustering** to identify issue patterns
- **Statistical analysis** of project characteristics

Note:
Today we'll explore patterns in software bugs and vulnerabilities across thousands of commits



## Research Questions

1. **Top Projects**: What are the top 10 projects with the most bug-fix commits?
   - What characteristics do they share?
   - What makes them different?
   - Do any of the projects have incivil commits?
   - Is there any correlation between the depth of the CFG and the number of bug-fix commits?



## Research Questions (cont.)

2. **Issue Types**: What are the most common types of bugs and vulnerabilities?
   - Can we identify patterns using semantic analysis?



## Methodology

### Data Collection Pipeline

1. **Boa Query**: Keyword-based commit detection
   - Keywords: `bug`, `fix`, `patch`, `issue`, `vulnerability`, `CVE`, etc.
2. **CFG Extraction**: Serialized control flow graphs
3. **Dataset Schema**: `project_url`, `commit_url`, `message`, `cfg_data`
4. **Scale**: ~1.1 GB dataset with thousands of commits

Note:
We used Boa's GitHub dataset to mine commits at scale, focusing on repositories with clear bug-fix signals



## Top 10 Projects

| Rank | Project | Commits | Domain |
|------|---------|---------|--------|
| 1 | Ceylon compiler | 2,126 | Language Engineering |
| 2 | Calendar | 1,040 | Android Mobile |
| 3 | OpenNaaS Routing | 679 | Networking/NFV |

Note:
Notice the massive drop after rank 1 - this is a power law distribution


## Top 10 Projects (cont.)

| Rank | Project | Commits | Domain |
|------|---------|---------|--------|
| 4 | Red5 Server | 630 | Media Streaming |
| 5 | Eclipse Web Tools | 595 | Eclipse IDE |
| 6 | Turmeric Runtime | 66 | Enterprise SOA |


## Top 10 Projects (cont.)

| Rank | Project | Commits | Domain |
|------|---------|---------|--------|
| 7 | Mez | 58 | Time Tracking |
| 8 | petulant-batman | 49 | Student Project |
| 9 | Bartsy Venue Android | 47 | Android App |
| 10 | Compass2 | 30 | Sesam Integration |

Note:
The steep decline from 2,126 to 30 commits indicates extreme skew in the dataset



## Similarities across the top 10 projects

1. **Infrastructure Focus**: Most are frameworks, compilers, or developer tools
   - Ceylon Compiler
   - Eclipse Web Tools
   - Red5 Server
   - Turmeric Runtime

Note:
The Java homogeneity could reflect the dataset focus or the prevalence of Java in enterprise infrastructure


## Key Differences

1. **Scale (Power Law Distribution)**
   - Top: 2,126 commits
   - Median: ~66 commits  
   - Bottom: 30 commits

2. **Governance Models**
   - Corporate/Foundation (Eclipse, eBay)
   - Community (Red5)
   - Academic (petulant-batman)

Note:
The presence of both enterprise and student projects in the top 10 shows diverse coding practices



## Dissimilarities (cont.)

3. **Application Domains**
   - Language Engineering (Ceylon)
   - Mobile/Android (Calendar, Bartsy)
   - Media Streaming (Red5)
   - Networking (OpenNaaS)
   - Enterprise SOA (Turmeric)

**Insight**: High bug-fix counts span multiple industries

Note:
This diversity suggests that bug-fixing intensity is not domain-specific but rather depends on project maturity and team practices



## Issue Type Clustering

**Goal**: Identify recurring bug patterns without manual labeling

**Pipeline**:
1. **Text Representation**: `Message + Files + Methods`
2. **Embedding**: `all-MiniLM-L6-v2` (384D vectors)
3. **Dimensionality Reduction**: UMAP (50D)
4. **Clustering**: HDBSCAN (density-based)
5. **Interpretation**: TF-IDF keyword extraction

Note:
We chose HDBSCAN because it doesn't require pre-specifying the number of clusters and can identify noise points



## Clustering Results

| Cluster | Size | Top Keywords | Theme |
|---------|------|--------------|-------|
| 3 | 180 | calendar, android, event | **Calendar/Events** |
| 14 | 95 | jsf, jst, eclipse, plugins | **IDE/Tooling** |
| 41 | 42 | opennaas, router, bundles | **Networking** |
| 17/23 | 87 | codegen, ceylon, transform | **Code Generation** |

Note:
These clusters align with the top projects we identified, validating our approach



## Cluster Visualization

*UMAP Projection of semantic clusters of commits*

- **Dense regions**: Well-defined issue types
- **Noise points**: Unique or rare bugs
- **Separation**: Distinct problem domains

Note:
The visualization shows clear separation between different types of issues, suggesting meaningful semantic structure in bug-fix commits



## Key Findings

1. **Java-Centric Dataset**: Strong bias toward Java infrastructure
2. **Power Law Distribution**: Few projects dominate fix activity
3. **Diverse Domains**: High bug counts across industries
4. **Semantic Patterns**: Clustering reveals 4+ distinct issue types
5. **Infrastructure Bias**: Tooling projects have higher fix rates

Note:
These findings have implications for how we think about software quality and maintenance across different project types



## Limitations

### Dataset Constraints

- **Language Bias**: Heavy Java representation
- **Keyword Reliance**: May miss unconventional commit messages
- **Time Period**: Snapshot of historical data
- **Incivility Detection**: Not implemented in this phase

Note:
Future work should address these limitations to provide a more comprehensive view



## Future Directions

1. **CFG Depth Analysis**: Correlate graph complexity with bug density
2. **Toxicity Analysis**: Detect incivil commit messages
3. **Cross-Language Study**: Expand beyond Java
4. **Temporal Analysis**: Track bug patterns over time
5. **Automated Classification**: ML models for issue type prediction

Note:
These extensions would provide deeper insights into the socio-technical aspects of software bugs



## Conclusions

### Impact & Significance

- **Pattern Recognition**: Semantic clustering effectively identifies issue types
- **Scale Insights**: Dataset dominated by infrastructure projects
- **Methodology**: Reproducible pipeline for repository mining
- **Research Value**: Foundation for bug prediction and developer tool improvement

**Next Steps**: Expand analysis and create automated classification systems

Note:
This work demonstrates the power of combining large-scale mining with modern NLP techniques for software engineering research



## Thank You

### Questions?

**Repository**: [phd-recruitment-task](https://github.com/akib1689/phd-recruitment-task)

**Analysis Notebooks**:
- `research_task_1.ipynb` - Top 10 projects
- `issue_clustering_analysis.ipynb` - Semantic clustering

**Documentation**:
- `docs/top_10_fix_projects_analysis.md`
- `docs/issue_clustering_analysis.md`



## Appendix: Technical Stack

### Tools & Technologies

- **Data Mining**: Boa Infrastructure (boa.cs.iastate.edu)
- **NLP**: Sentence Transformers (all-MiniLM-L6-v2)
- **Clustering**: UMAP + HDBSCAN
- **Analysis**: Python, Pandas, Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **Presentation**: Reveal.js

Note:
All code and data are available in the repository for reproducibility