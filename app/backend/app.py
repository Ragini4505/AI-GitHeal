from flask import Flask, jsonify
import socket
import os
import time

app = Flask(__name__)

START_TIME = time.time()


@app.route("/")
def home():
    return jsonify({
        "project": "AI-GitHeal",
        "message": "AI-GitHeal backend is running!",
        "hostname": socket.gethostname(),
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "ai-githeal-backend"
    }), 200


@app.route("/api/status")
def status():
    uptime = round(time.time() - START_TIME, 2)

    return jsonify({
        "application": "AI-GitHeal",
        "status": "running",
        "version": "1.0.0",
        "uptime_seconds": uptime,
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development")
    })


@app.route("/api/info")
def info():
    return jsonify({
        "name": "AI-GitHeal",
        "description": "AI-powered GitOps self-healing platform",
        "technology": [
            "Python",
            "Flask",
            "Docker",
            "Kubernetes",
            "GitHub Actions",
            "Prometheus",
            "Grafana",
            "AI"
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
