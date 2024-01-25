#!/bin/bash

# Send a request to 0.0.0.0:5000/catch_me with curl and set the User-Agent header to "Holberton School"
curl -s -X PUT -H "User-Agent: Holberton School" -d "user_id=98" 0.0.0.0:5000/catch_me
