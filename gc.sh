path='/usr/local/Cellar'

for i in `ls $path`; 
do
	if [[ -d $path/$i ]]; then
		cd $path/$i	&& git gc
	fi 
done
echo "ok"