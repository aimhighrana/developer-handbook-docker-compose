
SELECT 'CREATE DATABASE mdo_auth' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mdo_auth')\gexec