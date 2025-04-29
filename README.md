### Table of Contents
- [Getting Started](#getting-started)
- [For Production](#for-production)
- [About The Project](#about-the-project)
- [Populate the Project with Dummy Data](#populate-the-project-with-dummy-data)



# Getting Started

### Download Python
https://www.python.org/downloads/

### Virtual Environment
`py -m venv .venv`<br />
`.venv\Scripts\activate.bat`

### Install Requirements
`pip install -r requirements.txt`

### Database Setup (PostgreSQL)
name: **tekst_db**
<br />user: **postgres**
<br />password: **admin**
<br />`python manage.py makemigrations`
<br />`python manage.py migrate`
<br />`python manage.py createsuperuser`

### Create .env file
EMAIL_HOST_USER=<br />
EMAIL_HOST_PASSWORD=<br />
<br />**Note:** If you use a Google account, you need to set up an **App Password** or use **OAuth 2.0**.

### Run project
`python manage.py runserver`

### PyCharm (if you use it)
Configure Inspections: `Ctrl` `Alt` `Shift` `H`<br />
Reformat file: `Ctrl` `Alt` `L`



# For production
The project is ready for deployment on **Azure App Service**. No code changes are necessary - just configure through the Azure portal.

### Django Settings Module Switching
The project automatically switches between development and production settings using the following logic:

```python
settings_module = 'Tekst.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'Tekst.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
```
### Azure Setup Requirements
Set up an **Azure Database for PostgreSQL** to handle your application's data. Once the database is created, copy the full connection string from the Azure portal and store it in the environment variable `AZURE_POSTGRESQL_CONNECTIONSTRING`.

You need to create a **Storage Account** and a **Blob container** for user-uploaded files like images.
<br />
<br />
<br />
**Environment variables you need to create**
- `WEBSITE_SECRET_KEY` - Your Django secret key.
- `WEBSITE_HOSTNAME` - Automatically provided by Azure. Change it if you have your own domain.
- `AZURE_POSTGRESQL_CONNECTIONSTRING` - Full connection string for your PostgreSQL database.
- `AZURE_CONTAINER` - The name of your Blob Storage container.
- `AZURE_ACCOUNT_NAME` - Your Azure Storage account name.
- `AZURE_ACCOUNT_KEY` - Access key for your Azure Storage account.
- `EMAIL_HOST_USER` - Email address used for sending emails.
- `EMAIL_HOST_PASSWORD` - Email password or app-specific password.
- `EMAIL_USE_TLS` - Set to `True` if TLS is required (usually yes).



# About The Project
This platform allows users to create and explore content organized into various "spaces" based on specific topics or interests, such as history, technology, or art. Users can create posts within these spaces, tag them with relevant keywords, and interact with other users through likes, comments, and reactions.

Each space can be followed, verified for authenticity, and customized with a cover image. Posts can be made either within a space, using the space's predefined tags, or independently with custom tags. Additionally, users can attach images to posts to enhance content engagement.

The platform also includes features like user profiles, password management, and notifications for activities such as follows, comments, and likes. Whether users are sharing their own content, connecting with others, or exploring new topics, the platform offers a dynamic and engaging environment for all users.

### Screenshots
![1space1.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F1space1.png)
![2home1.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F2home1.png)
![3home2.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F3home2.png)
![4space2.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F4space2.png)
![5space3.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F5space3.png)
![6post1.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F6post1.png)
![7post2.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F7post2.png)
![8post3.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F8post3.png)
![9post4.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F9post4.png)
![10profile1.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F10profile1.png)
![11profile2.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F11profile2.png)
![12profile3.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F12profile3.png)
![13profile4.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F13profile4.png)
![14profile5.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F14profile5.png)
![15notifications.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F15notifications.png)
![16.png](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fscreenshots%2F16.png)



# Populate the project with Dummy Data
### Database
[BPSM_DB.backup](..%2F..%2FUsers%2FKaloyan%2FDesktop%2FBPSM_DB.backup)

This file should be used to load the database with example users, posts, tags, and other content - perfect for development or testing.

### Images
[Media Folder](..%2F..%2FUsers%2FKaloyan%2FDesktop%2Fmedia)

Make sure to add this folder to the `routing` directory for proper media file handling.
