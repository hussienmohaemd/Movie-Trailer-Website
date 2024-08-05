import fresh_tomatoes
import media
'''this file contain my favourite films with his trailers ,
title , photo and youtube link'''

toy_story = media.Movie(
                       "Toy Story ",
                       "https://encrypted-tbn0.gstatic.com/images?"
                       "q=tbn:ANd9GcRCgCFuV3jw95R05F3b9kIp6ifHQXcSYMpg"
                       "Jlqk5AAgbWVtyc_gGA",
                       "https://www.youtube.com/watch?v=0TUkzBqapZ4")


Avatar = media.Movie(
                       "Avatar ",
                       "https://ia.media-imdb.com/images/M/MV5BMTYwOTEw"
                       "NjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_"
                       "CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=6ziBFh3V1aM&t=55s")

jurassic_park = media.Movie(
                       "Jurassic Park",
                       "https://upload.wikimedia.org/wikipedia/en/e/e7"
                       "/Jurassic_Park_poster.jpg",
                       "https://www.youtube.com/watch?v=DTa6JhAVVJU")

i_am_legend = media.Movie(
                       "I Am Legend",
                       "https://upload.wikimedia.org/wikipedia/en/d/df/"
                       "I_am_legend_teaser.jpg",
                       "https://youtu.be/dtKMEAXyPkg")

inception = media.Movie(
                        "Inception",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn"
                        ":ANd9GcStJTWxnlHRYDrbtK4wKt4FLMHnUN0ZAhCBU_gVDPJ"
                        "0bqRunOww",
                        "https://youtu.be/8hP9D6kZseM")

five_hundred = media.Movie(
                       "500 Days of Summer",
                       "https://upload.wikimedia.org/wikipedia/en/d/d1/"
                       "Five_hundred_days_of_summer.jpg",
                       "https://youtu.be/PsD0NpFSADM")


moes = [toy_story, Avatar, jurassic_park, i_am_legend, inception, five_hundred]
fresh_tomatoes.open_movies_page(moes)
