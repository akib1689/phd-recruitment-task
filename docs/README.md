# PhD Recruitment Task Presentation

This directory contains the reveal.js presentation summarizing the findings and conclusions of the PhD recruitment task.

## 🚀 Quick Start

### Option 1: Open Directly in Browser
Simply open `index.html` in your web browser:
```bash
open presentation/index.html
# or
cd presentation && open index.html
```

### Option 2: Local Development Server
For the best experience, serve the presentation using a local web server:

```bash
# Using Python 3
cd presentation
python3 -m http.server 8000

# Then open http://localhost:8000 in your browser
```

Or using Node.js:
```bash
# Using npx (no installation required)
cd presentation
npx http-server -p 8000

# Then open http://localhost:8000 in your browser
```

## 📋 Presentation Structure

The presentation covers:

1. **Title & Overview** - Introduction to the analysis
2. **Methodology** - Data collection pipeline and approach
3. **Top 10 Projects Analysis** - Most bug-fix heavy projects
4. **Common Characteristics** - Java dominance and infrastructure focus
5. **Dissimilarities** - Power law distribution and governance models
6. **Issue Type Clustering** - Semantic analysis approach
7. **Discovered Clusters** - Calendar, IDE, Networking, Code Generation themes
8. **Key Findings** - Summary of major insights
9. **Limitations** - Dataset and analysis constraints
10. **Future Directions** - Potential research extensions
11. **Conclusions** - Impact and significance
12. **Appendix** - Technical stack details

## 🎨 Customization

The presentation uses reveal.js 5.0.4 with:
- **Theme**: Modified Black theme with purple gradient accents
- **Markdown Support**: Write slides in markdown format
- **Syntax Highlighting**: Code blocks with Monokai theme
- **Slide Navigation**: Arrow keys, space, or on-screen controls

## ✏️ Making Changes

To modify the presentation content:

1. Open `index.html` in your editor
2. Find the `<script type="text/template">` section
3. Edit the markdown content between slide separators (`---`)
4. Save and refresh your browser

### Adding New Slides
Add a new slide by inserting:
```markdown
---

## Your New Slide Title

Your content here

---
```

### Slide Navigation Shortcuts
- `→` / `Space`: Next slide
- `←`: Previous slide
- `Esc`: Slide overview
- `S`: Speaker notes
- `F`: Fullscreen

## 📊 Data Sources

The presentation content is based on:
- `notebooks/research_task_1.ipynb` - Top 10 projects analysis
- `notebooks/issue_clustering_analysis.ipynb` - Semantic clustering
- `docs/top_10_fix_projects_analysis.md` - Project characteristics
- `docs/issue_clustering_analysis.md` - Methodology documentation

## 🔧 Technical Details

**Framework**: reveal.js 5.0.4 (CDN)  
**Markdown Parser**: reveal.js markdown plugin  
**Styling**: Custom CSS with gradient effects  
**Font**: Inter (system fallback)

## 📦 No Installation Required

The presentation uses CDN-hosted libraries, so no `npm install` or dependencies are needed. Just open and present!
