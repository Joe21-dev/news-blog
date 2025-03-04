
# News Blog Site

This is a simple news-blog application built with **Django**. The app allows users to view, create, edit, and comment on posts. It also includes features for user authentication, 
including login, signup, password recovery, and logout. The application has a simple, basic UI for easy navigation and interaction.

## Features

- **User Authentication**: 
  - **Signup**: New users can register with the system.
  - **Login/Logout**: Users can log in and log out of their accounts.
  - **Password Recovery**: Users can recover their password via a link sent to their email. The link to reset the password is shown in the command line interface (CLI) when requested.

- **Post Management**: 
  - **View Posts**: Users can view posts created by other users.
  - **Create Posts**: Users can create their own posts with a title and content.
  - **Edit Posts**: Users can edit their existing posts.
  - **Delete Posts**: Users can delete their posts.
  
- **Comment System**: 
  - Users can comment on posts, and the comments are displayed below each post.

- **Simple User Interface**: The app provides a clean, easy-to-navigate user interface with all the main features easily accessible.

## Installation

To run the project locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Joe21-dev/news-blog.git
   ```

3. **Navigate to the project directory**:
   ```bash
   cd news-blog
   ```

4. **Install the required dependencies**:
   - Ensure you have Python,Django and pip installed.
   - Install the required Python packages by running:
     ```bash
     pip install -r requirements.txt
     ```

5. **Setup the database**:
   - Run the migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

7. **Run the server**:
   - Start the development server:
     ```bash
     python manage.py runserver
     ```

8. **Access the app**:
   - Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Password Recovery

If you forget your password, follow these steps:

1. Go to the **Login** page and click on **"Forgot Password?"**.
2. Enter your registered email address.
3. Check the command line for a link to reset your password.
4. Click on the link, which will take you to the page to set a new password.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests if you'd like to contribute improvements or fixes to the project.
