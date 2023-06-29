from app import app

from routes import auth_routes, movie_routes, render_routes, user_routes, rent_routes

app.register_blueprint(auth_routes.auth_bp)
app.register_blueprint(movie_routes.movie_bp)
app.register_blueprint(render_routes.render_bp)
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(rent_routes.rent_bp)

app.run(debug=True)