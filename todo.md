### Refactors/Minor Improvements
* Perhaps `Options` should also inherit from `Page`.
It would need to remember previous value of `game.page` though - not an issue.

* Button class for representing buttons on the main menu at least,
potentially could be used with saves as well. Need an `on_click()`/`click()` method for sure

* Go through attributes of game in `Game().__init__()` and see if any are only
used in one class (that isn't game). If so, move it there!

* Get rid of `initalise()` methods - just do it in `__init__()` methods.
Using `initialise()` methods means that the assets are always loaded,
instead of just when needed = memhog.

* Pass `Move`s `user` and `opponent`? So that they don't have to just get it from
`Game` and hope it's right. Also gets rid of any ambiguity and means that
any `Character` can use a move without worrying about it targeting the wrong character.

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
Be sure to check the issues on GitHub for any other bugs.

### Features
None at the moment.

### Other
* Remove docstring ignores from `.pylintrc` at some point.
