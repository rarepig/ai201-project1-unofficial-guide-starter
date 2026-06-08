# The Unofficial Guide — Project 1

---

## Domain   

This system covers student experiences with WGU Computer Science courses, including
difficulty ratings, time estimates, study tips, and passing strategies shared on
r/WGU_CompSci. This knowledge is valuable because WGU's self-paced model means
completion time and difficulty vary widely between students, and official course
descriptions provide no insight into what actually helps students pass. The real
guidance lives in student posts — scattered across Reddit threads that are hard to
search systematically.

---

## Document Sources

| # | Source | Title | Type | URL or file path |
|---|--------|------|------|-----------------|
| 1 |r/WGU_CompSci |BSCS completed in 3 terms | Reddit |https://www.reddit.com/r/WGU_CompSci/comments/1j1lea2/finished_in_3_terms15_months_and_job_offer_before/|
| 2 |r/WGU_CompSci |C950 Data Structures & Algorithms II - passed post  | Reddit |https://www.reddit.com/r/WGU_CompSci/comments/1bdf53t/c950_data_structures_and_algorithms_ii_finished/ |
| 3 |r/WGU_CompSci |D427 passed - tips and experience  | Reddit |https://www.reddit.com/r/WGU_CompSci/comments/1qv9i0u/just_passed_d427_my_thoughts/ |
| 4 |r/WGU_CompSci |First WGU course passed - Practical Applications  | Reddit |https://www.reddit.com/r/WGU_CompSci/comments/1imkzu5/passed_my_first_wgu_course_practical_applications/ |
| 5 |r/WGU_CompSci |C952 passed - difficulty and study tips  | Reddit | https://www.reddit.com/r/WGU_CompSci/comments/1s9ewy3/i_defeated_the_beast_c952/|
| 6 |r/WGU_CompSci |D281 Linux Foundation passed with perfect score | Reddit  | https://www.reddit.com/r/WGU_CompSci/comments/1hp0jas/passed_d281_linux_foundation_with_a_perfect_score/|
| 7 |r/WGU_CompSci |D683 tips and discussion | Reddit  | https://www.reddit.com/r/WGU_CompSci/comments/1k4nutg/d683/|
| 8 |r/WGU_CompSci |D682 AI Optimization Task 1 guide | Reddit  | https://www.reddit.com/r/WGU_CompSci/comments/1mcwbq3/wgu_d682_guide_task_1_ai_optimization/|
| 9 |r/WGU_CompSci |D480 Software Design & QA passed  | Reddit | https://www.reddit.com/r/WGU_CompSci/comments/16c60nh/software_design_and_quality_assurance_d480_passed/|
| 10 |r/WGU_CompSci |D284 Software Engineering review and tips  | Reddit | https://www.reddit.com/r/WGU_CompSci/comments/1lfqoc3/d284_software_engineering_might_legitimately_make/|

---

## Chunking Strategy

**Chunk size:** 500 characters

**Overlap:** 50 characters

**Why these choices fit your documents:**
Reddit posts and comments are short and focused — each comment typically covers
one topic (a time estimate, a study tip, or a difficulty rating). A 500-character
chunk captures one complete thought without merging unrelated topics. A 50-character
overlap prevents key information from being cut off at chunk boundaries, such as a
sentence that begins near the end of one chunk and continues into the next.
Before chunking, documents were cleaned to remove common Reddit noise such as
upvote/downvote buttons, award text, promotional content, and short filler lines
under 3 characters.

**Final chunk count:** 181 chunks across 10 documents

---

## Embedding Model

**Model used:** all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:**
For a production deployment, I would consider the following tradeoffs:

- **Accuracy:** all-MiniLM-L6-v2 is lightweight but may miss nuanced meaning in
  technical queries. A larger model like text-embedding-3-large (OpenAI) would
  retrieve more relevant chunks for course-specific questions.
- **Context length:** all-MiniLM-L6-v2 has a 256-token limit per chunk. For longer
  documents like full course guides or syllabi, a model with a larger context window
  would be more appropriate.

---

## Grounded Generation

**System prompt grounding instruction:**
The following system prompt was used to enforce grounding:

"You are a helpful assistant that answers questions about WGU Computer Science courses.
Answer using ONLY the information provided in the context below.
Even if the information is partial or mentioned briefly, use it to form an answer.
If the context contains ANY relevant information, use it to answer.
Only say 'I don't have enough information on that.' if the context has absolutely
nothing relevant. Always cite which document(s) your answer comes from using the
source names provided."

The retrieved chunks are passed directly into the user message as labeled context
blocks in the format [Source: filename.txt] followed by the chunk text. This
structure makes it explicit to the model which text comes from which document.

**How source attribution is surfaced in the response:**
Source filenames are extracted from the retrieved chunks and returned as a separate
field alongside the answer. The Gradio interface displays them in a dedicated
"Sources" text box below the answer, so the user always sees which documents
the response drew from.

---
## Sample Chunks

The following are 5 representative chunks produced by the ingestion pipeline.

**Chunk 1** — `subreddit1.txt`
FINISHED in 3 terms/15 months and job offer before graduation: course and job stats
Hi all! Finally finished my degree a few weeks ago and wanted to make a follow up post.
This is a write up summarizing descriptive stats on how long each class took to complete
as well as my difficulty rating. I've included data for all 3 terms, stats on job
applications, and the final job offer.

**Chunk 2** — `subreddit1.txt`
COURSE / TITLE  TOTAL STUDY TIME (hrs)  DIFFICULTY (out of 5)
D322 - Introduction to IT       9       1
D315 - Network and Security- Foundations        11.5    2
C958 - Calculus I       95.15   4
C867 - Scripting and Programming - Applications 29.5    3
D288 - Back-end Programming     26      4
D387 - Advanced Java    20.9    3

**Chunk 3** — `subreddit1.txt`
dealing with untreated depression and experienced a long term relationship break up
and was unemployed for half of term 2 and all of term 3 (6 months total).
Otherwise, I did not get any internship experience during this time.
The only experience I had on my resume were a few of the WGU projects.

**Chunk 4** — `subreddit1.txt`
Computer Architecture   43.75   4
Linux Foundations       37.5    2
Operating Systems for Programmers       60.45   4
Data Structures and Algorithms I        27      2
Discrete Math II        71      3
Data Structures and Algorithms II       65.5    4

**Chunk 5** — `subreddit1.txt`
D286 - Java Fundamentals        18.25   2
D287 - Java Frameworks  23.5    3
D288 - Back-end Programming     26      4
D387 - Advanced Java    20.9    3
Software Engineering    20.75   2
---
## Retrieval Test Results

### Query 1: "How long does C950 typically take to complete?"
**Top returned chunks:**
- `subreddit2.txt` (distance: 0.543) — "C950 - Data Structures and Algorithms II finished in 6 days with no python experience. This is my first post here but I've been lurking for the past couple years..."
- `subreddit1.txt` (distance: 0.570) — "stats on how long each class took to complete as well as my difficulty rating. I've included data for all 3 terms..."
- `subreddit9.txt` (distance: 0.623) — "I dove into Task 1. I'm estimating it took me 4 hours or so..."

**Why top chunks are relevant:** subreddit2.txt directly discusses C950 completion time. subreddit1.txt contains a course-by-course time breakdown table.

---

### Query 2: "What resources do students recommend for passing C952?"
**Top returned chunks:**
- `subreddit5.txt` (distance: 0.434) — "I used the Quizlets and watched the webinar series, along with listening to NotebookLM-generated podcasts. The chapter 4 labs are good, though."
- `subreddit1.txt` (distance: 0.556) — course difficulty ratings table including C952-related content

**Why top chunks are relevant:** subreddit5.txt is the C952 post and directly lists study resources used by the student.

---

### Query 3: "What study approach do students recommend for D427?"
**Top returned chunks:**
- `subreddit3.txt` (distance: 0.374) — "I just passed the OA for D427 Data Management - Applications. Once you finish ALL of the ZyBooks labs, install MySQL and start practicing in Workbench."
- `subreddit4.txt` (distance: 0.413) — related course tips and study strategies

**Why top chunks are relevant:** subreddit3.txt is the D427 post and directly answers the query with specific study advice. Distance score of 0.374 indicates strong semantic match.

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | How long does C950 typically take to complete? | About 20–30 hours; Task 1 (planning) and Task 2 (Python implementation) | One student finished in 6 days; another source suggested ~5 hours; completion time varies | Partially relevant | Partially accurate |
| 2 | What resources do students recommend for passing C952? | Quizlets, webinar series, NotebookLM podcasts, Zybook Chapter 4 labs | Correctly identified Quizlets, webinar series, NotebookLM podcasts, and Zybook Chapter 4 labs | Relevant | Accurate |
| 3 | What study approach do students recommend for D427? | Complete ZyBooks labs, practice in MySQL Workbench, ~15 hours | Mixed D427 tips with other course advice; mentioned ChatGPT and course objectives | Partially relevant | Partially accurate |
| 4 | Which courses in BSCS are considered the most difficult? | C958 Calculus I, Computer Architecture, Operating Systems, DSA II | Incorrectly listed Organic Chem and Genetics (not WGU CS courses) as most difficult | Off-target | Inaccurate |
| 5 | What challenges do students face when completing D284? | Ambiguous requirements and inconsistent feedback between instructors and evaluators | Correctly identified lack of guidance and inconsistency between instructors and evaluators | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:**
Which courses in BSCS are considered the most difficult?

**What the system returned:**
The system listed Organic Chemistry I and II and Genetics as the most difficult
courses, rating them 5/5 difficulty. These are not WGU CS courses — they were
mentioned by the post author as a personal comparison to their biology background.

**Root cause (tied to a specific pipeline stage):**
The failure occurred at two pipeline stages. First, during chunking, the passage
where the author compares WGU difficulty to Organic Chem was not separated from
the actual course difficulty data — both ended up in the same or adjacent chunks.
Second, during retrieval, the embedding model matched the query "most difficult
courses" to chunks containing difficulty comparisons, without distinguishing between
WGU courses and external references. The LLM then treated all mentioned courses as
WGU CS courses.

**What you would change to fix it:**
Adding metadata tags identifying each chunk's course code (e.g., C958, D288) during
ingestion would allow the retrieval stage to filter results to actual WGU course
codes. Alternatively, a larger chunk size might have included enough surrounding
context for the LLM to recognize the Organic Chem reference as a comparison, not
a WGU course.

---

## Spec Reflection

**One way the spec helped you during implementation:**
The Chunking Strategy section of planning.md directly guided the implementation of
chunk_text(). Having already decided on 500-character chunks with 50-character overlap
before writing any code meant I could give Claude a precise spec and get working code
on the first attempt. Without the spec, I would have had to make these decisions
mid-implementation, which would have slowed down debugging.

**One way your implementation diverged from the spec, and why:**
The spec assumed documents would be clean enough that basic cleaning (removing ad
keywords and short lines) would be sufficient. In practice, Reddit posts contained
more noise than expected — usernames, vote counts, comment metadata, and promotional
content were mixed throughout the text. The cleaning function had to be revised after
seeing actual retrieval results return ad text and comment artifacts instead of
course-relevant content.

---

## AI Usage

**Instance 1**

- *What I gave the AI:* The Chunking Strategy and Documents sections of planning.md,
  along with the list of .txt file paths in the documents/ folder.
- *What it produced:* A complete ingest.py with load_documents(), clean_text(), and
  chunk_text() functions using 500-character fixed-size splitting with 50-character overlap.
- *What I changed or overrode:* The initial clean_text() function only used regex
  patterns to remove ad text. After seeing retrieval results return Reddit usernames
  and vote count lines, I revised the function to also filter lines containing
  keywords like "upvote", "downvote", "reply", and lines under 3 characters.

**Instance 2**

- *What I gave the AI:* The Retrieval Approach section of planning.md and the
  grounding requirement (answer only from retrieved context, include source attribution).
- *What it produced:* store.py with embed_and_store() and retrieve() functions using
  ChromaDB, and query.py with a Groq API call and system prompt enforcing grounding.
- *What I changed or overrode:* The initial system prompt was too strict — it caused
  the model to return "I don't have enough information" even when relevant chunks were
  retrieved. I revised the prompt to instruct the model to use any partial information
  available in the context before declining to answer.
