#!/usr/bin/env python
import media
import fresh_tomatoes

# created new instance Frozen
Frozen = media.Movie(
    'Frozen',
    'Princess Elsa of Arendelle possesses cryokinetic magic',
    'https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=TbQm5doF_Uc')

# created new instance Moana
Moana = media.Movie(
    'Moana',
    'Untold ages ago, the goddess Te Fiti created all life.',
    'https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg',
    'https://www.youtube.com/watch?v=yfCOEGyHMwc')

# created new instance The_Boss_Baby

The_Boss_Baby = media.Movie(
    'The Boss Baby',
    'A man named Tim Templeton (Tobey Maguire) tells about his seven-year-old life',
    'https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg',
    'https://www.youtube.com/watch?v=O2Bsw3lrhvs')

# created new instance inside_Out
inside_Out = media.Movie(
    'Inside Out',
    'Riley Andersen is born in Minnesota and within her mind,five \
    personifications of her basic emotions Joy, Sadness, Fear, Disgust, and Anger',
    'https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=3bjHLsZWHgg')

# created new instance Zootopia
Zootopia = media.Movie(
    'Zootopia',
    'In a world populated by anthropomorphic mammals where predators and prey \
    species peacefully coexist, a rabbit from rural Bunnyburrow, Judy Hopps, \
    fulfills her childhood dream of becoming the first rabbit police officer \
    in urban Zootopia.',
    'https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg',
    'https://www.youtube.com/watch?v=yCOPJi0Urq4')

# created new instance Beauty_and_the_Beast
Beauty_and_the_Beast = media.Movie(
    'Beauty and the Beast',
    'Belle is a young woman who is taken prisoner by a Beast in his castle \
    in exchange for the freedom of her father Maurice. ',
    'https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=OvW_L8sTu5E')

# created new instance Hotel_Transylvania
Hotel_Transylvania = media.Movie(
    'Hotel Transylvania',
    'In the aftermath of the death of his wife Martha (Jackie Sandler) at the \
    hands of an angry human mob, Count Dracula (Adam Sandler) commissions and \
    builds a massive five-star, monsters-only hotel in Transylvania in which \
    he raises his daughter Mavis(Selena Gomez) and to serve as a safe-place \
    getaway for the world \'s monsters from fear of human persecution.',
    'https://upload.wikimedia.org/wikipedia/en/f/f5/HotelTransylvania.jpg',
    'https://www.youtube.com/watch?v=q4RK3jY7AVk')

# created new instance The_Angry_Birds
The_Angry_Birds = media.Movie(
    'The Angry Birds',
    'On Bird Island, an island inhabited by flightless birds, the reclusive \
    Red is sentenced to anger management classes after his temper causes a \
    "premature hatching" of a customer\'s egg.',
    'https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png',  # NOQA
    'https://www.youtube.com/watch?v=0qJzWrq7les')

# created new instance The_Secret_Life_of_Pets
The_Secret_Life_of_Pets = media.Movie(
    'The Secret Life of Pets',
    'A Jack Russell Terrier named Max lives with his owner Katie in a \
    Manhattan apartment. While she is at work during the day, he hangs out \
    with other pets in the building: tabby cat Chloe, pug Mel, dachshund Buddy,\
    and budgerigar Sweetpea. ',
    'https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=87bxIqvuBlY')

# create an array for created instances
movies = [
    Frozen,
    Moana,
    The_Boss_Baby,
    inside_Out,
    Zootopia,
    Beauty_and_the_Beast,
    Hotel_Transylvania,
    The_Angry_Birds,
    The_Secret_Life_of_Pets]
    
# call open_movies_page from fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
