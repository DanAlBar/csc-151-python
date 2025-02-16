alien_color = 'rED'

alien_color = alien_color.lower()

if alien_color == 'green':
  print('Congrats! You have earned 5 points for shooting a ' + alien_color + ' alien!')
elif alien_color == 'yellow':
  print('Woah! You just shot a ' + alien_color + ' alien, you get 10 points!')
else:
  print('Awesome! You shot a ' + alien_color + ' alien, those are worth 15 points!')
  
