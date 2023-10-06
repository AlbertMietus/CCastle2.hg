mypy_all: mypy_castle
mypy_now: mypy_RPy mypy_aigr

mypy_RPy:; 	mypy 	castle/writers/RPy
mypy_aigr:;	mypy	castle/aigr TestDoubles/AIGR

mypy_castle:; 	mypy	castle
