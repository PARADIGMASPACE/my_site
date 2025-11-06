FROM nginx:alpine

RUN mkdir -p /etc/nginx/ssl


COPY frontend/ /usr/share/nginx/html/

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
