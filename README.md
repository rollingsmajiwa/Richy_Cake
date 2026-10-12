# Richie's Cake

## Project Brief

The **Richie's Cake** platform is a modern, responsive full-stack web application designed for cake enthusiasts and customers looking for artisanal, handcrafted bakery products. It provides a streamlined interface for browsing daily menu offerings, customizing orders, and learning about bakery services to ensure an effortless ordering experience.

## Business Rationale

In a competitive bakery market, clarity, aesthetic presentation, and seamless user interaction are key. This project addresses two primary business needs:

* **Brand Authority:** A clean, semantic layout styled with Tailwind CSS establishes brand trust and positions Richie's Cake as a premium artisanal bakery.
* **Order Management:** Structured forms and Cloudinary image integration ensure product media are stored accurately and delivered securely.

## Technologies Used

* **Django 6.1.1:** Robust Python web framework for backend architecture, routing and secure session management.
* **Tailwind CSS & HTML5:** Semantic structure and custom utility-first styling for maximum responsiveness across devices.
* **Cloudinary:** Cloud storage service for handling media uploads, cake catalog images, and user-generated custom cake assets.
* **WhiteNoise:** Efficient static asset file serving optimized for production deployments.
* **Render:** Production cloud platform hosting the web service and PostgreSQL database configuration.
* **Git/GitHub:** Version control, continuous integration, and feature-based development branching.

## Accessibility Features

* **Semantic HTML:** Implemented using `<header>`, `<main>`, `<section>`, `<nav>`, and `<footer>` tags for screen readers and search engine optimization (SEO).
* **List Structures & Navigation:** Key features, catalog items, and interactive routes are organized in `<ul>` and `<li>` elements, offering clear navigation for assistive technologies.
* **Color Contrast:** Deep red accents paired with high-contrast text ensure high readability standards.

## Product Features

The application features two core tiers of cake and bakery offerings:

* **Daily Specials:** Freshly baked cupcakes, pastries, and signature daily slice catalog for fast ordering.
* **Elite Tier Creations:** Bespoke artisan multi-tiered wedding and milestone cakes built from scratch to customer specifications.

## Git Workflow

* **Fork the Repository:** Create your own copy of the project to work on.
* **Create a Feature Branch:**
  ```bash
  git checkout -b YourFeatureName
Commit Your Changes:

Bash
```
git commit -m "Add new bakery layout section"
```
Push to Branch:

Bash
```
git push origin feature/YourFeatureName
```
Open a Pull Request (PR): Describe your changes clearly and link related project issues.

## Set Up Instructions
a. Clone this repository on your local machine:

Bash
```
git clone https://github.com/rollingsmajiwa/Richy_Cake.git
```
```cd Richy_Cake```

b. Create and activate a virtual environment:

Bash
```
python -m venv .venv
```
```source .venv/bin/activate```  
### On Windows

use: .venv\Scripts\activate
c. Install required dependencies:

Bash
```
pip install -r requirements.txt
```
d. Configure environment variables in a local .env file (SECRET_KEY, CD_CLOUD_NAME, CD_KEY, CD_SECRET).

e. Run database migrations and start the development server:

Bash
```
python manage.py migrate
```

```python manage.py runserver```

## Screenshot

## Author
Rollings Majiwa

GitHub: [https://github.com/rollingsmajiwa](https://github.com/rollingsmajiwa)

Email: [rollingsmajiwa@gmail.com](rollingsmajiwa@gmail.com)

## Get Started
Interested in the code behind Richie's Cake? You can reach me directly via my profile or open an issue for collaboration. Visit my [GitHub profile](https://github.com/rollingsmajiwa)