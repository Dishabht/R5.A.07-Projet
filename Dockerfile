# Étape 1 : utiliser une image Java
FROM eclipse-temurin:21-jdk

# Étape 2 : définir le dossier de travail
WORKDIR /app

# Étape 3 : copier ton jar dans l’image
COPY target/demo-0.0.1-SNAPSHOT.jar app.jar

# Étape 4 : exposer le port de ton app
EXPOSE 2005

# Étape 5 : lancer ton jar
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
