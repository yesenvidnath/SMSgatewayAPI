from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to send SMS
def send_sms(phone_number, sender_id, message):
    api_url = "https://sms.send.lk/api/v3/sms/send"
    api_token = "2334|bH0R9fligE86CIzDKMZmViVZmykcOD0xPCLyrqhK"  # Replace with your actual access token

    msg_data = {
        "recipient": phone_number,
        "sender_id": sender_id,
        "message": message
    }

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_token}",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(api_url, json=msg_data, headers=headers, verify=False)

        if response.status_code == 200:
            return {"status": "success", "data": response.json()}
        else:
            return {"status": "error", "message": response.text}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

@app.route('/send_sms', methods=['POST'])
def send_sms_endpoint():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')
    sender_id = "SendTest"  # Fixed sender ID

    if not phone_number or not message:
        return jsonify({"status": "error", "message": "phone_number and message are required"}), 400

    result = send_sms(phone_number, sender_id, message)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
