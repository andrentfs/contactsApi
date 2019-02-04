from app import app, db
from app.models import User, Contact


@app.shell_context_processor
def shell_conext():
    return dict(
        app=app,
        db=db,
        User=User,
        Contact=Contact
    )


if __name__ == "__main__":
    app.run(debug=True)