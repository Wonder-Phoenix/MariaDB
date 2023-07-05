import mysql.connector

# Paramètres de connexion à la base de données
host = 'localhost'  # Remplacez par l'adresse de votre serveur MariaDB
user = 'useragenda'  # Remplacez par le nom d'utilisateur de connexion à la base de données
password = 'phénomène9'  # Remplacez par le mot de passe de connexion à la base de données
database = 'bddagenda'  # Remplacez par le nom de la base de données que vous avez créée

# Connexion à la base de données
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Création d'un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exemple de requête SQL pour récupérer des données de la base de données
cursor.execute("SELECT * FROM utilisateurs")
rows = cursor.fetchall()

# Affichage des résultats
for row in rows:
    print(row)

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
