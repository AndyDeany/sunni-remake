### Refactors/Minor Improvements
* add base Opponent class

* Perhaps `Battle` could inherit from `Page`? Perhaps Options as well.
If you make `Battle` inherit from `Page`, and MainMenu does too
(and `Options`?! - would need to remember previous current value though - not an issue),
you could just have a single `game.page.run()` command
and that literally be  everything in the `game.run()` logic
Could make `self.next_battle` a thing for storing the next loaded battle,
to then be used to do `self.current = self.next_battle` when next is clicked
(and set `self.next_battle` back to `None`. this could be a method that does these two things).
This solves the saving/levelling issue on the victory/defeat screens.
May need a `battle.current` if `game.page` is only used for current page,
for storing things like current move and choose ability etc.

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