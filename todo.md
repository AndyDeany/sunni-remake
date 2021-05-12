### Refactors/Minor Improvements
* Perhaps `Options` should also inherit from `Page`.
It would need to remember previous value of `game.page` though - not an issue.

* Pass `Move`s `user` and `opponent`? So that they don't have to just get it from
`Game` and hope it's right. Also gets rid of any ambiguity and means that
any `Character` can use a move without worrying about it targeting the wrong character.

* The `Session`/`Game` divide is intended so that when you load into a save
or start a new one, a new `Game()` instance could be created with all attributes
set to their original values like `Game.__init__()` currently sets them to.
This means you can leave `Session` with the stuff that doesn't need resetting
(META RELATED STUFF - fps, screen, etc.) whilst `Game` resets the
stuff that needs resetting. There is a slight issue with the divide being
"general to all games"/"specific to this game" (what the divide is currently)
or "never needs resetting"/"needs resetting on game load". 

This just means we get a clean slate for sure when the game is started from
the main menu again, and avoids any chance of variables carrying over
accidentally and causing bugs.

### Bugs
Be sure to check the issues on GitHub for any other bugs.

### Features
None at the moment.

### Other
* Remove docstring ignores from `.pylintrc` at some point.
