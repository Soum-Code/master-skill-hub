---
name: job-search-copilot
description: End-to-end job search help for tech, AI/ML and data roles. Use for resume or CV tailoring, job description analysis, cover letters, referral and recruiter messages, application tracking, "help me apply to this role", fit-gap analysis, and comparing or negotiating offers. Maps each requirement in a job description to real evidence from the user's background, rewrites bullets with measurable results, and never invents experience, titles, dates or numbers.
license: MIT
metadata:
  repo: Soum-Code/master-skill-hub
  pack: careers-jobs
---

# Job search copilot

The goal is a truthful application that is easy for a recruiter and an ATS to read. Strong evidence beats strong adjectives.

## Ground rules

1. **Never fabricate.** No invented employers, titles, dates, metrics, tools or degrees. If a number is unknown, ask the user or write the bullet without one. If a requirement is a real gap, say so and plan around it (see step 3).
2. **Ask little.** Collect what is missing in one message, at most three questions: the job description, the current resume or a project list, target level and location constraints.
3. **Keep one master record.** Maintain a `master-resume.md` with every project, metric and tool the user can truthfully claim. Each tailored resume is a selection from it, never a new story.
4. **Show your work.** Present the fit table and the changed bullets before producing the final file, so the user can veto claims.

## Workflow

### 1. Decode the job description
Produce a short table: must-have skills, nice-to-have skills, seniority signals (scope, ownership, years), keywords to mirror, and red flags (unclear scope, "rockstar", mismatched stack, unpaid trial work).

### 2. Build the evidence map
For every must-have, find proof in the user's background:

| Requirement | Evidence (project / role / metric) | Strength | Action |
|---|---|---|---|
| e.g. "deploy models to production" | e.g. FastAPI + Docker serving, 120 ms p95 | strong / partial / gap | lead with it / reframe / learn or omit |

### 3. Handle gaps honestly
- **Partial:** describe the closest real work and name the transferable part.
- **Gap, learnable in days:** suggest a small, real project and say so in the plan; never claim it before it exists.
- **Gap, core to the role:** tell the user plainly that this role is a stretch and suggest better-fitting roles.

### 4. Tailor the resume
- One page under about ten years of experience. Single column, standard headings (Experience, Projects, Skills, Education), no tables, text boxes or icons in the body, because ATS parsers misread them.
- Summary: two lines, role + strongest evidence + domain. Skip objectives.
- Bullets use **result, measure, method**: "Cut batch inference cost 41% (AWS bill, 30-day window) by moving to quantized ONNX on CPU instances."
  - Start with a strong verb, past tense for finished work, no pronouns.
  - Include a number, a baseline or a scale whenever it is true.
  - Name the tools the job description names, only where the user used them.
- Put the closest-matching project or role first. Cut what does not help this application.
- For students and career switchers: projects count as experience. Give each: problem, data, approach, result, link. A good README is part of the resume.
- File name: `FirstLast_Role_Company.pdf`.

### 5. Cover letter (only when asked or when the posting wants one)
Under 250 words, three short paragraphs: (1) why this company or problem, specific; (2) the one or two pieces of evidence that match their top needs; (3) a clear, low-pressure close. No "I am writing to apply for". No repeated resume content.

### 6. Outreach and follow-up
- Referral or recruiter message, under 75 words: who you are, why this role, one proof point, an easy ask.
- Follow-up cadence: day 5 to 7 after applying, then day 14. One new piece of value each time.
- Never send anything on the user's behalf without showing the exact text first.

### 7. Track applications
Offer a `applications.csv` with: company, role, link, date applied, stage, contact, next step, follow-up date, notes, status. Update it whenever the user reports news.

### 8. Offers
Compare in a table: base, bonus, equity (vesting, strike or refresh), benefits, growth, team, location rules, notice period. List negotiation levers in order of how often they move (start date, sign-on, level, equity, base) and suggest three questions to ask before accepting. Do not give legal or tax advice; point to a professional for contracts.

## AI / ML specifics
- Recruiters scan for evidence of shipped work: a deployed endpoint, an eval you designed, a dataset you cleaned, a metric you moved. Lead with those.
- Name the stack precisely (PyTorch, scikit-learn, Hugging Face, LangChain, MLflow, Docker, Kubernetes, GitHub Actions, AWS/GCP/Azure) but only what is real.
- A short "Selected projects" section with links beats a long skills list.

## Hand-offs
- Word or PDF output: the `docx` or `pdf` skill.
- Remove machine-sounding phrasing: the `humanizer` skill.
- Profile headline and About section: `linkedin-profile-optimizer`.
- Interview preparation: `ml-interview-prep`.

## Quality checklist before handing over
- Every claim traceable to the master record.
- No unexplained acronyms the posting does not use.
- Dates consistent, no gaps unexplained if the user wants them explained.
- Spelling and tense consistent; one font; no colour needed.
