# Weather Reporter Application

A simple Python-based command-line application that fetches real-time weather data for any city using the OpenWeatherMap API.

---

## Features

* Get weather details for any city
* Displays temperature in Celsius
* Shows humidity levels
* Displays wind speed
* Weather condition description
* Continuous input until user exits
* Error handling for invalid cities

---

## Technologies Used

* Python 3
* Requests Library
* OpenWeatherMap API

---

## Project Structure

```
weather-reporter/
│
├── weather.py        # Main Python script
├── README.md         # Project documentation
├── Project Report Fundamentals in AI ML.pdf         # Project Report
```

---

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/weather-reporter.git
cd weather-reporter
```

### 2. Install Required Library

```
pip install requests
```

### 3. Get API Key

* Go to https://openweathermap.org/
* Sign up and generate your API key

### 4. Add API Key

Replace this line in the code:

```
MY_API_KEY = '444eb7828a7aa2f78008631c86136049'
```

---

## ▶️ How to Run

```
python weather.py
```

---

## Usage

* Enter the city name when prompted
* Type `exit` to close the program

---

## Sample Output

```
Welcome to the Weather Reporter

Enter city name: Delhi

--- Current Weather in Delhi ---
Temperature: 30°C
Condition: Clear sky
Humidity: 45%
Wind Speed: 3 m/s
------------------------------
```

---

## Error Handling

* Invalid city name → Shows error message
* Network issues → Displays exception message

---

## Future Improvements

* GUI version using Tkinter
* Weather forecast feature
* Auto-detect location
* Mobile app version

---

## Contributing

Feel free to fork this repository and improve the project.

---

## License

This project is open-source and available under the MIT License.

---

## Author

Name: Vaibhav Naikwade   
Registration Number: 25BAI10507    
Subject: Fundamentals in AI ML

---
