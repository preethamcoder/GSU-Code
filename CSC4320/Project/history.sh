history > history.txt
sed 's/^[t ]*[0-9]* //g' history.txt > new.txt
sed 's/^[t ]* //g' new.txt > comphist.txt
python3 logsanalyzer.py comphist.txt
rm new.txt
rm history.txt
