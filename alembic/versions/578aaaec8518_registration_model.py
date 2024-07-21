"""registration model

Revision ID: 578aaaec8518
Revises: 50a52bc18428
Create Date: 2024-07-20 02:55:46.406655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '578aaaec8518'
down_revision = '50a52bc18428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_registration',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('Confirmed', 'Pending', 'Cancelled', name='registration_status'), nullable=True),
    sa.Column('number_of_tickets', sa.Integer(), nullable=True),
    sa.Column('additional_notes', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_registration_event_id'), 'event_registration', ['event_id'], unique=False)
    op.create_index(op.f('ix_event_registration_id'), 'event_registration', ['id'], unique=False)
    op.create_index(op.f('ix_event_registration_user_id'), 'event_registration', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_registration_user_id'), table_name='event_registration')
    op.drop_index(op.f('ix_event_registration_id'), table_name='event_registration')
    op.drop_index(op.f('ix_event_registration_event_id'), table_name='event_registration')
    op.drop_table('event_registration')
    # ### end Alembic commands ###
