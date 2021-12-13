from types import SimpleNamespace

from src.utils.keyboard import create_keyboard
import emoji

keys = SimpleNamespace(
    settings=emoji.emojize(':gear: Settings'),
    exit=emoji.emojize(':cross_mark: Exit'),
)

keyboards = SimpleNamespace(
    main=create_keyboard(keys.settings),
)
