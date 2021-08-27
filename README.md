# The Vinyl Hub

## Table of Contents

## Project Overview
The Vinyl Hub is an e-commerce site selling classic vinyls, audio accessories and record players.
It aims to build a customer base by providing high quality products and also developing a community,
by allowing registered user a way to interact and show their vinyl collections by filling out a profile form.
Registered users would also have the ability to request albums that could be added to the store. Due to the big scope
I have planned for this project the profile section is basic. In future releases it will be added to significally.
Theree is still discounts applied and the delivery details saved so I feel there is enough incentive for our shoppers to sign up
to become site members.

### Target Audience

The target audience is the ever growing vinyl market in Ireland and abroad.
There is a real movememt towards real and authentic sound and this site is hoping to be a part of that 
by offering top quality products to those looking.

### Business Logic

This is straight forward as the business aspect would come directly selling our products in 
the shop or fulfiiling our registered members request forms for products we can obtain.


### User Stories 
I built my user stories in an agile framework where I built upon the foundations laid in 
the code institue's Boutique Ado project and tailored them to the needs of my projects users and store owner.
The table below are the stories upon which this project was built

![user story table](media/user_story1.png)
![user story table 2](media/user_story2.png)

## UX

### Design Choices 

#### Colour Pallette

The overall structure of the site is based off bootstrap 5's row and column classes.
The colours and overall theme of the site is based off a vibrant 80's colour pallette, i.e. MTV'S 80's logo.

![80s brand inspiration](media/1980s-brand-inspiration_1_400x400.png)

From these images I decided on `#fcb014`, `#c01b21`and `#018bd4` as this would have the feel and style from the 80's,
a time when Vinyls were at their peak. Due to accessability reasons I had to alter the blue to `#047ab7` for greater contrast for the users.

![colour pallette](media/mtv-80s-color-scheme_400x400.png)

![update color pallette](media/new_color_palette.png)

### Font Choice

The fonts that I have chosen have come from Google Fonts.
They are Audiowide for headings https://fonts.google.com/specimen/Audiowide.
It really has an 80s vibe off the font that goes with the overall theme.
For the main bodies of text I have chosen Oswald as I find these really compliment each other. https://fonts.google.com/specimen/Oswald

### Wireframes

My wireframes were done with Balsamiq https://balsamiq.cloud/ . These provided a good outline for my product.
In the building process my designs adapted and changed throughout so these might look abit different.

![bag-view](media/bag_view.png)

![bag-view-alt](media/bag_view(Alternate732p).png)

![checkout](media/checkout.png)

![checkout-alt](media/checkout(Alternate266e).png)

![home](media/home.png)

![home-alt](media/home(mobile).png)

![product-detail](media/product_detail.png)

![product-detail-alt](media/product_detailAlternate549c).png)

![products](media/products.png)

![products-alt](media/products(Alternate750h).png)

![profile-hub](media/profile_hub.png)

![profile-hub-alt](media/profile_hub(mobile).png)

## Features

The first feature you see upon visiting the site is the responsive navbar.
This not only is great for navigating the site but it also has a serch field and a real time shopping bag which is 
continually updating your grand total.
![responsive navbar](media/navbar-feature.png)

This leads me nicely to the next feature where if the customer registers with the site they will receive a discount or special offer.
As of now that is 15% off all hip hop records. This is applied in real time through context processors.

When you register you will receive a confirmation email this will allow you to activate your user profile and build a profile.
At the moment its very basic but in the future it will be fleshed out. Here you can store your default delivery information for faster
checkouts in the future. 

A secure payment system from stripe where customers can pay with confidence.

A feature that will hopefully make it into this release is the request a product page. Where customers can request a product or record they would 
like to buy but find it hard to get.

## Future Features

The user profiles will be expanded into user profile section where users can interact with other users and have a
message system to promote traffic to the site.

I have added favourite genre to the user profile , whichever genre they pick will be used to show products on a carousel at the bottom
of the page for the user. Didnt have time to implement in this release.

## Technologies Used

- __HTML:__ The HyperText Markup Language, or HTML is the
 standard markup language for documents designed to be displayed in a web browser.

- __CSS:__ Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. 
 is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.[

- __JAVASCRIPT:__ JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled
, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions. 

- __JQUERY:__ jQuery is a JavaScript library designed to simplify HTML DOM tree traversal
 and manipulation, as well as event handling, CSS animation, and Ajax.

- __DJANGO:__ Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an American independent organization established as a 501 non-profit.

- __PYTHON:__ Python is an interpreted high-level general-purpose programming language.
 Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
 Its language constructs as well as its object-oriented
 approach aim to help programmers write clear, logical code for small and large-scale projects. 

- __SQLITE:__ SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private. SQLite is the most widely deployed database in the world with more applications than we can count, including several high-profile projects.

- __HEROKU POSTGRES:__ Heroku Postgres is a managed SQL database service provided directly by Heroku. You can access a Heroku Postgres database from any language with a PostgreSQL driver, including all languages officially supported by Heroku.

 - __Git:__ Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
Git is easy to learn and has a tiny footprint with lightning fast performance. It outclasses SCM tools like Subversion,CVS, Perforce
, and ClearCase with features like cheap local branching, convenient
 staging areas, and multiple workflows.

 - __Github:__ GitHub is a Git repository hosting service, but it adds many of its own features. While Git is a command line tool, GitHub provides a Web-based graphical interface.
  It also provides access control and several collaboration features, such as a wikis and basic task management tools for every project.

- __BOOTSTRAP5:__ Bootstrap, the most popular front-end framework built to design modern, responsive, and dynamic interfaces for professional design web pages, is currently undertaking a major update, Bootstrap 5.

- __Gitpod:__ Gitpod is a container-based development platform that puts developer experience first. Gitpod provisions ready-to-code development environments in the cloud accessible
 through your browser and your local IDE (stay tuned for a blog post with more details on that).

- __VSCODE:__ Visual Studio Code is a source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting,
  intelligent code completion, snippets, code refactoring, and embedded Git.

- __STRIPE:__ Stripe is an Irish-American financial services and software as a service company dual-headquartered in San Francisco, United States and Dublin, Ireland. The company primarily offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.

- Along with all of these technologies I used packages and other bits from these in development.They can also be found in my requirements.txt file

- asgiref==3.4.1
- boto3==1.18.29
- botocore==1.21.29
- crispy-bootstrap5==0.5
- dj-database-url==0.5.0
- Django==3.2.6
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.12.0
- django-storages==1.11.1
- gunicorn==20.1.0
- jmespath==0.10.0
- oauthlib==3.1.1
- Pillow==8.3.1
- psycopg2-binary==2.9.1
- pylint-django==2.4.4
- pylint-plugin-utils==0.6
- python3-openid==3.2.0
- pytz==2021.1
- requests-oauthlib==1.3.0
- s3transfer==0.5.0
- sqlparse==0.4.1
- stripe==2.60.0

## Manual Testing 

I have been doing continual testing throughout development , catching bugs outlined further on, So I will concentrate my manual testing on 
the user stories I have generated as this covers all aspects of functionality! crud operations payments and database manipulation.
Here is the link for the [manual testing](manual_testing.md)


## Bugs & Fixes 

* Had an issue on the home page when I was checking responsiveness the h1 was being going over the page on devices under 700px.
* This was a straight forward fix as I was able to adjust the font-size with media queries
* Had an issue with the contrast of the blue text on the white background that would of been an issue 
for users due to a contrast issue.
* I solved this by switching from `#018bd4` to a slightly deeper blue `#047ab7`
* Encountered a bug when I was updating my products page where the icon for each product appeared several times instead of once.
* I checked my code and relised i left out the closing i tag
* Encountered a bug when using javascript to update the quantity on the bag , it wouldnt trigger the form to update
* I solved this my giving the form an id and targetting it directly
* Upon further testing this was only updating the first item in the bag.
* So I rechecked my bag.html and after alot of headscratching realised for stlying I put the 2 anchors in a div and this stopped my javascript function from finding the form class with the .prev method. I deleted the div and this solved the issue.
* Had an issue with my messages where they would trigger but I couldn't see them , through Chrome Dev tools I could see the outline on the page
so after checking the bootstrap 5 documentation I found this snippet `Options can be passed via data attributes or JavaScript. For data attributes, append the option name to data-bs-, as in data-bs-animation="".` they were `True` by default so I changed data-bs-autohide to `False` and the messages started to appear.
* I had a big issue with my line item order , in fixing it I managed to mess up my discount context processor 
* To fix this I had to rework the discount to a straight 15% for registered users. This is something that will be adjusted in later releases.
* Have an issue on deployment to heroku where my media files in certain folders are not loading
*  I solved this my altering te jinja templates
* Issue where the profile form is not saving the media for user profiles , but is when adding manually through the admin.
* I added request.FILES to the view and added enctype to the form this solved the issue.

## Html and CSS Validation

Passed all HTML and CSS was passed too but it only didnt recognise the :is pseudo selector, I checked and it seems to be used quiet alot
so I decided to keep it in.

![html valid](media/html-valid.png)

![html valid](media/html-products-validation.png)


## Deployment 

Deployment was followed step by step from the Code Institutes Boutique Ado


### Heroku

1. First you will need Heroku's `PostGres` add on to ensure that the sqlite file-based database can work once deployed. Search for PostGres in  the **Resources** tab in Heroku. 

2. Add the add on. You will now see a `DATABASE_URL` within the config vars.

3. Install the following packages to your app: `pip3 install dj-database-url`, `pip3 install psycopg2-binary`

4. Import dj-database-url in your settings.py file: `import dj_database_url`

5. To get database to work on the deployed version, we need to tell the app to use the PostGres `DATABASE_URL` from Heroku. However, we still want to use the default database setting when running the project locally. To fix this issue you need to connect to sqlite when using the local version, and postgres for the deployed version. Do by updating the database settings to the following:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

6. To ensure that the databases work correctly, we need a few things. First install **unicorn** using `pip3 install gunicorn`. Don't forget to update your requirements.txt by using `pip3 freeze > requirements.txt`.

7. Remember, because you are now connected to Postgres, you need to run migrations again with `python3 manage.py migrate`.

8. Since we’re now using a different database, it won’t have any of our models or user information in it. To fix that, we need it to match the sqlite3 database by importing all of your data by using your fixtures, using the following command syntax: `python3 manage.py loaddata <object>`. Ensure that any tables with dependencies are loaded first to avoid any issues. E.g. `python3 manage.py loaddata categories` should be done **before** `python3 manage.py loaddata subcategories`.

9. Finally, set your superuser again so that it can work in the deployed site, using `python3 manage.py createsuperuser`.

10. Now you can create your Procfile to tell Heroku to create a web dyno which will run unicorn and serve our django app, using the following syntax: `web: gunicorn <app_name>.wsgi:application`. In my case, this is: `web: gunicorn legion.wsgi:application`

11. If you aren't logged in to Heroku already, log in via the CL using `heroku login -i`. You also may need to initialize your heroku git remote, using: `heroku git:remote -a <appname>`

12. Temporarily disable `collectstatic` so that Heroku won't collect static files when deploying the app, using `heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>`. This will be added to your config vars in Heroku.

13. Add the hostname of your Heroku app to `allowed_hosts` in `settings.py`. Add localhost also so that your local version will still work. **Note** if you are using Visual Studio code, then you may need to add or change `localhost` to '127.0.0.1' to ensure that the application can still run locally. Below is what it may look like in your settings:
```
ALLOWED_HOSTS = ['my-legion-app.herokuapp.com', 'localhost', '127.0.0.1']
```

14. Commit changes and push to GitHub. Then push to heroku by using `git push heroku master`.

15. Within Heroku, navigate to the **Deploy** tab and **Enable Automatic Deploys** to sync Heroku to your GitHub repository.

16. Generate a secret Django key using a generator, and add it to your config variables in Heroku. Then in your` setting.py` file, update your `SECRET_KEY` settings and your `Debug` settings to the following:
```
SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = 'DEVELOPMENT' in os.environ
```


### AWS

Amazon AWS was used to store the application's static and media files. Listed below are the required steps to get AWS running correctly.

Create an AWS account and work your way through the registration process. 

#### Create Bucket

1. Once your account is created, navigate to the services tab and searh for **S3**, click on it to get started.

2. Create a new bucket via the AWS S3 service by clicking the `create bucket` button. 

3. Enter your bucket name. It's good practice to name the bucket to match the Heroku app name. In my case, my bucket name was `the-vinyl-hub`, which matches the name on Heroku.

4. Select the region that is closest to you and uncheck `block all public access` and acknowledge that the bucket will be public.

5. Click `create bucket` to create your bucket.


#### Bucket Settings

1. Click on your new bucket to navigate to its settings.

2. Once there, first click the **properties** tab to turn on static website hosting.

3. Scroll down to **Static website hosting** and click edit. Ensure that `static website hosting` is enabled, and add the default values to index document and error document, which would be 'index.html' and 'error.html'. Once done, click **save changes**.

4. Next, navigate to the **permissions** tab, and scroll down to the **Cross-origin resource sharing (CORS)** section. Click the edit button and paste in the following code:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

5. Then navigate to **Bucket policy** and click the edit button. Click **Policy generator** to generate a security policy for your bucket. 

6. Choose `S3 Bucket Policy` for your **policy type**.

7. Allow **all** principles by adding a `*` to the **Principal** field.

8. Select `Get Object` in the **Actions** select field.

9. Copy the **Amazon ARN** from the previous tab (your bucket policy tab) and copy your `Bucket ARN` and paste it into the **Amazon Resource Name ARN** field.

10. Click **Add statement** and then **Generate policy**, and then copy the generated policy into the bucket policy editor. Before you click save, add `/*` to the end of your Resource url to allow full access to all resources in the bucket. It may look something like this:
```
"Resource": "arn:aws:s3:::my-legion-app/*"
```

11. Finally, navigate to the **Access Control List** section, still within the Permissions tab, to set the **List Objects** permission to **Everyone** under the **Public Access** section.


#### Create a User Access

1. Navigate to the AWS Services menu and search for **IAM**. IAM stands for Identity and Access Management and will allow a user to access the S3 bucket we have created.

2. First we want to create a group for our user to live in. To do that, click on the **User Groups** tab in the sidenav, and create a new group by clicking the **Create group** button to your right. Give the group a name that is relevant to your application and purpose. In my case, I named the group `manage-the-vinyl-hub`. Click **Create group** to create your new group.

3. Next, navigate to the **Policies** tab in the sidenav and click **Create Policy**.

4. Navigate to the JSON tab and click **Import managed policy** to import a AWS pre-built policy for full access to S3.

5. Search for **S3** and then import the **AmazonS3FullAccess** policy.

6. However we only want full access to *our* bucket and everything within it, to do that we are going to create a group access policy to give group access to the S3 bucket we have created.

7. Using a new tab so you don't loose the one you are currently on, navigate to the **bucket policy page** in S3 to get the bucket ARN. Paste that into **Resources** inside the JSON tab inside **IAM**. You'll also want to add another rule for all files and folders in the bucket. Look below for an example:
```
"Statement": [
    {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": [
            "arn:aws:s3:::my-legion-app",
            "arn:aws:s3:::my-legion-app/*"
        ]
    }
]
```

8. Click Next, and next again to navigate to **Review Policy**. Give your policy a name and description then click **Create Policy**.

9. Now navigate back to the **User Groups** tab in the sidenav and click on the group you create before. In the **Permissions** tab, click **Add Permissions** and then **Attach Policies**. Search for the policy you just created, check it and click **Add Permissions**. 

10. Finally, we want to assign the user to the group, so that it can use the policy to access the files within the application.

11. Navigate to the **Users** tab in the sidenav and click **Add User**. Create a user using the following syntax `<appname>-staticfiles-user`, which in my case is, `the-vinyl-hub-static-user`,as I forgot the files part :-), then give them **programmatic access** and select **Next**.

12. Now you and add the user to your group with the policy attached by clicking on the group name you just created.

13. Click through until the end and click **Create user**.

14. Finally click **Download .csv** - a CSV file containing the user access key and secret access key - which you will use in the Django app. Note that you cannot go through this process again so ensure that you keep this file safe.


#### Connect to Django and Add Static Files

1. Add the AWS **Access Key ID** and **Secret Access Key** that you just downloaded in the previous step to your config vars in Heroku. Also add the variable `USE_AWS: True`.

2. In your project, install the boto3 and django-storages using the following commands: `pip3 install boto3`, `pip3 install django-storages`. Remember to freeze your requirements.txt file by using the command: `pip freeze > requirements.txt`.

3. Add storages to your installed apps.

4. Next we need to tell Django which bucket it should be communicating with. We’ll only want to do this on Heroku so use an if statement to check if there’s an environment variable called `USE_AWS` in the environment, and if so define the `AWS_STORAGE_BUCKET_NAME` and `AWS_S3_REGION_NAME` and also the access key and secret access key which we’ll get from the environment. Additionally, you need to tell Django where the static files will be coming from in production, which is going to be the bucket name from AWS, stored inside the `AWS_S3_CUSTOM_DOMAIN`. It’s very important to keep these keys secret, because if they end up in version control, someone could use them to store or move data through your S3 bucket and Amazon would charge your card.

5. Your settings file may now look something like this:
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'my-legion-app'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

6. If it exists, remove the `DISABLE_COLLECTSTATIC` from your Heroku config vars as this time django will collect static files automatically and upload them to S3.

7. The next step is to tell Django that in production, we want to use S3 to store static files whenever someone runs `collectstatic`, and that any uploaded product images should go there also. To do that create a new py file called `custom_storages.py` and import your settings and s3boto3 storage class. Paste the following code inside:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

8. The last step is to go to `settings.py` and tell it that we want to use our storage class for static file storage, and that the location it should save static files to is a folder called **static**, and then do the same thing for media files. We also need to override and explicitly set URLS for static and media files using our custom domain and the new locations. Add the following code below the code you added in **step 5**:
```
# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_LOCATION = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLS in production
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

9. Add `AWS_S3_OBJECT_PARAMETERS` to tell the browser it’s okay to cache static files for a long time to improve performance:
```
AWS_S3_OBJECT_PARAMATERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

#### Add Media Files to S3

1. Navigate to your bucket in S3 and create a **new folder** called **media**.

2. Inside click **upload** and select all images from your project directory.

3. Under the **Permissions** tab, check **Grant public read-access** to these objects.

4. Click Upload to upload your media files.



### Stripe and Heroku

1. Create a Stripe account if you haven't done so already and navigate to **API Keys** under the **Developers** tab.

2. From there, find and copy `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` and paste them into the Heroku config vars. Give them the same name so that they can be accessed by your application.

3. To setup a webhook, navigate to to the **Webhooks** tab on Stripe, and click **Add Endpoint**. In there paste in the appropriate url for your application. For me this was `
https://my-legion-app.herokuapp.com/checkout/wh/` and check *recieve all events**. Add the endpoint.

4. You can now reveal your webhook signing secret, which you can add to Heroku config variables as done before. 

5. Ensure all your variable names match the names defined in `settings.py`.

6. Send a test webhook from Stripe to ensure that the listener is working by clicking **send test webhook**.

Now everything should be up and running on Heroku!!

As you can guess it never goes this easy and I found a few small bugs in the process.
For example I couldn't get the database to switch over but a quick search on slack found that if I 
typed `unset PGHOSTADDR` into the terminal it should work after that.


## Credits 

* The images for the record players and the description were taken from https://www.worldwidestereo.com/blogs/wws-underground/entries/best-turntables.
* The images for the vinyls and the descriptions were taken from https://longlivevinyl.net/2020/02/18/the-essential-hiphop/ and https://www.radiox.co.uk/features/best-vinyl-records-to-collect/

* Code Institue and their Boutique Ado project really was the guiding light for me

* My partner and kids for sticking with me this last hectic week !