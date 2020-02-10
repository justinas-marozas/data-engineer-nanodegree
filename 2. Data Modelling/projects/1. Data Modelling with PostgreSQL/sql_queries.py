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
    songplay_id serial primary key,
    start_time timestamp not null,
    user_id int not null,
    level text not null,
    song_id text,
    artist_id text,
    session_id int not null,
    location text not null,
    user_agent text not null
);
""")

user_table_create = ("""
create table if not exists users
(
    user_id int primary key,
    first_name text,
    last_name text,
    gender text,
    level text not null
);
""")

song_table_create = ("""
create table if not exists songs
(
    song_id text primary key,
    title text not null,
    artist_id text not null,
    year int not null,
    duration float not null
);
""")

artist_table_create = ("""
create table if not exists artists
(
    artist_id text primary key,
    name text not null,
    location text,
    latitude float,
    longitude float
);
""")

time_table_create = ("""
create table if not exists "time"
(
    start_time timestamp primary key,
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
insert into songplays
(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
)
values (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
insert into users
(
    user_id,
    first_name,
    last_name,
    gender,
    level
)
values (%s, %s, %s, %s, %s)
on conflict (user_id) do update
set first_name = excluded.first_name,
    last_name = excluded.last_name,
    gender = excluded.gender,
    level = excluded.level;
""")

song_table_insert = ("""
insert into songs
(
    song_id,
    title,
    artist_id,
    year,
    duration
)
values (%s, %s, %s, %s, %s)
on conflict (song_id) do update
set title = excluded.title,
    artist_id = excluded.artist_id,
    year = excluded.year,
    duration = excluded.duration;
""")

artist_table_insert = ("""
insert into artists
(
    artist_id,
    name,
    location,
    latitude,
    longitude
)
values (%s, %s, %s, %s, %s)
on conflict (artist_id) do update
set name = excluded.name,
    location = excluded.location,
    latitude = excluded.latitude,
    longitude = excluded.longitude;
""")


time_table_insert = ("""
insert into "time"
(
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
)
values (%s, %s, %s, %s, %s, %s, %s)
on conflict (start_time) do nothing;
""")

# FIND SONGS

song_select = ("""
select
    s.song_id,
    a.artist_id
from songs as s
join artists as a on a.artist_id = s.artist_id
where s.song_id = %s
and a.artist_id = %s
and s.duration = %s;
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
