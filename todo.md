### Refactors/Minor Improvements
* add base Opponent class

* Perhaps `Options` should also inherit from `Page`.
It would need to remember previous value of `game.page` though - not an issue.

* Button class for representing buttons on the main menu at least,
potentially could be used with saves as well. Need an `on_click()`/`click()` method for sure

* use SCALED screen mode in fullscreen to make it """1080p""" (at least by mouse movement standards).

* Probably shouldn't store an instance of each page in `Game()`
as this means assets are never unloaded=memhog.
Just create a new one to go to the page.
This can be done by making `visit()` a classmethod which sets cls.game.page = cls(cls.game).
Alternatively, scrap the `visit()` method and just write `current = Page()` to go to a page.
The code from `visit()` can just be in the `Page().__init__()` method.
Will also have to use `isinstance(self.game.page, PageClass)` instead of
`self.game.page == self.game.page_class` if you do this. Which is fine,
just make you sure you go through and do it.

* Go through attributes of game in `Game().__init__()` and see if any are only
used in one class (that isn't game). If so, move it there!

* Could (distant-ish future) have like a `Playthrough` class which takes most of `Game`'s logic.
This would be so that when you load into a save or start a new one,
a new `Playthrough()` instance could be created with all attributes
set to their original values like `Game.__init__()` currently sets them too.
This means you can leave game with the stuff that doesn't need resetting
(GAME RELATED STUFF - fps, screen, etc.) whilst `Playthrough` resets the
stuff that needs resetting.
Alternatively use `Game` as the `Playthrough` class and rename current `Game` to `Session`
or something. Or the other way around with `Game`/`Session` taking
technical stuff and playthrough related stuff respectively.

This just means we get a clean slate for sure when the game is started from
the main menu again, and avoids any chance of variables carrying over
accidentally and causing bugs.

### Bugs
* fix bug(s?) with player/memedog 'flickering'/disappearing for a frame at the end of some moves.

* `choose_character_overlay.png` is either 1pixel too thin
or is transparent for 1 column of pixels on the left (probably the latter)

* Potential/Foreseen: Next battle's dead body shows after winning a fight due to `game.opponent`
being changed to the next opponent pre-emptively in `game.load_next_battle`...
Try think of a fix if this is an issue as predicted.

### Other
* Remove docstring ignores from `.pylintrc` at some point.

* Once you've deleted old files, remove them from the ignored files in `.pylintrc` too.