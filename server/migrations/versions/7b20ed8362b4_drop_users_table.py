"""Drop users table

Revision ID: 7b20ed8362b4
Revises: ee9e7c11fa75
Create Date: 2024-10-18 08:50:53.195429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b20ed8362b4'
down_revision = 'ee9e7c11fa75'
branch_labels = None
depends_on = None


def upgrade():
    # Drop the users table only
    op.drop_table('users')


def downgrade():
    # Recreate the users table if downgrading
    op.create_table('users',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('first_name', sa.VARCHAR(), nullable=True),
        sa.Column('last_name', sa.VARCHAR(), nullable=True),
        sa.Column('email', sa.VARCHAR(), nullable=True),
        sa.Column('age', sa.VARCHAR(), nullable=True),
        sa.Column('role', sa.VARCHAR(), nullable=True),
        sa.Column('_password_hash', sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
