import os
import unittest
import tempfile

class JSONReadingTestCase(unittest.TestCase):
    def _testDB():
        jsonschema = [dict(
                test=dict(
                    this='that',
                    unce='the other thing',
                    ),
                worlds=dict(
                    title='world one',
                    foxy='world twoish'
                    )],
                hobbit=[],
                )
        fh, fp = tempfile.mkstemp(suffix='.jsondb', dir=os.getcwd())
        with os.fdopen(fh, 'rw') as f:
            f.write(jsonschema)
    def testReadKey(self): # tests to make sure that the file returns a key
        return
    def testReadError(self): # ensures that the proper error is called
        return

if __name__ == "__main__":
    unittest.main()

