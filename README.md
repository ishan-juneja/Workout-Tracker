# Workout-Tracker
This program tracks your workouts and calories exhurted in a spreadsheet for you!

## Structure
- `main.py` behaves as the nucleus and runs the entirety of the program
  
## Dependencies & Configurations
1. The [Sheety API](https://sheety.co/) used for storing our workouts and calories in a spreadsheet
   - Retrieve **Username** & **Password** once you create your account
   - Create 1 spreadsheet with 5 columns: 
   - Add all info to `main.py`
2. The [Nutritionix API](https://www.nutritionix.com/business/api?creative=344317953788&keyword=food%20nutrition%20api&matchtype=b&network=g&device=c&utm_source=google&utm_medium=cpc&utm_campaign=NutritionAPI&gclid=CjwKCAjwqZSlBhBwEiwAfoZUIJi80pQdUX5AeV4ksIeoGRxNr2l_yxtfqP7Xb2OQ56DwhtrGWDArAhoCZYQQAvD_BwE) to use NLP to break down our user input and retrieve how many calories the excercise is worth.
   - Retrieve your **NUTRI_APP_ID** & **NUTRI_API_KEY** once you create your account
   - Add to `main.py`

## Demo
The program inquires what excercises you did in the day
<img width="546" alt="Screenshot 2023-07-05 at 9 18 14 AM" src="https://github.com/ishan-juneja/Workout-Tracker/assets/69048541/dbce71bf-73b9-46eb-9deb-d93ed9817f8d">

After entering, the data is then transferred to our linked spreadsheet
![Screenshot 2023-07-05 at 9 18 47 AM](https://github.com/ishan-juneja/Workout-Tracker/assets/69048541/a0a27cab-2b4e-4c2f-9f82-3d9622578048)
