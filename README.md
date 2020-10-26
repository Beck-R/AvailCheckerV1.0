!!!PLEASE NOTE THAT I AM NOT AN EXPERIENCED PROGRAMMER
THIS IS MY FIRST MAJOR PROJECT THAT I HAVE BEEN WORKING ON!!!

*ALL SOFTWARE/PROGRAMS ARE MEANT TO BE OPEN-SOURCE AND FREE, HOWEVER PLEASE
DO NOT ATTEMPT TO MAKE ANY PROFIT OFF OF THIS, PERSONAL USE IS FINE THOUGH.
I AM NOT LIABLE*

AUTHORS:
Beck-R

THANKS:
people who made listed modules
bs4
playsound
win10toast
colorama


CHANGELOG:
Version 1.0 | Currently there is a dormant function autoBuy() and it is possible I wont implement
or at least not for a while  


INSTALL/USAGE:
(change variables at user discretion)
For general use and adaptation for any website the first thing you need to do is change
the fe_url variable to a string of whatever website you want to scrape. then you want
to change the headers variable to the user agent of your current browser. Then you want
to change the variable username to the gmail you want to get emails to.
Then change the vtext variable to the phone number you want to recieve sms messages to
(the format should be along the lines of 111-222-3333@CarrierEmailHere.com.
Next you want to change the body variable in both sms and sms2 function to whatever you want
your phone to recieve. Same goes for send_mail function. Then change the fe_avail variable to
whatever the name and class of the add to cart or sold-out label is on the webpage you want to scrape.
Finally change the if statements to check the availability of the product you want ie. Add to Cart or 
Sold Out


BUGS:
no currently known bugs
