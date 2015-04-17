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

##### constructor method

The constructor method is called when a new Movie object is created and must include four arguments -- [title](#movietitle), [year](#movieyear), [poster_url](#movieposter_url), and [trailer_url](#movietrailer_url). Each of these arguments is discussed further below.

```
import media

#information for object arguments
title = "Pulp Fiction"
year = 1994
poster_url = "http://goo.gl/V5fb9n"
trailer = "https://www.youtube.com/watch?v=ewlwcEBTvcg"

# Create Movie object
pulp_fiction = media.Movie(title, year, poster_url, trailer_url)
```

###### movie.title

movie.title is any string used to identify the movie object.

###### movie.year

movie.year is an integer representing the year the movie was released.  

###### movie.poster_url

movie.poster_url is a string containing a URL linking to an image which will be used to represent the Movie object, such as a movie poster or DVD box cover. The movie trailer page portion of this project displays these images with a width of 188px and a height of 292px. So, images with a ratio of 1:1.5 will work best. 

###### movie.trailer_url

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is usful for testing but is not used by the script that generates the finished movie trailers page.




## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Edward Bryant]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

- Background image by [sethoscope](https://www.flickr.com/photos/sethoscope/2884743046/) used under [Creative Coomons Attribution-NonCommercial-ShareAlike 2.0 Generic License (BY-NC-SA)](http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en).




