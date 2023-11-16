# CI/CD for Machine Learning: Search Bar with SBERT and FAISS

## Objective

Create an SBERT and FAISS based search bar and ensure that any change in the training data, i.e feature store, or any change in the code, i.e resulting from hyper-parameter tuning or bert/faiss model upgrade, will trigger an end-to-end training job without disruption of the service already in production

## Scope
In this current work, we assume that the search bar is already built and we only focus on introducing the automation pipeline that monitors changes in data and/or model and therefore train and deploy a new model to production

## Approach
We are going to use 
- Jenkins for continuous deployment: this will keep track of code change
- Deepcheck/Airflow for auto-training of the model: this will keep track of data change

### To Do 
- [x] Create `stage` and `prod` branch
- [x] Containerize the application
- [x] Setup Jenkins server (dockerized)
- [x] Create Jenkins jobs to continuously poll from `stage`
- [x] Create auto-trigger jobs on push to a PR
- [x] Create data drift checker
- [x] Pipeline to retrain the model on each data change
- [x] Update code change in the remote searchbar server
- [x] Create functional unit tests
- [x] Create PR to merge `stage` to `prod`
- [x] Documentation
- [ ] Pipeline for daily changes in data
  - [ ] Save a copy of current training dataset
  - [ ] Generate new training dataset
  - [ ] Check whether there is a difference: raw_data = utils.generate_data(project_description_df, project_topics_df)
  - [ ] Create a PR to trigger the entire pipeline
- [ ] ...

  

### How to push daily updates
1. Checkout a new branch from `stage`. 
   ```
   # while you are in the directory
   git checkout stage
   git checkout -b <new-branch>
   ```
2. Make your changes locally, commit and push to remote repo
   ```
   git add .
   git commit -m '<this can be any sentence of your choice>'
   # since multiple people might be working off of stage, always pull-rebase stage for new changes
   git pull origin stage --rebase
   git push origin <new-branch>
   ```
3. Go to github repo and create a pull request against `stage`
   From here, the pipeline to run tests will be automatically triggered. 
   If tests run successfully, the new changes will be deployed to stage and production.
   If tests fail, your PR will be rejected and you will be asked to make changes

### Tutorial on Jenkins and CI/CD for ML project

1. Setup Jenkins Server
   1. Setup docker and docker-compose
   2. Setup Jenkins with docker-compose
   3. Installing required plugins and restart
      1. Github Pull Request
      2. Github Auto Merge
      3. SSH
      4. Github Integration (github-pullrequest-plugin)
   5. Login Jenkins container and create conda env manually
2. Integrate Jenkins with Github 
   1. Generating tokens
   2. Webhooks
   3. Required Jenkins Plugins
3. Setup Searchbar Server
   1. setup ec2
   2. install: git, requirements
   3. clone the repo
   4. set remote-url with access token
   5. set config with email and name
4. Script to check for data changes
5. Unittests
6. JenkinsFile
