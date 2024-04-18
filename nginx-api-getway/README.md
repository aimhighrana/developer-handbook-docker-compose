### Custom nginx with rate limit 
#### How this will work ?
1. docker-compose build 
2. docker-compose up -d

#### How to test ?
1. Test with jwt token
```
curl --location 'http://localhost/jwt' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhdXRoIiwic3ViIjoie1widXNlcm5hbWVcIjpcIjJlOGRmNzg5LTQzZTAtNDgwNS05OTM1LWQyODI4NDM5MjYyMlwiLFwicm9sZXNcIjpbXCIyODIxNjYxMjg2Mjg4MTMwMTVcIl0sXCJ0ZW5hbnRDb2RlXCI6XCI3NzYwOTlcIixcIm9yZ0lkXCI6XCIxNTM4NzkxNTYyNzAzMzU5MjRcIixcInJlY29yZE51bWJlclwiOm51bGwsXCJmcWRuXCI6bnVsbCxcInNjb3BlXCI6bnVsbCxcImVtYWlsXCI6XCJib3hpbjIyMDQ0QGtyYXZpZnkuY29tXCIsXCJ1c2VySWRcIjpcImJveGluMjIwNDRAa3JhdmlmeS5jb21cIixcImRhdGFzZXRJZFwiOm51bGx9IiwiYXVkIjpbImxpYnJhcnkiLCJNUk8iLCJhbmFseXRpY3MiLCJjb3JlIiwic3luYyJdLCJleHAiOjE3MTMzNDIyODEsImlhdCI6MTcxMzM0MjE2MX0.XVXLK-Wt3gcrt8wlyzR1JGbjGvqWT0OcdaOHTIkPtUc'
```
2. Without jwt with rate limit
```
curl 'http://localhost/user-profile/' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Connection: keep-alive' -H 'Cookie: jenkins-timestamper-offset=-19800000; _ga_0C4M1PWYZ7=GS1.1.1712291211.13.0.1712291212.0.0.0; _ga=GA1.1.1680275956.1711025357; _ga_T11SF3WXX2=GS1.1.1712291211.13.0.1712291211.60.0.0; _ga_K2SPJK2C73=GS1.1.1712291211.13.0.1712291211.60.0.0; __utma=111872281.1680275956.1711025357.1711091232.1711107119.2; __utmz=111872281.1711091232.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=111872281.|1=Treatment=PE=1; wp-settings-time-1=1712134760; wp-settings-1=libraryContent%3Dbrowse' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: none' -H 'Sec-Fetch-User: ?1'
```
ex. curl http://localhost/user-profile/

2. http://localhost/user-account/