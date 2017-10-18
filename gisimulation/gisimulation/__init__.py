# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - '
'%(message)s', level=logging.INFO)

# Set all publically accessible packages
__all__ = ["bar"]