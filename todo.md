### Refactors/Minor Improvements
* add base Opponent class

* Perhaps `Options` should also inherit from `Page`.
It would need to remember previous value of `game.page` though - not an issue.

* Button class for representing buttons on the main menu at least,
potentially could be used with saves as well. Need an `on_click()`/`click()` method for sure

* use SCALED screen mode in fullscreen to make it """1080p""" (at least by mouse movement standards).

* Change MemeDog AI to check the actual mana costs of
moves and add them to the returned list in `attack_options()`

* Probably shouldn't store an instance of each page in `Game()`
as this means assets are never unloaded=memhog.
Just create a new one to go to the page.
This can be done by making `visit()` a classmethod which sets cls.game.page = cls(cls.game).
Alternatively, scrap the `visit()` method and just write `current = Page()` to go to a page.
The code from `visit()` can just be in the `Page().__init__()` method

* Go through attributes of game in `Game().__init__()` and see if any are only
used in one class (that isn't game). If so, move it there!

### Bugs
* fix bug(s?) with player/memedog 'flickering'/disappearing for a frame at the end of some moves.

* `choose_character_overlay.png` is either 1pixel too thin
or is transparent for 1 column of pixels on the left (probably the latter)

* Potential/Foreseen: Next battle's dead body shows after winning a fight due to `game.opponent`
being changed to the next opponent pre-emptively in `game.load_next_battle`...
Try think of a fix if this is an issue as predicted.