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
![1space1](https://github.com/user-attachments/assets/d3edf825-c30e-4cfe-9b31-1bb1298f6ff1)
![2home1](https://github.com/user-attachments/assets/d13711db-6cf7-4c70-8f5a-f10112a45299)
![3home2](https://github.com/user-attachments/assets/74e1513e-ab61-4f57-ae01-051c096028b5)
![4space2](https://github.com/user-attachments/assets/269977c7-7e83-4219-a60b-9078eb74158f)
![5space3](https://github.com/user-attachments/assets/c9ae21e8-c289-48ff-a07d-c7f1096cc10a)
![6post1](https://github.com/user-attachments/assets/37ea374a-3743-4f54-a461-8df4e7128c47)
![7post2](https://github.com/user-attachments/assets/ed7eac40-f635-4156-9484-e133caeb5478)
![8post3](https://github.com/user-attachments/assets/95993271-b9c5-489e-9b5f-f18c4d1969e2)
![9post4](https://github.com/user-attachments/assets/d58c299e-4885-45cd-9382-2057b55cb118)
![10profile1](https://github.com/user-attachments/assets/c15ccb68-bd40-4f00-8fa5-4d76082282f0)
![11profile2](https://github.com/user-attachments/assets/34c3f7d2-70c0-46ca-8894-dd18a167bec0)
![12profile3](https://github.com/user-attachments/assets/8ce4161c-41e3-4cd8-91bb-41849b042ba1)
![13profile4](https://github.com/user-attachments/assets/5354fa4b-1477-40b7-85f1-b20e02895052)
![14profile5](https://github.com/user-attachments/assets/29707cd5-1572-4ba8-9401-22c626aa96e3)
![15notifications](https://github.com/user-attachments/assets/3a30248b-ece5-4973-8e37-5edbe74f9f0f)
![16](https://github.com/user-attachments/assets/a6c413a8-bb60-4fd8-9ca4-f92142ee3e38)



# Populate the project with Dummy Data
### Database
[BPSM_DB.backup](https://www.dropbox.com/scl/fi/dl0dvgw4plglljj0j2mhh/BPSM_DB.backup?rlkey=dh7ioaoxqoi3lwu063aaihd40&st=n4y5xrhf&dl=0)

This file should be used to load the database with example users, posts, tags, and other content - perfect for development or testing.

### Images
[Media Folder](https://www.dropbox.com/scl/fi/vtu4jp5f7ckojpk28a3ep/media.rar?rlkey=rwqjy2ce7zlap8ceqhcr2zkud&st=149bg2o8&dl=0)

Make sure to add this folder to the `routing` directory for proper media file handling.
