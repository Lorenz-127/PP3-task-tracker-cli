# Manual Testing Procedures for Task Tracker CLI

## 1. Adding a Todo

### Test Case 1.1
Description: Add a new todo with valid input
Steps:
1. Run the application
2. Select "Add Todo" from the main menu
3. Enter a task description: "Complete project documentation"
4. Select a category from the list
5. Enter a due date in YYYY-MM-DD format
Expected Result: The todo is added successfully, and a confirmation message is displayed

![Screenshot](/resources/Add_todo_valid.gif)

Actual Result:
- Pass
### Test Case 1.2
Description: Add a new todo with invalid date format
Steps:
1. Run the application
2. Select "Add Todo" from the main menu
3. Enter a task description: "Test invalid date"
4. Select a category from the list
5. Enter an invalid due date: "2023/07/15"
Expected Result: An error message is displayed, and the user is prompted to enter the date again

![Screenshot](/resources/add_todo_invalid.gif)

Actual Result:
- Pass

## 2. Viewing Todos

### Test Case 2.1
Description: View all todos
Steps:
1. Run the application
2. Select "Show Todo's" from the main menu
Expected Result: A list of all todos is displayed, including task descriptions, categories, and due dates

![Screenshot](/resources/show_todos.gif)

Actual Result:
- Pass

## 3. Updating a Todo

### Test Case 3.1
Description: Update an existing todo's description
Steps:
1. Run the application
2. Select "Update Todo" from the main menu
3. Choose a todo from the list
4. Enter a new description: "Updated task description"
5. Keep the existing category and due date
Expected Result: The todo's description is updated, and a confirmation message is displayed

![Screenshot](/resources/manual_test_1.png)

Actual Result:
Pass/Fail:

## 4. Completing a Todo

### Test Case 4.1
Description: Mark a todo as complete
Steps:
1. Run the application
2. Select "Complete Todo" from the main menu
3. Choose a todo from the list of incomplete todos
4. Confirm the action
Expected Result: The todo is marked as complete, and a confirmation message is displayed

![Screenshot](/resources/manual_test_1.png)

Actual Result:
Pass/Fail:

## 5. Deleting a Todo

### Test Case 5.1
Description: Delete an existing todo
Steps:
1. Run the application
2. Select "Delete Todo" from the main menu
3. Choose a todo from the list
4. Confirm the deletion
Expected Result: The todo is removed from the list, and a confirmation message is displayed

![Screenshot](/resources/manual_test_1.png)

Actual Result:
Pass/Fail:

## 6. Viewing Statistics

### Test Case 6.1
Description: View todo statistics
Steps:
1. Run the application
2. Select "Show Statistics" from the main menu
Expected Result: Statistics are displayed, including total todos, completed todos, overdue todos, and todos by category

![Screenshot](/resources/manual_test_1.png)

Actual Result:
Pass/Fail: