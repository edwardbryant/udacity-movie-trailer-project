import media
import fresh_tomatoes

"""
declare favorite movies, with 4 args each:
title (movie's title)
year (year movie was released)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""
pulp_fiction = media.Movie(
    "Pulp Fiction",
    1994,
    "http://goo.gl/V5fb9n",
    "https://www.youtube.com/watch?v=ewlwcEBTvcg")
aliens = media.Movie(
    "Aliens",
    1986,
    "http://goo.gl/BB9U80",
    "https://www.youtube.com/watch?v=bTCaVjQ8nU4")
the_big_lebowski = media.Movie(
    "The Big Lebowski",
    1998,
    "http://goo.gl/2cxt3f",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")
back_to_the_future = media.Movie(
    "Back to the Future",
    1985,
    "http://goo.gl/IxgBni",
    "https://www.youtube.com/watch?v=yosuvf7Unmg")
time_bandits = media.Movie(
    "Time Bandits",
    1981,
    "http://goo.gl/yndMxB",
    "https://www.youtube.com/watch?v=Yd4DBq8a2y0")
fight_club = media.Movie(
    "Fight Club",
    1999,
    "http://goo.gl/BR5nIh",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")
faq_about_time_travel = media.Movie(
    "FAQ About Time Travel",
    2009,
    "http://goo.gl/somUuo",
    "https://www.youtube.com/watch?v=a6SVDNQmyA4")
groundhog_day = media.Movie(
    "Groundhog Day",
    1993,
    "http://goo.gl/Xhl8Ma",
    "https://www.youtube.com/watch?v=tSVeDx9fk60")

# assign individual movies to movies array
movies = [pulp_fiction,aliens,the_big_lebowski,back_to_the_future,
    time_bandits,fight_club,faq_about_time_travel,groundhog_day]

# call movie trailer page method and pass movies array and sorting option
fresh_tomatoes.open_movies_page(movies,"cron")
