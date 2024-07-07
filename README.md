# Blog Project

This is a Django-based blog application where users can create, read, update, and delete blog posts. It includes functionalities for user authentication and an admin panel for managing posts.

## Features

- List all blog posts with pagination.
- View details of a single blog post.
- Create new blog posts (authenticated users only).
- Update existing blog posts (authors only).
- Delete blog posts (authors only).
- User authentication system (register, login, logout).
- Admin panel for managing blog posts and users.

## Installation

### Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/your-username/blog-project.git
cd blog-project
```
### Install Dependencies
Install Python dependencies using pip (make sure you are in your virtual environment):

```bash
pip install -r requirements.txt
```
### Set Up Django
1. Apply database migrations:
```bash
python manage.py migrate
```
2. Create a superuser for accessing the admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to create a superuser account (username, email, password).

### Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
Access the application at http://localhost:8000/.

## User Authentication
- Register: New users can register by navigating to /register/ and filling out the registration form.
- Login: Registered users can log in at /login/.
- Logout: Users can log out using the Logout link in the navigation bar.

## Authorizing Post Actions
- Create: Authenticated users can create new posts via the New Post link in the navigation bar.
- Update: Users can only update posts they have authored. If a user tries to access the edit page of a post they did not create, they will be redirected to the post detail page.
- Delete: Similar to update, users can only delete posts they have authored.

## Admin Panel
- Access the admin panel at http://localhost:8000/admin/.
- Log in using the superuser credentials created earlier.
- In the admin panel, you can manage blog posts (CRUD operations) and user accounts.
- 
## Folder Structure
- blog/: Django app directory containing models, views, forms, and templates related to the blog functionality.
- templates/blog/: HTML templates for rendering blog pages.
- static/blog/: Static files (CSS) for styling functionality.
