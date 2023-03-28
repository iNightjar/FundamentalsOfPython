import requests

# Make API request
response = requests.get("https://graph.facebook.com/v2.7/me", params={
    "access_token": "EAAGYR5ZBqgo8BAAZAeZAQCDIDL6rcQvDc0YyGwiR8rQPKTYXZBGzMFWsCDXgdRC9MPcsq7U6NWGhMzHhP9ivJgNcGtQxwscIpJ3jnWCHEHC0EMmg7CMcy5fJyadSjLQDFqv4rtmyvuV7ewD0aAbtce9AJ0ZBiZBmuXwKt8OVfFWZBBUEAe55bgkEZBso2fl8VikHVFzUJiL5KzS3Yd6N682X7JxdmTU6s6MZD"
})

# Check status code
if response.status_code == requests.codes.ok:
    # Handle successful response
    print(response.json())
else:
    # Handle error response
    error_response = response.json()
    # print(error_response)
    error_message = error_response.get(
        "error", {}).get("message", "Unknown error")
    print("API request failed: {}".format(error_message))
