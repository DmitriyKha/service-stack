"""create recommended_playlists

Revision ID: cbc2b4740a41
Revises: 
Create Date: 2026-03-09 13:17:20.094323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbc2b4740a41'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'recommended_playlists',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('playlistId', sa.Integer, nullable=False),
        sa.Column('userId', sa.Integer, sa.ForeignKey('Customer.CustomerId'), nullable=False),
        sa.Column('trackId', sa.Integer, sa.ForeignKey('Track.TrackId'), nullable=False),
        sa.Column('method', sa.String(50), nullable=False)
    )

def downgrade():
    op.drop_table('reccomended_playlists')
