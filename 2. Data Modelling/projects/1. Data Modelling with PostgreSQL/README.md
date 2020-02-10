# Project: Data Modeling with Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

This project is meant to create a relational database and an ETL pipeline to load the data from aforementioned JSON files and prepare it for analysis.

## Database Structure

### Fact Table

1. **songplays** - records in log data associated with song plays i.e. records with page `NextSong`
    - songplay_id
    - start_time
    - user_id
    - level
    - song_id
    - artist_id
    - session_id
    - location
    - user_agent

### Dimension Tables

1. **users** - users in the app
    - user_id
    - first_name
    - last_name
    - gender
    - level
2. **songs** - songs in music database
    - song_id
    - title
    - artist_id
    - year
    - duration
3. **artists** - artists in music database
    - artist_id
    - name
    - location
    - latitude
    - longitude
4. **time** - timestamps of records in songplays broken down into specific units
    - start_time
    - hour
    - day
    - week
    - month
    - year
    - weekday

## Project Structure

In addition to the data files, the project workspace includes six files:

- `test.ipynb` displays the first few rows of each table to let you check your database.
- create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
- `etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- `etl.py` reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
- `sql_queries.py` contains all your sql queries, and is imported into the last three files above.
- `README.md` provides discussion on your project.

## Running the Pipeline

Before you start, you'll want a running PostgreSQL instance you have permissions to create databases in. Please see/modify the connection string in `etl.py` and `create_tables.py` files.

Then you'll need to run `$ python3 create_tables.py` to create the database and tables.

Then you'll need to run `$ python3 etl.py` to read the log files and load data to the database.

You can use `test.ipynb` to verify data is now in the database and looks as expected.
