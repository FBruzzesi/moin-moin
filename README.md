# Moin moin: Empowering Communities to Build Better Cities

Moin moin is a project created and developed by [@fabridamicelli](https://github.com/fabridamicelli), [@FBruzzesi](https://github.com/FBruzzesi), and [@JurijWollert](https://github.com/JurijWollert) during the [NumHack 2024](https://github.com/numfocus/numhack-2024) hackaton for the category **build**.

## Table of Contents

- [Moin moin: Empowering Communities to Build Better Cities](#moin-moin-empowering-communities-to-build-better-cities)
  - [Table of Contents](#table-of-contents)
  - [Project Title](#project-title)
  - [Description](#description)
  - [Core Features](#core-features)
  - [Submission Items](#submission-items)
  - [Future Work](#future-work)
  - [Repository Structure](#repository-structure)
  - [Getting started](#getting-started)
    - [Docker Compose](#docker-compose)
    - [Manual Setup](#manual-setup)
  - [Tech Stack](#tech-stack)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Contributors](#contributors)
  - [License](#license)

## Project Title

Moin Moin: Empowering Communities to Build Better Cities

## Description

Moin Moin is a web application designed to bridge the communication gap between citizens and municipal governments, making urban problem-solving more efficient and accessible. Moin Moin aims to empower citizens to take an active role in maintaining and improving their communities.

Its core goals are:

* **For Citizens**: Simplify the process of reporting urban issues, such as potholes, broken streetlights, or illegal dumping, to the local government. Users only need to take a photo of the issue, indicate its location on a map, and optionally provide a short description. The system then categorizes the problem and directs it to the appropriate department.
* **For Municipal Officials**: Provide a centralized dashboard where city officers can view and prioritize citizen-reported issues. The dashboard includes both a map view and a tabular format, enabling officials to efficiently manage and dispatch tasks to the relevant teams.

By streamlining this interaction, Moin Moin empowers citizens to actively participate in improving their communities and helps municipalities optimize their response efforts. This act of active citizenship aligns with the principles of the [broken windows theory](https://en.wikipedia.org/wiki/Broken_windows_theory), which posits that addressing small-scale urban problems promptly can prevent more severe decay and foster civic pride of communities.


## Core Features

1. **Citizen-Friendly Reporting**

    * Simple and intuitive interface for reporting urban issues digitally.
    * Ability to attach an image, mark a location on the map, and add an optional description.

2. **Automatic categorization of issues**

    * Uses a CLIP-based model to process images and descriptions into predefined departments.
    * Currently the possibilities are: Infrastructure, Public Safety, Waste Management and Cleanliness, Public Amenities and Facilities, Street Signage and Markings.

3. **Dashboard for Officials**

    * Interactive map displaying all reported issues with real-time categorization.
    * Tabular view for sorting and filtering issues by category, priority, time since upload.

4. **Deployability**

    * Ready-to-use solution deployable via Docker Compose for quick adoption.
    * Extremely frugal in terms of resources required to run it, making it suitable for small municipalities.

5. **Technical Documentation**

    * Step-by-step guide for deployment and setup.
    * Detailed architecture overview for developers.

## Submission Items

* **Deliverable**: A fully functional web application featuring both the citizen reporting page and the municipal officer dashboard.
* **Documentation**: [Repository Structure](#repository-structure), [Getting Started](#getting-started), and [Tech Stack](#tech-stack) sections.
* **Demo Video**: A video showcasing the application
    
    [![Watch it now](https://drive.google.com/file/d/1LdL8C3gbD0zsMX4-NNfKo68huBDYRFSP/view)](https://drive.google.com/file/d/1LdL8C3gbD0zsMX4-NNfKo68huBDYRFSP/view)

## Future Work

To enhance its utility and scalability, we envision several improvements:

1. **Citizen-Focused Enhancements**

   * Mobile App Development: Expand Moin Moin to a mobile application, enabling on-the-go issue reporting via smartphone cameras and GPS for automatic location tagging.
   * Batch Uploads: Allow users to upload multiple images for a single issue, providing more context for the problem.

2. **Advanced AI Features**

    * Improved Categorization: Integrate advanced multimodal models, such as [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct), to refine categorization accuracy and handle more complex scenarios.
    * Image Annotation Tools: Automatically generate bounding boxes around detected issues in uploaded images and allow citizens or municipal officers to adjust them as needed.

3. **Administrative Tools**

    * Customizable Categories: Enable municipalities to define and update issue categories dynamically to adapt to local needs.
    * Content Moderation: Implement a layer to automatically flag inappropriate or offensive images using AI-driven filters.

4. **Broader Impacts**

    * Localization and Accessibility: Provide support for multiple languages and accessibility standards to ensure inclusivity.
    * Data-Driven Insights: Aggregate issue data to provide analytics dashboards for municipal leaders, offering insights into trends and hotspots.

5. **Social and Environmental Impact**

    * Community Engagement: Integrate social features, such as the ability for citizens to upvote reported issues, highlighting problems that affect many.

By integrating these features, Moin Moin would become a comprehensive platform for civic engagement and urban development, driving meaningful improvements in cities worldwide.

## Repository Structure

The repository is organized as follows:

```terminal
moin-moin/
├── db/
│   └── .gitkeep
├── docker/
│   ├── backend.dockerfile
│   └── frontend.dockerfile
├── models/
│   └── .gitkeep
├── notebooks/
│   ├── *.ipynb
│   └── requirements.txt
├── src/
│   └── moin_moin/
│       ├── __init__.py
│       ├── backend/
│       └── frontend/
├── docker-compose.yml
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

- The main codebase is located in the `src/moin_moin` directory, which contains two subdirectories: `backend` and `frontend`. The backend directory contains the FastAPI API, which serves as the backend for the web application. The frontend directory contains the Streamlit web application, which serves as the frontend for the web application.

- The `docker` directory contains the Dockerfiles for building the backend and frontend images. The `docker-compose.yml` file is used to define the services for running the application using Docker Compose.

- `model` and `db` directories are used to store the models and the database, respectively. These are currently empty as the models and database are not included in the repository. Yet the first time the application is run, the models will be downloaded and the database will be created. These directories are mounted as volumes in the Docker Compose configuration.

- The `notebooks` directory contains Jupyter notebooks used for downloading images and evaluating the model. The `requirements.txt` file contains the dependencies for the notebooks.

## Getting started

### Docker Compose

The simplest and safest way to run the application is via [Docker Compose](https://docs.docker.com/compose/):

1. Clone and move into the repository:

    ```bash
    git clone https://github.com/FBruzzesi/moin-moin.git
    cd moin-moin
    ```

2. Build and run the application:

    ```bash
    docker-compose up --build -d
    ```

3. Now the webapp will be available at `http://localhost:8501`, and the endpoint for the API will be at `http://localhost:8081`.

4. To stop the application, run:

    ```bash
    docker-compose down
    ```

### Manual Setup

If docker is not an option, you can still run the application manually. We recommend using a virtual environment to avoid conflicts with your system's Python installation.

1. Clone and move into the repository:

    ```bash
    git clone https://github.com/FBruzzesi/moin-moin.git
    cd moin-moin
    ```

2. Create and activate a virtual environment:

    ```bash
    uv venv -p 3.12
    source .venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    uv pip install -e . --all-extras
    ```

    This will install all the dependencies in the same virtual environment (both for frontend and backend).

4. At this point, two terminals are needed to run the frontend and the backend. In the first terminal, run the backend:

    ```bash
    fastapi run src/moin_moin/backend/api.py --port 8081
    ```

    This will start the backend server at `http://localhost:8081`.

5. In the second terminal, run the frontend:

    ```bash
    streamlit run src/moin_moin/frontend/app.py --server.port=8501 --server.address=0.0.0.0
    ```

Now the webapp will be available at `http://localhost:8501`, and the endpoint for the API will be at `http://localhost:8081`.

## Tech Stack

### Backend

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs based on standard Python type hints.
- [SQLModel](https://sqlmodel.tiangolo.com/): A SQL database interface for FastAPI that simplifies database operations. We used [SQLite](https://www.sqlite.org/index.html) as the database engine.
- [Sentence-Transformers](https://www.sbert.net/): A Python library for computing sentence embeddings using transformer models. We used the [CLIP](https://www.sbert.net/examples/applications/image-search/README.html?highlight=clip) model to process images and descriptions in the same embedding space.

### Frontend

- [Streamlit](https://streamlit.io/): An open-source app framework for Machine Learning and Data Science projects. We used Streamlit to create the frontend web application for Moin Moin.
- [Geopy](https://geopy.readthedocs.io/en/stable/): A Python library for geocoding and reverse geocoding. We used Geopy to convert human-readable addresses into latitude and longitude coordinates of the reported issues.
- [httpx](https://www.python-httpx.org/): A fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

## Contributors

| Name | GitHub Profile |
|------|----------------|
| Fabrizio Damicelli | [@fabridamicelli](https://github.com/fabridamicelli) |
| Francesco Bruzzesi | [@FBruzzesi](https://github.com/FBruzzesi)           |
| Jurij Wollert      | [@JurijWollert](https://github.com/JurijWollert)     |

## License

This project is licensed under the Apache-2.0 license - see the [LICENSE](LICENSE) file for details.
