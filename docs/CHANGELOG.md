
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Automated testing procedures with pytest
- Manual testing procedures and documentation
- Welcome screen and start function for improved user experience
- Category color coding for better task visualization
- Task status logic with color coding
- Time library integration for enhanced UX with sleep function
- Option to return to main menu in todo selection
- Helper function clear_terminal for better UX
- Comprehensive error handling for all scenarios
- Local caching for categories to improve performance

### Changed
- Refactored TodoCLI initialization with improved error handling
- Enhanced data handling and added serialization methods in Todo class
- Improved CLI messaging and app name consistency
- Adjusted terminal dimensions to 100x30 for better display
- Improved package structure and imports
- Enhanced docstrings across the project
- Optimized Google Sheets queries for improved performance

### Fixed
- Corrected CI Python Linter formatting issues
- Improved error handling for spreadsheet access
- Added missing imports and finalized error handling in CLI

### Documentation
- Created new README for the MVP project
- Added comprehensive content to README including:
  - Project rationale and user stories
  - Planning content
  - Data Model and ER-Diagram
  - Features section
  - Libraries section
  - Deployment instructions
  - Testing procedures (manual and automated)
  - Git version control workflow
  - Credits and acknowledgements
  - Reflection and future improvements
- Created manual testing procedures document
- Added flowcharts and sequence diagrams
- Updated documentation for new MVP structure due to project scope change

## [0.2.0] - 2023-08-10

### Added
- Implemented main CLI loop
- Added category color coding
- Implemented show_statistics functionality
- Added delete_todo functionality
- Implemented complete_todo functionality
- Added update_todo functionality
- Implemented show_todos functionality with rich formatting
- Added add_todo functionality
- Implemented category selection menu
- Added todo selection menu for user interaction
- Implemented display_menu method for CLI interface

### Changed
- Refactored and improved package structure and imports
- Enhanced TodoCLI class with menu items and Google Sheets integration

## [0.1.0] - 2023-07-29

### Added
- Initial project setup
- Basic README structure
- Planning files
- CHANGELOG file
- Core functionality implementation:
  - Google Sheets integration for data storage
  - Basic CRUD operations for todos
- Deployment to Heroku
- Added folder structure and __init__ files
- Implemented GoogleSheets class with various methods for data manipulation
- Added context manager to GoogleSheets class

### Changed
- Updated requirements.txt with necessary dependencies
- Adjusted styling for better user interface

This changelog reflects the development of the Task Tracker CLI application, highlighting the significant features, improvements, and documentation updates made throughout the project's lifecycle.
