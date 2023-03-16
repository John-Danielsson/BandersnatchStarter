from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    Initializes the Database using a dictionary
    with which to perform CRUD operations on a MongoDB database,
    or make a DataFrame or an HTML table.
    """
    def __init__(self, collection: str):
        load_dotenv()
        database = MongoClient(getenv("MONGO_URL"), tlsCAFile=where())["Database"]
        self.collection = database[collection]
        self.version = 0

    """Inserts the specified number of documents, 'amount', into the collection."""
    def seed(self, amount) -> None:
        for i in range(amount):
            monster = Monster()
            self.collection.insert_one(document={
                "name": monster.name, "type": monster.type,
                "level": monster.level, "rarity": monster.rarity,
                "damage": monster.damage, "health": monster.health,
                "energy": monster.energy, "sanity": monster.sanity,
                "timestamp": monster.timestamp
            })

    """Deletes all documents in the collection."""
    def reset(self) -> None:
        self.collection.delete_many(filter={})

    """Returns the number of documents in the collection."""
    def count(self) -> int:
        return self.collection.count_documents({})

    """Returns a pandas DataFrame representation of all the documents in the collection."""
    def dataframe(self) -> DataFrame:
        rows = [
                [
                    row['name'], row['type'], row['level'],
                    row['rarity'], row['damage'], row['health'],
                    row['energy'], row['sanity'], row['timestamp']
                ] for row in self.collection.find({})
            ]
        return DataFrame(
            columns=[
                'Name', 'Type', 'Level',
                'Rarity', 'Damage', 'Health',
                'Energy', 'Sanity', 'Timestamp'
            ],
            data=rows
        )

    """Returns an HTML table representation of all the documents in the collection."""
    def html_table(self) -> str:
        return self.dataframe().to_html()

    """Saves the current data as a .csv file."""
    def save(self) -> None:
        self.version += 1
        self.dataframe().to_csv(
            path_or_buf=f'bandersnatch_data_{self.version}.csv'
        )
