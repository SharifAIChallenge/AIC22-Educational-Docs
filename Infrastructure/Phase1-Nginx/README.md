## Sources:
* Videos:
  - [Nginx basics](https://www.youtube.com/watch?v=C5kMgshNc6g)
  - [Nginx configuration](https://www.youtube.com/watch?v=JaVb-VRlihg)
  - [Load balancing with nginx](https://www.youtube.com/watch?v=a41jxGP9Ic8)
  - [Master in nginx](https://www.youtube.com/watch?v=GGS6KMRbONo)
* Documents:
  - [Nginx basics](https://nginx.org/en/docs/beginners_guide.html)

## Challenge:
1. Clone the repo and start the flask app
2. Put `nginx.conf` file in `/etc/nginx/conf.d/` directory and start Nginx.
3. Complete Nginx configuration with these capabilities:
  * Send all incoming requests to flask backend
  * If the request is from a mobile device, send it to the `/mobile` endpoint.
  * If the request is not from a mobile device and it's trying to get `/mobile`, Nginx should block the request by 403 status code.
  * Requests to the `/limit` endpoint should have a limitation (10 requests per minute)
  * `/static` endpoint should load static files in `/static` directory
