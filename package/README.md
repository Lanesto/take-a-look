# Project Configurations
This directory includes various settings for projects, mainly k8s.

## Kubernetes
This project uses blue/green deployment pattern, and followings are important metadatas:

* Naming convetion: { resource-type(shortname if possible) }-{ resource-name }-{ suffix }
* Namespace: takealook
* Apps: main, db, storage
* Labels: env, app

### Google Cloud Platform
We are using GCP API for prototype demonstration:

* <b>GKE - Google Kubernetes Engine</b>: For kubernetes cluster
* <b>GCR - Google Container Registry</b>: Project registry for containers built with Cloud Build
* <b>Cloud Build</b>: Automated build for docker images (cloudbuild.yaml)
* <b>Cloud Filestore</b>: Persistent volume for database and shared media files
