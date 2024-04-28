## add jwt module 
FROM ghcr.io/max-lt/nginx-jwt-module:v3.4.0


# FROM nginx:1.20-alpine
## Nginx opensource
# FROM nginx:1.15-alpine
LABEL author="sandeep.rana(aimhigh.excel@gmail.com)"


## Create the directory for the PID file
RUN mkdir -p /run/nginx

# RUN apk update
# RUN apk add nginx

## Install the module 
# RUN apk install https://extras.getpagespeed.com/release-latest.rpm
# RUN apk add nginx-module-ndk
# RUN apk add --no-cache nginx-mod-devel-kit

# RUN echo "https://extras.getpagespeed.com/alpine/v3.14/main" >> /etc/apk/repositories
# RUN rm -rf /var/cache/apk/*
# RUN apk update
# RUN apk add nginx-module-jwt
# RUN apk add --no-cache nginx-mod-http-lua
# RUN apk add --no-cache nginx-mod-http-js
    
## copy modules
# COPY lua/ /etc/lua/

## copy nginx-jwt module
# COPY --from=nginx-jwt /usr/lib/nginx/modules/ngx_http_auth_jwt_module.so /usr/lib/nginx/modules/ngx_http_auth_jwt_module.so

## copy nginx.conf.template
COPY nginx.conf.template /etc/nginx/nginx.conf.template



## copy the jwt.js
COPY jwt.js /etc/nginx/jwt.js


## copy jwt mpodule 
# COPY nginx-jwt/ /etc/nginx/nginx-jwt/

## Start Nginx
STOPSIGNAL SIGTERM

CMD ["/bin/sh" , "-c", "envsubst '$${jwt_secret}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]
