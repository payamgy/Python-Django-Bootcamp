
# Problem Statement:
You are tasked with developing a program to process a log file generated by a web server and extract useful information for analysis. The input file, named `access.log`, contains log entries in the Common Log Format (CLF) as follows:

```log
192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [10/Oct/2023:13:56:12 +0000] "POST /submit_form HTTP/1.1" 302 -
192.168.1.3 - - [10/Oct/2023:13:56:43 +0000] "GET /images/logo.png HTTP/1.1" 304 0
192.168.1.4 - - [10/Oct/2023:13:57:18 +0000] "GET /page.html HTTP/1.1" 404 0
192.168.1.5 - - [10/Oct/2023:13:57:45 +0000] "GET /styles/main.css HTTP/1.1" 200 4567
127.0.0.1 - - [10/Apr/2022:10:11:23 +0000] "GET /index.html HTTP/1.1" 200 3456
127.0.0.1 - - [10/Apr/2022:10:12:45 +0000] "POST /login HTTP/1.1" 302 0
127.0.0.1 - - [10/Apr/2022:10:13:57 +0000] "GET /about.html HTTP/1.1" 404 0
127.0.0.1 - - [10/Apr/2022:10:14:12 +0000] "GET /contact.html HTTP/1.1" 200 2345
127.0.0.1 - - [10/Apr/2022:10:15:30 +0000] "GET /products HTTP/1.1" 200 5432
127.0.0.1 - - [10/Apr/2022:10:16:02 +0000] "GET /products/item123 HTTP/1.1" 200 6789

```

Each line in the file represents a log entry, where:
- The first field is the client's IP address.
- The second field (usually a hyphen) is the identity of the client, which is typically omitted.
- The third field (usually a hyphen) is the user's name, which is also typically omitted.
- The fourth field is the timestamp of the request in the format `[day/month/year:hour:minute:second + timezone]`.
- The fifth field is the request line, which includes the HTTP method, requested URL, and HTTP version.
- The sixth field is the HTTP status code returned by the server.
- The seventh field is the size of the response body in bytes. For non-file requests (e.g., status code 302 or 304), this field may contain a hyphen.

Your task is to write a Python program that reads the `access.log` file, analyzes the log entries, and generates a summary report in a new file named `log_summary.txt`. The summary report should include the following information:

1. Total number of requests processed.
2. Number of requests for each HTTP method (GET, POST, etc.).
3. Number of requests for each HTTP status code (200, 404, etc.).
4. Total size of the response body in bytes.

The summary report should be formatted as follows:

```yml
Total Requests: 5
HTTP Methods:
  GET: 3
  POST: 1
  ...
HTTP Status Codes:
  200: 2
  302: 1
  ...
Total Response Body Size: 5767 bytes
```

Ensure the following considerations:
- Properly handle file reading and writing operations, including error handling.
- Implement logic to parse and analyze each log entry.
- Format the output in a neat and organized manner.
- Consider using appropriate data structures and functions to simplify the implementation and improve readability.