# DROP TABLES

songplay_table_drop = """drop table if exists songplays;"""
user_table_drop = """drop table if exists users;"""
song_table_drop = """drop table if exists songs;"""
artist_table_drop = """drop table if exists artists;"""
time_table_drop = """drop table if exists "time";"""

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays
(
    songplay_id int,
    start_time timestamp,
    user_id int,
    level text,  -- enum?
    song_id text,
    artist_id text,
    session_id int,
    location text,
    user_agent text
);
""")

user_table_create = ("""
create table if not exists users
(
    user_id int,
    first_name text,
    last_name text,
    gender text,  -- enum?
    level text  -- enum?
);
""")

song_table_create = ("""
create table if not exists songs
(
    song_id text,
    title text,
    artist_id text,
    year int,
    duration float
);
""")

artist_table_create = ("""
create table if not exists artists
(
    artist_id text,
    name text,
    location text,
    latitude float,
    longitude float
);
""")

time_table_create = ("""
create table if not exists "time"
(
    start_time timestamp,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop
]
