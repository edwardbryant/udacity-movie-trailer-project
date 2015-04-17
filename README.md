# Movie-Trailer-Project 

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube. The project also includes some CSS and jQuery involved in the display of the webpage.  

## Table of contents

- [Demo](#demo)
- [Download](#download)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Copyright and license](#copyright-and-license)

## Demo

For a demo, check out <http://edwardbryant.github.io/udacity-movie-trailer-project/fresh_tomatoes.html>!

## Download

The files for the project, may be [downloaded here](https://github.com/edwardbryant/udacity-movie-trailer-project/archive/master.zip).

## Quick Start

After downloading the project files, a movie trailer page can be created by importing [media.py](https://github.com/edwardbryant/udacity-movie-trailer-project/blob/master/media.py) and [fresh_tomatoes.py](https://github.com/edwardbryant/udacity-movie-trailer-project/blob/master/fresh_tomatoes.py) at the start of your Python script. Then create idividual Movie objects by calling media.Movie() and supplying it with four arguments -- title, year, poster_url, and trailer_url. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an array of the movie objects you created. 

```
import media
import fresh_tomatoes

#information for object arguments
title = "Pulp Fiction"
year = 1994
poster_url = "http://goo.gl/V5fb9n"
trailer = "https://www.youtube.com/watch?v=ewlwcEBTvcg"

# Create Movie object
pulp_fiction = media.Movie(title, year, poster_url, trailer_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([pulp_fiction])

```

A more detailed example with multiple movie objects, which is used for the [demo](http://edwardbryant.github.io/udacity-movie-trailer-project/fresh_tomatoes.html), can be found in [entertainment_center.py](https://github.com/edwardbryant/udacity-movie-trailer-project/blob/master/media.py) 


### What's included

Within the download you'll find the following directories and files:

```
master.zip/
├── css/
│   └── main.css
├── img/
│   └── curtains.jpg
├── js/
│   └── main.js
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer.  

#### constructor method

##### movie.title

##### movie.year

##### movie.poster_url

##### movie.trailer_url



## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Edward Bryant]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

- Background image by [sethoscope](https://www.flickr.com/photos/sethoscope/2884743046/) used under [Creative Coomons Attribution-NonCommercial-ShareAlike 2.0 Generic License (BY-NC-SA)](http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en).




