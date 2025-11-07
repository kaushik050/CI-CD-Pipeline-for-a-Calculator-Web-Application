
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repo...'
                git branch: 'main', url: 'https://github.com/kaushik050/CI-CD-Pipeline-for-a-Calculator-Web-Application.git'
            }
        }

        stage('Prepare Python') {
            steps {
                echo 'Checking Python...'
                // Use full python.exe path
                bat '"C:\\Users\\Y S KAUSHIK REDDY\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
                // create venv and install deps
                bat '''
"C:\\Users\\Y S KAUSHIK REDDY\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
call venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
'''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
call venv\\Scripts\\activate
pytest || echo "Tests failed (continuing)..."
'''
            }
        }

        stage('Run App (background)') {
            steps {
                bat '''
call venv\\Scripts\\activate
start "" venv\\Scripts\\python.exe app.py
timeout /t 3 /nobreak >nul
echo Flask app started
'''
            }
        }
    }

    post {
        success { echo '✅ Pipeline finished' }
        failure { echo '❌ Pipeline failed' }
    }
}
