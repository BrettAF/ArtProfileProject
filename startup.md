cd Documents/cs3300/ArtPortfolio
source ~/Documents/cs3300/Portfolio/djvenv/Scripts/activate

create a git branch
    git branch <branch name>
    git checkout <branch name>

to migrate
    ./manage.py makemigrations
    ./manage.py migrate

start the server with 
    python manage.py runserver
    http://127.0.0.1:8000
    or
    http://127.0.0.1:8000/admin

    bford
    R120

the command line shell for queries
    python manage.py shell
    from portfolio_app.models import project
    project.objects.all()
    <QuerySet [<project: asdf>]>