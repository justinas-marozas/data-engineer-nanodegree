import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Description: Read a song JSON file and save contents to the given cursor.

    Arguments:
        cur: A cursor object.
        filepath: A filepath.

    Returns:
        None
    """
    # open song file
    with open(filepath, mode='r', encoding='utf-8') as fh:
        song_json = fh.read()
        df = pd.read_json(f'[{song_json}]')

    # insert song record
    song_data = df[[
        'song_id',
        'title',
        'artist_id',
        'year',
        'duration'
    ]].values[0]
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = df[[
        'artist_id',
        'artist_name',
        'artist_location',
        'artist_latitude',
        'artist_longitude'
    ]].values[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Description: Read a log JSON file and save contents to the given cursor.

    Arguments:
        cur: A cursor object.
        filepath: A filepath.

    Returns:
        None
    """
    # open log file
    log_json = ','.join(open(filepath, mode='r', encoding='utf-8'))
    df = pd.read_json(f'[{log_json}]')

    # filter by NextSong action
    df = df.query('page == "NextSong"')

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')

    # insert time data records
    time_data = (
        t,
        t.dt.hour,
        t.dt.day,
        t.dt.week,
        t.dt.month,
        t.dt.year,
        t.dt.weekday
    )
    column_labels = (
        'start_time',
        'hour',
        'day',
        'week',
        'month',
        'year',
        'weekday'
    )
    time_dict = {
        key: series
        for key, series in zip(column_labels, time_data)
    }
    time_df = pd.DataFrame(time_dict)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            pd.to_datetime(row['ts'], unit='ms'),  # start_time
            row['userId'],  # user_id
            row['level'],  # level
            songid,  # song_id
            artistid,  # artist_id
            row['sessionId'],  # session_id
            row['location'],  # location
            row['userAgent']  # user_agent
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Description: Read JSON files in a given `filepath` and use given `func`
    to process them.

    Arguments:
        cur: A cursor object.
        conn: A connection object.
        filepath: A filepath string to the directory with JSON files.
        func: A callable to use to process the JSON files.

    Returns:
        None
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Description: Entrypoint of this script.

    Arguments:
        None

    Returns:
        None
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
