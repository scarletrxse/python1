# Sings "Row Row Row Your Boat" ten times.

def repeat_stuff (stuff, num_repeats=10):
  return stuff*num_repeats
  
repeated = repeat_stuff("Row ", 3)

lyrics = repeated + "Your Boat. "

song = repeat_stuff(lyrics)

print(song)
