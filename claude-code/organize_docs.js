const fs = require('fs');
const path = require('path');

// 1. Load Metadata
const metadataPath = path.join(process.cwd(), 'metadata.json');
const metadata = JSON.parse(fs.readFileSync(metadataPath, 'utf8'));

// Detection Patterns
const categories = [
    { priority: 1, name: "Introduction & Overview", patterns: ["welcome", "overview", "index", "intro", "readme", "about", "home", "start"] },
    { priority: 2, name: "Quick Start & Installation", patterns: ["quickstart", "quick-start", "install", "setup", "getting-started", "beginner"] },
    { priority: 3, name: "Tutorials & How-To", patterns: ["tutorial", "guide", "how-to", "howto", "learn", "example", "walkthrough"] },
    { priority: 4, name: "Concepts & Fundamentals", patterns: ["concept", "fundamental", "basic", "introduction", "understanding", "explained", "memory"] },
    { priority: 5, name: "Configuration & Settings", patterns: ["config", "setting", "customize", "preferences", "options", "statusline"] },
    { priority: 6, name: "Features & Capabilities", patterns: ["feature", "capability", "what-is", "what-can", "functionality", "interactive-mode", "sandboxing", "checkpointing", "desktop", "web", "chrome"] },
    { priority: 7, name: "Integration & Connection", patterns: ["integrate", "connect", "provider", "plugin", "extension", "adapter", "jetbrains", "vs-code", "slack", "gitlab", "github", "bedrock", "vertex", "microsoft", "mcp"] },
    { priority: 8, name: "Authentication & Security", patterns: ["auth", "security", "permission", "access", "login", "user", "account", "iam", "sandboxing"] },
    { priority: 9, name: "API & Reference", patterns: ["api", "reference", "sdk", "library", "endpoint", "method", "cli"] },
    { priority: 10, name: "Operations & Deployment", patterns: ["deploy", "operation", "run", "execute", "manage", "monitor", "scale", "costs", "analytics", "data-usage"] },
    { priority: 11, name: "Automation & Workflow", patterns: ["automat", "workflow", "hook", "trigger", "pipeline", "batch", "sub-agent", "headless"] },
    { priority: 12, name: "Advanced Topics", patterns: ["advanced", "expert", "optimize", "performance", "tuning", "deep-dive", "best-practices"] },
    { priority: 13, name: "Troubleshooting & Support", patterns: ["trouble", "faq", "help", "support", "error", "issue", "fix"] },
    { priority: 14, name: "Reference & Appendix", patterns: ["glossary", "appendix", "cheat-sheet", "lookup"] },
    { priority: 15, name: "Changelog & Releases", patterns: ["changelog", "release", "version", "update", "history", "news"] },
    { priority: 16, name: "Meta & Resources", patterns: ["pricing", "license", "legal", "community", "contributing", "other"] }
];

// Helper to find category
function detectCategory(doc) {
    const text = (doc.url + " " + doc.title + " " + (doc.category || "")).toLowerCase();
    
    // Special case overrides for "Docs En Overview" vs specific feature overviews
    if (doc.file_path.includes("overview.md") && !doc.file_path.includes("features")) return categories[0];

    for (const cat of categories) {
        if (cat.patterns.some(p => text.includes(p))) {
            return cat;
        }
    }
    return { priority: 99, name: "Other Resources" };
}

// 2. Assign Categories
const docsWithCats = metadata.documents.map(doc => {
    const cat = detectCategory(doc);
    return { ...doc, detectedCategory: cat };
});

// 3. Sort Logic
docsWithCats.sort((a, b) => {
    // Primary: Category Priority
    if (a.detectedCategory.priority !== b.detectedCategory.priority) {
        return a.detectedCategory.priority - b.detectedCategory.priority;
    }
    
    // Secondary: Specific file priorities within categories
    const getFilePriority = (d) => {
        const lower = d.file_path.toLowerCase();
        if (lower.includes("overview") || lower.includes("index") || lower.includes("intro")) return 1;
        if (lower.includes("quickstart") || lower.includes("setup")) return 2;
        return 3;
    };

    const pA = getFilePriority(a);
    const pB = getFilePriority(b);

    if (pA !== pB) return pA - pB;

    // Tertiary: Alphabetical by title
    return a.title.localeCompare(b.title);
});

// 4. Assign New Names & Generate Rename Map
const renameMap = {};
const newDocuments = [];
const groupedDocs = {};

docsWithCats.forEach((doc, index) => {
    const num = String(index + 1).padStart(3, '0');
    const oldName = doc.file_path;
    const newName = `${num}-${oldName}`;
    
    renameMap[oldName] = newName;
    
    // Update doc object
    const newDoc = {
        ...doc,
        file_path: newName,
        original_file_path: oldName,
        // Keep detected category for index generation (optional but helpful)
        _assigned_category: doc.detectedCategory.name
    };
    delete newDoc.detectedCategory; // Clean up temp property
    newDocuments.push(newDoc);

    // Group for index
    const catName = doc.detectedCategory.name;
    if (!groupedDocs[catName]) groupedDocs[catName] = [];
    groupedDocs[catName].push({
        num,
        file: newName,
        title: doc.title,
        summary: doc.summary,
        tags: doc.tags ? doc.tags.join(", ") : ""
    });
});

// 5. Generate Rename Script
let renameScript = "#!/bin/bash\n\n";
for (const [oldName, newName] of Object.entries(renameMap)) {
    if (fs.existsSync(oldName)) {
        renameScript += `mv "${oldName}" "${newName}"\n`;
    } else {
        console.warn(`Warning: File ${oldName} not found locally.`);
    }
}
fs.writeFileSync('rename_docs.sh', renameScript);
fs.chmodSync('rename_docs.sh', '755');

// 6. Update Metadata
const newMetadata = {
    ...metadata,
    documents: newDocuments,
    organization: {
        method: "sequential-numbering",
        organized_at: new Date().toISOString(),
        total_files: newDocuments.length,
        categories: Object.keys(groupedDocs)
    }
};
fs.writeFileSync('metadata.json', JSON.stringify(newMetadata, null, 2));

// 7. Generate Index
let indexContent = `---
description: Auto-generated documentation index
generated: ${new Date().toISOString()}
source: ${metadata.source_url || 'local'}
total_docs: ${newDocuments.length}
categories: ${Object.keys(groupedDocs).length}
---

# ${path.basename(process.cwd())} Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary
| Property | Value |
|----------|-------|
| **Source** | ${metadata.source_url || 'local'} |
| **Generated** | ${new Date().toISOString()} |
| **Total Documents** | ${newDocuments.length} |
| **Strategy** | Universal Category Detection |

---

## Document Index
`;

// Sort categories for index display based on priority order
const sortedCatNames = Object.keys(groupedDocs).sort((a, b) => {
    const getP = (name) => categories.find(c => c.name === name)?.priority || 99;
    return getP(a) - getP(b);
});

let currentStart = 1;

sortedCatNames.forEach((catName, idx) => {
    const docs = groupedDocs[catName];
    const start = docs[0].num;
    const end = docs[docs.length - 1].num;
    
    indexContent += `
### ${idx + 1}. ${catName} (${start}-${end})

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
`;

    docs.forEach(d => {
        // Truncate summary if too long
        const summary = d.summary.length > 100 ? d.summary.substring(0, 97) + "..." : d.summary;
        indexContent += `| ${d.num} | \`${d.file}\` | ${d.title} | ${summary} | ${d.tags} |\n`;
    });
});

// Generate Learning Path (Simple version based on category priorities)
indexContent += `
---

## Learning Path

### Level 1: Foundation
- Read **Introduction & Overview** documents.
- Complete **Quick Start & Installation** guides.

### Level 2: Core Understanding
- Study **Concepts & Fundamentals**.
- Configure the environment using **Configuration & Settings**.

### Level 3: Practical Application
- Follow **Tutorials & How-To**.
- Explore **Features & Capabilities**.
- Integrate with **Integration & Connection**.

### Level 4: Advanced
- Master **Advanced Topics** and **Automation & Workflow**.
- Review **Operations & Deployment**.

### Level 5: Reference
- Consult **API & Reference** and **Troubleshooting & Support**.
`;

fs.writeFileSync('000-index.md', indexContent);

console.log(`Processed ${newDocuments.length} documents.`);
console.log(`Generated rename_docs.sh`);
console.log(`Updated metadata.json`);
console.log(`Generated 000-index.md`);
