# Big_Data_RealTime_Analytics

## Problem Statement
- Multiple temperature sensors are deployed in each U.S state
- Each sensor regularly sends temperature data to a Kafka server in HortonWorks  (Simulated by feeding 10,000 JSON data by using kafka-console-producer)
- Kafka client retrieves the streaming data every 3 seconds
- PySpark processes and analyzes them in real-time by using Spark Streaming, and show the results

## Key Technologies:
- Apache Spark (Spark Streaming))(PySpark)
- Apache Kafka

##  Analysis of data
Achieved 4 types of real-time analysis. 
- Average temperature by each state (Values sorted in descending order)
- Total messages processed
- Number of sensors by each state (Keys sorted in ascending order)
- Total number of sensors
## Format of sensor data

I used the simulated data for this project. ```iotsimulator.py``` generates JSON data as below format.

```
<Example>

{
    "guid": "0-ZZZ12345678-08K",#sensor id
    "destination": "0-AAA12345678",#destination id
    "state": "CA", #US State name code
    "eventTime": "2016-11-16T13:26:39.447974Z", 
    "payload": {
        "format": "urn:example:sensor:temp", 
        "data":{
            "temperature": 59.7
        }
    }
} 
```
Field | Description
---   | ---
guid | A global unique identifier which is associated with a sensor.   
destination | An identifier of the destination which sensors send data to (One single fixed ID is used in this project)
state | A randomly chosen U.S state. A same guid always has a same state
eventTime | A timestamp that the data is generated
format | A format of data
temperature | Calculated by continuously adding a random number (between -1.0 to 1.0) to each state's average annual temperature everytime when the data is generated.  https://www.currentresults.com/Weather/US/average-annual-state-temperatures.php





![image](https://user-images.githubusercontent.com/66690240/156993717-6ac69187-e880-4d9b-88ac-8c77a75718ea.png)

