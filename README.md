# Space Invaders 👽
Space Invaders game built using Python

### Demo

### How to Run

````
$ git clone https://github.com/barclayd/SpaceInvaders.git
$ cd SpaceInvaders
$ python space_invaders.py
````
Space Invaders game will now open in a new window and you can start playing!

##### Controls

<kbd>left</kbd><kbd>right</kbd><kbd>space</kbd>

_Please note that sound currently only works when run on Mac/Linux_

### To get sound working on Windows:

Replace ```os.system("afplay ./audio/bullet.wav&")``` with ```winsound.PlaySound("./audio/bullet", winsound.SND_ASYNC)```
Replace ```os.system("afplay ./audio/explosion.wav&")``` with ```winsound.PlaySound("./audio/explosion", winsound.SND_ASYNC)```
Replace ```os.system("afplay ./audio/collision.wav&")``` with ```winsound.PlaySound("./audio/collision", winsound.SND_ASYNC)```

### Features to be Added

* Leaderboard
* Save high score
* Random enemy speeds
* Game over message
* Intro message whilst window loads
* Game music to run throughout (optional)
* Settings for sound and easy/medium/hard
