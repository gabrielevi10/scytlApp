run:
	python3 src/main.py

all_test:
	python3 -m unittest tests/ConnectionTestSuite.py
	python3 -m unittest tests/EncoderTestSuite.py
	python3 -m unittest tests/DecoderTestSuite.py 

test_connection:
	python3 -m unittest tests/ConnectionTestSuite.py

test_encoder:
	python3 -m unittest tests/EncoderTestSuite.py

test_decoder:
	python3 -m unittest tests/DecoderTestSuite.py 

coverage:
	coverage run src/main.py
	coverage report -m