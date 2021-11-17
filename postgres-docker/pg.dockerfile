FROM postgres:13.1-alpine
ENV POSTGRES_USER=template_user
ENV POSTGRES_PASSWORD=template_pass
ENV POSTGRES_DB=template_db
EXPOSE 5432