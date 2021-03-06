"""empty message

Revision ID: 0498754ad78f
Revises: ba58aa9b924c
Create Date: 2021-02-06 18:50:51.656983

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0498754ad78f'
down_revision = 'ba58aa9b924c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('upload_time', sa.TIMESTAMP(), nullable=False),
    sa.Column('log_storage_time', sa.TIMESTAMP(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('cypher_mutation', sa.Text(), nullable=False),
    sa.Column('fhir_data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient')
    # ### end Alembic commands ###
