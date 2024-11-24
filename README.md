# Moin moin: Smart City

Moin moin is a project created and developed by @fabridamicelli, @FBruzzesi, and @JurijWollert during the [NumHack 2024](https://github.com/numfocus/numhack-2024) hackaton for the category **build**.

## Project Title

Moin Moin

## Description

Moin Moin is a web application that serves two goals:

* On one hand, it simplifies the process of reporting issues around a city for citizens. All that is required is to take a picture of what a citizen considers to be a problem worth addressing by the municipality, and point where such issue is located. The application will then categorize the problem into the responsable department which is more suited to address it.
* On the other hand, the application provides a map with the reported and categorized issues for the municipality officers, which serves as a tool to prioritize and dispatch the work to the different departments.

## Core Features

* Digitalization of the process of reporting issues around the city.
* Automatic categorization of the reported problem via CLIP model (text and images embeddings).

## Submission Items

* **Deliverable**: Web application with the two pages, one for the citizens to report the issues and another for the municipality officers to see the reported problem both on a map and on a table. This is easily deployable via docker compose.
* **Documentation**: TODO

## Future Work

There are a lot of features that we would like to implement to improve the application:

* To be _actually_ of easy access to the citizens, what's now a dedicated page in the web application, should be available as a mobile app. This would allow the citizens to report issues on the go, by taking a picture with their phone and allowing GPS to locate where the issues is.
* Allow a citizen to upload more than one image at the time.
* The categorization of the reported issues could be improved by using a pretrained Image-Text-to-Text LLM model (such as [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)), with structured output (being the categories we have). The drawback of this approach is that it would require significant more computational resources.
* For the municipality officers in charge, we would consider the possibility of automatically create bouding boxes on the issue for each image, and allow them to change it if necessary before dispatching the work downstream.
