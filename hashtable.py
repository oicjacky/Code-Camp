import pprint

class Hashtable:
    '''[Implement of Hash table](https://thepythoncorner.com/posts/2020-08-21-hash-tables-understanding-dictionaries/)
    
    A Hash table is created by 
        - buckets: store the data like (key, value)
        - bucket_size: the number of buckets in the hash table
        - index: defined as hash(key) mod bucket_size
    '''
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None

    def __str__(self):
        return pprint.pformat(self.buckets) # here pformat is used to return a printable representation of the object


if __name__ == "__main__":

    capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]
    hashtable = Hashtable(capitals)
    print(hashtable)
    print(f"The capital of Italy is {hashtable.get_value('Italy')}")
