# Moin moin: Empowering Communities to Build Better Cities

Moin moin is a project created and developed by @fabridamicelli, @FBruzzesi, and @JurijWollert during the [NumHack 2024](https://github.com/numfocus/numhack-2024) hackaton for the category **build**.

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

    * Uses a CLIP-based model to process images and descriptions into predefined departments (TODO: Add examples).

3. **Dashboard for Officials**

    * Interactive map displaying all reported issues with real-time categorization.
    * Tabular view for sorting and filtering issues by category, priority, time since upload.

4. **Deployability**
  
    * Ready-to-use solution deployable via Docker Compose for quick adoption.

5. **Technical Documentation**

    * Step-by-step guide for deployment and setup.
    * Detailed architecture overview for developers.

## Submission Items

* **Deliverable**: A fully functional web application featuring both the citizen reporting page and the municipal officer dashboard.
* **Documentation**:

    * Deployment instructions (via Docker Compose).
    * Internal architecture and workflow explanation

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
