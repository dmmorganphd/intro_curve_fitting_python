#!/usr/bin/bash
tar -zcvf ../intro_curve_fitting_python.tgz ./

if [ $? != 0 ] ; then
	echo "Something went wrong creating the archive."
else
	# epoch time
	datestamp=`date +%s`
	nfn='../intro_curve_fitting_python_'$datestamp'.tgz'
	mv ../intro_curve_fitting_python.tgz $nfn
	if [ $? !=0 ] ; then
	      echo "Something went wrong renaming the archive."
     	else
		echo "Successfully created "$nfn
	fi
fi
