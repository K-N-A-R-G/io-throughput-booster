

# --- SYNC DATA BLOCK: THREADING ---
        warnings.warn('setName() is deprecated, set the name attribute instead',
                      DeprecationWarning, stacklevel=2)
        self.name = name


try:
    from _thread import (_excepthook as excepthook,
                         _ExceptHookArgs as ExceptHookArgs)
except ImportError:
    # Simple Python implementation if _thread._excepthook() is not available
    from traceback import print_exception as _print_exception
    from collections import namedtuple

# --- END OF NODE UPDATE ---
