# Banana Palace
TODO: Add logo image

![Amiresponsive image](TODO)


Link to live website: [Banana Palace](TODO) <br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)

<hr>

## Table of contents

TODO

* [Introduction](#introduction)
    * [Website goals](#website-goals)
    * [First time user goals](#first-time-user-goals)
    * [Returning user goals](#returning-user-goals)
* [Design](#design)
    * [Colours](#colours)
    * [Typography](#typography)
    * [Images](#images)
    * [Logo and Favicon](#logo-and-favicon)
* [Features](#features)
    * [Welcome screen](#welcome-screen)
    * [Welcome screen]()
    * [Welcome screen]()
    * [Welcome screen]()
    * [Security Features and Defensive Design](#security-features-and-defensive-design)
    * [Future features](#future-features)
* [Project planning and execution](#project-planning-and-execution)
    * [Design thinking](#design-thinking)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
        * [Business goals](#business-goals)
        * [Progressive data model](#progressive-data-model)
        * [Conceptional](#conceptional)
        * [Logical](#logical)
        * [Physical](#physical)
    * [Agile software development](#agile-software-development)
        * [Epics](#epics)
        * [User stories](#user-stories)
        * [Product backlog](#product-backlog)
        * [MoSCoW prioritization](#moscow-prioritization)
        * [Iterations](#iterations)
        * [Kanban board](#kanban-board)
    * [Technologies used](#technologies-used)
        * [Languages](#languages)
        * [Frameworks](#frameworks)
        * [Libraries](#libraries)
        * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Heroku](#deployment-to-heroku)
    * [Changes](#changes-to-the-code)
    * [Local development](#local-development)
        * [Forking](#forking-the-project)
        * [Cloning](#cloning-the-project)
* [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Code](#code)

<hr>




## Introduction

This website is ... for ...

### Website goals
- Help

### First time user goals
- Think about

### Returning user goals
-


# UX and UI - (user experience and user interface)


### Mobile first approach
All pages are designed to be responsive to different screen sizes to accommodate users with different preferred devices.

<details><summary>Screenshot examples of responsive behavior from mobile to tablet to computer</summary> <p align="left"><img src="TODO" alt="examples of responsive behavior" width="700"/></p> </details>


### Accessibility

Semantic HTML is used to aid people with dissabilities such as visual impairment and alternative text is used for all images so it can be read by screen readers. Semantic HTML also helps with search engine optimization so the right users can find this site and find it useful.



## Design

### Colours


 <p align="left"><img src="./documentation/images/color-pallet.png" alt="Color pallet for Banana Palace" width="700"/></p>


### Typography
Headings - Merienda
Button-font - M PLUS Rounded 1c
Main-font - Noto Sans
Google fonts


### Images



### Logo and Favicon



[Back to top](#table-of-contents)

## Features

### Welcome screen

The ...

<details><summary>Screenshot of the feature</summary> <p align="left"><img src="TODO" alt="TODO" width="700"/></p> </details>


### Feature 2

The ...

<details><summary>Screenshot of the feature</summary> <p align="left"><img src="TODO" alt="TODO" width="700"/></p> </details>


### Feature 2

The ...

<details><summary>Screenshot of the feature</summary> <p align="left"><img src="TODO" alt="TODO" width="700"/></p> </details>




### Security Features and Defensive Design

TODO
Validating every user input creates a defensive design that runs correctly and keeps running no matter what action the user takes.






## Future features
-


[Back to top](#table-of-contents)


# Project planning and execution


### Design thinking

TODO (maybe)


### Wireframes

<p align="left"><img src="./documentation/images/wireframes-all.png" alt="Entity relationship diagram" width="700"/></p>

Initial wireframes as a guide for development and design.

Screenshots of individual wireframes for the:
<details><summary>top part of home page</summary> <p align="left"><img src="./documentation/images/wireframes-home-top.png" alt="wireframes for the top part of home page" width="600"/></p> </details>
<details><summary>middle part of home page</summary> <p align="left"><img src="./documentation/images/wireframes-home-middle.png" alt="wireframes for the middle part of home page" width="600"/></p> </details>
<details><summary>bottom part of home page</summary> <p align="left"><img src="./documentation/images/wireframes-home-bottom.png" alt="wireframes for the bottom part of home page" width="600"/></p> </details>
<details><summary>about page</summary> <p align="left"><img src="./documentation/images/wireframes-about.png" alt="wireframes for the about page" width="600"/></p> </details>
<details><summary>users profile page</summary> <p align="left"><img src="./documentation/images/wireframes-user-profile.png" alt="wireframes for the users profile page" width="600"/></p> </details>
<details><summary>owners profile page</summary> <p align="left"><img src="./documentation/images/wireframes-owner-profile.png" alt="wireframes for the owners profile page" width="600"/></p> </details>
<details><summary>fun booking page with date and time</summary> <p align="left"><img src="./documentation/images/wireframes-fun-booking-date-time.png" alt="wireframes for the fun booking page with date and time" width="600"/></p> </details>
<details><summary>booking page with date and time</summary> <p align="left"><img src="./documentation/images/wireframes-booking-date-time.png" alt="wireframes for the booking page with date and time" width="600"/></p> </details>
<details><summary>booking page with personal info</summary> <p align="left"><img src="./documentation/images/wireframes-booking-info.png" alt="wireframes for the booking page with personal info" width="600"/></p> </details>
<details><summary>menu page</summary> <p align="left"><img src="./documentation/images/wireframes-menu.png" alt="wireframes for the menu page" width="600"/></p> </details>
<details><summary>feedback section</summary> <p align="left"><img src="./documentation/images/wireframes-feedback.png" alt="wireframes for the feedback section" width="600"/></p> </details>




### Database Schema

A relational database is used for this project, it is a PostgreSQL provided by Code Institute. <br>Entity relationship diagrams (ERD) are used to plan the SQL tables and relationships, i.e. how tables interact with eachother.

#### Business goals
- The menu is visible on website and can easily be edited.
- Customers can reserve tables if they register an account.
- Customers can make multiple reservations in advance.
- Reservations are limited to 1 per customer per day
- Each table is avalible for booking once per day, rest of the time it is saved for walk-in customers.
- Customers can leave reviews about their experience.
- Staff members can comment on customers reviews.
- A select few customers can recieve a friends and family discount.

#### Progressive data model
A progressive data model is used with three levels of abstraction. <br>These evolving stages bridges the communication gap between buisness people and the technical team.

#### Conceptional
The conceptional ERD is used by business analysts to bind the scope, key entities, and relationships in a way that is easy for the business people to confirm and understand. Business goals are used as guide to create tables at this stage. See image below.

<p align="left"><img src="./documentation/images/entity-relationship-diagram-conceptual.png" alt="Entity relationship diagram" width="700"/></p>

#### Logical
When the conceptional stage is complete and confirmed, the logical ERD evolves the conceptional by going deeper into what each table need and what type of relationships that will be needed. Business analysts provide a simple visual that both business people and the development team can understand. See image below.

<p align="left"><img src="./documentation/images/entity-relationship-diagram-logical.png" alt="Entity relationship diagram" width="700"/></p>

#### Physical
Lastly the development team elaborates upon the logical model with data specifications to transforms it into a blueprint for building and implementing the database. See image below.

<p align="left"><img src="./documentation/images/entity-relationship-diagram-physical.png" alt="Entity relationship diagram" width="700"/></p>


## Agile software development


Scrum, using both incremental and iterative development, was chosen as the main Agile methodology to use in this project. Planning workload into iterations, also known as sprints, with a mindset of "continuous improvement". For each iteration, a kanban board was used to visualize the current workload. Between iterations, remaining workload in the product backlog was reviewed and next iteration was planned.

All features that could possibly be implemented were added as [issues](https://github.com/NiclO1337/pp4-banana-palace/issues) on GitHub.<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)



### Epics

Project was broken down into different epics, large bodies of work, with features that might be included in the project. Each epic in turn is broken into smaller user stories where each user story provides a value to a specified user. User stories were created from both restaurant owner and users of the website.

<details><summary>Screenshot of one of the Epics</summary> <p align="left"><img src="./documentation/images/epic.png" alt="Example of a project Epic" width="600"/></p> </details>


### User stories

All user stories are added as [issues](https://github.com/NiclO1337/pp4-banana-palace/issues) on GitHub. They consist of what value they brings, which acceptence criteria is required for it to be marked as complete and tasks to complete. Some commits were linked to the user story they completed a task for.


<details><summary>Screenshot of example of a user story</summary> <p align="left"><img src="./documentation/images/user-story.png" alt="Example of a project User story" width="600"/></p> </details>

<details><summary>Screenshot of example of user story commits</summary> <p align="left"><img src="./documentation/images/user-story-commits.png" alt="Example of a project User story commit" width="400"/></p> </details>



### Product backlog

All deliverable user stories are added to the product backlog. [GitHub milestone](https://github.com/NiclO1337/pp4-banana-palace/milestone/1) is used as the backlog for this project. They are prioritized, top to bottom, based on what needs their readiness to be completed and what needs to be delivered first. PBI's (product backlog items) are reviewed and re-prioritized between development iterations, also known as backlog refinement.


### MoSCoW prioritization

<p align="left"><img src="./documentation/images/moscow-prioritization.png" alt="MoSCoW prioritization labels" width="800"/></p>

The MoSCoW prioritization was used for this project. While planning each iteration, user stories are divided into categories depending on their importance to the project at this stage in development. Remaining user stories at the end of the iteration are marked as WONT-HAVE for this iteration and returned to the product backlog for review. They can still be developed in future iterations if time permits.

### Iterations

Iteration process were tracked as [GitHub milestones](https://github.com/NiclO1337/pp4-banana-palace/milestones) for this project.

<details><summary>Screenshot of the start of iteration 1</summary> <p align="left"><img src="./documentation/images/iteration-1-start.png" alt="Beginning of iteration 1" width="800"/></p> </details>
<details><summary>Screenshot of the end of iteration 1</summary> <p align="left"><img src="./documentation/images/iteration-1-end.png" alt="end of iteration 1" width="800"/></p> </details>
<details><summary>Screenshot of the start of iteration 2</summary> <p align="left"><img src="./documentation/images/iteration-2-start.png" alt="Beginning of iteration 2" width="800"/></p> </details>
<details><summary>Screenshot of the end of iteration 2</summary> <p align="left"><img src="./documentation/images/iteration-2-end.png" alt="end of iteration 2" width="800"/></p> </details>
<details><summary>Screenshot of the start of iteration 3</summary> <p align="left"><img src="./documentation/images/iteration-3-start.png" alt="Beginning of iteration 3" width="800"/></p> </details>
<details><summary>Screenshot of the end of iteration 3</summary> <p align="left"><img src="TODO" alt="end of iteration 3" width="800"/></p> </details>
<details><summary>Screenshot of the start of iteration 4</summary> <p align="left"><img src="TODO" alt="Beginning of iteration 4" width="800"/></p> </details>
<details><summary>Screenshot of the end of iteration 4</summary> <p align="left"><img src="TODO" alt="end of iteration 4" width="800"/></p> </details>
<details><summary>Screenshot of the start of iteration 5</summary> <p align="left"><img src="TODO" alt="Beginning of iteration 5" width="800"/></p> </details>
<details><summary>Screenshot of the end of iteration 5</summary> <p align="left"><img src="TODO" alt="end of iteration 5" width="800"/></p> </details>


### Kanban board

Github projects was used as a kanban board during development. In each iteration, relevant user stories are moved onto the board and development began. Features were developed to fulfil the acceptence critera's of the user stories.

Link to [Kanban board](https://github.com/users/NiclO1337/projects/3/views/1) used on GitHub.<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)

<p align="left"><img src="./documentation/images/kanban-board.png" alt="Banana palace project board" width="auto"/></p>


[Back to top](#table-of-contents)

## Technologies used

### Languages
- HTML
- CSS
- JavaScript
- Python

### Frameworks
- **Django 5.0.2** as main framework for web development
- **Bootstrap v5.3.2** as framefork for styling and positioning
- **jQuery** for more efficient DOM manipulation


### Libraries
- **Os**, provides functions for interacting with the operating system
- **psycopg2**, PostgreSQL database adapter for the Python programming language
- **dj-database-url**, enables the ability to represent their database settings via a string
- **gunicorn**, handles HTML rendering, authentication, administration, and backend logic
- **whitenoise**, allows web app to serve its own static files
- **Allauth**, dealing with account authentication, registration, management, and third-party (social) account authentication


### Tools
- **Git** for source control
- **GitHub** for storing software project
- **Heroku** for deployment
- **Balsamiq** for all of the wireframes
- **Lucidchart** for ERD (entity relationship diagram)
- **VS Code** as primary IDE during development
- **w3schools** for general information
- **Stack Overflow** for specific issues/errors
- **Looka.com** for the logo and symbol
- **Favicon.io** for the favicon
- **color.adobe.com** to extract color pallet from image
- **Bootstrap Docs** to build page structure and design
- **Bootstrap GitHub page** to check properties of classes [Link to v5.3.2](https://github.com/twbs/bootstrap/blob/v5.3.0/dist/css/bootstrap.css)
- **Django Docs** to build project and apps
- **Grammarly** for spellchecking
- **cdnjs.com** to find relevant CDN fast
- **paint.net** to edit logo, images and favicon
- **phind.com** to search for specific solutions


## Testing

Testing made in separate file [TESTING.md](TESTING.md)

## Deployment

#### Deployment to Heroku

TODO

1. Log in (or sign up) to Heroku. ( https://www.heroku.com/ )
2. From the dashboard, create a "new app" and follow the instructions.
3. When created go to the settings tab.
    - Add a Config Var with PORT as the key and 8000 as value.
    - TODO
4. Go to the deployment tab.
    - Select GitHub as deployment method.
    - Connect app to the correct repository.
5. Choose to deploy either manully or enable automatic deploys.


#### Changes to the code
If changes has been made in local development, the requirements.txt might need to be updated.
- It is done by entering the following command in the terminal: 'pip3 freeze > requirements.txt'
- Updated file must then be commited and pushed to GitHub.

### Local development

#### Forking the project

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Banana Palace](https://github.com/NiclO1337/pp4-banana-palace).
<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)
3. Click the Fork button in the top right corner.

#### Cloning the project

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Banana Palace](https://github.com/NiclO1337/pp4-banana-palace).
<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3.
5. Press enter.

TODO: create env.py
TODO: Optional, create viritual environment.
TODO: install requirements with correct versions


[Back to top](#table-of-contents)

## Credits

### Content

- Design and content inspiration from: [Getbento](https://www.getbento.com/blog/best-restaurant-websites-design/)
and [Limely](https://www.limely.co.uk/blog/top-restaurant-website-designs)

- Footer link idea from above websites, mainly from [dim t](https://dimt.co.uk/book/)

- Hours & location text from [Colletta Atlanta](https://www.collettarestaurant.com/location/colletta-atlanta/)


### Media

- Logo created by AI tool - [Looka.com](https://looka.com/logo-maker/)

- Favicon created from logo with help of [paint.net](https://www.getpaint.net/)

#### Index page
- Photo by [Pierre Blaché](https://www.pexels.com/sv-se/foto/restaurang-solnedgang-hus-manniskor-2901215/)

#### About page
- Photo by [Rene Asmussen](https://www.pexels.com/sv-se/foto/restaurang-hus-bord-arkitektur-1581384/)
- Photo by [Tamas Tuzes-Katai](https://unsplash.com/photos/person-holding-white-iphone-5-c-rEn-AdBr3Ig)
- Photo by [Rachel Claire](https://www.pexels.com/sv-se/foto/mat-restaurang-drycker-stilleben-6127316/)
- Photo by [Pablo Merchán Montes](https://unsplash.com/photos/woman-holding-fork-in-front-table-Orz90t6o0e4)
- Photo by [Lisa Fotios](https://www.pexels.com/sv-se/foto/restaurang-lampor-foretag-interior-776538/)
- Photo by [Rachel Claire](https://www.pexels.com/sv-se/foto/tallrik-restaurang-semester-konst-4577179/)


### Code

- Inspiration from my own previous portfolio projects.
  - HTML/CSS from [Strawberry lovers](https://github.com/NiclO1337/pp1-strawberry-lovers)
  - JS from [RPS Battle Arena](https://github.com/NiclO1337/pp2-playtime)

- Some of the code from the Code Institutes blog walkthrough project was used and adapted.

- Navbar adjusted when scroll down: [w3schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_navbar_shrink_scroll)

- Multiple items per carousel slide from [Hello Mev](https://codepen.io/hellomev/pen/LYORMQW)

- Information on good way to divide up templates and link them - [Stack Overflow answer](https://stackoverflow.com/questions/16498176/is-dividing-a-template-into-parts-and-including-each-part-bad)

- How to animate the navbar toggler from [Clueless Expert](https://www.youtube.com/watch?v=vJ85fm4m7lw)

- How to create entity relationship diagrams from [The Business Analysis Doctor](https://www.youtube.com/watch?v=wMgirP7z4k8&t=2s)

- Django tutorial by [Net Ninja](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)<br>
Outdated content but Shaun is amazing at explaining things.
Specifically used for urls and views.

- Django tutorial by [Hana Belay](https://dev.to/earthcomfy/django-user-profile-3hik)<br>
How to extend user model and update account information.

- Delete account guide by [Cloud With Django](https://www.youtube.com/watch?v=wRFUTDBUgsA)

- Fireworks CSS by [Eddie Lin](https://jsfiddle.net/elin/7m3bL/)

- Insert data in database by [Anjaneyulu Batta](https://learnbatta.com/course/django/insert-data/)

- Loading screen animation by [Tobias Ahlin](https://tobiasahlin.com/spinkit/)


#### Phind.com

After spending too many hours on google trying various outdated or incorrect or incapatible solutions I changed tactic and tested phind.com because of multiple recommendations. Immediatly amazed at the speed and accuracy of search results.

- Better looking datepicker: [Phind search 1](https://www.phind.com/search?cache=q6943vmjbf51bp9848g2hlcb)

- Help with how to get date from datepicker as a variable: [Phind search 2](https://www.phind.com/search?cache=sqrlc22rb0n70z8fbuh61mvs)

- Help with specific server error due to mistake in code: [Phind search 3](https://www.phind.com/search?cache=hlyju3zxzwvjql9yktalgy49)

- Help with adding and styling jQuery datepicker: [Phind search 4](https://www.phind.com/search?cache=ikbfeuzueqibp1far0jj35pt)

- Cascading save from one model to another: [Phind search 5](https://www.phind.com/search?cache=f2dg3carzn3lkulie483rui5)

- Limit avalible dates in datepicker: [Phind search 6](https://www.phind.com/search?cache=abcz5qcai1whrk4z47hjtd7g)


*Message from the developer*:<br>
Phind makes me feel stupid but project deadline is coming fast and I need workable solutions faster so that I can create the best possible project for the product owner and their users.

If online links stops working, results are saved in .txt format [here](https://github.com/NiclO1337/pp4-banana-palace/tree/main/documentation/phind-searches/)


[Back to top](#table-of-contents)