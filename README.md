[![Build Status](https://travis-ci.com/martinmaguire89/milestone-project-4.svg?branch=master)](https://travis-ci.com/martinmaguire89/milestone-project-4)
# Milestone-project-4
# One For The Road

My 4th milestone project is a full-stack site website based around business logic used to control a centrally-owned dataset. One for the road is a e-commerce webpage selling craft beer from all around the country. The reason for this idea was due to me looking for a place to buy a variety of different craft beers from around Ireland. This website allows users to look at many different beers from all the different counties and have them deliver straight to there door. There is also the added bonus for customers once they have registered, they can enjoy a regular updated blog of new crafts beers around the island and best places to visit for the very best craft beer.  Valuable information for the serious craft beer enthusiast. 

It can be viewed on heroku [One For The Road](https://on-for-the-road-ms4.herokuapp.com/)

## UX
### Who is the target audience?

* The target audience is craft beer enthusiast who would like somewhere where they can get a wide range of beers from across the country.  The Blog page  targets people who are interested in craft beer but would like to learn more about different type of craft beers and good a compliments. Finally its ease of use will appeal to partners of craft beer drinker who will find it easy to buy craft beers for their significant other.  


### How does this attract our target audience?
*  The initial page starts with a large image of a pint of beer to capture the image of a tasty thirst-quenching beer.  The green colour stirs up images of Ireland and relaxing with a craft beer.  The easy layout supports the users need and makes their experience even better so they come back again. The quotes from previous users of the site help the claimant know this is a good site to use and use again.


## User Stories
*	As a user, I want the initial page to be eye catching
*	As a user, I want it to be easy to navigate
*	As a user, I want it to be easy to register if i need to.
*   As a user, I want it easy to browse different beers
*	As a user, I want it to be easy for me to add any items i want to a basket and  pay for any products


## Wireframe
* Link to my [balsamiq wireframe](https://github.com/martinmaguire89/milestone-project-4/blob/master/milestone%20project-4.pdf)
*	I decided to use Balsamiq to create my wireframe because it was recommended in the milestone project and by code institute mentors on slack.

## Technologies used
*  Html
*  CSS
*  [Python](https://www.python.org/)
*  [Google Fonts](https://fonts.google.com/) - Used to style the fonts of the website.
*  [jQuery](https://jquery.com/) - To make certain features function on the page.
*  [git](https://github.com/) - Used as a repository
*  [Gitpod](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki) - Used for a development and testing area.
*  [Bootstrap](https://www.bootstrapcdn.com/) - Bootstrap framework to create responsive design.
*  [fontawesome](https://fontawesome.com/) - for social media icons.
*  [Django](https://www.djangoproject.com/)- a Python-based free and open-source web framework that follows the model-template-view architectural pattern.
*  [PostgresSQL](https://www.postgresql.org/) - backend database used to store the information on the products
*  [Travis-CI](https://travis-ci.org/getting_started) - Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket
*  [Heroku](https://dashboard.heroku.com/auth/heroku/callback?code=61fc81a2-ba86-42ec-ac96-a904a0153b77)- A cloud platform as a service enabling deployment for this CRUD application.
*  [Stripe](https://stripe.com/gb)-  An API that allows individuals and businesses to make and receive payments over the Internet.


## Features
### Feature 1 –  .

### Feature 2 – .


### Feature 3 –  .


### Feature 4 – .


### Feature 5 – .



## Features Left to Implement
* 
* 
*  

## Testing
* Used Google Chrome developer tools to test website responsiveness across multiple devices such as Tablets, Mobiles and laptop. This allowed me to see any issue's with sizing in different version control.
*  I used different web browsers such as Microsoft edge and Firefox to test how my page would run on different web browsers. I then used each responsive tool in each browser to again test my version control to see if it would still work effectively or if I would encounter any problems. 
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
* I used [cssautoprefixer](https://autoprefixer.github.io/) to help get the appropriate vendor prefixes needed for my code to work in all browsers.
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
*  I used [codebeautify](https://codebeautify.org/python-formatter-beautifier) to help with the correct Indentation of my python code

## Issues when Testing
*
## Deployment

This full stack application was developed using github and version controlled via local (git) pushes.
Any secret environment variables were stored in an env.py file which was added to a .gitignore file keeping those files out of play from the public repo.
When deploying to Heroku the variables detailed in the env.py file was added to Heroku Settings tab for this application under the Config Vars section allowing the deployed site to utilise these secret variables.

Heroku
* This site is deployed on Heroku
My project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud Heroku in a range of programming languages. Python was the mainly used for this project.

The following process was undertaken to succesfully deploy the project on the Heroku:

As per the requirements, before I can push my code to the Heroku app, I installed:
* we need to Pip3 install dj_database_url and pip3 install psycopg2.
* A requirements.txt file is needed to run the installed dependencies, so to create and commit this file, the following command was used: $  pip3 freeze --local > requirements.txt (and also used to update the file if any libraries were added).
* A Procfile is needed to direct the Heroku app to the file that it needs to run. So I used the command $ echo web: python > Procfile in the terminal to install the file. 
* This was followed by a simple command in the terminal to run the web process: $ heroku ps:scale web=1.
* Create an app on Heroku with a unique name for your app
* In resources add a Postgres database – Hobby Dev and copy the URL for the new database to Config Vars
* we need to migrate all excisting migrations to our new postgres databse and create a new superuser.
* In settings tab add any secret environment variables to the Config Vars of those the secret values held in the env.py for Live Deployment.
•	Adding any secret environment variables to the Config Vars of Heroku App Settings tab and assigning those the secret values held in the env.py for Live Deployment.
•	
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx


If you wish to clone this project from GitHub:
*	Click on this [link](https://github.com/martinmaguire89/milestone-project-4) to the GitHub repository.
*	There is a green button saying "Clone or download" on the right-hand side, click on this.
*	Next copy the clone URL for the repository that is provided.
*	Open Git hub in your local IDE.
*	Change the current working directory to the location where you want the cloned directory to be created.
*	Type git clone, and then paste the URL copied in Step 3. git clone https://github.com/martinmaguire89/milestone-project-4.git
*	Press Enter to create your local clone.
*	Once open create an env.py file and assign the Database URL, Secret Key, Stripe Publishable & Stripe Secret, and finally Emailing variables. Ensure the env.py is living in the root of your project directory and then add it to .gitignore so now of this is exposed once you commit your code.



## Credits
* Credit goes to the tutos for there hlep wiht my log in problems and my mentor rahul for everything.
### Content
*

### Media

