# Data Model Documentation

Back to [README.md](README.md)

This ER diagram is based on the mvp structure Python files, specifically the `Todo` class in `model.py` and the table structures implied by `google_sheets_db.py`. Here's a breakdown of the entities and their relationships:

![ER-diagram-MVP](/resources/ER-diagramm.mvp.png)

1. TODO Entity:
   - Represents a todo item.
   - Fields include:
     - task_id (Primary Key)
     - task (the description of the todo)
     - category (stored as a string, but relates to the CATEGORY entity)
     - date_added
     - due_date
     - date_completed
     - position

2. CATEGORY Entity:
   - Represents categories for organizing todos.
   - Fields include:
     - category_id (Primary Key)
     - category_name

Relationship:
- A TODO belongs to one CATEGORY, and a CATEGORY can have many TODOs (many-to-one relationship).

Keys:
1. Simplified Structure: The current implementation has a relatively simple structure, focusing on the core entities needed for a todo list application.

2. Date Handling: All date fields (date_added, due_date, date_completed) are stored as strings, which allows for flexibility but may require careful handling for date operations.

3. Category Implementation: While categories are stored as strings in the Todo class, there's a separate CATEGORY entity implied by the `get_all_categories()` method in `google_sheets_db.py`.

4. No Explicit User Entity: The current model doesn't include a separate user entity, which suggests the application might be designed for single-user use or that user management is handled externally.

