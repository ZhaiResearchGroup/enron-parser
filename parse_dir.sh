for file in $1/*
do
	echo processing "$file"
	python email-parse.py $file >> parsed/$(basename $file).json
	exit 0
done
