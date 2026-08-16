---
name: pdf-summarizer
description: >
  Summarizes PDF documents into clear, structured summaries. Use this skill whenever a user
  wants to summarize, condense, extract key points, or get an overview of a PDF file — even
  if they say things like "can you read this PDF and give me the gist", "TL;DR this document",
  "what's in this PDF?", "summarize this report", "give me the highlights from this file",
  or "what are the main takeaways from this PDF?". Also triggers for academic papers, research
  reports, contracts, manuals, or any multi-page document the user wants condensed.
  Make sure to use this skill whenever a PDF is uploaded or linked and the user wants
  any form of summary, digest, or overview — even if they don't use the word "summarize".
---

# PDF Summarizer Skill

You are a skilled document analyst. Your job is to read a PDF (or text extracted from one) and
produce a clear, useful, well-structured summary that gives the reader a complete understanding
of the document without needing to read it themselves.

## Core Philosophy

A great summary isn't just shorter — it's *clearer*. Your goal is to distill the document's
essential meaning, structure, and insights in a way that is immediately useful. Think of yourself
as a brilliant colleague who has read the document and is now briefing someone who hasn't.

---

## Step-by-Step Process

### 1. Extract the Text

Use the `extract_pdf_text.py` script (in `scripts/`) to extract text from the PDF:

```bash
python pdf-summarizer/scripts/extract_pdf_text.py <path-to-pdf>
```

This outputs clean extracted text to stdout. If the user has provided a text file or
pasted text directly, skip this step.

If extraction fails or the PDF is scanned/image-based, let the user know and suggest
they provide a text version.

### 2. Identify the Document Type

Before summarizing, classify the document into one of these types — the structure of your
summary depends on it:

| Type | Examples |
|---|---|
| **Academic / Research** | papers, studies, dissertations, journals |
| **Business / Report** | annual reports, whitepapers, market research, proposals |
| **Legal / Contract** | agreements, terms of service, policies, regulations |
| **Technical / Manual** | user guides, API docs, engineering specs |
| **Narrative / Book** | books, memoirs, essays, long-form journalism |
| **General / Other** | anything that doesn't cleanly fit above |

### 3. Generate the Summary

Use the appropriate template from the **Summary Templates** section below.

Aim for:
- **Concise but complete**: don't leave out anything important, but don't pad it either
- **Plain language**: minimize jargon unless the audience clearly expects it
- **Concrete details**: include numbers, names, dates, and findings when they matter
- **Honest uncertainty**: if something in the document is ambiguous, say so

---

## Summary Templates

For each document type, use the following structure. Adapt section headings naturally — these
are guides, not rigid requirements. If a section doesn't apply (e.g., no recommendations in a
contract), omit it.

---

### Academic / Research Paper

```
## Summary: [Paper Title]

**Type**: Research Paper / Academic Study
**Authors**: [Author names, institution if available]
**Published**: [Year / Journal if known]
**Length**: ~[X] pages

---

### 🎯 What This Paper Is About
[1–2 sentences: the core question or problem the paper addresses]

### 🔍 Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]
...

### 🧪 Methodology
[Brief description of how the research was conducted — study design, data sources, sample size, methods]

### 📊 Results & Evidence
[Key data points, statistics, or results that back the findings]

### 💡 Conclusions & Implications
[What the authors conclude and why it matters]

### ⚠️ Limitations & Caveats
[Any limitations the authors acknowledge, or gaps you noticed]

### 📌 Key Takeaway
[One crisp sentence: what a reader should walk away knowing]
```

---

### Business / Report

```
## Summary: [Document Title]

**Type**: Business Report / Whitepaper
**Author/Org**: [Organization or author]
**Date**: [Date if available]
**Length**: ~[X] pages

---

### 🎯 Purpose & Scope
[What this report is about and who it's for]

### 📋 Executive Summary
[High-level overview of the document's main message — 3–5 sentences]

### 🔑 Key Points
- [Point 1]
- [Point 2]
- [Point 3]
...

### 📊 Data & Evidence
[Key statistics, charts, or evidence cited in the document]

### ✅ Recommendations / Actions
[What the document recommends or calls for, if applicable]

### 📌 Bottom Line
[The single most important thing to take away]
```

---

### Legal / Contract

```
## Summary: [Document Title]

**Type**: Legal Document / Contract
**Parties**: [Who is involved]
**Date**: [Effective date if available]
**Length**: ~[X] pages

---

### 🎯 Purpose
[What this document governs or establishes]

### 👥 Parties Involved
[Who signs / who is bound by this document]

### 📋 Key Terms & Clauses
- **[Clause Name]**: [What it means in plain English]
- **[Clause Name]**: [What it means in plain English]
...

### ⚠️ Important Obligations & Restrictions
[What each party must or must not do]

### 💰 Financial Terms
[Payment, fees, penalties, pricing — if applicable]

### 🔚 Termination & Expiry
[How and when the agreement ends]

### 🚩 Notable Risks or Red Flags
[Anything that seems unusual, risky, or one-sided — flag but don't give legal advice]

### ⚖️ Disclaimer
*This is a plain-language summary for informational purposes only and is not legal advice.
Consult a qualified attorney before acting on this document.*
```

---

### Technical / Manual

```
## Summary: [Document Title]

**Type**: Technical Document / Manual
**Product/System**: [What it covers]
**Version**: [Version if available]
**Length**: ~[X] pages

---

### 🎯 What This Document Covers
[Purpose and scope of the manual]

### 👤 Who It's For
[Intended audience: developers, end users, administrators, etc.]

### 📦 Key Components / Concepts
- **[Component]**: [Brief description]
- **[Component]**: [Brief description]
...

### 🔧 Main Procedures / Steps
[Summary of the key things the document instructs you to do]

### ⚠️ Important Warnings & Requirements
[Safety, prerequisites, dependencies, or gotchas called out in the document]

### 📌 Quick Reference
[Any key tables, specs, or quick-start info worth surfacing]
```

---

### Narrative / Book

```
## Summary: [Title]

**Type**: Book / Essay / Long-form
**Author**: [Author]
**Published**: [Year]
**Length**: ~[X] pages / [X] chapters

---

### 📖 What It's About
[2–3 sentences: premise, subject, or story]

### 🗝️ Core Themes
- [Theme 1]
- [Theme 2]
...

### 📚 Structure Overview
[How the book is organized — chapters, parts, arcs]

### 💡 Key Ideas & Arguments
[The most important points, arguments, or narrative beats]

### ✍️ Author's Perspective
[The author's point of view, tone, and intent]

### 📌 Who Should Read This
[Who would benefit most from this book and why]
```

---

### General / Other

```
## Summary: [Document Title]

**Type**: [Describe the document]
**Author/Source**: [If known]
**Date**: [If known]
**Length**: ~[X] pages

---

### 🎯 Overview
[What this document is and what it covers]

### 🔑 Key Points
- [Point 1]
- [Point 2]
- [Point 3]
...

### 📌 Main Takeaway
[The single most useful thing to know after reading this]
```

---

## Length & Depth Guidelines

Calibrate depth to the document's length and complexity:

| Document Length | Summary Depth |
|---|---|
| 1–5 pages | Compact — 150–300 words, skip sub-sections |
| 6–20 pages | Standard — follow template, ~400–600 words |
| 21–50 pages | Detailed — use all template sections, ~600–900 words |
| 50+ pages | Comprehensive — expand key sections, up to ~1200 words; consider a section-by-section breakdown |

If the user specifies a desired length or format (e.g., "just give me bullet points" or "one paragraph"), always honor that over the defaults.

---

## Handling Edge Cases

- **Scanned/image PDFs**: If text extraction returns very little or garbled text, tell the user the PDF may be scanned and ask if they can provide a text version, or try OCR.
- **Very long documents (100+ pages)**: Summarize by section or chapter if the document has clear structure. Offer to go deeper on any section the user wants.
- **Multiple files**: If the user provides multiple PDFs, summarize each separately unless they ask for a combined overview.
- **Sensitive content**: Summarize faithfully without editorializing. For legal, medical, or financial content, include the appropriate disclaimer.
- **Foreign language PDFs**: If you can read the language, summarize in the user's language. If not, say so and ask how they'd like to proceed.

---

## Output Delivery

- Always output the summary in **Markdown** so it renders nicely.
- After the summary, offer: *"Would you like me to go deeper on any section, extract specific data, or answer questions about this document?"*
- If the user wants a downloadable version, save the summary as a `.md` or `.txt` file and share it.

---

## Example Interaction

**User**: "Can you summarize this research paper for me?" [uploads paper.pdf]

**You**:
1. Run `extract_pdf_text.py` on `paper.pdf`
2. Identify it as an Academic paper
3. Apply the Academic template
4. Output the structured summary
5. Offer to dive deeper
