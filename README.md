## Studying and analysing the Indian Domestic Flight Market
I have been collecting data for Flight fare for Indian domestic flight carrier from 7-Aug-2019.
I have created a python script which makes an api call and stores the data in a csv file.The file has been Scheduled on my Computer,i.e. the scripts runs automatically at specified time to collect the data.
I have started with 4 routes with Origin of the flight being Delhi(DEL) in each case and Destination are based on Airport category
The Airport category are based on the traffic handled by the airport.
the four routes are:
<ul>
  <li>DELHI-MUMBAI(BOM) {both Cat 1}
  <li>DELHI-HYDERABAD(HYD) {Hyd being Cat2}
  <li>DELHI-PUNE(PNQ) {Pune being Cat3}
  <li>DELHI-NAGPUR(NAG){Nagpur being Cat4}
</ul>
<br><hr>

## Why these routes?
There are alot of airports in each of the category,but I selected these routes because the distance and flight duration(non stop) of these cities from Delhi is almost similar.
<br>
I have been analysing these data and plan to make a ML model which will be able to predict the price of the flight fare with given parameters.
The parameters will be decided based on the data analysis.
<hr>
You can find the Python Script that is being used to extract the data in this Repository.
Open to any further suggestion or improvement.
thanks :)
<hr>

# Flight Fare Prediction Demo Model
A simple flight fare prediction model for INDIGO.

## https://indigoflight.herokuapp.com/
