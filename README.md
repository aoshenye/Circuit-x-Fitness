# CutZ

This primary goal of Circuit X is to provide a website for consumers to find a diverse range of professional Personal trainers on one website.  Consumers will be able to  to contact a trainer, make a payment for their service. That service itself is only offered to consumers that sign up for an account. With the account, consumers will be able to view the trainers that are available and pick and pay for their services. They will also be able to track their usage and show who they have previously picked to be trained by.  Consumers will be able to delete their previous usage and comment on how their session went as well, with all shown on the login page. 

## UX

### Strategy

The main goal of this project is to provide users with a sleek and simple user experience of blogger comments for signed up users and a chance for them to provide their reviews as well as buy products from the shop related to fitness. User needs are described below. 

User Stories:

![image](https://user-images.githubusercontent.com/56303835/113061870-a7c36380-91aa-11eb-93ad-4524c3fb84a2.png)


## Features
-   Navigation bar: Simple and swift and initiated with bootstrap
- CRUD functionality
	- The Form on sign up page - simple form. 
	- reviews page - get_reviews.html - provides users to read all reviews. 
	- Edit and Delete function provided on the user's profile page. 
	- Forgotten password function
- Flash messages provided to warn people when logging in or trying to register with a password that does not meet the minimum requirements. 
- Buttons: initialized from Bootstrap for sign up and sign in and check out
- sign in and sign up buttons to gain access into links to those respective pages and to highlight them to users. 
- Blog section in profile page provides a means for users to create, edit and delete reviews or any comments they have when signed in to the their profile. 
- Checkout section allows users to submit the card details and personal details to complete their purchase. 
- Form page in About us page is used for user to send any other feedback about the company generally.  


# Wireframes

![image](https://user-images.githubusercontent.com/56303835/113062140-31733100-91ab-11eb-822f-fc7ec22f4aea.png)
![image](https://user-images.githubusercontent.com/56303835/113062168-3cc65c80-91ab-11eb-9dcc-2d8d0f65f831.png)
![image](https://user-images.githubusercontent.com/56303835/113062183-418b1080-91ab-11eb-99a0-bf28419b5cff.png)
![image](https://user-images.githubusercontent.com/56303835/113062197-48198800-91ab-11eb-923b-c381da909a70.png)
![image](https://user-images.githubusercontent.com/56303835/113062232-549de080-91ab-11eb-8609-59370f8bbce3.png)
![image](https://user-images.githubusercontent.com/56303835/113062243-59fb2b00-91ab-11eb-943d-06343170ecf4.png)
![image](https://user-images.githubusercontent.com/56303835/113062277-654e5680-91ab-11eb-936d-65d4b9cd7507.png)
![image](https://user-images.githubusercontent.com/56303835/113062298-6d0dfb00-91ab-11eb-859f-ea81335ead85.png)

# Mockups 
![image](https://user-images.githubusercontent.com/56303835/113062394-93339b00-91ab-11eb-892d-a1f9a2c7c7e7.png)
![image](https://user-images.githubusercontent.com/56303835/113062413-99c21280-91ab-11eb-956e-9292cfb92126.png)
![image](https://user-images.githubusercontent.com/56303835/113062436-a21a4d80-91ab-11eb-856f-e07957fdc431.png)











## Technologies Used

-   
    -   **HTML**  for the outline of the website and all it pages 
    - **CSS** for styling support rather than full styling of website. 
    - **Python** for background logic of website. 

	- **Bootstrap** - creating the layout of the pages, navigation bar and footer.
		- Crispy FORMS - For the forms used
	- **Django** for the overall set up and use of templates. 
	- **SQLLITE** for relational database 
	- **Stripe** for payments
	

## Testing
- Testing the checkout by clicking on secure checkout after purchasing the products, Inputting test inputs into the form and test card details from stripe, and purchasing the product. First test did not take me to the checkout successful page but once I had altered the view so that the success page would show in the checkout app, The success page finally loaded after purchase, showing that my purchase went through. I checked the Events page of stripe to ensure that was the case as well as the Django Administration. The django Administration page showed the purchase but when clicking the purchase, I was taken to an error page which suggested that I had a view in the checkout app requiring the sku. I thus removed the sku view as I was not using that and re-loaded the page for the administration and finally was able to view and edit the purchases made through the GUI. 

- Tested the CRUD functionality of the comments section and every part of it worked with success apart from the edit functionality. After making a new profile, making a new comment deleting and then making another one again and editing it, an error occurred -(Not Found: /profile/comment/edit/5). Ichanged the urls.py entry for blog from path('blog/', include('blog.urls')), to path('',include('blog.urls')) instead and run a refresh and tried to edit and delete. Edit was functioning properly, but delete was not. I went to the urls.py for the blog app and put in post_detail before the path name slug for both the first entry and last entry path and finally got the functions to work. 

 - Testing on links and and sign in and sign up buttons works with no errors. Testing of the error message functions well based on the logic provided. 

Testing took place using: 
- Google Chrome - Version 86.0.4240.183 (Official Build) (64-bit)

- Microsoft Edge - Version 86.0.622.63 (Official build) (64-bit)

- Firefox - 75.0 (64 bit)

- The website...

- The site was also tested on the following Devices:

	- Google pixel 5a using Google Chrome on Android 10 iphone xr using Safari on IOS 13.4.1 

## Deployment new

 1. log in to heroku
 2. create new app
 3. give the app the name
 4. click on resources and provision new postgress database (find and click on Heroku Postgress)
 5.  click on the free plan and click submit
 6.  go back to gitpod and install dj_database and psycopg2-binary
 7. ensure requirements installed by freezing
 8. add import  dj_database_url to setting.py
 9. go down to default databases and comment it out. 
 10. below it create  a new one -  'default': dj_database_url.parse()
 11. got to Heroku and settings
 12. click on config and reveal config
 13. copy and paste the postgress url from Heroku into the brackets after "url.parse" with quote marks
 14. save and run migrations
 15. then load data for the fixtures used
 16. then create superuser
 17. insall unicorn
 18. freeze requirements to add installed unicorn
 19. create Procfile
 20.Then run login for heroku
 20. then heroku config:set DISABLE_COLLECSTATIC=1 --app circuitx
 21. got to settings.py and on AllOWED HOSTS type in 'circuitx.herokuapp.com', 'localhost'


### Final part of Deployment 
	1. Link git hub repository to Heroku
			-click Deploy
			- got to App connected to GitHub
			- find my github page
			- click connect and ensure connection  made. 
			- scroll down to Automatic Deploys
			- In the choose a branch to deploy section, click Master
			- scroll down to Manual deploy and click Deploy Branch.
			- Wait a few seconds for deployment.   


## Credits

### Content
- Bootstrap used for layout and design of website Particularly the home page is inspired by example themes by [Bootstrap](https://getbootstrap.com/)
- The grid for the shop created by [Bootstrap example](https://bbbootstrap.com/snippets/simple-product-shopping-grid-styles-89973846)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
Checkout app was inspired by the Boutique Ado project and the use of Stripe was inspired by Boutique Ado as well. 

### Media
 - The background, trainers and products photos used in this site were obtained from:
[Trainer](https://unsplash.com/@hayleykimdesign?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
[Sports bra](https://unsplash.com/@aloragriffiths?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText%22%3EAlora%20Griffiths)
[Dip bar](https://www.ebay.co.uk/itm/MaxStrength-Parallel-Dip-Bars-Home-Gym-Workout-Crossfit-Calisthenics-Station-/353051251838)
[Gravity strap set]( https://www.hsn.com/products/gofit-gravity-straps-set/7403913?sz=3&sf=HF0189&ac=&utm_source=pinterest&utm_medium=social-organic)
[Under armour](https://www.amazon.com/Under-Armour-Mens-CoolSwitch-ArmourVent/dp/B07CPRMLMP)
[Nike Personal Trainer used](https://www.behance.net/gallery/109596433/NIKE-WomensJDI-Retouch?tracking_source=project_owner_other_projects)
[Nike Personal Trainers used](https://www.nike.com/gb/ntc-app)
[Bands](https://www.cpsc.gov/Recalls/2017/dicks-sporting-goods-recalls-resistance-tubes)
[Sneakers](https://www.carolsdolls.xyz/ProductDetail.aspx?iid=316341898&pr=68.99)
[Backgrounds and trainer images](https://www.behance.net/gallery/97315025/361-20Q3-Training)

- Colours schemes were influenced using [Coolors](https://coolors.co/palettes/trending)
### Acknowledgements
- [StackEdit for the readme](https://stackedit.io/app#)
- [Smart mockups for the mockups](https://smartmockups.com/mockups)
- [Wireframes](https://app.moqups.com/)

-   I received inspiration for this project from code institutes Boutique Ado mini project Checkout and Stripe Payments use. [Boutiqe Ado - Mini Project](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/?activate_block_id=block-v1%3ACodeInstitute%2BFSF_102%2BQ1_2020%2Btype%40sequential%2Bblock%40d3188bf68530497aa5fba55d07a9d7d7)
- [Stripe](https://dashboard.stripe.com/test/dashboard) was used to test out and as the preferred payment option for this project as well. 
- [Django Blog](https://djangocentral.com/building-a-blog-application-with-django/) to help inspire build on a blogging system for the comments section. 
