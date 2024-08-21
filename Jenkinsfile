pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3 function.py'  // Cambia el comando según tus necesidades
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'pytest tests'  // Ejecuta las pruebas
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Aquí iría la lógica de despliegue, como copiar archivos o ejecutar scripts
            }
        }
    }
}