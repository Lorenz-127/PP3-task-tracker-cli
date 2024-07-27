
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

## Data Model

I implement a refined hybrid data storage solution that separates content and logic, using Google Sheets for task content and local JSON files for application logic and user data.

For a detailed breakdown of our data model, including table structures, ER diagram, and a comprehensive data dictionary, please refer to my [Data Model Documentation](data_model_documentation.md).

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