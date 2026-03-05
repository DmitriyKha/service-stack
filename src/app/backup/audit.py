from datetime import datetime

from audit_models import AuditLog, CustomerActivity, InvoiceHistory
from models import Customer, Invoice
from sqlalchemy import event
from sqlalchemy.orm import Session


def serialize(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def register_audit_listeners(session: Session):

    @event.listens_for(Invoice, "after_insert")
    def log_invoice_insert(mapper, connection, target):
        connection.execute(
            AuditLog.__table__.insert(),
            {
                "table_name": "invoices",
                "operation": "INSERT",
                "record_id": target.InvoiceId,
                "new_data": serialize(target),
                "created_at": datetime.utcnow(),
            },
        )

    @event.listens_for(Customer, "after_update")
    def log_customer_update(mapper, connection, target):
        connection.execute(
            CustomerActivity.__table__.insert(),
            {
                "customer_id": target.CustomerId,
                "action": "UPDATE",
                "data": serialize(target),
                "created_at": datetime.utcnow(),
            },
        )
