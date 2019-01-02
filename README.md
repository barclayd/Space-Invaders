# Space Invaders 👽

Classic Arcade style Space Invaders.
Built using Python and Turtle.

### Demo

![Space Invaders Game Play](https://user-images.githubusercontent.com/39765499/50606242-f9da8900-0ebc-11e9-8940-cb53c3731593.gif)
<img width="832" alt="SpaceInvaders Game Play" src="https://user-images.githubusercontent.com/39765499/50606139-92243e00-0ebc-11e9-9509-d91dcb12a1ba.png">


### How to Run

````
$ git clone https://github.com/barclayd/SpaceInvaders.git
$ cd SpaceInvaders
$ python space_invaders.py
````
Space Invaders game will now open in a new window and you can start playing!

##### Controls

- <kbd>left</kbd>: move left
- <kbd>right</kbd>: move right
- <kbd>space</kbd>: fire bullet

_Please note that sound currently only works when run on Mac/Linux_

### To get sound working on Windows:

Replace ```os.system("afplay ./audio/bullet.wav&")``` with ```winsound.PlaySound("./audio/bullet", winsound.SND_ASYNC)```
Replace ```os.system("afplay ./audio/explosion.wav&")``` with ```winsound.PlaySound("./audio/explosion", winsound.SND_ASYNC)```
Replace ```os.system("afplay ./audio/collision.wav&")``` with ```winsound.PlaySound("./audio/collision", winsound.SND_ASYNC)```

### Features to be Added

* Leaderboard of highscores
* Save high score
* Random enemy speeds
* Game over message
* Count down timer - 1 min
* Intro message whilst window loads
* Game music to run throughout (optional)
* Settings for sound and easy/medium/hard, choose length of game
* Get extra time for killing space invaders and more points based on timing
* Multiplier
* Health bonuses and set a number of lives
