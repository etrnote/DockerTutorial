# Instructions

1. to run:
```bash
docker compose up --build
```

2. open `http://localhost:5000` on your web browser

3. to add a message:
```
curl -X POST -H "Content-Type: application/json" -d '{"content":"Your message content","creator":"Message creator"}' http://localhost:5000/messages
```
In this curl command, we use the -X POST option to specify the HTTP method as POST.   
The `-H` option sets the "Content-Type" header to "application/json" to indicate that we're sending JSON data in the request body.  
The `-d` option is used to specify the JSON payload containing the message content and creator details.   
Finally, we provide the URL of the server's /messages endpoint.

4. connect to db:
   ```bash
   docker exec -it python_server_demo-db-1 psql -U dbuser messages
   ```

   ```sql
   \dt
   ```

   ```sql
   \d+ message
   ```

   
docker compose down <--volumes>