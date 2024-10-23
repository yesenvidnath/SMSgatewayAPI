# SMS Gateway API

This API allows seamless integration with the **Dialog SMS Gateway**, enabling you to send and manage SMS communications programmatically.

## Features
- **Dialog SMS Gateway** integration.
- Send single or bulk SMS.
- Real-time message status tracking.
- RESTful API interface for easy integration.

## Installation

1. Clone the repository:
   git clone https://github.com/yesenvidnath/SMSgatewayAPI.git
   cd SMSgatewayAPI

2. Install dependencies:
   npm install

3. Set up environment variables:
   - API_KEY: Your Dialog SMS gateway service API key.
   - API_URL: The base URL for the Dialog SMS service.

4. Start the application:
   npm start

## Usage

To send an SMS, use the following HTTP request:

POST /api/send
Content-Type: application/json

{
    "recipient": "+123456789",
    "message": "Your message here"
}

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
