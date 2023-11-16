# Projects

## End-to-end ML Orchestration
## CI/CD in ML
### Setting Up Docker
This was only tested on Ubuntu 22.04
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

```
# Installing Docker-ce
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl enable --now docker

# Adding docker-compose-plugin
sudo apt install python3-pip
pip install --upgrade pip
sudo pip install docker-compose
```

### Setting Up Jenkins Server
- https://www.cloudbees.com/blog/how-to-install-and-run-jenkins-with-docker-compose
- https://www.cloudbees.com/blog/jenkins-multibranch-pipeline-with-git-tutorial

1. Generate key pairs for sshing into jenkins container
    ```
    ssh-keygen -t rsa -f ~/.ssh/jenkins_agent_key
    ```
2. cd to the `jenkins` directory and update `docker-compose.yml` file with the content from the new pubkey generated in step 1.
    ```
    version: '3.8'
    services:
    jenkins:
        .
        .
        .
    agent:
        .
        .
        environment:
            - JENKINS_AGENT_SSH_PUBKEY=<NEW-PUB-KEY-HERE>

    ```
3. build and run docker containers for master and slave jenkins
    ```
    sudo docker-compose build up -d
    sudo docker logs agent
    ```
    copy the password displayed here. It will be used during the setup on Jenkins
4. Create Jenkins credential
5. Create a new node/agent
6. Create a job
