
# Data Model Documentation

This data model represents a hybrid approach where task content is stored in Google Sheets for easy sharing and collaboration, while metadata and user information are stored locally in JSON files for improved security and performance.
## Google Sheets Structure

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| task_id     | Integer   | Unique identifier for the task |
| title       | String    | Title of the task |
| content     | String    | Detailed content of the task |
| status      | String    | Current status of the task (e.g., "Not Started", "In Progress", "Completed") |
| category    | String    | Name of the category the task belongs to |
| completion_date | Date  | Date when the task was completed (if applicable) |

## Local JSON Structures

### users.json

```json
{
  "users": [
    {
      "username": "String",
      "password_hash": "String",
      "settings": {
        "theme": "String",
        "language": "String"
      }
    }
  ]
}
```

### tasks_metadata.json

```json
{
  "tasks": [
    {
      "id": "Integer",
      "sheet_row_id": "Integer",
      "priority": "Integer",
      "due_date": "Date",
      "category_id": "Integer"
    }
  ]
}
```

### categories_metadata.json

```json
{
  "categories": [
    {
      "id": "Integer",
      "name": "String",
      "color_code": "String"
    }
  ]
}
```

## ER Diagram

![ER-Diagram](/resources/ER-Diagramm.drawio.png)

## Data Dictionary

| Entity | Attribute | Data Type | Description |
|--------|-----------|-----------|-------------|
| User | username | String | Unique identifier for the user |
| User | password_hash | String | Hashed version of the user's password |
| User | settings | JSON | User-specific settings (theme, language, etc.) |
| Task | id | Integer | Unique identifier for the task (local) |
| Task | sheet_row_id | Integer | Corresponding row ID in Google Sheets |
| Task | title | String | Brief title of the task |
| Task | content | String | Detailed description of the task |
| Task | status | String | Current status of the task |
| Task | priority | Integer | Priority level of the task (e.g., 1-3) |
| Task | due_date | Date | Date when the task is due |
| Task | completion_date | Date | Date when the task was completed |
| Category | id | Integer | Unique identifier for the category |
| Category | name | String | Name of the category |
| Category | color_code | String | Color associated with the category |
