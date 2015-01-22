easylog
=======

Easy configuration for python logging. Configure a logger so that ERROR ends up
on stderr and everything else on stdout.

Usage:

```python
import logging
import easylog

logger = logging.getLogger()
easylog.configure_logger(logger)

logger.info(...)        # -> stdout
logger.error(...)       # -> stderr
```
