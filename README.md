# Hindi_Song_Recommender_from_Image
This project uses computer vision and machine learning to recommend Hindi songs based on the contents or mood of an image. By analyzing the visual features, color palette, and emotional tone of an uploaded image, the system suggests a suitable Hindi song that matches the detected vibe — such as romantic, sad, energetic, or peaceful.

## Building the Docker Image

To build the Docker image for this application, make sure you have Docker installed and running. Then, navigate to the project's root directory in your terminal and run the following command:

```bash
docker build -t hindi-song-recommender .
```

This command will:
- `docker build`:  Initiate the Docker image building process.
- `-t hindi-song-recommender`: Tag the image with the name `hindi-song-recommender`. You can choose a different tag if you prefer.
- `.`: Specify that the Dockerfile is located in the current directory.

After the build process is complete, you can verify that the image was created by running:

```bash
docker images
```
You should see `hindi-song-recommender` in the list of your Docker images.

## Deployment Options

Once you have the application running locally or have built the Docker image, here are a few options to deploy it:

### 1. Streamlit Sharing

Streamlit Sharing is a free service provided by Streamlit to deploy public applications directly from your GitHub repository.

**Steps:**
1.  Ensure your project is in a public GitHub repository.
2.  Make sure you have a `requirements.txt` file.
3.  Go to [share.streamlit.io](https://share.streamlit.io/) and sign up or log in.
4.  Click on "Deploy an app" and connect your GitHub account.
5.  Select the repository, branch, and the main Python file (`app.py`).
6.  Click "Deploy".

Your app will be deployed with a unique URL.

### 2. Deploying the Docker Image

If you have built the Docker image as described above, you can deploy it to various cloud platforms that support Docker containers. Here are a couple of popular options:

**a. Google Cloud Run**

Google Cloud Run is a fully managed serverless platform that enables you to run stateless containers.

**General Steps:**
1.  **Push your Docker image to Google Container Registry (GCR) or Artifact Registry:**
    ```bash
    # Tag your local image
    docker tag hindi-song-recommender gcr.io/YOUR_PROJECT_ID/hindi-song-recommender

    # Configure Docker to use gcloud as a credential helper
    gcloud auth configure-docker

    # Push the image
    docker push gcr.io/YOUR_PROJECT_ID/hindi-song-recommender
    ```
    Replace `YOUR_PROJECT_ID` with your actual Google Cloud Project ID.
2.  **Deploy to Cloud Run:**
    You can do this via the Google Cloud Console UI or using the `gcloud` command-line tool:
    ```bash
    gcloud run deploy hindi-song-recommender-service         --image gcr.io/YOUR_PROJECT_ID/hindi-song-recommender         --platform managed         --region YOUR_REGION         --port 8501         --allow-unauthenticated
    ```
    Replace `YOUR_PROJECT_ID` and `YOUR_REGION` with your specific details. `--allow-unauthenticated` makes the service publicly accessible.

**b. AWS App Runner**

AWS App Runner is a fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs, at scale and with no prior infrastructure experience required.

**General Steps:**
1.  **Push your Docker image to Amazon Elastic Container Registry (ECR):**
    - Create an ECR repository.
    - Authenticate Docker to your ECR registry.
    - Tag your local image with the ECR repository URI.
    - Push the image to ECR.
    (Refer to AWS documentation for specific `aws ecr` commands)
2.  **Create an App Runner Service:**
    - Open the AWS App Runner console.
    - Choose "Create an App Runner service".
    - Select "Container registry" as the source.
    - Choose "Amazon ECR" as the provider and select your image.
    - Configure the service settings, including port (8501 for Streamlit).
    - Deploy.

**c. Other Platforms**

Many other platforms support deploying Docker containers, such as:
-   Azure Container Instances
-   Heroku (using their container registry)
-   DigitalOcean App Platform

The general idea is to push your Docker image to a container registry (like Docker Hub, GCR, ECR) and then point the hosting service to that image.

Remember to manage your API keys and other sensitive information securely, especially when deploying to public platforms. Consider using environment variables or secret management services provided by the cloud platforms.
