

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
   #Parse the 'url' Query Parameters
    urls = request.args.getlist('http://localhost:port/numbers?url=http://20.244.56.144/numbers/primes&url=http://20244.5% 144/mumber/bok url=http://20.244.56.144/numbers/odd')

    
    responses = []

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)  # Set timeout to 500 milliseconds
            if response.status_code == 200:
                data = response.json()
                if 'numbers' in data:
                    responses.append(data['numbers'])
        except requests.exceptions.RequestException:
            # Handle network errors or timeouts here.
            pass

   
    merged_numbers = sorted(set(number for numbers_list in responses for number in numbers_list))

    # Prepare the JSON Response
    response_data = {'numbers': merged_numbers}

    # Handle Errors (You can customize this part for different error scenarios)
    if not response_data['numbers']:
        return Response("No valid data found", status=400, content_type='text/plain')

    # Return the Response
    return jsonify(response_data), 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8008)