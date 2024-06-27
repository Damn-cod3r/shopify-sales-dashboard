# Shopify Sales Data Visualization



## Description

This Django application connects to the Shopify API to pull a merchant’s sales data and displays the daily sales data in both a chart and tabular format. The application fetches sales data for the last 10 days and stores it in a Django database. The data is then visualized in table and chart format using Chart.js.

## Features

- Connects to the Shopify API to fetch sales data.
- Stores sales data in a Django database.
- Displays sales data in a bar chart using Chart.js.
- Shows sales data in a tabular format.

## Getting Started

### Prerequisites

- Python 3.12.2
- Django 5.0.6
- ShopifyAPI
- MySQL Database

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Damn-cod3r/shopify-sales-dashboard.git
    cd shopify-sales-dashboard
    ```

2. Install the required packages:

    ```bash
    pip install shopifyapi
    pip install mysqlclient
    ```
 3. Set up your MySQL database:

    - Install MySQL Server if not already installed.
    - Create a new database for the project.
    - Update `sales_dashboard/settings.py` with your MySQL database configuration:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

4. Set up your Shopify API credentials:

    - Register on the [Shopify Developer Portal](https://shopify.dev/) and create an account.
    - Obtain your API key, API secret, and access token.
    - Update your settings with your Shopify credentials.

5. Run database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Fetch the latest sales data from Shopify:

    ```bash
    python manage.py fetch_sales
    ```

7. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Usage

- The application fetches sales data for the last 10 days.
- Sales data is visualized in a bar chart and displayed in a table.

## Example Screenshot

![image](https://github.com/Damn-cod3r/shopify-sales-dashboard/assets/72695900/6b25f9ab-96ff-45eb-a99b-9f0aadd9dcae)

![image](https://github.com/Damn-cod3r/shopify-sales-dashboard/assets/72695900/0c18665c-4e4c-418e-b9e4-2763e71a6e97)

![image](https://github.com/Damn-cod3r/shopify-sales-dashboard/assets/72695900/a064fd29-a540-4cd3-933a-dcf2610e1a70)

![image](https://github.com/Damn-cod3r/shopify-sales-dashboard/assets/72695900/2d95cc6e-0f9d-4365-9d9d-79e823e4146c)


## Project Structure

- `sales_dashboard/`: Main Django project directory.
- `sales/`: Django app for handling sales data.
- `templates/`: HTML templates for rendering views.
- `static/`: Static files (CSS, JavaScript).
- `management/commands/fetch_sales.py`: Script to fetch sales data from Shopify API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Shopify Developer Portal](https://shopify.dev/)
- [Chart.js](https://www.chartjs.org/)
- [Django Documentation](https://docs.djangoproject.com/)

## Contact

For any questions or feedback, please contact [chidambaram097@gmail.com](chidambaram097@gmail.com).
