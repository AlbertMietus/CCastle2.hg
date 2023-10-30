mypy: 		mypy_notOld
mypy_all: 	mypy_castle mypy_TestDoubles
mypy_now: 	mypy_RPy mypy_aigr


mypy_castle:; 		mypy	castle
mypy_aigr:;		mypy	castle/aigr
mypy_RPy:; 		mypy 	castle/writers/RPy
mypy_AIGR:;		mypy 	TestDoubles/AIGR
mypy_TestDoubles:;	mypy 	TestDoubles/AIGR

mypy_notOld: mypy_aigr mypy_RPy  mypy_AIGR
