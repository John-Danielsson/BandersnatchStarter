from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    Initializes the Database using a dictionary
    with which to make a MongoDB database, a DataFrame,
    or an HTML table.
    """
    def __init__(self):
        self.columns = [
            'Name', 'Type', 'Level',
            'Rarity', 'Damage', 'Health',
            'Energy', 'Sanity', 'Timestamp'
        ]
        self.df = {column:[] for column in self.columns}

    """Inserts the specified number of documents, 'amount', into the collection."""
    def seed(self, amount):
        for i in range(amount):
            monster = Monster()
            self.df['Name'].append(monster.name)
            self.df['Type'].append(monster.type)
            self.df['Level'].append(monster.level)
            self.df['Rarity'].append(monster.rarity)
            self.df['Damage'].append(monster.damage)
            self.df['Health'].append(monster.health)
            self.df['Energy'].append(monster.energy)
            self.df['Sanity'].append(monster.sanity)
            self.df['Timestamp'].append(monster.timestamp)

    """Deletes all documents in the collection."""
    def reset(self):
        for key in self.df.keys():
            self.df[key] = []

    """Returns the number of documents in the collection."""
    def count(self) -> int:
        return len(self.df['Name'])

    """Returns a pandas DataFrame representation of all the documents in the collection."""
    def dataframe(self) -> DataFrame:
        return DataFrame(data=self.df, columns=self.columns)

    """Returns an HTML table representation of all the documents in the collection."""
    def html_table(self) -> str:
        return self.dataframe().to_html()
