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

        stage('Deploy to Remote Server') {
            steps {
                script {
                    def remoteDir = "/home/iot/Desktop/tecnologias-emergentes"
                    def serverIP = "192.168.200.135"
                    def user = "iot"
                    def password = "123"
                    sh """
                    sshpass -p ${password} -o StrictHostKeyChecking=no scp -r main.py test.py ${user}@${serverIP}:${remoteDir}
                    """

                    // SSH into the remote server and run the application
                    sh """
                    sshpass -p ${password} ssh ${user}@${serverIP} << EOF
                    cd ${remoteDir}
                    pkill -f "uvicorn" || true
                    nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                    exit
                    EOF
                    """
                }
            }
        }
    }
}