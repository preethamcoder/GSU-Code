import unittest

database = [{'id':1, 'rating':5, 'username':"Hemlo", 'timestamp':1234567}, {'id':2, 'rating':5, 'username':"BhaiHemlo", 'timestamp':2134567}, {'id':3, 'rating':2, 'username':"Aree", 'timestamp':4567123}]
print("Current database is:", database)

class TestDB(unittest.TestCase):
    def test_add_rate(self):
        obj = {'id':4, 'rating':1, 'username':"Jaao", 'timestamp':7654321}
        database.append(obj)
        print("After adding:", database)
        self.assertEqual(database, [{'id':1, 'rating':5, 'username':"Hemlo", 'timestamp':1234567}, {'id':2, 'rating':5, 'username':"BhaiHemlo", 'timestamp':2134567}, {'id':3, 'rating':2, 'username':"Aree", 'timestamp':4567123}, {'id':4, 'rating':1, 'username':"Jaao", 'timestamp':7654321}])
    def test_del_rate(self):
        obj = {'id':4, 'rating':1, 'username':"Jaao", 'timestamp':7654321}
        for each in range(len(database)):
            if(database[each]['timestamp'] == 7654321):
                del database[each]
                break
        print("After deleting:", database)
        self.assertEqual(database, [{'id':1, 'rating':5, 'username':"Hemlo", 'timestamp':1234567}, {'id':2, 'rating':5, 'username':"BhaiHemlo", 'timestamp':2134567}, {'id':3, 'rating':2, 'username':"Aree", 'timestamp':4567123}])
    def test_query_all(self):
        print("All values in database:", database)
        self.assertEqual(database, database)

if __name__ == '__main__':
    unittest.main()

