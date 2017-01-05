========
Usage
========

To use clapton in a project::

    import clapton



Create a Migration Script

    # create manuel
    alembic revision -m "01 init"

    # create from sqlalchemy model
    alembic revision --autogenerate -m "01 create table"
