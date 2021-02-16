#Use postgres image
FROM postgres
# Copy create_tables.sql into docker-entrypoint-initdb to load when db starts
COPY sql/ /docker-entrypoint-initdb.d
