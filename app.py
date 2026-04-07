from flask import Flask, render_template, jsonify
from flask_cors import CORS
from extensions import db
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    # Register Blueprints
    from routes.students    import students_bp
    from routes.analytics   import analytics_bp
    from routes.chatbot     import chatbot_bp
    from routes.predictions import predictions_bp

    app.register_blueprint(students_bp,    url_prefix='/api/students')
    app.register_blueprint(analytics_bp,   url_prefix='/api/analytics')
    app.register_blueprint(chatbot_bp,     url_prefix='/api/chatbot')
    app.register_blueprint(predictions_bp, url_prefix='/api/predictions')

    @app.route('/')
    def index():
        return render_template('dashboard.html')

    @app.route('/health')
    def health():
        return jsonify({
            'status':   'ok',
            'database': 'AWS RDS PostgreSQL',
            'message':  'Student AI App is running!'
        })

    # Create all tables + seed demo data on first run
    with app.app_context():
        db.create_all()
        from utils.seed_data import seed_if_empty
        seed_if_empty(db)

    return app

app = create_app()

if __name__ == '__main__':
    print("\n" + "="*50)
    print("  STUDENT AI PERFORMANCE ANALYZER")
    print("  Connected to: AWS RDS PostgreSQL")
    print("="*50)
    print("🌐 Open browser at: http://localhost:5000")
    print("🔴 Press Ctrl+C to stop\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
