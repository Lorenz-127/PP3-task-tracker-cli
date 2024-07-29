
# Advanced Todo List CLI Application

## Table of Contents
01. [**Project Overview**](#project-overview)
02. [**Project Rationale**](#project-rationale)
    - [Key Project Goals](#key-project-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
03. [**Planning**](#planning)
    - [Brainstorming](#brainstorming)
    - [Basic Idea](#basic_idea)
    - [First overview](#first_overview)
    - [Refined Project overview](#refined_overview)
    - [Roadmap and Criteria Checklist](#roadmap)(Issues, Tasks, and Milestones)
04. [**Data Model**](#data-model)
05. [**Features**](#features)
06. [**Technologies Used**](#technologies-used)
07. [**Project Structure**](#project-structure)
08. [**Testing**](#testing)
09. [**Deployment**](#deployment)
10. [**Credits and Acknowledgements**](#credits-and-acknowledgements)
11. [**Reflection and Future Improvements**](#reflection-and-future-improvements)

## Project Overview

The Advanced Todo List CLI Application is a command-line interface tool designed to provide a powerful, efficient, and customizable task management solution. This project aims to combine the simplicity of CLI with advanced features typically found in GUI applications, offering a unique tool for productivity enthusiasts and developers.

## Project Rationale

The Advanced Todo List CLI Application is designed to provide a powerful, efficient, and customizable task management solution for users who prefer command-line interfaces. This project aims to combine the simplicity of CLI with advanced features typically found in GUI applications, offering a unique tool for productivity enthusiasts and developers.

### Key Project Goals

1. Develop a fast and responsive CLI todo list application that can handle complex task management efficiently.
2. Implement advanced features such as task prioritization, categorization, and analytics while maintaining a simple command-line interface.
3. Create a flexible data model that allows for future scalability and potential integration with other productivity tools.
4. Demonstrate best practices in Python development, including modular code structure, effective error handling, and comprehensive testing.
5. Provide a secure and privacy-focused solution by keeping all data local and under the user's control.

### Target Audience

The primary target audience for this application includes:

1. Software developers and IT professionals who are comfortable with command-line interfaces and prefer keyboard-driven workflows.
2. Productivity enthusiasts who value speed, efficiency, and customization in their task management tools.
3. Students or professionals in technical fields who need a flexible todo list that can be easily integrated into their existing workflow.

### User Stories

1. Alex - The Software Developer

    - Demographics:
        - Age: 28
        - Occupation: Full-stack developer at a tech startup
        - Location: Urban area, works remotely

    - Background:
        - Experienced in using Git and command-line tools
        - Manages multiple projects simultaneously
        - Values efficiency and automation in daily tasks

    - Motivations and Goals:
        - Wants to streamline task management without leaving the terminal
        - Needs to categorize tasks by project and priority
        - Aims to improve productivity by tracking task completion rates

    - Detailed User Journey:
        Alex starts his day by opening the terminal and running the todo list CLI. He quickly adds new tasks related to his current sprint, categorizing them by project and setting priorities. Throughout the day, he uses quick commands to view, update, and complete tasks. At the end of the week, Alex generates a report to analyze his productivity across different projects.

    - User Benefits:
        - Seamless integration with existing development workflow
        - Quick task entry and management without context switching
        - Ability to track productivity across multiple projects

2. Sarah - The Graduate Student

    - Demographics:
        - Age: 24
        - Occupation: Ph.D. student in Computer Science
        - Location: University campus, splits time between lab and library

    - Background:
        - Familiar with basic command-line operations
        - Juggles research projects, coursework, and teaching assistant duties
        - Prefers minimalist, distraction-free tools

    - Motivations and Goals:
        - Needs a flexible system to manage academic tasks and deadlines
        - Wants to prioritize tasks effectively to balance multiple responsibilities
        - Aims to improve time management and reduce stress

    - Detailed User Journey:
        Sarah begins her week by reviewing and updating her todo list in the terminal. She adds new tasks related to her research, upcoming assignments, and TA duties, setting due dates and priorities. Throughout the week, she uses the CLI to quickly add or modify tasks as new commitments arise. She regularly uses the priority and due date features to focus on the most critical tasks.

    - User Benefits:
        - Distraction-free task management that aligns with her technical background
        - Flexible categorization to separate academic, research, and personal tasks
        - Ability to quickly reprioritize tasks to adapt to changing deadlines

## Planning

1. [Brainstorming](/docs/brainstorming.md)
    - Process of finding the App Idea.
2. [Basic Idea](/docs/basic-idea.md)
    - Brainstorm about the chosen idea
3. [First overview](/docs/first-overview.md)
    - Outline the first high level overview
4. [Refined Project overview](/docs/refined-overview.md)
    - Refine and structure the idea with project needs
5. [Roadmap and Criteria Checklist](/docs/roadmap-checklist.md)
    - Create a Agile "ish" (Issues, Tasks, and Milestones) Roadmap combined with assessment criteria.
6. [Development Approach](/docs/development-approach.md)
    - Outline of my development methodology and practices

### Conventional Commits

As part of my development approach, we use Conventional Commits to standardize my commit messages. This helps in maintaining a clear and structured project history. my commit messages follow this format:

Our commit messages follow this structure:

    <type>[optional scope]: <description>
    [optional body]
    [optional footer(s)]

Example:

    build: add requirements.txt for project dependencies

    - Lists all Python packages required for the project
    - Ensures consistent environment setup across different machines

We use the following types in my commits:

1. feat: A new feature
2. fix: A bug fix
3. docs: Documentation only changes
4. style: Changes that do not affect the meaning of the code
5. refactor: A code change that neither fixes a bug nor adds a feature
6. perf: A code change that improves performance
7. test: Adding missing or correcting existing tests
8. build: Changes affecting the build system or external dependencies
9. ci: Changes to my CI configuration files and scripts
10. chore: Other changes that don't modify src or test files
11. revert: Reverts a previous commit

This approach allows us to:
- Automatically generate changelogs
- Determine semantic version bumps
- Clearly communicate the nature of changes
- Facilitate easier project contributions through a structured commit history

For more details on my development approach, including my use of Conventional Commits, please refer to my [Development Approach](/docs/development-approach.md) document.

## Data Model

I implement a refined hybrid data storage solution that separates content and logic, using Google Sheets for task content and local JSON files for application logic and user data.

Detailed breakdown of the data model:
- Table structures,
- ER-Diagram,
- and a comprehensive data dictionary,

please refer to my [Data Model Documentation](data-model-documentation).

### Google Sheets (Cloud Storage)

- Task content
- Task titles
- Task status
- Category names
- Completion dates

### Local JSON Files

- User authentication data
- Application settings
- Task metadata
- Category metadata

(To be expanded with more details and versions)

## Project Structure

(To be filled with project structure details)

## Testing

(To be filled with testing procedures and results)

## Deployment

(To be filled with deployment instructions)

## Credits and Acknowledgements

(To be filled with credits and acknowledgements)

## Reflection and Future Improvements

(To be filled as the project progresses)