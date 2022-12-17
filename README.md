# project-of-the-week-2022

This repository contains of an API that serves a Machine Learning model using FastAPI. It was created as part of [Project of the Week at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week)

The goal of this project is to predict the used car price and to apply FastAPI deployment.

[100,000 UK Used Car Dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes)

100,000 scraped used car listings, cleaned and split into car make.

![image](https://user-images.githubusercontent.com/82657966/208224757-0e7681c2-c59b-4320-878e-878c268b6e67.png)

## About Dataset
If you download/use the data set I'd appreciate an up vote, cheers.

## Updated
Scraped data of used cars listings. 100,000 listings, which have been separated into files corresponding to each car manufacturer. I collected the data to make a tool to predict how much my friend should sell his old car for compared to other stuff on the market, and then just extended the data set. Then made a more general car value regression model.

## previous version

Picked two fairly common cars on the British market for analysis (Ford Focus and Mercedes C Class). The hope is to find info such as: when is the ideal time to sell certain cars (i.e. at what age and mileage are there significant drops in resale value). Also can make comparisons between the two, and make a classifier for a ford or Mercedes car. Can easily add more makes and models, so comment for any request e.g. if you want a big data set of all Mercedes makes and models.

## Content
The cleaned data set contains information of price, transmission, mileage, fuel type, road tax, miles per gallon (mpg), and engine size. I've removed duplicate listings and cleaned the columns, but have included a notebook showing the process and the original data for anyone who wants to check/improve my work.

## Running the API

Activate the my environment:

   ```
   my env
   ```

## Requirements

Python 3.7+

FastAPI stands on the shoulders of giants:

* [Starlette](https://www.starlette.io/) for the web parts.
* [Pydantic](https://pydantic-docs.helpmanual.io/) for the data parts.

## Installation:

First
```
pip install fastapi
```
Second
```
pip install "uvicorn[standard]"
```
Create a file main.py then run it with:

```
uvicorn main:app --reload
```
Interactive API docs

```
http://127.0.0.1:8000/docs
```

### Running the API using Docker

Before running the API with Docker, make sure that you install it following these [steps](https://docs.docker.com/get-docker/).

To run the API using Docker:

1. Build the Docker image:

   ```
   docker build -t fastapi-used-car-price-pred . 
   ```

2. Run the API:

   ```
   docker run -p 8000:8000 fastapi-used-car-price-pred
   ```
   
