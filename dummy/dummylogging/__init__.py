import structlog
import uuid
from contextlib import contextmanager


structlog.configure(
    processors=[
        # the ordering of processors matters!
        structlog.threadlocal.merge_threadlocal_context,
        structlog.processors.TimeStamper(utc=True),
        structlog.processors.JSONRenderer(indent=2, sort_keys=True)
    ],
    wrapper_class=structlog.BoundLogger, # default
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.PrintLoggerFactory()
)

log = structlog.get_logger()
structlog.threadlocal.bind_threadlocal(event_id=str(uuid.uuid4()))

#@contextmanager
#def structured_logging(**context):
#    global log
#    log.bind(**context)
#    yield     
