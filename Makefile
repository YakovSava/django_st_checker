wininstall:
	py -m venv ./venv
	./venv/Scripts/activate
	pip install -r requirments.txt

run:
	cd tested
	make run

linuxinstall:
	sudo apt install libreoffice -y
	python3 -m venv ./venv
	./venv/bin/activate
	pip install -r requirments.txt
	