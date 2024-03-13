# H&M Color Trends & Product Info Chatbot
Youtube link: https://youtu.be/fv-5G4PHppA

Explore the latest color trends and product details from H&M with our interactive chatbot and data visualizations.

# Technologies Used 
Streamlit for web app interface
Selenium for web scraping
Pandas for data manipulation
Seaborn and Matplotlib for data visualization
OpenAI (GPT-3.5-turbo) for chatbot intelligence
dotenv for environment variable management

# Problem Statement
Our project aims to aggregate and visualize product information from H&M to identify color trends and provide users with an interactive platform to inquire about products through a chatbot powered by OpenAI's GPT-3.5-turbo model.


## How to Run
1. Ensure Python and pip are installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory and install required packages using pip install -r requirements.txt.
4. Run streamlit run app.py to start the Streamlit application.
5. Visit the local URL provided by Streamlit in your web browser to interact with the application.


## Reflections

Learning Experience
Advanced Web Scraping Techniques: This project deepened our understanding of web scraping, especially in handling dynamic content with tools like Selenium, which goes beyond basic static content scraping.
Data Processing and Visualization: We gained valuable experience in processing scraped data for clarity and coherence and visualizing this data to uncover insights, such as color trends among H&M products.

Challenges Faced
Dynamic Content Loading: One of the initial challenges might have been dealing with dynamically loaded content on H&M's product listing pages. Traditional scraping methods without JavaScript execution would not load all products, requiring a more sophisticated approach with Selenium to interact with the page as a user would.


