from datetime import datetime

from database import Base
from sqlalchemy import JSON, Column, DateTime, Float, Integer, String


class AuditLog(Base):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True)
    table_name = Column(String)
    operation = Column(String)  # INSERT / UPDATE / DELETE
    record_id = Column(Integer)
    old_data = Column(JSON)
    new_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class InvoiceHistory(Base):
    __tablename__ = "invoice_history"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer)
    operation = Column(String)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class CustomerActivity(Base):
    __tablename__ = "customer_activity"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    action = Column(String)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class QueryPerformance(Base):
    __tablename__ = "query_performance"

    id = Column(Integer, primary_key=True)
    query_hash = Column(String, unique=True)
    avg_time = Column(Float)
    min_time = Column(Float)
    max_time = Column(Float)
    calls = Column(Integer, default=1)
    last_executed = Column(DateTime, default=datetime.utcnow)
