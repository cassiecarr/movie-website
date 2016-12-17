import webbrowser

class Video():
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube):
        self.title = video_title
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie(Video):
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube):
        Video.__init__(self, video_title, video_storyline, poster_image, trailer_youtube)

class TvShow(Video):
    """This class provides a way to store TV Show related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube):
        Video.__init__(self, video_title, video_storyline, poster_image, trailer_youtube)
