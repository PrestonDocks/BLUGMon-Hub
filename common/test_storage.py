import unittest
import storage

class Test(unittest.TestCase):
    def test_get_put(self):
        s = storage.MemoryStorage('hub')
        key = 'name'
        value = 'Client 1'        
        s.put(key, value)
        x = s.get(key)
        self.assertEqual(s.get(key), value)

if __name__ == '__main__':
    unittest.main()
