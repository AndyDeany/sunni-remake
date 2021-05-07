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

* Could make `CHOOSE_ABILITY`, `opponent.DEAD`, and `player.DEAD` members of the
`Move` class somehow so that `Battle().current` is always a `Move`? Unsure if
this makes complete sense. Perhaps it can be a subclass of a new
`State` (or `BattleState`) parent class that `Move` will also inherit from.

* Get rid of `initalise()` methods - just do it in `__init__()` methods.
Using `initialise()` methods means that the assets are always loaded,
instead of just when needed = memhog.

* Pass `Move`s `user` and `opponent`? So that they don't have to just get it from
`Game` and hope it's right. Also gets rid of any ambiguity and means that
any `Character` can use a move without worrying about it targeting the wrong character.

* `MouseButton` class.

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
* When hp damage and mana damage done at the same time (like Spook Dog's Teleport move)
only one stat change is shown since `stat_change_text` can only hold one value.
This might need fixing by having a list of `stat_change_texts` and `display_stat_change_text()`
display them 1by1 with a slight delay so they don't overlap, and then removing
the text from the list when it's complete. May need to be a tuple to store the y
value of the stat change text too so it's known when each one is done.
Alternatively to the delay, subsequent values could just show below the first one,
at the same time. I *much* prefer this solution from both a user standpoint
(the damages happened at the same time... so show them at the same time)
**and** a coding standpoint, as this means only one `y` value needs storing,
and subsequent items in the `stat_change_texts` lists can just be
blitted 20px (or whatever the height of the font is plus a couple px buffer)
below until the normal blit duration has passed.

### Features
* Replace `random.randint()` for calculating move damage/healing with two parameters:
`move.damage` (or `move.average_damage`) and `move.damage_variance`
(should be between `0.0` and `1.0`). Then the damage/healing calculation for each move can
just be `int(damage*(1+random.random(-variance, variance)))`.
This homogenises how damage is calculated.
Can allow for things like crit chance etc in the future too,
instead of each move having it's own special way of calculating damage.

* Change kick/confuse/other mana restoring moves to have a mana cost of `0` and
then have a `restore_mana()` call at a later point? Could also have a 
`mana_restoration` parameter showing how much mana will be restored,
which also means you can use it for `attack_options()` as well,
so that doesn't get ruined by the new `mana_cost` being `0`.

### Other
* Remove docstring ignores from `.pylintrc` at some point.

* Once you've deleted old files, remove them from the ignored files in `.pylintrc` too.