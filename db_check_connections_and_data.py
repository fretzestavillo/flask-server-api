from pymongo import MongoClient

# Function to connect to MongoDB and fetch data


def connect_and_fetch_data():
    try:
        # Connect to MongoDB server running locally
        client = MongoClient('mongodb://localhost:27017/')

        # List all databases
        print("Available databases:")
        print(client.list_database_names())

        # Select the 'sample_db' database
        db = client.sample_db

        # List all collections in the selected database
        print("\nCollections in 'sample_db':")
        print(db.list_collection_names())

        # Select the 'sample_collection' collection
        collection = db.sample_collection

        # Fetch all documents from the collection
        print("\nDocuments in 'sample_collection':")
        for document in collection.find():
            print(document)

    except Exception as e:
        print("Error:", e)


# Call the function to connect and fetch data
connect_and_fetch_data()
