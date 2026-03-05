from audit_models import AuditLog, QueryPerformance
from sqlalchemy import desc, func


def analyze_slow_queries(session):
    results = (
        session.query(QueryPerformance)
        .order_by(desc(QueryPerformance.max_time))
        .limit(10)
        .all()
    )

    print("\nTOP SLOW QUERIES:")
    for r in results:
        print(f"{r.query_hash} | max={r.max_time:.3f}s | calls={r.calls}")


def generate_audit_report(session):
    stats = (
        session.query(AuditLog.operation, func.count().label("count"))
        .group_by(AuditLog.operation)
        .all()
    )

    print("\nAUDIT REPORT:")
    for op, count in stats:
        print(f"{op}: {count}")
