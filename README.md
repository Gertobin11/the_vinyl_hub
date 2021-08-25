# The Vinyl Hub

## Table of Contents

## Project Overview
The Vinyl Hub is an e-commerce site selling classic vinyls, audio accessories and record players.
It aims to build a customer base by providing high quality products and also developing a community,
by allowing registered user a way to interact and show their vinyl collections by filling out a profile form.
Registered users would also have the ability to request albums that could be added to the store.


### User Stories 
I built my user stories in an agile framework where I built upon the foundations laid in 
the code institue's Boutique Ado project and tailored them to the needs of my projects users and store owner.
The table below are the stories upon which this project was built

## UX

### Design Choices 

The overall structure of the site is based off bootstrap 5's row and column classes.
The colours and overall theme of the site is based off a vibrant 80's colour pallette, i.e. MTV'S 80's logo.

![80s brand inspiration](media/1980s-brand-inspiration_1_400x400.png)

From these images I decided on `#fcb014`, `#c01b21`and `#018bd4` as this would have the feel and style from the 80's,
a time when Vinyls were at their peak. Due to accessability reasons I had to alter the blue to `#047ab7` for greater contrast for the users.

![colour pallette](media/mtv-80s-color-scheme_400x400.png)

![update color pallette](media/new_color_palette.png)





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

## Credits 

* The images for the record players and the description were taken from https://www.worldwidestereo.com/blogs/wws-underground/entries/best-turntables.
* The images for the vinyls and the descriptions were taken from https://longlivevinyl.net/2020/02/18/the-essential-hiphop/ and https://www.radiox.co.uk/features/best-vinyl-records-to-collect/