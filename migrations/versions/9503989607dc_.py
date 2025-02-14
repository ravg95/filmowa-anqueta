"""empty message

Revision ID: 9503989607dc
Revises: f89baacacdbd
Create Date: 2019-10-23 21:37:15.968053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9503989607dc'
down_revision = 'f89baacacdbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    op.drop_constraint('rfk1', 'rating', type_='foreignkey')
    op.create_foreign_key(None, 'rating', 'info', ['movie_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rating', type_='foreignkey')
    op.create_foreign_key('rfk1', 'rating', 'movies', ['movie_id'], ['id'])
    op.create_table('movies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('tmdb_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=70), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='movies_pkey')
    )
    # ### end Alembic commands ###
