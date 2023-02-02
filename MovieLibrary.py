import random 
import datetime as dt 

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

movie_series_list = [Movie(title = "Skazani na Shawshank", year = 1994, genre ="Dramat", views = 0),
                     Movie(title = "Nietykalni" , year = 2011, genre ="Komedia", views = 0),
                     Movie(title = "Zielona mila", year = 1990, genre ="Dramat", views = 0),
                     Movie(title = "Ojciec chrzestny", year = 1972, genre ="Gangsterski", views = 0),
                     Movie(title = "12 gniewnych ludzi", year = 1957, genre = "Dramat sądowy", views = 0),
                     Series(title = "Breaking Bad" , year = 2008, genre = "Dramat", views = 0, episode = 5, season = 2),
                     Series(title = "Gra o tron", year = 2011, genre = "Fantasy", views = 0, episode = 3, season = 5),
                     Series(title = "Twin Peaks", year = 1990, genre ="Thriller", views = 0, episode = 6, season = 1),
                     Series(title = "House of Cards", year = 2013, genre ="Polityczny", views = 0, episode = 5, season = 3),
                     Series(title = "The Crown" , year = 2016, genre ="Biograficzny", views = 0, episode = 1, season = 4)
                    ]
movie_list =[]
series_list = []

def get_movies():
    movie_list = []
    for position in movie_series_list:
        if isinstance(position, Series) == False:
            movie_list.append(position)
        else:
            pass
    movies_by_title = sorted(movie_list, key = lambda movie: movie.title)
    return movies_by_title

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

def multiply(func):
    def wrapper():
        for i in range (10):
            func()
    return wrapper

@multiply       
def generate_views():
    position = random.choice(movie_series_list)
    position.play(random.randrange(101))
    return f'{position.title}, views: {position.views}'

def top_titles(amount, content_type):
    if content_type == "movies":
        movies_list = get_movies()
        movies_by_views = sorted(movies_list, key=lambda movie: movie.views)
        return movies_by_views[-amount:]
    elif content_type == "series":
        series_list = get_series()
        series_by_views = sorted(series_list, key = lambda series: series.views)
        return series_by_views[-amount:]

def add_series(title, year, genre, season, episodes):
    for i in range (episodes):
        position = Series(title = title, year = year, genre = genre, views = 0, episode = i, season = season)
        movie_series_list.append(position)
    return movie_series_list

def How_many_episodes(title):
    series_list = get_series()
    number_of_episodes = 0
    for position in series_list:
        if position.title == title:
            number_of_episodes += 1 
    return f'Tytuł serialu :{title}, liczba odcinków w bibliotece: {number_of_episodes}'

#Program po uruchomieniu

print("Biblioteka filmów")

generate_views()

print(f'Najpopularniejsze filmy i seriale dnia {dt.date.today().strftime("%d.%m.%Y")}')

for movie in top_titles(3, "movies"):
    print(movie)
for series in top_titles(3, "series"):
    print(series)
