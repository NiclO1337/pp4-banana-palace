# <img src="./static/images/banana-palace-symbol.png" alt="Banana Palace restaurant logo" width="25"/> Banana Palace restaurant

![Amiresponsive image](./documentation/images/amiresponsive.png)

Link to live website: [Banana Palace](https://banana-palace-9ad263ab8cf3.herokuapp.com/) <br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)


## Table of contents

* [Automatic testing](#automatic-testing)
    * [Code validators](#code-validators)
    * [Lighthouse testing](#lighthouse-testing)
        * [Improvements](#improvements)
        * [Left to improve](#left-to-improve)
    * [Wave](#wave-testing)
        * [Improvements](#improvements-1)
        * [Left to improve](#left-to-improve-1)
* [Manual testing](#manual-testing)
    * [User story testing](#user-story-testing)
    * [Features](#features)
    * [Browser](#browser)
    * [Devices](#devices)
* [Bugs](#bugs)
    * [Solved bugs](#solved-bugs)
    * [Unfixed bugs](#unfixed-bugs)


## Automatic testing

### Code validators

**HTML** validated through [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). <br>Some errors related to automatically created Django forms has been found but all custom written code passes the tests.
<br>![Passed without errors](https://res.cloudinary.com/dmntcacug/image/upload/v1693510294/html-validator-pass_lwfaja.jpg)

**CSS** validated through [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator) and returns 1 error and 22 warnings.
<br>![Passed without errors](./documentation/images/css-error.jpg)

Validator is not able to parse this CSS selector because it checks for CSS level 3 and this selector uses modern CSS level 4 which has not yet been implemented. The warnings are due to the use of CSS variables. These are ignored because this CSS targetting works as intended in all browser testing.

TODO: Update after browser testing if problems occur

All other CSS styles passed without errors
<br>![Passed without errors](https://res.cloudinary.com/dmntcacug/image/upload/v1693422108/css-validator-pass_xthpbi.jpg)


**JavaScript** checked with [JSHint](https://jshint.com/) to test for errors and potential problems.<br>
Script files has no warnings or errors.
<br>(*Uses ES6 features and jQuery which needs to be enabled in the configuration*).

- **Python**
All code validated through [PEP8 validator](https://pep8ci.herokuapp.com/) and TODO


### Lighthouse testing

Used lighthouse to test performance, accessibility, best practices, and search engine optimization of the website.

Result after optimization
<p align="left"><img src="TODO" alt="Result after optimization" width="250"/></p>

#### Improvements
-
-

#### Left to improve
-
-

### Wave testing

TODO


#### Improvements
-
-

#### Left to improve
-
-


[Back to top](#table-of-contents)

## Manual testing

### User story testing

| User story | How are they achived |
| --- | --- |
| **EPIC Create website** |
| #6 As an owner I want to have website so that our restaurant has a stronger online presence and can attract more customers | To enhance the online presence of the restaurant and attract a wider customer base, I set out to design and implement a user-friendly website. Understanding the importance of a strong digital footprint, I embarked on a comprehensive process that began with thorough research into our business requirements and target audience preferences. |
| #7 As an owner I want to show our contact details so that customers can contact us for queries | To ensure easy access for customers seeking to contact us, I strategically placed our contact details in multiple prominent locations across the website. By integrating this information seamlessly into the design, I guarantee that visitors can quickly locate our contact information whenever they have inquiries or feedback.  |
| #8 As an owner I want display our address so that customer can find our location easily | To facilitate customers in finding our location effortlessly, these were also incorporated into various prominent sections. This enhances the user experience and enables visitors to locate our establishment with ease.
| #9 As an owner I want it to be easy to find the website on search engines so that anyone can find us and we get more business | To enhance the website's visibility on search engines and attract more potential customers, I focused on optimizing its search engine ranking. Implementing an effective SEO strategy, meta tags were added to all pages and employed semantic HTML techniques. |
| #10 As an owner I want to make sure the website is a good user experience so that customers enjoy their visit and wants to return | By implementing clear navigation pathways, I ensured that users can easily explore the site and find the information they need. Additionally, visual feedback mechanisms were incorporated to confirm users' actions, enhancing their interaction with the website. |
| #31 As an owner I want to have an about page so that so that customers can learn about our restaurant | To meet the owner's request for an about page that provides customers with insights into the restaurant, two distinct pages were added. The first page offers essential details such as contact information, location, and operating hours, ensuring easy access to key information for visitors. The second page delves into the restaurant's unique story, origin, and inspiration, providing a deeper understanding of its background and values.  |
| #32 As an owner I want to have custom error pages so that so that customers do not leave our website if an error occurs | To prevent customer departures during errors, we've added custom error pages (400, 403, 404, 500) with consistent design, including header and footer. These pages also feature a prominent button for quick return to the homepage. |
| #42 As an owner I want to show images of our menu items in a stylish way so that customers will get peckish when they visit the website | To entice customers and stimulate their appetite upon visiting the website, images of signature dishes have been incorporated into a sleek carousel on the landing page. |
| #11 As a user I want to visit the restaurants website so that I can see if I am interested in going there | To cater to users' desire to explore the restaurant's offerings and gauge their interest in visiting, the website has been designed with a focus on intuitive navigation and captivating content. By prioritizing ease of use and implementing engaging elements, such as vivid imagery and fun features, the website aims to pique users' curiosity and encourage them to consider a visit to the restaurant. |
| #12 As a user I want the website to have a familiar design so that it is intuitive for me to navigate and it is easy to use | To ensure a seamless user experience, the website's design was crafted with familiarity in mind. Drawing inspiration from established conventions in restaurant website layouts, extensive research was conducted to identify common practices.  |
| **EPIC Sign in feature** |
| #15 As an owner I want users to be able to delete their account and information so that we are in compliance with GDPR regulations | To align with GDPR regulations full CRUD functionality has been implemented for user accounts. This enables users to easily manage their personal information, including the option to delete their account and associated data as desired. |
| #16 As an owner I want to be able to give some user accounts special discounts so that my friends and family can get better price directly when booking online | To facilitate the owner's ability to offer special discounts to selected user accounts, the application has been configured to grant the owner exclusive permissions accessible from both the frontend and backend. |
| #40 As an owner I want to be able to see a list of all current users so that I can find their information and grant some people special "friends and family" discount | To fulfill the owner's request for visibility into all current users and the ability to grant special "friends and family" discount, a custom account page has been added specifically for the owner's access. This dedicated page allows the owner to conveniently view information about all users and easily select individuals to receive the a special discount. |
| #17 As a user I want to be able to sign in with password so that my account is secure | To ensure user account security, the system has been equipped with password-protected sign-in functionality. Users can create accounts secured by passwords, with their information stored using industry-standard encryption methods.  |
| #19 As a user I want to be able to update my personal information so that it can always be accurate when I make my bookings | To enable users to maintain accurate personal information for their bookings, an edit button has been added to the account page. This feature empowers users to conveniently update their account details, ensuring that their information remains current and relevant |
| #20 As a user I want to be able to delete my account so that so that I can keep my personal information secure by not sharing it anymore| To empower users to maintain control over their personal information and ensure their privacy, full CRUD (Create, Read, Update, Delete) permissions have been granted on their own accounts. This enables users to easily delete their accounts if they wish, thereby discontinuing the sharing of their personal information and enhancing their data security. By providing this level of autonomy, the system prioritizes user privacy and trust. |
| #21 As a user I want to be able to reset my password so that I can access my account even if I forget my password | To facilitate seamless access to user accounts, an option to reset passwords has been enabled. This functionality allows users to easily regain access to their accounts in the event of forgotten passwords, ensuring uninterrupted use of the platform. |
| **EPIC Reserve a table** |
| #22 As an owner I want users to be able to book a table online so that it reduces our administration costs for handling bookings | To streamline the booking process and reduce administration costs associated with handling reservations, a reservation page has been added to the website. This page allows users to conveniently book a table for a specified date and time without the need to contact the restaurant directly. |
| #23 As an owner I want to be able to see all current bookings so that we can plan ahead regarding space, table placements and purchasing raw materials | To facilitate effective planning for space, table placements, and purchasing of raw materials, a feature has been implemented allowing restaurant staff members to access all current bookings. This functionality is integrated into the reservation page, presenting a list of reservations for the selected date exclusively to authorized staff members. |
| #24 As a user I want to be able to book a table online so that booking will be easier and faster than with phone or email | To enhance the booking experience for users, an online reservation feature has been implemented with a focus on being fun, fast, and user-friendly. This feature enables users to easily book tables online, offering a seamless and efficient alternative to traditional phone or email reservations. |
| #25 As a user I want to be able to see all my bookings so that I can be reminded of when I made the reservations for | To facilitate users in keeping track of their reservations, all current bookings are now conveniently displayed on the account page. This feature ensures that users can easily access and review their reservations, providing a helpful reminder of when the bookings were made. |
| #26 As a user I want to be able to edit my current bookings so that I can I can have flexibility incase my schedule changes | To accommodate users' changing schedules and provide flexibility, an edit button has been added along with functionality allowing users to modify their reservations. This feature empowers users to easily adjust booking details as needed, ensuring that their reservations align with their updated schedules. |
| #27 As a user I want to be able to delete my booking so that I can let the restaurant know in advance that I changed my mind and want to cancel | To accommodate users who need to cancel their reservations, a delete button has been incorporated along with functionality allowing users to delete their bookings. To prevent accidental deletions, defensive design measures have been implemented. |
| **EPIC Menu** |
| #29 As an owner I want to show our current menu online so that we can attract customers and increace efficiency by reducing the time it takes users to decide what to eat | To showcase our offerings and improve efficiency in decision-making for users, a dedicated menu page has been added. This page displays all current menu items, allowing customers to easily browse and select their preferred dishes. |
| #30 As an owner I want be able to edit our menu online so that it is easy to keep it current and updated | To ensure the menu remains current and updated, restaurant staff members have been enabled to add new menu items and edit existing ones online. Additionally, the owner has been granted full CRUD permissions over menu items, allowing for seamless management and updates. |
| #41 As a user I want to look at the restaurants menu so that I can see if I am interested in going there | To assist users in evaluating their interest in visiting the restaurant, the website now features a dedicated menu section. Additionally, pictures of signature dishes have been added to the landing page, providing users with a visual preview of the restaurant's offerings. |

### Features

| Feature tested | Expected outcome | Testing Performed | Result | Pass / Fail |
| --- | --- | --- | --- | --- |
| **Header / navigation bar** |
| Logo | Clicking takes the user to the home page | Clicked Banana Palace logo | If on index page, page is reloaded, else redirected to index page | Pass |
| Menu | Clicking takes the user to the menu page | Clicked link "Menu" | Takes user to menu page | Pass |
| Hours & Location | Clicking takes the user to the Hours & Location page | Clicked link "Hours & Location" | Takes user to Hours & Location page | Pass |
| Our story | Clicking takes the user to the story page | Clicked link "Our story" | Takes the user to the story page | Pass |
| Login/register | Clicking takes the user to the sign in page | Clicked link "Login/register" | Takes the user to the sign in page | Pass |
| Account/logout | Clicking takes the user to the account page | Clicked link "Account/logout" | Takes the user to the account page  | Pass |
| Book a table | Clicking takes the user to the reservation page | Clicked button | Takes the user to the reservation page | Pass |
| **Index page** |
| Scrolltop down | Scrolling down from top of index page shows smooth animation and change positions of navbar, logo and removes address and phone number | Scroll down from the top of index page | Smooth animation and elements changes positions as expexted | Pass |
| Scrolltop up to the top of index page | Scrolling up to top of index page shows smooth animation and reverts back to initial view | Scroll up to top | Smooth animation and elements changes positions as expexted | Pass |
| Carousel right | Clicking on right button shows the next menu item that is to the right of the current view | Click on right button | All images are shifted left and the next image to the right is visible | Pass |
| Carousel left | Clicking on left button shows the next menu item that is to the left of the current view | Click on left button | All images are shifted right and the next image to the left is visible | Pass |
| **Footer / Social media icons** |
| Facebook | Clicking opens Facebook in a separate tab | Clicked link "Facebook icon" |  Facebook opens in a separate tab | Pass |
| Twitter | Clicking opens Twitter in a separate tab | Clicked link "X icon" |  Twitter opens in a separate tab | Pass |
| Instagram | Clicking opens Instagram in a separate tab | Clicked link "Instagram icon" |  Instagram opens in a separate tab | Pass |
| YouTube | Clicking opens YouTube in a separate tab | Clicked link "YouTube icon" | YouTube opens in a separate tab | Pass |
| **Footer / company information links** |
| Home | Clicking takes the user to the home page | Clicked link "Home" | Takes the user to the home page | Pass |
| Allergens | Clicking takes the user to the allergens page | Clicked link "Allergens" | Takes the user to the allergens page | Pass |
| Careers | Clicking takes the user to the careers page | Clicked link "Careers" | Takes the user to the careers page | Pass |
| Contact | Clicking takes the user to the Hours & Location page | Clicked link "Contact" | Takes the user to the Hours & Location page | Pass |
| Terms & Conditions | Clicking takes the user to the terms & conditions page | Clicked link "Terms & Conditions" | Takes the user to the terms & conditions page | Pass |
| Privacy Policy | Clicking takes the user to the privacy policy page | Clicked link "Privacy Policy" | Takes the user to the privacy policy page | Pass |
| Cookie Policy | Clicking takes the user to the cookie policy page | Clicked link "Cookie Policy" | Takes the user to the cookie policy page | Pass |
| Modern Slavery Statement | Clicking takes the user to the modern slavery statement page | Clicked link "Modern Slavery Statement" | Takes the user to the modern slavery statement page | Pass |
| Gender Pay Gap | Clicking takes the user to the gender pay gap page | Clicked link "Gender Pay Gap" | Takes the user to the gender pay gap page | Pass |
| Animal Welfare | Clicking takes the user to the animal welfare page | Clicked link "Animal Welfare" | Takes the user to the animal welfare page | Pass |
| Investor Relations | Clicking takes the user to the investor relations page | Clicked link "Investor Relations" | Takes the user to the investor relations page | Pass |
| **Menu** |
| View menu | When navigating the the menu page, the menu is displayed | Navigate to menu and wait | Menu page is loaded and menu is visible | Pass |
| Add menu item | If logged in user has permission (staff), they are able to add new menu items | Log in with correct permissions and add new item | Add menu page opens and able to add new item | Pass |
| Edit menu item | If logged in user has permission (staff), they are able to edit current menu items | Log in with correct permissions and edit an item | Edit item page opens and can edit the item | Pass |
| Delete menu item | If logged in user has permission (owner), they are able to delete current menu items | Log in with correct permissions and delete item | Delete confirmation page with warning opens and deletion must be confirmed | Pass |
| **Account management** |
| Sign up  | New visitors are able to sign up to website | Click on login/register and then on sign up and enter required information | Able to sign up and it sais confirmation email is sent | Pass |
| Verify email address  | When clicking on verification link in email, should be directed to confirm email page and get verified | Click on email link | Got directed to confirm email page and clicked confirm | Pass |
| Sign in | Able to log in and redirected to account page | Sign in with valid log in credentials | Newly created and confirmed account worked and was redirected to account page | Pass |
| Sign out | Can log out form the account | Navigate to account page and click logout | Redirected to logout confirmation page where logout needs to be confirmed | Pass |
| Reset password | Able to reset password if needed | Clicking on "Forgot your password?" link | Redirected to password reset page, enter email address, got email, click link and got directed to change password page, enter new password, password successfully changed | Pass |
| Edit account | Can change personal details on the account | Edit personal details | New information is saved and displayed on account page | Pass |
| Change password | Able to change the password on the account | Change password on edit account page | Password successfully changed | Pass |
| Delete account | Can delete account and personal information | Click on delete account on account page | Delete confirmation page with warning opens and deletion must be confirmed, once confirmed directed to home page | Pass |
| **Make reservation** |
| Choose date | Choosing a date shows available tables on that date | Choose a date in the datepicker | Animated loading icon is shown and then new date is displayed and same tables are not reserved on this day | Pass |
| Choose table | Clicking on an available table takes user to the next page where reservation can be completed | Click a table that is available | Directed to the reserve table page where details are entered | Pass |
| Prepopulated form | When creating a reservation, the form should be prepopulated with users information | Select a table to get to reserve table screen | Form is prepopulated with users personal information | Pass |
| Terms & Conditions | Clicking takes the user to the terms & conditions page so they can read it before accepting | Click on Terms & Conditions link | Directed to terms & condition page | Pass |
| Previous page | Clicking takes the user back to previous page and can continue with reservation | Click on previous page button | Returned to reserve table page and can continue with current booking | Pass |
| Make reservation | Filling out all fields and clicking reserve table confirms the reservation | Fill out information and click reserve table | Reservation completed successfully and reservation is displayed on account page | Pass |
| Reserved table | After a table is reserved it should not be possible to select that table anymore | Make a reservation and remember which table was chosen, then go back to reservation page and look | Table is no longer available | Pass |
| Edit information | When editing user details on a reservation, the new details are saved on the account | Edit user information on reservation and confirm changes | New updated information is shown on the account page | Pass |
| Prepopulated form | When editing a reservation, the form should be prepopulated with reservation information | Edit a reservation, select a table to get to reserve table screen | Reservation details are automatically added to the edit form | Pass |
| Edit reservation | When editing the reservation, the chosen table becomes available again and user can change all details | Remember which table was reserved and click on edit reservation and look | Same table is available when clicking edit reservation | Pass |
| Delete reservation | When deleting the reservation, the reservation is removed from users account page and the table becomes available again | Remember which table was reserved, delete reservation and go back to reservation page and look | Directs to a delete confirmation page where deletion must be confirmed, once confirmed directed back to account page and reservation is not shown anymore, table is available again | Pass |
| Delete account | When deleting user account the table becomes available again | Remember which table was reserved, delete account and go back to reservation page and look | Table is still marked as reserved | Fail |
| **Hover effects** |
| Header links | Hover effect shows as intented on mouseover | Mouseover element | Hover effect is shown | Pass |
| Header logo | Hover effect shows as intented on mouseover | Mouseover element | Hover effect is shown | Pass |
| Buttons | Hover effect shows as intented on mouseover | Mouseover element | Hover effect is shown | Pass |
| Input fields | Hover effect shows as intented on mouseover | Mouseover element | Hover effect is shown | Pass |
| Tables on reservation page | Hover effect shows as intented on mouseover | Mouseover element | Hover effect is shown | Pass |
| Footer links and icons | Hover effect shows as intented on mouseover | Mouseover element | Hover effect is shown | Pass |
| **Form validation** |
| Enter valid information | Form submits without problems and redirects to next page | Enter valid information and submit | Entered information is accepted and shown | Pass |
| Enter invalid information | It is not possible to submit form and error messages show informing about what is wrong | Enter invalid information and submit | Field with invalid information became red and information about needs to be entered is displayed | Pass |
| Leave fields empty | Error message displays about missing information | Submit form without information | Error message with exclamation mark shows and says "Please fill out this field." | Pass |
| Enter blank spaces | Error message displays that field is required | Submit form with blank spaces | Field with blanks became red and information about that field is required is showing | Pass |
| **Security** |
| Change another users account details | Should not be possible to attempt | Try accessing with URLs | Not possible, url is always same for every account | Pass |
| Delete another users account | Should not be possible to attempt | Try accessing with URLs | Not possible, url is always same for every account  | Pass |
| Double book a table | When trying to make a reservation on reserved table, error is shown | Look with dev tools to see ID of tables, click on table and change URL to one that is reserved | Error message is shown when trying to confirm reservation | Pass |
| Change another users reservation details | Error message displaying that user does not have permission to edit this reservation | Try accessing with URLs | Error message is displayed and it is not possible to change reservation | Pass |
| Delete another users reservation | Error message displaying that user does not have permission to delete this reservation | Try accessing with URLs | Error message is displayed and it is not possible to delete reservation | Pass |
| Change a menu item without permission | User is not able to change menu items without correct permission | Try accessing with URLs | Try and access /menu/add/ but it is a blank page | Pass |
| Delete a menu item without permission | Error message displaying that user does not have permission to delete this menu item | Try accessing with URLs | Accessing /menu/delete/10 successfully but when clicking delete an error is shown | Pass |
| **CSS Error / warning** |
| CSS validation error | Can see the CSS as intended even though validator flags it as error | Look at affected areas | See that CSS works as intended | Pass |
| CSS validation warnings | All styles with CSS variables looks as intended | Look at affected areas | See that the CSS variables works | Pass |



### Browser
Each website [feature](#features) has been tested on Google Chrome, Microsoft Edge, Firefox, and Samsung Internet Browser.

| Feature tested \  On browser | Google Chrome | Microsoft Edge | Firefox | Samsung Internet  |
| --- | --- | --- | --- | --- |
| Works as intended | Yes | Yes | Yes | Yes |

Note: Hover effects were not tested on Samsung internet because a tablet was used.


### Devices
Manually tested on mobile device (Xiaomi 12), tablet (Samsung Galaxy tab S4) laptop, and desktop computer.

| Devices | Expected outcome / responsive | Pass / fail |
| --- | --- | --- |
| Mobile (Xiaomi 12) | Looks as intended on this small screen size | Pass |
| Tablet (Galaxy tab S4) | Looks as intended on this screen size | Pass |
| Laptop (1366x768px) | Looks as intended on medium size screen | Pass |
| Desktop (1920x1080px) | Looks as intended on big size screen | Pass |

Notes:
All testing was made on up-to-date browsers.
The desktop computer also tested with Chrome developer tools from 280px wide screen up to 2560px.

Note: Datepicker on reservation does not look good on Galaxy fold (unfolded) 280px width. Problem ignored since it is functional on Galaxy fold with a sideways scrollbar and that model can be opened to be viewed larger. Problem does not exist on screenwidth 300px and above.


## Bugs

### Solved bugs

A large number of bugs was accidentally created during development and had to be fixed.
Fixes included:
- looking through code line by line
- using print() and console.log() statements to see what was going on
- put python variables into the HTML pages and show the content on the page to see what variable contains
- review commit history
- search google and phind for possible solutions
- a lot of trial and error

Noteworthy bugs are added as [issues](https://github.com/NiclO1337/pp4-banana-palace/issues?q=is%3Aopen+is%3Aissue+label%3Abug) on GitHub and placed on the Kanban board as high priority.


### Unfixed bugs

Bugs that remain after project deadline for release are currently labelled as [wont-fix-yet](https://github.com/NiclO1337/pp4-banana-palace/issues?q=is%3Aopen+is%3Aissue+label%3A%22wont+fix+yet%22) on GitHub issues page.