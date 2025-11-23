.PHONY: exception
exception:
	python -m budwing.messy.exception.exception_client

.PHONY: race-condition
race-condition:
	python -m budwing.messy.concurrency.race_condition