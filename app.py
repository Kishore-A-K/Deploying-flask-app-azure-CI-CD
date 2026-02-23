from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask!</h1><p>CI/CD Pipeline is working!</p>'

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Portfolio</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: #fff; }
        header { background: linear-gradient(135deg, #1a1a2e, #16213e); padding: 60px 20px; text-align: center; }
        header h1 { font-size: 3em; color: #00d4ff; margin-bottom: 10px; }
        header p { font-size: 1.2em; color: #aaa; }
        .badges { display: flex; justify-content: center; gap: 15px; margin-top: 20px; flex-wrap: wrap; }
        .badge { background: #00d4ff22; border: 1px solid #00d4ff; padding: 8px 16px; border-radius: 20px; font-size: 0.85em; color: #00d4ff; }
        .section { padding: 60px 20px; max-width: 900px; margin: auto; }
        .section h2 { font-size: 2em; color: #00d4ff; margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 10px; }
        .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .card { background: #1a1a2e; border: 1px solid #333; border-radius: 12px; padding: 25px; transition: transform 0.2s; }
        .card:hover { transform: translateY(-5px); border-color: #00d4ff; }
        .card h3 { color: #00d4ff; margin-bottom: 10px; }
        .card p { color: #aaa; font-size: 0.95em; line-height: 1.6; }
        .pipeline { background: #1a1a2e; border-radius: 12px; padding: 30px; margin-top: 20px; }
        .steps { display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 20px; }
        .step { background: #00d4ff22; border: 1px solid #00d4ff; padding: 10px 20px; border-radius: 8px; color: #00d4ff; font-size: 0.9em; }
        .arrow { color: #00d4ff; font-size: 1.2em; }
        footer { text-align: center; padding: 30px; color: #555; border-top: 1px solid #222; }
    </style>
</head>
<body>
    <header>
        <h1>DevOps Portfolio</h1>
        <p>Cloud Infrastructure | CI/CD Pipelines | Container Orchestration</p>
        <div class="badges">
            <span class="badge">Azure</span>
            <span class="badge">Terraform</span>
            <span class="badge">Docker</span>
            <span class="badge">Kubernetes</span>
            <span class="badge">Jenkins</span>
        </div>
    </header>

    <div class="section">
        <h2>Projects</h2>
        <div class="cards">
            <div class="card">
                <h3>Flask App on AKS</h3>
                <p>Containerized a Python Flask application and deployed it on Azure Kubernetes Service with load balancing and auto-scaling.</p>
            </div>
            <div class="card">
                <h3>Infrastructure as Code</h3>
                <p>Provisioned Azure resources including AKS, ACR, and Resource Groups using Terraform with automated state management.</p>
            </div>
            <div class="card">
                <h3>CI/CD Pipeline</h3>
                <p>Built an automated Jenkins pipeline that builds Docker images, pushes to ACR, and deploys to Kubernetes on every code push.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>Pipeline Architecture</h2>
        <div class="pipeline">
            <p style="color:#aaa">Every push to GitHub triggers this automated pipeline:</p>
            <div class="steps">
                <div class="step">GitHub Push</div>
                <div class="arrow">→</div>
                <div class="step">Jenkins Build</div>
                <div class="arrow">→</div>
                <div class="step">Docker Image</div>
                <div class="arrow">→</div>
                <div class="step">Push to ACR</div>
                <div class="arrow">→</div>
                <div class="step">Deploy to AKS</div>
                <div class="arrow">→</div>
                <div class="step">Live 🚀</div>
            </div>
        </div>
    </div>

    <footer>
        <p>Deployed on Azure Kubernetes Service | Powered by Docker & Jenkins</p>
    </footer>
</body>
</html>
"""

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
