# Task Tracker CLI Application

![Task-Tracker-CLI](/resources/task_tracker_cli_show_all.png)

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
09. [**Credits**](#credits)
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

### Flowchart

![Business Logic](/resources/flochart-ttc.drawio.png)

This detailed flowchart provides a comprehensive view of your Todo List CLI application's business logic. Here are some key aspects that align with distinction-level criteria:

1. Detailed Process Flow: The chart shows the step-by-step process for each operation, including user inputs, data validation, and error handling. This demonstrates a thorough understanding of the application's logic (D3).

2. Error Handling: Each major operation includes error checking and appropriate error messages, showing robust error handling (D5).

3. Data Validation: The chart includes validation steps for user inputs, such as checking if a due date is valid or if a category is selected (D5).

4. User Feedback: Success and error messages are displayed after each operation, demonstrating good user interaction design (D4).

5. Complex Operations: The update process is broken down into multiple steps, showing how the application handles more complex operations (D1, D2).

6. Data Consistency: The chart includes a step to update remaining todo positions after deletion, showing attention to data integrity (D7).

7. Integration with Google Sheets: The chart clearly shows how the application interacts with Google Sheets for data persistence, demonstrating the use of external APIs (D6).

## Features

The Task Tracker CLI Application offers a robust set of features designed to enhance productivity and streamline task management. Here's an overview of the key functionalities:

### Core Task Management

1. **Add Tasks**: 
   - Quickly add new tasks with a simple command
   - Automatically assign task IDs for easy reference
   - Set due dates for better time management

2. **View Tasks**: 
   - List all tasks with color-coded categories for easy visualization
   - Sort tasks by various criteria (e.g., due date, category)
   - Display task details including status, due date, and category

3. **Update Tasks**: 
   - Modify task details such as description, due date, and category
   - Mark tasks as complete or reopen completed tasks

4. **Delete Tasks**: 
   - Remove tasks from the list with a simple command
   - Confirmation prompt to prevent accidental deletions

### Advanced Organization

5. **Categorization**: 
   - Assign tasks to custom categories
   - Color-coding for quick visual identification of task categories
   - Filter tasks by category for focused work sessions

6. **Due Date Management**: 
   - Set and modify due dates for tasks
   - Highlight overdue tasks for immediate attention
   - Sort tasks by due date to prioritize work

### User Experience Enhancements

7. **Interactive CLI Interface**: 
   - User-friendly menu system for easy navigation
   - Rich text formatting for improved readability
   - Clear prompts and feedback for all actions

8. **Data Persistence**: 
   - Tasks automatically saved to Google Sheets for multi-device access
   - Local caching for improved performance and offline capabilities

### Productivity Insights

9. **Task Statistics**: 
   - View completion rates and task distribution across categories
   - Track overdue tasks and productivity trends
   - Generate simple reports to analyze work patterns

### Security and Data Integrity

10. **Error Handling**: 
    - Robust error messages for invalid inputs or failed operations
    - Graceful handling of network issues and API errors

11. **Data Validation**: 
    - Input validation to ensure data integrity
    - Prevention of duplicate task entries

### Extensibility and Integration

12. **Google Sheets Integration**: 
    - Seamless synchronization with Google Sheets for data storage
    - Potential for easy sharing and collaboration on tasks

13. **Modular Design**: 
    - Well-structured codebase allowing for easy addition of new features
    - Potential for future integrations with other productivity tools

These features have been carefully designed and implemented to create a powerful, yet user-friendly task management solution. The application aims to provide a streamlined experience for developers and productivity enthusiasts who prefer command-line interfaces, while offering the advanced functionalities typically found in GUI-based task management tools.

## Libraries

Here's a list of the libraries used in my project:

1. **typing**
- Purpose:
    - Provides support for type hints.
- Why chosen:
    - Enhances code readability and helps catch type-related errors early in development.

2. **rich**
- Purpose:
    - Provides rich text and beautiful formatting in the terminal.
- Why chosen:
    - Improves the user interface of the CLI application, making it more visually appealing and easier to read.

3. **simple_term_menu**
- Purpose:
    - Creates simple interactive menus in the terminal.
- Why chosen:
    - Provides an easy way to create interactive menus, improving user experience in the CLI.

4. **datetime**
- Purpose:
    - Supplies classes for working with dates and times.
- Why chosen:
    - Necessary for handling task due dates and completion times.

5. **sys**
- Purpose:
    - Provides access to some variables used or maintained by the Python interpreter.
- Why chosen:
    - Used for graceful exit of the program when encountering critical errors.

6. **gspread**
- Purpose:
    - Python API for Google Sheets.
- Why chosen:
    - Enables interaction with Google Sheets, allowing for cloud-based storage of tasks.

7. **google.auth.exceptions**
- Purpose:
    - Provides exceptions for Google authentication.
- Why chosen:
    - Allows for specific handling of Google authentication errors.

8. **google.oauth2.service_account**
- Purpose:
    - Provides authentication for Google services using a service account.
- Why chosen:
    - Necessary for authenticating with Google Sheets API.

9. **os**
- Purpose:
    - Provides a way of using operating system dependent functionality.
- Why chosen:
    - Used for accessing environment variables, which is a secure way to store sensitive information like API credentials.

10. **dataclasses**
- Purpose:
    - Provides a decorator and functions for automatically adding generated special methods to classes.
- Why chosen:
    - Simplifies the creation of classes that are primarily used to store values, like the Todo class.

11. **pytest**
- Purpose: 
    - Provides a framework for writing and running tests in Python.
- Why chosen:
    - Offers a simple and scalable way to write small to complex functional testing for applications and libraries.
    - Supports both unit testing and integration testing.
    - Provides powerful features like fixtures, parameterization, and plugins that enhance testing capabilities.
    - Allows for clear and concise test code, improving readability and maintainability.
    - Integrates well with other testing tools and CI/CD pipelines.


## Technologies Used


## Version Control

This project utilizes Git for version control and GitHub for remote repository hosting, enabling efficient collaboration and tracking of project history. Our development process is characterized by frequent, well-documented commits and a structured branching strategy.

### Git Workflow

I follow a feature branch workflow, where each new feature or bugfix is developed in a separate branch before being merged into the main development branch. This approach allows for:

- Parallel development of multiple features
- Easier code reviews through pull requests
- Stable main branch that always reflects the production-ready state of the project

### Commit History

Our commit history demonstrates a consistent and organized approach to development:

![Git Commit History](/resources/git-source-control.png)

Key points about my commit history:

1. **Regular Merges**: The image shows a series of merge pull requests, indicating frequent integration of new features and fixes.
2. **Feature Branches**: Each merge comes from a feature branch (e.g., `dev-2`), aligning with my feature branch workflow.
3. **Descriptive Commit Messages**: Commits include clear, descriptive messages such as "feat: add new dependencies to requirements.txt" and "style(cli): adjust table column styles for better readability".
4. **Consistent Naming**: Branch names follow a consistent pattern (`Lorenz-127/dev-2`), facilitating easy tracking and management.

### Conventional Commits

I adhere to the Conventional Commits specification for commit messages. This practice ensures that my project history is readable and that automated tools can parse my commit history. Examples from my commit history include:

- `feat: add new dependencies to requirements.txt`
- `style(cli): adjust table column styles for better readability`
- `feat(cli): add welcome screen and start function`

### Pull Requests

My development process heavily utilizes pull requests for code review and integration. Each significant change is submitted as a pull request, allowing for:

- Code review by team members
- Automated checks and tests
- Discussion and refinement of features before integration

### Continuous Integration

While not explicitly shown in the image, my GitHub workflow likely includes continuous integration processes that run automated tests and checks on each pull request, ensuring code quality and functionality before merging.

This structured approach to version control and collaborative development ensures a high-quality, well-documented codebase that meets industry standards and facilitates efficient teamwork.

## Deployment

The project was developed to be used with the [Code Institute Template](https://github.com/Code-Institute-Org/p3-template) on a mock terminal. It was deployed on Heroku following these steps:

1. Create a Heroku account and **log in**.
2. Click **New** and **Create new app** on the dashboard.
3. Enter a unique **name** and select the region and click **Create app**.
4. Within the created app select the tab **Settings**.
5. At the *Config Vars* section click **Reveal Config Vars**.
6. To use Google Sheets add a new config var with the key *CREDS*, for the value, paste the contents of the creds.json file.
7. Add another config var with the key *PORT* and the value *8000*.
8. Below the *Config Vars* section click **Add buildpack**. Select *Python* and save. Then add another buildpack and select *node.js*. It is important that the buildpacks are shown in this order.
9. Navigate to the **Deploy** tab on top.
10. Select **GitHub** as the deployment method and connect to GitHub.
11. Search for the **repository name** of the project and click **connect**.
12. Optionally **enable automatic deploys** to deploy each time new code is pushed to the repository.
13. Click **Deploy Branch** to deploy the project now.

[Link to my deployed project](https://task-traker-f4de740956e7.herokuapp.com/)

## Testing

### PEP8 Testing

PEP8 testing focuses on ensuring that the codebase adheres to the guidelines outlined in PEP8, the official style guide for Python code. Key aspects of PEP8 testing include:

- **Code Formatting**: Verify that the code follows consistent formatting conventions, including indentation, line length, and spacing.

- **Naming Conventions**: Ensure that variable names, function names, and other identifiers adhere to PEP8 naming conventions to improve code readability and maintainability.

- **Code Structure**: Review the overall structure of the codebase to identify any potential improvements in organization and clarity.

- **Code Linting**: Utilize automated code analysis tools such as Flake8 or Python Indent to identify and correct violations of PEP8 guidelines.

**All Python files** have been validated using the [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to ensure compliance with PEP8 standards. Each file returned the same result: "All clear, no errors found."

examples before:

![before validation](/resources/linter_validation_pytest.png)

and after validation:

![after validation](/resources/linter_validation_pytest_after.png)

### Manual Testing Procedures for Task Tracker CLI

As part of my commitment to ensuring the reliability and functionality of the Task Tracker CLI, I have developed and implemented a comprehensive set of manual testing procedures. My testing suite covers all core features of the application, including adding, viewing, updating, completing, and deleting todos, as well as viewing statistics. For each test case, I've outlined detailed steps to perform the test, specified the expected results, and provided space to record actual outcomes and pass/fail status. This methodical approach allows me to thoroughly validate the application's behavior, identify potential issues, and ensure a smooth user experience. I consider this manual testing process crucial for maintaining the quality and dependability of the Task Tracker CLI. To review my detailed manual testing procedures, please refer to my [manual_tests.md](/docs/manual_tests.md) file.

### Automated Testing Procedures for Task Tracker CLI

To complement my manual testing and further enhance the reliability of the Task Tracker CLI, I've implemented a suite of automated tests using pytest. These tests focus on validating the core functionalities of the application programmatically, ensuring consistent behavior across different scenarios and as the codebase evolves. My test suite covers key operations such as adding, viewing, updating, and deleting todos, as well as more complex interactions within the CLI interface. By mocking external dependencies like the Google Sheets integration, I've isolated the CLI functionality for thorough testing. This automated approach not only helps me catch regressions quickly but also serves as living documentation of the expected behavior of various components. To run these tests or review the test cases, you can refer to the `test_todo_cli.py` file in the project directory. Implementing these automated tests demonstrates my commitment to code quality and my ability to use advanced testing methodologies, aligning with higher-level software development practices.

#### Automated Testing Manual

This project uses pytest for automated testing. To run the tests:

    1. Ensure you have pytest installed:
        - pip install pytest
    2. From the project root directory, run:
        - pytest
    3. To see more detailed output, including print statements, use:
        - pytest -v -s
    4. For a coverage report, first install pytest-cov:
        - pytest --cov=mvp

Example:

![auto-test-cli](/resources/auto_test_cli.png)

## Credits

### Content

- The text on the website is written entirely by me. However, I have used [deepl.com](https://www.deepl.com/translator) for some parts of the translation.
- Some questions were answered with the help of AI. Primarily for faster planning and structural help.

### Inspiration

- [Patrick Loeber's](https://www.youtube.com/watch?v=ynd67UwG_cI&pp=ygUNdG9kbyBsaXN0IGNsaQ%3D%3D) tutorial gave me the basic idea for the app.
- [Corey Schafer](https://www.youtube.com/@coreyms)
Python Tutorial: [Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI&t=668s)
Even though I decided to use the pytest library for my automated tests, the inspiration came from Corey Schafer's tutorial. I gathered the necessary knowledge from the official documentation [pytest documentation](https://docs.pytest.org/en/stable/index.html).


### Acknowledgements

- I would like to thank my mentor Luke Buchanan, for great feedback and advice. [LinkedIn](https://www.linkedin.com/in/lukebuchanan67/)
- Daisy Mc Girr for her expertise in automated testing. [LinkedIn](https://www.linkedin.com/in/daisy-mcgirr-4a3671173/) [GitHub](https://github.com/Dee-McG)
- Tomáš_Kubánčik_Alumni_lead For additional advice on docstrings. [LinkedIn](https://www.linkedin.com/in/tomas-kubancik/) [GitHub](https://github.com/tomik-z-cech)

### Honourable mentions

- IoanZaharia_5p_Lead for his valuable feedback. [LinkedIn](https://www.linkedin.com/in/ioan-zaharia/) [GitHub](https://github.com/zioan)
- Vernell_5p_Lead for his moral support. [LinkedIn](https://www.linkedin.com/in/vernellclark/) [GitHub](https://github.com/VCGithubCode)

## Reflection and Future Improvements

fun
stress
original plan with more features
more auto-test cases
full stack app
mobile app
