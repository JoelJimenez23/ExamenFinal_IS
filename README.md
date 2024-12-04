Here's a complete and well-structured README:

# ExamenFinal_IS

A Flask-based application for the final exam project in Information Systems.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- `pip` (Python package installer)

## How to Run

Follow these steps to set up and run the project:

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   cd ExamenFinal_IS
   ```

2. **Set Up a Virtual Environment**  
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**  
   Install the required Python packages:
   ```bash
   pip install flask coverage
   ```

4. **Run the Application**  
   Start the Flask application:
   ```bash
   python app.py
   ```

   By default, the app will run at `http://127.0.0.1:5000`. Open this URL in your web browser to access the application.

5. **Run Tests and Coverage Report**  
   To run the unit tests and generate a coverage report:
   ```bash
   python3 -m coverage run -m unittest test_app.py
   python3 -m coverage report
   ```
