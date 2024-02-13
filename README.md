# Email Sending Service

This Flask application listens for POST requests containing email details and sends an email using those details through a specified Gmail account. It's designed for simplicity and ease of testing email functionality.

## Setup and Installation

### Prerequisites

- Python 3.x
- A Gmail account
- Git (optional)

### Environment Setup

1. **Clone the repository** (if available online):
    ```bash
    git clone https://your-repository-link.git
    cd your-project-directory
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # Use `env\Scripts\activate` on Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install Flask requests
    ```

### Configuring Gmail SMTP

Before using your Gmail account to send emails, you need to configure it to allow access through this application.

1. **Allow Less Secure Apps** (if not using 2-Step Verification):
    - Navigate to Google Account -> Security -> Less secure app access -> Turn on access (Not recommended if you use 2-Step Verification).

2. **Using 2-Step Verification**:
    - Set up an App Password for your Gmail account:
        - Go to Google Account -> Security -> App passwords -> Select app (Mail) -> Select device -> Generate.
    - Use this generated App Password in your application.

### Updating the Application

Update `app.py` with your Gmail details:

```python
sender_email = "your_email@gmail.com"  # Your Gmail address
password = "your_app_password"  # Your Gmail App Password
```

Ensure Gmail's SMTP settings are correct:

```python
with smtplib.SMTP('smtp.gmail.com', 587) as server:
```

## Running the Application

Execute the following command to run the application:

```bash
python app.py
```

## Using the Service

To send an email, make a POST request to `http://127.0.0.1:5000/emails` with a JSON payload structured as follows:

```json
{
  "to": "recipient@example.com",
  "subject": "Your Subject Here",
  "body": "The content of your email goes here."
}
```

### Sending a POST Request

#### Using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/emails \
-H "Content-Type: application/json" \
-d '{"to": "recipient@example.com", "subject": "Hello", "body": "Hello World!"}'
```

#### Using Python `requests`:

```python
import requests

url = 'http://127.0.0.1:5000/emails'
data = {
    "to": "recipient@example.com",
    "subject": "Hello",
    "body": "Hello World!"
}

response = requests.post(url, json=data)

print(response.text)
```

### Expected Response

After making a POST request, you will receive a JSON response indicating the outcome of the operation:

- **Success**: `{"message": "Email sent successfully"}`
- **Failure**: A JSON object containing an `error` key with details about the failure.

## Deployment

This guide includes steps for deploying the application on Heroku. Ensure you replace sensitive information like email and password with environment variables in production for security.

