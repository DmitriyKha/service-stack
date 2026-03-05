import hashlib
import time
from datetime import datetime
from functools import wraps

from audit_models import QueryPerformance


def monitor_query_performance(session):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()

            result = func(*args, **kwargs)

            duration = time.time() - start
            query_hash = hashlib.md5(func.__name__.encode()).hexdigest()

            record = (
                session.query(QueryPerformance).filter_by(query_hash=query_hash).first()
            )

            if record:
                record.calls += 1
                record.avg_time = (record.avg_time + duration) / 2
                record.min_time = min(record.min_time, duration)
                record.max_time = max(record.max_time, duration)
                record.last_executed = datetime.utcnow()
            else:
                record = QueryPerformance(
                    query_hash=query_hash,
                    avg_time=duration,
                    min_time=duration,
                    max_time=duration,
                    calls=1,
                )
                session.add(record)

            session.commit()

            if duration > 0.1:
                print(f"Slow query: {func.__name__} ({duration:.3f}s)")

            return result

        return wrapper

    return decorator
