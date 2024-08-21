pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3 main.py'  // Cambia el comando según tus necesidades
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'pytest test.py'  // Ejecuta las pruebas
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