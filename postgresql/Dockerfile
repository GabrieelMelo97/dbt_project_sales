# Use a imagem oficial do PostgreSQL como base
FROM postgres:latest

# Defina as variáveis de ambiente para configurar o banco de dados
ENV POSTGRES_DB=project_sales \
    POSTGRES_USER=posgresql \
    POSTGRES_PASSWORD=admin

# Exponha a porta padrão do PostgreSQL (5432)
EXPOSE 5432

# Opcional: carregue um script SQL para inicializar o banco de dados (se necessário)
COPY init.sql /docker-entrypoint-initdb.d/

# Execute o PostgreSQL
CMD ["postgres"]
