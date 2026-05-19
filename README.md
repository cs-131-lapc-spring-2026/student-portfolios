# CS 131 Student Portfolios – Los Angeles Pierce College Spring 2026

[![Course](https://img.shields.io/badge/Course-CS131-blue)]()
[![Subject](https://img.shields.io/badge/Subject-Discrete%20Mathematics-purple)]()
[![Institution](https://img.shields.io/badge/Institution-LAPC-orange)]()
[![Workflow](https://img.shields.io/badge/Workflow-Fork%20→%20PR-green)]()
[![Submissions](https://img.shields.io/badge/Submissions-Student%20Portfolios-red)]()
[![GitHub](https://img.shields.io/badge/GitHub-Organization-black)](https://github.com)

Welcome to the official repository for CS 131 student portfolio submissions. 
This repository serves as a central portfolio for all students to showcase code, projects, and related work.

## Prerequisites
- Create a GitHub account: <a href="https://github.com/signup" target="_blank">GitHub Sign Up</a>
- Download and install Git Bash: <a href="https://git-scm.com/downloads" target="_blank">Git Bash Download</a> (Optional: Windows using cmd line)
#### GitHub Fork & PR Tutorial
<a href="https://youtu.be/8ifZr4zjkZ8" target="_blank">
  <img src="public/tutorial-preview.png" width="200">
  <p>Click to watch the tutorial video.</p>
</a>

---
## 🧱 Repository Structure
```
📁 first-last-name/
├── 📁 doc/            # citations / sources         
├──📁 presentation/   # links to presentation videos
│   └── 📄 link_to_presentation.txt
├── 📁 src/            # optional source code
└── README.md       # description of their project
```

/students-portfolios/
/first-last-name/
/doc/
/presentation/
/src (optional)/
README.md

- Each student creates a folder with their **first-last name**.  
- Inside your folder, create subfolders as needed (`doc/`, `presentation/`,`src/` etc.).  
- Add a `README.md` inside your folder if you want to describe your portfolio content.  

---

## 🔄 Submission Workflow (Fork + Pull Request)

1. **Fork** this repository to your personal GitHub account.  
2. In your fork, add your portfolio files under `/students-portfolios/your-first-last-name/`.  
3. Commit your changes.  
4. Open a **Pull Request (PR)** from your fork to the main branch of this repository.  
5. Include a descriptive PR title, e.g.:
6. Wait for review and merge.  

> Note: You **cannot push directly** to the main branch. All submissions must be via PR.

---
## 📖 CS 131 GitHub Fork & Portfolio Submission Instructions

> Follow these steps to fork the class repository, create your portfolio folder, and submit a Pull Request (PR) for review.

#### 1: Fork the Repository
- Go to the org repo: [cs-131-lapc-spring-2026/student-portfolios](https://github.com/cs-131-lapc-spring-2026/student-portfolios)
- Click **Fork** at the top-right.
- In the **Create a new fork** menu:
  1. **Owner:** select your personal GitHub account  
  2. **Repository name:** leave as-is (`student-portfolios`)  
  3. Click **Create fork**

#### 2: Clone Your Fork Locally
> Copy the fork to your local machine:
```
$ git clone git@github.com:<your-github-account>/student-portfolios.git
```

#### 3: Verify Your Remote
```
$ git remote -v

You should see:
> origin  git@github.com:(your-github-accout)/student-portfolios.git (fetch)
> origin  git@github.com:(your-github-accout)/student-portfolios.git (push)
```

#### 4: Create Your Student Folder
```
$ mkdir first-last-name 
```
> 📝 replace first-last-name with `your name`. ( e.g joe-shomole )


#### 5:  Create Required Subfolders 📁
```
$ cd first-last-name
$ mkdir doc
$ mkdir presentation
$ mkdir src
```
> ⚠️ Make sure to create a placeholder file in each folder


#### 6: Create a README File
```
$ touch README.md
```

#### 7: Commit and Push Your Changes
```
$ cd ..
$ git add .
$ git commit -m "Add student portfolio folder for Joe Shomole"
$ git push origin main
```
> 📝 commit message --> "Add student portfolio folder for `your name here`"

#### 8: Create a Pull Request (PR)
> Go to your GitHub and select the class repo

  - Click Pull requests → New pull request
  - Ensure: Base repository: `cs-131-lapc-spring-2026:main` <- Head repository: `your-account:main`
  - Title your PR: " Add student portfolio folder for: `your name`. "
  - Description (example):
      This is my initial commit for the CS 131 LAPC Spring semester project.
      Key changes:
        - Created my folder
        - Created subdirectories: doc/, presentation/, src/
        - Added README.md
   - Click `Create pull request` 
> Note: You cannot add yourself as a reviewer. The instructor/admin will review and merge your PR.

---


## Video Guidelines

- Do **not upload large video files** directly to the repo.  
- Upload videos to **YouTube (Unlisted)**, **Google Drive**, or **Vimeo**.  
- Include a `video-links.md` file in your folder with links to your videos.

---

## File Naming & Best Practices

- Use descriptive filenames.  
- Avoid spaces; use `-` or `_` instead, e.g., `project-1.cpp`.  
- Keep your folder organized.  

---

## Support & Questions

- For questions about submissions or repo workflow, contact **your instructor or the repo admin**.  
- Ensure all contributions follow this structure — it keeps the repository clean and professional.

---

Thank you for contributing!  
Let’s build an organized and professional CS 131 portfolio together.  
