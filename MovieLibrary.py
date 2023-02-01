import random 

class Movie():
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views

    def __str__(self):
        return f'"{self.title}" ({self.year})'

    def play(self, add_views =1):
        self.views += add_views
        return self.views

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'"{self.title}" S{self.season:02d}E{self.episode:02d}'

movie_series_list = [Movie(title = "The Shawshank Redemption", year = 1994, genre ="Dramat", views = 0),
                     Movie(title = "Intouchables" , year = 2011, genre ="Komedia", views = 0),
                     Movie(title = "The Green Mile", year = 1990, genre ="Dramat", views = 0),
                     Movie(title = "The Godfather", year = 1972, genre ="Gangsterski", views = 0),
                     Movie(title = "12 Angry Men", year = 1957, genre = "Dramat sądowy", views = 0),
                     Series(title = "Breaking Bad" , year = 2008, genre = "Dramat", views = 0, episode = 5, season = 2),
                     Series(title = "Game of Thrones", year = 2011, genre = "Fantasy", views = 0, episode = 3, season = 5),
                     Series(title = "Twin Peaks", year = 1990, genre ="Thriller", views = 0, episode = 6, season = 1),
                     Series(title = "House of Cards", year = 2013, genre ="Polityczny", views = 0, episode = 5, season = 3),
                     Series(title = "The Crown" , year = 2016, genre ="Biograficzny", views = 0, episode = 1, season = 4)
                    ]

def get_movies():
    movie_list = []
    for position in movie_series_list:
        if isinstance(position, Series) == False:
            movie_list.append(position)
        else:
            pass
    movie_by_title = sorted(movie_list, key = lambda movie: movie.title)
    return movie_by_title

def get_series():
    series_list = []
    for position in movie_series_list:
        if isinstance(position, Series) == True:
            series_list.append(position)
        else:
            pass
    series_by_title = sorted(series_list, key = lambda series: series.title) 
    return series_by_title

def search(title):
    for position in movie_series_list:
        if position.title == title:
            return position
        else:
            pass

def generate_views():
    position = random.choice(movie_series_list)
    position.play(random.randrange(101))
    return f'{position.title}, views: {position.views}'

print("najpierw filmy")
for position in get_movies():
    print(position)

print("potem seriale")
for position in get_series():
    print(position)

print(search("Twin Peaks"))
print(generate_views())


