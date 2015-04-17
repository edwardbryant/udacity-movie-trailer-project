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

After downloading the project files, ... need Python (2.7 used to for project)

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
├── entertainment-center.py
├── fresh-tomatoes.html
├── fresh-tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Using the Movie object class

The Movie object class used for the Movie Trailer Project can be used by importing [media.py](https://github.com/edwardbryant/udacity-movie-trailer-project/blob/master/media.py) at the start of your Python script and creating a new Movie object (see example 1).

```
import media

pulp_fiction = media.Movie(
    "Pulp Fiction",
    1994,
    "http://goo.gl/V5fb9n",
    "https://www.youtube.com/watch?v=ewlwcEBTvcg")

```

#### movie.title

#### movie.year

#### movie.poster_url

#### movie.trailer_url



## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Edward Bryant]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

- Background image by [sethoscope](https://www.flickr.com/photos/sethoscope/2884743046/) used under [Creative Coomons Attribution-NonCommercial-ShareAlike 2.0 Generic License (BY-NC-SA)](http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en).




