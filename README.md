# Ingredient Substitution Tool  
  
## Overview
  
The **Ingredient Substitution Tool** is a web application designed to help users find and contribute cooking ingredient substitutes. This application is built with a React.js frontend and a Django REST Framework backend.  
  
### Features  
  
- **Find Ingredient Substitutes**: Input an ingredient and get a recommended substitute.  
- **View Common Substitutes**: Browse a list of common ingredient substitutions.  
- **Submit New Substitutes**: Add new substitutions to the list.  
  
## Project Structure  
  
The project is organized into two main parts:  
  
- `frontend`: Contains the React.js application.  
- `backend`: Contains the Django application.  
  
## Technology Stack  
  
- **Frontend**: React.js  
- **Backend**: Django REST Framework  

## Prerequisites  
  
- Python 3.x  
- Node.js  
- Django  
- pip  
- Virtualenv  
  
## Setup and Installation  
  
### Backend Setup  
  
1. **Clone the repository**:  
    ```bash  
    git clone https://github.com/your-username/ingredient-substitution-tool.git  
    cd ingredient-substitution-tool/backend  
    ```  
  
2. **Create and activate a virtual environment**:  
    ```bash  
    python3 -m venv env  
    source env/bin/activate  # On Windows use `env\Scripts\activate`  
    ```  
      
5. **Apply migrations and run the Django server**:  
    ```bash  
    python manage.py migrate  
    python manage.py runserver  
    ```  
  
### Frontend Setup  
  
1. **Navigate to the frontend directory**:  
    ```bash  
    cd ../frontend  
    ```  
  
2. **Install dependencies**:  
    ```bash  
    npm install  
    ```  
  
3. **Start the React development server**:  
    ```bash  
    npm start  
    ```  
  
## Usage  
  
- Visit `http://localhost:3000` in your browser to use the Ingredient Substitution Tool.  
- Use the forms on the page to find substitutes, view common substitutes, or submit new ones.  


  
For questions or comments, please contact [Dheeraj Reddy Kukkala](mailto:your.kdheerajreddy97@gmail.com).  
