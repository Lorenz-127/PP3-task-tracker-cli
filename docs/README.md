# Task Tracker CLI Application

## Table of Contents

01. [**Project Rationale**](#project-rationale)
    - [Key Project Goals](#key-project-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
02. [**Planning**](#planning)
03. [**Data Model**](#data-model)
04. [**Features**](#features)
05. [**Technologies Used**](#technologies-used)
06. [**Project Structure**](#project-structure)
07. [**Testing**](#testing)
08. [**Deployment**](#deployment)
09. [**Credits and Acknowledgements**](#credits-and-acknowledgements)
10. [**Reflection and Future Improvements**](#reflection-and-future-improvements)

## Project Rationale

The Task Tracker CLI Application is a command-line interface tool designed to provide a powerful, efficient task management solution. This project aims to combine the simplicity of CLI with advanced features typically found in GUI applications, offering a unique tool for productivity enthusiasts and developers.

### Key Project Goals

1. Develop a fast and responsive CLI todo list application that can handle complex task management efficiently.
2. Implement advanced features such as categorization analytics, and task prioritization(future feature) while maintaining a simple command-line interface.
3. Create a flexible data model that allows for future scalability and potential integration with other productivity tools.

### Target Audience

The primary target audience for this application includes:

1. Software developers and IT professionals who are comfortable with command-line interfaces and prefer keyboard-driven workflows.
2. Productivity enthusiasts who value speed, efficiency, and customization in their task management tools.
3. Students or professionals in technical fields who need a flexible todo list that can be easily integrated into their existing workflow.

### User Stories

1. Alex - The Software Developer

    - Demographics:
        - Age: 35
        - Occupation: Full-stack developer at a tech startup
        - Location: Urban area, works remotely

    - Background:
        - Experienced in using Git and command-line tools
        - Manages multiple projects simultaneously
        - Values efficiency and automation in daily tasks

    - Motivations and Goals:
        - Wants to streamline task management without leaving the terminal
        - Needs to categorize tasks by project and priority(future feature)
        - Aims to improve productivity by tracking task completion rates

    - Detailed User Journey:
        Alex starts his day by opening the terminal and running the todo list CLI. He quickly adds new tasks related to his current sprint, categorizing them by project and setting priorities(future feature). Throughout the day, he uses quick commands to view, update, and complete tasks. At the end of the week, Alex generates a report to analyze his productivity across different projects.

    - User Benefits:
        - Seamless integration with existing development workflow
        - Quick task entry and management without context switching
        - Ability to track productivity across multiple projects

2. Sarah - The Graduate Student

    - Demographics:
        - Age: 24
        - Occupation: Fulltime student at Code Institute 
        - Location: University campus, splits time between lab and library

    - Background:
        - Familiar with basic command-line operations
        - Juggles research projects, coursework, and teaching assistant duties
        - Prefers minimalist, distraction-free tools

    - Motivations and Goals:
        - Needs a flexible system to manage academic tasks and deadlines
        - Wants to prioritize tasks effectively(future feature) to balance multiple responsibilities
        - Aims to improve time management and reduce stress

    - Detailed User Journey:
        Sarah begins her week by reviewing and updating her todo list in the terminal. She adds new tasks related to her research, upcoming assignments, and TA duties, setting due dates and priorities(future feature). Throughout the week, she uses the CLI to quickly add or modify tasks as new commitments arise. She regularly uses the priority(future feature) and due date features to focus on the most critical tasks.

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
7. [Refactoring the Project Scope](/docs/mvp-redesign.md)
    - Due to the sudden death of my father, I had to look after the family in Switzerland. I was therefore unable to build the app as originally planned. I'm building a smaller MVP version of the original approach, but still with best practices.
    
### Conventional Commits

As part of my development approach, I use Conventional Commits to standardize my commit messages. This helps in maintaining a clear and structured project history. My commit messages follow this format:

Our commit messages follow this structure:

    <type>[optional scope]: <description>
    [optional body]
    [optional footer(s)]

Example:

    build: Add requirements.txt for project dependencies

    - Lists all Python packages required for the project
    - Ensures consistent environment setup across different machines

I use the following types in my commits:

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
- Automatically generate changelogs (if implemented)
- Determine semantic version bumps
- Clearly communicate the nature of changes
- Facilitate easier project contributions through a structured commit history

For more details on my development approach, including my use of Conventional Commits, please refer to my [Development Approach](/docs/development-approach.md) document.

## Data Model

I implement cloud data storage solution to keep it simple and multi device accessible, using Google Sheets for task content and data.

Detailed breakdown of the data model:
- Table structures,
- ER-Diagram,
- and a comprehensive data dictionary,

please refer to my [New Data Model Documentation](/docs/data-model-documentation-mvp.md).

### ER-Diagram

This ER diagram is based on the mvp structure Python files, specifically the `Todo` class in `model.py` and the table structures implied by `google_sheets_db.py`.

![ER-Diagram](/resources/ER-diagramm.mvp.png)

### Sequence Diagram

Example for: Add New Todo

This sequence diagram illustrates the process of adding a new todo item in the Task Tracker CLI application. Here's a breakdown of the interactions:

![Sequence Diagram](/resources/sequence_diagram_add-todo.drawio.png)

1. The User initiates the process by selecting "Add Todo" from the CLI menu.
2. The TodoCLI prompts the user for task details.
3. The User enters the task details.
4. The CLI creates a new Todo object using the provided details.
5. The Todo model returns the created object to the CLI.
6. The CLI calls the insert_todo method of TodoGoogleSheets to save the new todo.
7. TodoGoogleSheets performs several internal operations:
    - Gets the next available task ID
    - Gets the category ID for the provided category
    - Gets the next available position for the todo item
8. TodoGoogleSheets appends a new row to the Google Sheets document with the todo data.
9. Google Sheets confirms the operation.
10. TodoGoogleSheets relays the confirmation to the CLI.
11. The CLI displays a success message to the User.

This sequence diagram helps to visualize the flow of data and control between different components of the application. It demonstrates:

1. The separation of concerns between the CLI interface, data storage, and data model.
2. The interaction with external services (Google Sheets).
3. The steps involved in creating and persisting a new todo item.


## Deployment

## Credits and Acknowledgements

## Reflection and Future Improvements
