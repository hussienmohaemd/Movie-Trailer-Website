# Entertainment Center

**Entertainment Center** is a project from Udacity's Web Developer course. It generates an HTML file that displays a list of movies with their details and trailers. This project demonstrates how to create a web application using Python to showcase movies and integrate YouTube trailers.

## Features

- **Dynamic Movie List**: Displays a list of movies with posters and trailers.
- **YouTube Integration**: Embeds YouTube trailers directly into the web page.
- **Responsive Design**: Utilizes Bootstrap for a mobile-friendly design.

## How to Run

To run the website locally, follow these steps:

1. **Execute the Application**

    Open your terminal or command prompt and run:

    ```bash
    python entertainment_center.py
    ```

2. **Access the Website**

    The application will generate an HTML file named `fresh_tomatoes.html` in the same directory. Open this file in your web browser to view the list of movies.

## Adding Movies

To add a new movie to the website, use the following template in `entertainment_center.py`:

```python
film_name = media.Movie(
    "film_name",
    "film_description",
    "film_poster_image_url",
    "youtube_trailer_url"
)


