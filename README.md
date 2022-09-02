
# 🏃Workout Tracker

This web app helps you to keep all our workout vidoes organised. You can add or delete vidoes at your wish. The vidoes that you add will be stored to the [HarperDB](https://harperdb.io/). This app will also recommed the workout video everyday. 


## 🪛Installation

How to run project:

```
https://github.com/vishalsingh17/FitnessVideoApp
```
```
cd FitnessVideoApp
```
```
conda create -p venv python==3.10.4
```
```
conda activate ./venv
```
```
pip install -r requirements.txt
```
```
streamlit run app.py
```
## 👨‍💻Tech Stack

**Client:** Streamlit, Python

**Server:** HarperDB


## 🕵️‍♂️Environment Variables

To run this project, you will need to add the following environment variables to your config.py file

`HARPERDB_USERNAME` = "YOUR  HARPERDB USERNAME"

`HARPERDB_PASSWORD`= "YOUR HARPERDB PASSWORD"

NOTE - Store your API key and SECRET key in your environment variable for eshtablishing secure connections.



## ✍🏻Acknowledgements

 - [Get Binance API](https://www.binance.com/en/support/faq/360002502072)
 - [TA-LIB Github](https://github.com/mrjbq7/ta-lib)
 - [KLine Github](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#klinecandlestick-data)


## 🎯App Screenshots

![image](https://user-images.githubusercontent.com/55878408/188103624-255b7bf9-c64a-454b-b5db-192e5fd70240.png)

![image](https://user-images.githubusercontent.com/55878408/188103798-1ffcd3dd-b4dc-461c-a73e-6588a3abedb2.png)

![image](https://user-images.githubusercontent.com/55878408/188103906-c9b3dee5-1077-41f6-aebd-32b174d76014.png)