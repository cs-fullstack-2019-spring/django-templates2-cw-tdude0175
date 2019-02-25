from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# not necessary to hard code this way could use a model instead of this more likey to be better to handle that way as well
movies = [
    {
        'movie_id': 0,
        'movie_title': 'Star Wars',
        'movie_synopsis': 'The Imperial Forces, under orders from cruel Darth Vader, hold Princess Leia hostage in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker and Han Solo, captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 and C-3PO to rescue the beautiful princess, help the Rebel Alliance and restore freedom and justice to the Galaxy.',
        'movie_details': 'Released: 1977, Runtime: 121 min, Gross USA: $322,740,140'
    },
    {
        'movie_id': 1,
        'movie_title': 'Monty Python and the Holy Grail',
        'movie_synopsis': 'History is turned on its comic head when, in 10th century England, King Arthur travels the countryside to find knights who will join him at the Round Table in Camelot. Gathering up the men is a tale in itself but after a bit of a party at Camelot, many decide to leave only to be stopped by God who sends them on a quest: to find the Holy Grail. After a series of individual adventures, the knights are reunited but must face a wizard named Tim, killer rabbits and lessons in the use of holy hand grenades. Their quest comes to an end however when the police intervene - just what you would expect in a Monty Python movie.',
        'movie_details': 'Released: 1975, Runtime: 91 min, Gross USA: $1,229,197'
    },
    {
        'movie_id': 2,
        'movie_title': 'Brazil',
        'movie_synopsis': "Sam Lowry is a harried technocrat in a futuristic society that is needlessly convoluted and inefficient. He dreams of a life where he can fly away from technology and overpowering bureaucracy, and spend eternity with the woman of his dreams. While trying to rectify the wrongful arrest of one Harry Buttle, Lowry meets the woman he is always chasing in his dreams, Jill Layton. Meanwhile, the bureaucracy has fingered him responsible for a rash of terrorist bombings, "
                          "and both Sam and Jill's lives are put in danger.",
        'movie_details': 'Released: 1985, Runtime: 132 min, Gross USA: $9,929,135'
    }
]

# simply renders movies(normally would use index but requirements say to use movies instead
def index(request):
    return render(request , 'movieApp/movies.html',{'movieList':movies})
# this function and {synopsisRender} are carbon copys with a few exceptions as the information supplied is different
def detailRender(request, indexNum):
    return render(request , 'movieApp/movie_detail.html',{'movie':movies[indexNum]})


def synopsisRender(request, indexNum):
    return render(request , 'movieApp/movie_synopsis.html',{'movie':movies[indexNum]})