import media
import fresh_tomatoes

# Enter Movie Content
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://img.csfd.cz/files/images/film/posters/000/071/71453_2f3f15.jpg?h180", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

harry_potter_deathly_hallows = media.Movie("Harry Potter and the Deathly Hallows - Part 2", "Harry Potter takes on Lord Voldemort", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2MTk3MDQ1N15BMl5BanBnXkFtZTcwMzI4NzA2NQ@@._V1_SY1000_SX675_AL_.jpg", "https://www.youtube.com/watch?v=5NYt1qirBWg")

mockingjay_part_2 = media.Movie("The Hunger Games: Mockingjay Part 2", "Katniss must bring together the army against evil President Snow","https://images-na.ssl-images-amazon.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5BanBnXkFtZTgwNTAyMDQ5NjE@._V1_UY1200_CR79,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=n-7K_OjsDCQ")

movies = [toy_story, avatar, harry_potter_deathly_hallows, mockingjay_part_2]

# Enter TV Show Content
walking_dead = media.TvShow("The Walking Dead", "A group of individuals struggling through a world where the dead come back as zombies", "http://cdn.bgr.com/2015/01/the-walking-dead-season-5-trailer.png", "https://www.youtube.com/watch?v=R1v0uFms68U")

blacklist = media.TvShow("The Blacklist", "An ex-con helps the FBI take down the members of his blacklist", "https://s-media-cache-ak0.pinimg.com/originals/ba/8f/fa/ba8ffaf54d9990f58aacf71c258de835.jpg", "https://www.youtube.com/watch?v=JGBIimq1I3A")

the_good_wife = media.TvShow("The Good Wife", "A stay at home mom comes back to her job as a lawyer after her husband is publically investigated and found to have mulitple affairs", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI2OTk4MDk3OF5BMl5BanBnXkFtZTcwMTY3NTc3Mg@@._V1_UY1200_CR89,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=OLN6Dp1Gi-8")

orphan_black = media.TvShow("The Orphan Black", "A number of young women find that they are all identical sisters from a scientific clone project","https://images-na.ssl-images-amazon.com/images/M/MV5BNDUwMjA1NjE2N15BMl5BanBnXkFtZTgwOTM5OTkzODE@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=do_BCA-vR9E")

tvshows = [walking_dead, blacklist, the_good_wife, orphan_black]

# Open the movies page
fresh_tomatoes.open_movies_page(movies, tvshows)
print("The movie page has been opened")
print("Class Movie Documentation: "+media.Movie.__doc__)
print("Class Movie Name: "+media.Movie.__name__)
print("Calss Movie Module: "+media.Movie.__module__)
