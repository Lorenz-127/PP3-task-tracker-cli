# Development Approach

## Table of Contents
1. [Introduction](#introduction)
2. [Modular Approach](#modular-approach)
3. [Version Control](#version-control)
4. [Data Structure](#data-structure)
5. [Feature Planning](#feature-planning)
6. [Implementation Plan](#implementation-plan)
7. [Testing Strategy](#testing-strategy)
8. [Documentation](#documentation)
9. [Deployment](#deployment)
10. [Project Management](#project-management)

## Introduction
This document outlines my development approach for the Advanced Todo List CLI Application. my methodology is designed to meet all assessment criteria systematically, demonstrating clear progression in coding skills from pass to merit to distinction levels.

## Modular Approach
I take a modular approach to development, building from pass to merit to distinction. This approach allows for:
- Incremental development
- Clear demonstration of learning
- Manageable complexity
- Alignment with version control practices
- Effective risk management

For a detailed breakdown of my development stages, please refer to my [Roadmap and Criteria Checklist](/docs/roadmap-checklist.md).

## Version Control
I use Git for version control, with a focus on clear, descriptive commit messages following the Conventional Commits specification.

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
Types used include:
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

## Data Structure
I implement a refined hybrid data storage solution, as detailed in my [Data Model Documentation](/docs/data-model-documentation.md):

### Google Sheets (Cloud Storage)
- Task content (title, content, status, category, completion date)

### Local JSON Files
- User data (username, password hash, settings)
- Task metadata (id, sheet row id, priority, due date, category id)
- Category metadata (id, name, color code)

For a detailed Entity-Relationship diagram and data dictionary, please refer to the Data Model Documentation.

## Feature Planning
my feature planning is divided into three phases, aligned with pass, merit, and distinction criteria. For a comprehensive list of features, please see my [Refined Project Overview](/docs/refined-overview.md).

1. Pass Level Features
2. Merit Level Features
3. Distinction Level Features

## Implementation Plan
my implementation plan follows the same three-phase structure as my feature planning. Detailed implementation steps can be found in the [Refined Project Overview](/docs/refined-overview.md) and the [Roadmap and Criteria Checklist](/docs/roadmap-checklist.md).

1. Pass Level Implementation
2. Merit Level Implementation
3. Distinction Level Implementation

### Basic file structure

<details>
<summary>Initial File Structure</summary>

<img src="https://github.com/Lorenz-127/PP3-task-tracker-cli/blob/main/resources/initial_file_structure.png">

</details>

- Explanation of the structure:

1. `src/`: This directory contains all the source code for your application.
   - `main.py`: The entry point of your application.
   - `database/`: Handles all database operations.
   - `cli/`: Contains code for the command-line interface.
   - `tasks/`: Manages task-related operations.
   - `utils/`: Houses utility functions and error handling.
   - `config.py`: Stores configuration variables.

2. `tests/`: Contains all your test files, organized to mirror the `src/` structure.

3. `docs/`: Holds project documentation.

4. `resources/`: Stores any additional resources, like SQL schemas.

5. `requirements.txt`: Lists all Python dependencies.

6. `setup.py`: For packaging your project.

7. `run.py`: A simple script to run your application.

## Testing Strategy
my testing strategy evolves through the development phases:
- Implement basic manual testing procedures for code validation (Pass level)
- Enhance and document comprehensive manual testing procedures (Merit level)
- Implement unit tests for critical functions and consider integration tests (Distinction level)

Detailed testing procedures will be documented in a separate testing document.

## Documentation
my documentation process includes:
- Writing initial README.md with project description and basic usage instructions (Pass level)
- Enhancing README with project rationale, detailed user instructions, and flow charts/diagrams (Merit level)
- Creating comprehensive API documentation, detailed setup guide, and usage examples (Distinction level)

my documentation approach is reflected in my [README.md](/docs/refined-overview.md) structure and content.

## Deployment
my deployment strategy progresses through the development phases:
- Deploy basic application to a cloud-based platform (Pass level)
- Document detailed deployment procedure in README (Merit level)
- Ensure deployed application is optimized for performance and execute a flawless deployment with additional optimizations (Distinction level)

## Project Management
We use GitHub Issues and Projects for task tracking and project management. my approach includes:
- Creating and managing issues for features, bugs, and tasks
- Organizing work into milestones aligned with my development phases
- Using project boards to visualize workflow and track progress

This development approach is designed to ensure we meet all criteria levels systematically, demonstrating clear progression in coding skills, project management, and attention to user needs. We'll use Conventional Commits throughout the development process to maintain clear version control and project history.

For a visual representation of my application's structure and logic, please refer to my [flowcharts](/docs/flowcharts.md).