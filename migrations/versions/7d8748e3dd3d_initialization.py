"""Initialization

Revision ID: 7d8748e3dd3d
Revises: 
Create Date: 2023-10-12 01:58:06.456165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d8748e3dd3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('bank_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bik', sa.String(length=9), nullable=False),
    sa.Column('bank_name', sa.String(length=30), nullable=False),
    sa.Column('checking_account', sa.String(length=20), nullable=False),
    sa.Column('correspondent_account', sa.String(length=20), nullable=False),
    sa.Column('swift', sa.String(length=11), nullable=False),
    sa.Column('iban', sa.String(length=34), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_active_models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bank_details_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bank_details_id'], ['bank_details.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_active_models')
    op.drop_table('bank_details')
    op.drop_table('users')
    # ### end Alembic commands ###