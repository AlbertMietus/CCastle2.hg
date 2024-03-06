

missing: missing_visitor missing_serialization
open:    coverage-open mutmut-open
remake:  veryclean coverage mutmut open


GAM: clean_generated current-only diff_TestDoubles


diff_TestDoubles:
	echo "This rule is outdated"
	diff -w -rs  -x _keepThisDir -x .DS_Store TestDoubles/reference/ TestDoubles/_generated/

