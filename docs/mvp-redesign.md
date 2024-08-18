# Updated Project Scope - Task Tracker CLI

Back to [README.md](README.md)

## 1. Core Functionality

- Create, Read, Update, and Delete (CRUD) operations for todo items
- Google Sheets integration for data storage
- Command-line interface (CLI) using simple-term-menu and Rich libraries

## 2. Todo Item Structure

- Task description
- Category
- Due date
- Completion status
- Position (for ordering)

## 3. Features

- Add new todos
- View all todos
- Update existing todos
- Mark todos as complete
- Delete todos
- View basic statistics (total todos, completed todos, overdue todos, todos by category)

## 4. User Interface

- Menu-driven CLI with colored output and formatted tables
- Confirmation prompts for critical actions

## 5. Data Management

- Google Sheets integration for cloud-based storage
- Local caching of categories for improved performance

## 6. Error Handling and Input Validation

- Basic error handling for Google Sheets operations
- Input validation for user inputs (e.g., date formats)

## Changes from Original Scope

1. **Simplified Data Model**: 
   - Removed complex hybrid data approach (Google Sheets + local JSON files)
   - Focused on a single Google Sheets spreadsheet for data storage

2. **Reduced Feature Set**:
   - Removed advanced features like task prioritization and detailed analytics
   - Simplified category management
   - Removed user authentication and multi-user support

3. **Streamlined User Interface**:
   - Implemented a simpler CLI interface instead of a more complex TUI or GUI
   - Focused on essential CRUD operations and basic task management

4. **Cloud Integration**:
   - Maintained Google Sheets integration for cloud storage, aligning with original plan's cloud aspect

5. **Performance Optimizations**:
   - Simplified database queries and operations due to use of Google Sheets
   - Implemented basic caching for categories to improve performance

6. **Testing and Documentation**:
   - Focused on manual testing procedures instead of automated unit tests
   - Simplified documentation requirements to match MVP scope

## Alignment with Project Criteria

### Pass Criteria
- Implements core CRUD functionality
- Uses standard programming constructs
- Integrates with external service (Google Sheets)
- Deploys to a cloud-based platform

### Merit Criteria
- Well-organized code structure
- Implements error handling
- Effectively uses libraries for enhanced CLI experience
- Provides clear documentation and user instructions

### Distinction Potential
- Demonstrates cloud integration
- Includes basic analytics features
- Shows thoughtful code organization and error handling
- Utilizes version control effectively

This MVP approach allows for demonstration of key Python skills and meets core project requirements while accommodating challenging personal circumstances. The project can be further developed to incorporate more advanced features and optimizations as time allows.

[Back to Top](#updated-project-scope---task-tracker-cli)