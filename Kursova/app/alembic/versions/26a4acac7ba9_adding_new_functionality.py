"""adding new functionality

Revision ID: 26a4acac7ba9
Revises: 00500598fdba
Create Date: 2024-12-31 00:33:07.634815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26a4acac7ba9'
down_revision: Union[str, None] = '00500598fdba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('imageUrl', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albums',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('songs', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('songs', sa.Column('album_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'songs', 'albums', ['album_id'], ['id'])
    op.create_foreign_key(None, 'songs', 'artists', ['artist_id'], ['id'])
    op.drop_column('songs', 'artist')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('artist', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'songs', type_='foreignkey')
    op.drop_constraint(None, 'songs', type_='foreignkey')
    op.drop_column('songs', 'album_id')
    op.drop_column('songs', 'artist_id')
    op.drop_table('albums')
    op.drop_table('artists')
    # ### end Alembic commands ###
