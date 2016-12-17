import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/embed/KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://img.csfd.cz/files/images/film/posters/000/071/71453_2f3f15.jpg?h180", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

harry_potter_deathly_hallows = media.Movie("Harry Potter and the Deathly Hallows - Part 2", "Harry Potter takes on Lord Voldemort", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2MTk3MDQ1N15BMl5BanBnXkFtZTcwMzI4NzA2NQ@@._V1_SY1000_SX675_AL_.jpg", "https://www.youtube.com/watch?v=5NYt1qirBWg")

mockingjay_part_2 = media.Movie("The Hunger Games: Mockingjay Part 2", "Katniss must bring together the army against evil President Snow","https://images-na.ssl-images-amazon.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5BanBnXkFtZTgwNTAyMDQ5NjE@._V1_UY1200_CR79,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=n-7K_OjsDCQ")

movies = [toy_story, avatar, harry_potter_deathly_hallows, mockingjay_part_2]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
